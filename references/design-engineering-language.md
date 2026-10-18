# Design Engineering Language (DEL)

Design like an industrial design engineer, not like an AI generating pretty UI. DEL is this skill's convention (not an external standard) for writing design instructions the way aircraft documentation writes maintenance steps: controlled, measurable, testable. Its ancestors are ASD-STE 100 controlled language, CAD drawing discipline, tolerance engineering and compiler design.

## 1. Controlled instruction rules

Every design rule this skill writes (in specs, briefs, design systems, style definitions, handoffs) follows these:

| Rule | Required behaviour |
|---|---|
| One instruction | Each rule states one action or constraint, with one meaning. |
| Defined vocabulary | Terms like depth, contrast, material, hierarchy carry the precise meanings this skill's references give them. |
| Explicit scope | Say whether a rule applies to web, posters, SVG, print or all media. |
| Measurable output | Dimensions, ratios, stroke widths, spacing values wherever the property is measurable. |
| Conflict resolution | The priority order below decides when rules disagree. |
| Validation | A rule worth writing names how to check it (automated test or review procedure). |
| Controlled exceptions | Deviations only when the brief requires them, recorded as exceptions. |

The transformation DEL exists for:

- Weak: "Make the icon look premium, balanced and modern, with beautiful details."
- DEL: "Use a 24x24 viewBox. One stroke width of 2 units. Centre the primary shape optically. Preserve at least 2 units of padding. Test at 16, 24 and 48 pixels on light and dark."

The second is implementable, testable and reproducible. When you catch yourself writing the first kind, rewrite it or delete it.

## 2. Conflict resolution priority

When rules disagree, apply in this order and say which level decided:

1. Explicit user requirements.
2. Technical correctness, safety and accessibility floors.
3. Medium-specific rules (what SVG, print or a viewport physically demands).
4. The selected style's rules.
5. Universal design defaults.

A conflict that cannot be resolved without changing the intended result is reported, not silently absorbed.

## 3. The compiler model

A compiler does not suggest valid code; it transforms input through defined stages and reports errors. Treat every design job the same way:

1. **Parse the brief**: medium, objective, audience, dimensions, constraints; reject or query an unparseable brief (one focused question).
2. **Resolve tokens**: typography, spacing, colour, geometry and style rules bound to values BEFORE generation; an existing design system is the token source when one governs (see SKILL.md "Design systems"). Tokens are typed: a colour token never fills a spacing slot, a raster asset never stands in for a vector one, and an invalid combination is rejected at this stage, not discovered in the render.
3. **Generate**: the artefact in the target medium's native capabilities.
4. **Automated checks** (the deterministic pass): parse validity, dimensions, dangling references, contrast ratios, overflow, missing assets, rule violations. Machine-checkable things are machine-checked.
5. **Visual evaluation** (the judgement pass): rendered output inspected for balance, hierarchy, consistency, style fidelity. Automated checks never substitute for this, and this never substitutes for them.

Errors from stage 4 are defects; disagreements in stage 5 are findings (confirmed vs taste, per `design-evaluation.md`). Not every aesthetic quality reduces to a deterministic test; do not pretend otherwise in either direction.

## 4. Failure anticipation (FMEA habit)

Before declaring any deliverable complete, run the known failure modes for its medium, each with its check:

| Failure mode | Check |
|---|---|
| Text clipping/overflow at real content lengths | render with longest realistic strings |
| Broken SVG references, duplicate IDs | automated scan |
| Contrast below floor on any meaningful pair | computed ratios, not impressions |
| Font fallback changing metrics | render without the preferred font |
| Layout overflow at narrow widths | true-viewport test (beware the headless window floor; see LESSONS.md) |
| Icon illegible at smallest size | render the family as a row at target size |
| Effects that die in export (shadows, filters) | test the actual export path |
| Drift across repeated components | tolerance rules: one spacing scale, one stroke set, stated rounding policy |

Add newly discovered failure modes to `../LESSONS.md`; promote recurring ones into this table.

## 5. Tolerances and property thinking

Small deviations accumulate: three "close enough" paddings read as sloppiness at the fourth. Define the scale (spacing, stroke, radius, type) once and snap to it; record any exception. Where variation is real (content length, viewport, theme, state), think like property-based testing: do not check one happy example, sweep the realistic range and look for the combination that breaks.

## 6. Style grammar

A style in the catalogue is a grammar, not a mood board. Its entry fields map to five grammar parts: visual DNA (philosophy + characteristics), construction rules (geometry, colour, typography, materials, lighting), allowed variation (use cases across media), anti-patterns (common mistakes + when not to use), and tests (the QA checklist). Compose within the grammar; never abandon the system because one artefact feels special. A grammar is portable: Art Deco can inform a poster, an icon or a landing page without the three looking identical.
