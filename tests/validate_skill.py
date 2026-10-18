#!/usr/bin/env python3
"""Structure validator for the design-styles skill.

Checks, with no third-party dependencies:
  1. SKILL.md frontmatter: name, description, disable-model-invocation: true.
  2. SKILL.md stays under 500 lines (Claude Code guidance).
  3. Every relative .md / .svg link or backtick path reference in every
     markdown file resolves to an existing file.
  4. Every SVG parses as XML, has a viewBox, has unique ids, and every
     internal reference (url(#id), href="#id") resolves.
  5. No em dashes in any skill file (user style rule).
  6. The expected file inventory is present (catalogue covers 64 styles).

Run:  python3 validate_skill.py            (from tests/, or pass the skill root)
Exit: 0 clean, 1 failures.
"""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
failures: list[str] = []
warnings: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)


def check_frontmatter() -> None:
    skill = ROOT / "SKILL.md"
    if not skill.exists():
        fail("SKILL.md missing")
        return
    text = skill.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) > 500:
        fail(f"SKILL.md has {len(lines)} lines (limit 500)")
    if not text.startswith("---"):
        fail("SKILL.md missing frontmatter")
        return
    fm = text.split("---", 2)[1]
    for key, pattern in [
        ("name", r"^name:\s*design-styles\s*$"),
        ("description", r"^description:\s*\S"),
    ]:
        if not re.search(pattern, fm, re.M):
            fail(f"SKILL.md frontmatter missing/invalid: {key}")
    # activation-mode consistency (tools/set-activation.py switches between the two)
    opt_in = bool(re.search(r"^disable-model-invocation:\s*true\s*$", fm, re.M))
    strict_section = "Operate ONLY when the user explicitly invoked" in text
    if opt_in != strict_section:
        fail("SKILL.md activation mode inconsistent: frontmatter and Activation section disagree")
    print(f"  activation mode: {'opt-in' if opt_in else 'auto'}")
    desc = re.search(r"^description:\s*(.+)$", fm, re.M)
    if desc and len(desc.group(1)) > 1536:
        fail("description exceeds 1536 characters")


LINK_RE = re.compile(r"\]\(([^)#\s]+\.(?:md|svg|py))\)|`((?:\.\./)?(?:references|workflows|examples|tests|styles)/[\w./-]+\.(?:md|svg|py))`")


def is_evidence(rel: Path) -> bool:
    # evaluation run outputs and judging copies are frozen evidence produced by
    # evaluated agents; they are never edited, so style and link rules skip them
    return rel.parts[0] == "evaluation" and len(rel.parts) > 1 and rel.parts[1] in ("runs", "judging", "flagship")


def check_links() -> None:
    for md in ROOT.rglob("*.md"):
        rel = md.relative_to(ROOT)
        # variant SKILL files are written for the skill root; their links resolve
        # only after tools/set-activation.py or a manual copy puts them there
        if rel.parts[0] == "variants" or is_evidence(rel):
            continue
        text = md.read_text(encoding="utf-8")
        for m in LINK_RE.finditer(text):
            target = m.group(1) or m.group(2)
            if target.startswith(("http:", "https:")):
                continue
            if not (md.parent / target).resolve().exists():
                fail(f"{rel}: broken reference {target}")


def check_svgs() -> None:
    svgs = sorted(ROOT.rglob("*.svg"))
    if not svgs:
        fail("no SVG examples found")
    for svg in svgs:
        rel = svg.relative_to(ROOT)
        # evaluation SVGs are exempt: run outputs are frozen evidence, and the
        # fixtures are deliberately defective audit inputs
        if rel.parts[0] == "evaluation":
            continue
        try:
            tree = ET.parse(svg)
        except ET.ParseError as e:
            fail(f"{rel}: XML parse error: {e}")
            continue
        svg_root = tree.getroot()
        if "viewBox" not in svg_root.attrib:
            fail(f"{rel}: missing viewBox")
        ids: list[str] = []
        refs: set[str] = set()
        for el in svg_root.iter():
            if "id" in el.attrib:
                ids.append(el.attrib["id"])
            for attr, val in el.attrib.items():
                for ref in re.findall(r"url\(#([\w-]+)\)", val):
                    refs.add(ref)
                if attr.endswith("href") and val.startswith("#"):
                    refs.add(val[1:])
                if attr == "aria-labelledby":
                    refs.update(val.split())
        dupes = {i for i in ids if ids.count(i) > 1}
        if dupes:
            fail(f"{rel}: duplicate ids {sorted(dupes)}")
        missing = refs - set(ids)
        if missing:
            fail(f"{rel}: unresolved internal references {sorted(missing)}")


def check_em_dashes() -> None:
    for f in list(ROOT.rglob("*.md")) + list(ROOT.rglob("*.svg")):
        if is_evidence(f.relative_to(ROOT)):
            continue
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if "—" in line:
                fail(f"{f.relative_to(ROOT)}:{n}: em dash present")


EXPECTED = [
    "SKILL.md",
    "references/design-principles.md",
    "references/design-engineering-language.md",
    "references/perception-and-attention.md",
    "references/style-catalogue.md",
    "references/design-history.md",
    "references/cross-disciplinary-design.md",
    "references/svg-and-vector-graphics.md",
    "references/ui-ux.md",
    "references/typography-and-graphics.md",
    "references/accessibility-and-quality.md",
    "references/design-evaluation.md",
    "references/industrial-design.md",
    "references/architecture.md",
    "references/art-and-composition.md",
    "references/aerospace-and-instrumentation.md",
    "references/horology.md",
    "references/design-leadership.md",
    "references/styles/foundation.md",
    "references/styles/heritage.md",
    "references/styles/digital-dimensional.md",
    "references/styles/illustration-expressive.md",
    "references/styles/typographic-editorial.md",
    "references/styles/contemporary-specialist.md",
    "workflows/new-design.md",
    "workflows/critique.md",
    "workflows/style-selection.md",
    "workflows/cross-disciplinary-transfer.md",
    "workflows/ui-ux-audit.md",
    "workflows/svg-creation.md",
    "workflows/image-gen-brief.md",
    "workflows/design-system.md",
    "workflows/research.md",
    "workflows/implementation-verification.md",
    "workflows/design-loop.md",
    "workflows/parallel-exploration.md",
    "agents/README.md",
    "agents/scout.md",
    "agents/relic.md",
    "agents/muse.md",
    "agents/forge.md",
    "agents/roast.md",
    "agents/ramp.md",
    "agents/pixel.md",
    "agents/penny.md",
    "LESSONS.md",
    "examples/annotated-cases.md",
    "examples/svg/critique-notes.md",
]


def check_inventory() -> None:
    for rel in EXPECTED:
        if not (ROOT / rel).exists():
            fail(f"expected file missing: {rel}")
    # catalogue coverage: count style headings across category files
    styles_dir = ROOT / "references" / "styles"
    if styles_dir.exists():
        count = 0
        for f in styles_dir.glob("*.md"):
            count += len(re.findall(r"^##\s+\S", f.read_text(encoding="utf-8"), re.M))
        if count < 64:
            fail(f"style catalogue has {count} style headings, expected >= 64")
        else:
            print(f"  catalogue: {count} style entries")


def main() -> int:
    print(f"validating {ROOT}")
    check_frontmatter()
    check_links()
    check_svgs()
    check_em_dashes()
    check_inventory()
    for w in warnings:
        print(f"WARN  {w}")
    if failures:
        for f in failures:
            print(f"FAIL  {f}")
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
