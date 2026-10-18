# Changelog

## 1.1.0 (2026-10-18)

- The design loop with dynamic depth tiers (Sketch / Studio / Flagship): `workflows/design-loop.md`.
- Parallel exploration (develop 2-4 directions in parallel, judge blind-ish, collapse to one): `workflows/parallel-exploration.md`.
- The crew: 8 named installable agent personas in `agents/` (SCOUT, RELIC, MUSE, FORGE, ROAST, RAMP, PIXEL, PENNY) with a shared mindset and strict cost discipline.
- `LESSONS.md`: append-only mistake ledger loaded on Studio/Flagship work, seeded with this build's evaluated failures; generalising lessons get promoted into references.
- Design-system composition: detect and follow an existing design system (installed skill or project tokens) before styling; the design-system workflow can package a brand system as its own SKILL.md.
- Measured evaluation shipped: pre-registered protocol, 8 blind-judged control-vs-treatment tasks, failure root-caused, fixed and re-run; n=3 replication on three tasks went 9/9 to the skill, mean +8.5 (`EVALUATION.md`).
- Flagship crew run delivered the repository's own social banner (SCOUT brief, 3 parallel MUSEs, blind ROAST collapse, FORGE fixes): `evaluation/flagship/`, `docs/assets/social-preview.svg`.
- New references from engineering practice: `design-engineering-language.md` (controlled rules, compiler model, FMEA, tolerances) and `perception-and-attention.md` (attention architecture, four loops, ethical floor).
- Release packaging: LICENSE (MIT), CONTRIBUTING, SECURITY, GitHub templates, gallery, dated ecosystem notes, cross-glyph equalisation rule in the SVG reference.

## 1.0.0 (2026-10-18)

Initial release.

- `SKILL.md` entrypoint: identity (designer, researcher, founder), 10-step decision engine, five levels of judgement, 12 modes, 20 permanent principles, honesty rules, load-on-demand reference map. Ships in strict opt-in mode (`disable-model-invocation: true`).
- Activation modes: `tools/set-activation.py` switches between opt-in and auto; `variants/SKILL-v1-auto.md` is the auto copy.
- 15 reference modules covering principles, history, cross-disciplinary transfer, SVG engineering, UI/UX, typography, industrial design, architecture, fine art, aerospace instrumentation, horology, design leadership, accessibility/quality and evaluation.
- Style catalogue: 64 styles across six category files, full schema per entry.
- 10 workflows (design, critique, style selection, cross-disciplinary transfer, UI/UX audit, SVG creation, image-gen briefs, design systems, research, implementation verification).
- Examples: 3 annotated cross-disciplinary cases; 6 SVGs validated and render-verified, including a full critique before/after pair.
- Tests: `tests/validate_skill.py` structure validator; `tests/behavioural-tests.md` scenario suite with honest run log.
- Evaluation: pre-registered controlled comparison protocol and results in `evaluation/` and `EVALUATION.md`.
