# Contributing to design-styles

Contributions are welcome: new styles, historical corrections, cross-disciplinary examples, SVG cases, workflows, evaluation tasks, compatibility fixes and documentation improvements. The bar is usefulness, not volume.

## Before you open a PR

1. Run the structure validator and keep it green:
   ```bash
   python3 -I tests/validate_skill.py
   ```
   It checks the entrypoint, every cross-file link, SVG integrity, catalogue coverage and the no-em-dash style rule.
2. Keep the activation boundary intact: `SKILL.md` ships in opt-in mode. Do not add hooks, triggers or changes to other skills or global configuration.
3. Match the house style: British -ise spelling, no em dashes, dense practical prose over encyclopaedic padding.

## Adding or changing a style

- One `##` heading per style in the right `references/styles/*.md` category file, using the same field schema as existing entries (philosophy, characteristics, geometry, colour, typography, materials, lighting, motion, use cases, when not to use, mistakes, accessibility, implementation, complements, conflicts, transferable principles, brief example, QA checklist).
- A new entry must state how it differs from the nearest existing entries. Minor variants of an existing style are merged into that entry, not added as duplicates.
- Historical claims need credible sources, or they are phrased as interpretation with approximate dates ("c."). Never invent practitioners, dates or works.
- Add the style to the index table in `references/style-catalogue.md`.

## Adding SVG examples

- Follow `references/svg-and-vector-graphics.md` and the verification loop in `workflows/svg-creation.md`.
- Ship only examples you actually validated and rendered; record what was checked (and what was not) in `examples/svg/README.md`.
- Use neutral example names (no real companies or clients).

## Adding evaluation tasks

- Extend `evaluation/protocol.md` style: pre-registered brief, fixed rubric, honest limitations. Evaluation claims in the README must trace to recorded results, never to expectations.

## Scope of reviews

Pull requests are reviewed for: validator passing, factual honesty, distinctiveness (no duplicate knowledge), link integrity, and whether the change makes the skill decide better rather than merely say more.
