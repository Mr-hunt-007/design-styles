#!/usr/bin/env python3
"""Switch the design-styles skill between activation modes.

Usage:
  python3 tools/set-activation.py status    show the current mode
  python3 tools/set-activation.py opt-in    strict: only explicit /design-styles invocation (default)
  python3 tools/set-activation.py auto      Claude may invoke it on matching design tasks

The script edits SKILL.md in place (frontmatter + Activation section) and keeps
variants/SKILL-v1-auto.md as a readable copy of the auto variant. Run it from
anywhere; it locates SKILL.md relative to itself. No dependencies.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"

DESC_OPTIN = (
    'description: "Cross-disciplinary design intelligence: problem-first design reasoning, '
    "a 64-style catalogue, critique rubrics, principle transfer from aerospace/architecture/"
    "horology/fine art to any medium, and SVG engineering. OPT-IN ONLY: invoke solely when the "
    "user explicitly names design-styles (/design-styles or 'use the design-styles skill'). "
    'Never activate merely because a task involves design, UI, SVG, styling or visual critique."\n'
    "disable-model-invocation: true"
)

DESC_AUTO = (
    'description: "Cross-disciplinary design intelligence: problem-first design reasoning, '
    "a 64-style catalogue, critique rubrics, principle transfer from aerospace/architecture/"
    "horology/fine art to any medium, and SVG engineering. Use for design direction, visual "
    "style selection or comparison, design critique and audits, design systems and tokens, "
    "art direction and image-generation briefs, SVG/icon/diagram/illustration creation, "
    'UI/UX visual decisions, posters, landing pages, dashboards and brand identity work."'
)

ACT_OPTIN = """## Activation (strict)

Operate ONLY when the user explicitly invoked `design-styles` by name (`/design-styles`, "use the design-styles skill", "apply design-styles"). If this file loaded any other way, do not apply its special behaviour; handle the request normally. Never inject these instructions into unrelated tasks, never modify other skills or global config to trigger this one."""

ACT_AUTO = """## Activation

Applies whenever it loads: on explicit `/design-styles` invocation or when a design task matches the description. Scale the depth to the task: a simple colour tweak does not need the full decision engine, and cross-disciplinary references are never forced into simple requests. Never modify other skills or global config."""

DESC_RE = re.compile(r'^description: ".*?"\n(?:disable-model-invocation: true\n)?', re.M | re.S)
ACT_RE = re.compile(r"## Activation.*?(?=\n## )", re.S)


def current_mode(text: str) -> str:
    if "disable-model-invocation: true" in text:
        return "opt-in"
    return "auto"


def set_mode(mode: str) -> None:
    text = SKILL.read_text(encoding="utf-8")
    if current_mode(text) == mode:
        print(f"already in {mode} mode")
        return
    desc, act = (DESC_OPTIN, ACT_OPTIN) if mode == "opt-in" else (DESC_AUTO, ACT_AUTO)
    new, n1 = DESC_RE.subn(desc + "\n", text, count=1)
    new, n2 = ACT_RE.subn(act + "\n", new, count=1)
    if n1 != 1 or n2 != 1:
        sys.exit("SKILL.md has drifted from the known layout; edit the frontmatter and "
                 "Activation section by hand (see variants/SKILL-v1-auto.md for the auto form).")
    SKILL.write_text(new, encoding="utf-8")
    print(f"SKILL.md switched to {mode} mode")
    if mode == "auto":
        print("Claude may now invoke the skill on matching design tasks.")
    else:
        print("The skill now runs only on explicit /design-styles invocation.")


def main() -> None:
    if len(sys.argv) != 2 or sys.argv[1] not in ("status", "opt-in", "auto"):
        sys.exit(__doc__.strip())
    if not SKILL.exists():
        sys.exit(f"SKILL.md not found at {SKILL}")
    if sys.argv[1] == "status":
        print(f"current mode: {current_mode(SKILL.read_text(encoding='utf-8'))}")
    else:
        set_mode(sys.argv[1])


if __name__ == "__main__":
    main()
