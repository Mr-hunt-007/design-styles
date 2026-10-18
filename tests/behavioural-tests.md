# Behavioural tests for design-styles

Structure tests are automated (`validate_skill.py`). Behaviour cannot be unit-tested the same way: these are scenario probes to run against the skill (invoke `/design-styles` with the prompt, judge the output against the pass criteria). Record each run in the log at the bottom with a date, so claims about what was tested stay honest.

For every scenario, also grade the universal criteria: correct understanding of the request; quality of reasoning; suitability of references; practical usefulness; technical and historical accuracy; trade-offs identified; resistance to trend-chasing; consistency with `../SKILL.md` principles.

## Activation tests

- **ACT-1 (positive):** `/design-styles critique this landing page` loads the skill and applies its workflow. PASS: skill behaviour engaged.
- **ACT-2 (negative):** an ordinary request ("make this button blue", "draw me an SVG icon") without naming design-styles must NOT trigger the skill. PASS: `disable-model-invocation: true` prevents auto-invocation; normal behaviour applies. Verify the frontmatter field rather than trusting intent.

## Design judgement scenarios (master spec, A-J)

- **A Digital product:** design a security-intelligence dashboard. PASS: hierarchy, information density, analyst workflow and severity communication addressed; accessibility included; no decorative sci-fi styling that damages usability.
- **B Aerospace instrumentation:** cockpit-inspired monitoring interface. PASS: legibility, fault communication, human factors lead; explicitly distinguishes aesthetic inspiration from validated safety-critical engineering.
- **C Watch design:** contemporary watch concept. PASS: dial hierarchy, case proportions, materials, finishing, movement constraints discussed; no unsupported feasibility claims.
- **D Architecture:** climate-responsive building concept. PASS: form, spatial experience, local context, structure, environment balanced; structural feasibility never casually asserted.
- **E Fine art:** analyse a painting. PASS: composition, colour, perspective, light, historical context, narrative; method from `../references/art-and-composition.md`; fact vs interpretation separated.
- **F Historical transformation:** reinterpret a Victorian object with contemporary manufacturing. PASS: heritage-recognisable features identified and preserved; restraint; no pastiche.
- **G Style conflict:** minimalism + maximalism + glassmorphism + Swiss Design in one interface. PASS: tensions named, coherent hierarchy defined, dominant influence chosen and justified.
- **H Poor existing design:** attractive but confusing interface. PASS: usability prioritised over aesthetics; names the aesthetic decisions that must change.
- **I Real implementation:** given a web codebase, audit it. PASS: evidence-based findings tied to actual code/rendering; no rewrite of unrelated code.
- **J Unfamiliar discipline:** a design problem outside the references. PASS: reasons from principles, names the missing expertise, researches rather than fabricates authority.

## Cross-disciplinary and SVG scenarios (amendment, 1-8)

- **X-1 Cybersecurity dashboard:** aerospace + Swiss + scientific-viz principles. PASS: usable software interface, not a cockpit mock-up.
- **X-2 Technical poster:** architectural composition + painterly light + aerospace annotation. PASS: influences explained as one coherent system.
- **X-3 SVG technical illustration:** system architecture / process diagram. PASS: valid structure, hierarchy, labels, connectors; rendered where tools allow. (Reference implementation: `../examples/svg/diagram-order-journey.svg`; the original run used a since-replaced attack-surface diagram.)
- **X-4 Watch-inspired icon system:** horological proportion and finishing at icon scale. PASS: recognisable at small sizes, no decorative watch parts. (Reference: `../examples/svg/icon-shield-scan.svg`, `../examples/annotated-cases.md` case 3.)
- **X-5 Cross-disciplinary landing page:** industrial design + editorial type + architectural whitespace. PASS: one coherent identity.
- **X-6 SVG visual audit:** given an existing SVG, find syntax problems, visual defects, geometry inconsistency, excess complexity, accessibility issues, optimisation chances. PASS: confirmed problems separated from possible improvements. (Reference: `../examples/svg/critique-notes.md`.)
- **X-7 Unnecessary influence:** ask for a simple functional icon. PASS: no aerospace/architecture/painting forced in; simple tool for a simple job.
- **X-8 Visual verification:** generate an SVG, render, inspect, correct. PASS: reports which checks actually ran and which remain unverified.

## Run log

| Date | Scenario | Outcome | Notes |
|---|---|---|---|
| 2026-10-18 | ACT-2 (frontmatter) | PASS | `disable-model-invocation: true` present; verified by validate_skill.py. Live negative-trigger behaviour not exercised in a fresh session yet. |
| 2026-10-18 | X-3 | PASS | diagram-attack-surface.svg built, XML-validated, rendered via headless Chrome, two visual defects (label overflow) found and fixed, re-rendered clean. |
| 2026-10-18 | X-6 | PASS | critique-before.svg audited: 8 confirmed defects, 2 improvements, fixes verified by render (critique-after.svg, incl. 50% size and dark backdrop). |
| 2026-10-18 | X-8 | PASS | Art Deco composition: render exposed an asymmetric-skyline defect invisible in source review; fixed and re-rendered. Checks run and gaps reported in `../examples/svg/README.md`. |
| 2026-10-18 | A / X-1 | PASS | Controlled comparison task 1 (SOC dashboard): blind judge 87.5 vs control 75.0, high confidence; aerospace principles transferred without cockpit theming. See `../EVALUATION.md`. |
| 2026-10-18 | X-2 | PASS | Task 2 poster: 90.0 vs 80.5, high confidence; Swiss + Isotype influences coherent, sourced statistics. |
| 2026-10-18 | X-4 | PASS after fix | First run regressed (-4.0): cross-glyph optical sizing missed. Cause fixed in the SVG reference + workflow (cross-glyph equalisation); fresh rerun + fresh blind judge: 87.0 vs 80.5, high confidence. See `../EVALUATION.md`. |
| 2026-10-18 | X-5 | PASS | Task 5 landing page: 84.5 vs 83.0, medium confidence; two styles as one identity, defect-free execution. |
| 2026-10-18 | G (partial) | PASS | Task 5/8 runs named conflicting styles and justified exclusions (Cyberpunk, Dark Luxury, Glassmorphism). |
| 2026-10-18 | I (partial) | PASS | Task 7 evolve: 87.5 vs 81.0; intent preserved, claimed contrast verified by judge (control's claim failed measurement). |
| 2026-10-18 | Crew/Flagship (loop + parallel exploration) | PASS | Full crew run on the repo's own social banner: SCOUT brief, 3 isolated MUSEs, PIXEL renders, blind ROAST collapse (8.50/8.40/8.05), FORGE fixes verified by re-render. Records in `../evaluation/flagship/`. |
| 2026-10-18 | A, X-1 (replication) | PASS | n=3 per condition on tasks 1/3/8: treatment 9/9, mean +8.5 (task means +9.7/+12.5/+3.3). See `../EVALUATION.md`. |
| 2026-10-18 | B-F, H, J, X-7, ACT-1 | NOT RUN | Defined above; run in a fresh session and record here. |
