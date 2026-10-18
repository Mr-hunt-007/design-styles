# Evaluation protocol (pre-registered)

Written and fixed 2026-10-18, before any evaluation run was executed. The rubric, tasks and thresholds below were not changed after seeing results.

## Hypothesis

Invoking `design-styles` produces measurably better design deliverables (quality, correctness, fewer defects) than the same agent class working without it, at an acceptable cost in time and tokens.

## Method

- **Control:** a fresh general-purpose agent receives the task brief only. It is not told the skill exists.
- **Treatment:** an identical fresh agent receives the same brief, prefixed with an instruction to first read `SKILL.md` and follow it, loading referenced files as needed. This simulates explicit `/design-styles` invocation (the skill is deliberately not installed during evaluation).
- Same model family, same tool access (shell, file IO, headless Chrome available to both), same output contract. One run per condition per task (single-run limitation acknowledged below).
- **Blind judging:** per task, a fresh judge agent receives the two artefact sets at neutral paths labelled A and B, with no mention of conditions or the skill, and scores both against the rubric. The A/B-to-condition key is held by the orchestrator and applied only after scores are returned.
- Task 6 is additionally scored objectively against a sealed answer key of defects planted in the fixture (key stored outside the repo until runs complete).
- Token usage per run is recorded from the harness.

## Tasks (briefs given verbatim to both conditions)

1. **Dashboard:** cybersecurity monitoring dashboard for a SOC analyst triaging alerts across 40 client organisations; single self-contained `dashboard.html`, inline placeholder data; must communicate severity, alert queue, trends, asset context; dark theme preferred; plus `DECISIONS.md` (max 20 lines).
2. **Poster:** technical conference poster (A3 portrait, single self-contained `poster.svg`) explaining credential-stuffing attacks and defences; clear hierarchy, readable from 2 m; plus `DECISIONS.md`.
3. **Architecture diagram:** `architecture.svg` of a web platform (CDN, WAF, LB, 3 app services, queue, workers, Postgres, Redis, object storage, monitoring) with connectors, labels, grouped edge/app/data zones; plus `DECISIONS.md`.
4. **Icon family:** 6 consistent 24x24 interface icons (scan, alert, report, asset, settings, user) as `icons.svg` symbol sheet + `preview.html` grid; precise, consistent, legible at 16px; plus `DECISIONS.md`.
5. **Landing page:** self-contained `landing.html` for "Meridian", a B2B attack-surface-management product, combining exactly two compatible styles (named and justified in `DECISIONS.md`); hero, 3 features, social proof, CTA.
6. **SVG audit:** audit `fixtures/defective-status-board.svg`; `audit.md` listing every confirmable defect with evidence and fix, confirmed separated from suggestions; optional `fixed.svg`.
7. **Evolve:** improve `fixtures/status-page.html` (public service-status page for "Northbeam") preserving purpose and content; `improved.html` + `DECISIONS.md` (changed, why, deliberately preserved).
8. **Style selection:** regulated private bank's client wealth dashboard; `recommendation.md` with one primary style + max one supporting influence, principles, 3 rejected alternatives with concrete reasons (at least one fashionable-but-unsuitable), implementation notes; max 120 lines.

## Scoring rubric (0-5 per criterion, weighted to 100)

| Criterion | Weight |
|---|---:|
| Brief and user-goal alignment | 20 |
| Visual hierarchy and composition | 15 |
| Typography, colour and legibility | 10 |
| Usability and accessibility | 15 |
| Technical correctness | 15 |
| Cross-disciplinary reasoning | 10 |
| Originality and coherence | 5 |
| Maintainability and implementation quality | 5 |
| Efficiency and absence of unnecessary complexity | 5 |

Total = sum(score/5 x weight), out of 100. Judges mark truly inapplicable criteria N/A; their weight is redistributed proportionally. Judges must render HTML/SVG artefacts (headless Chrome) and score what they observe, not what the source promises.

## A/B assignment key (fixed before judging)

Tasks 1, 4, 6, 7: A = control, B = treatment. Tasks 2, 3, 5, 8: A = treatment, B = control.

## Decision thresholds (fixed in advance)

- No activation-boundary failures in negative tests (structural check: `disable-model-invocation: true` + mode-consistency test in `../tests/validate_skill.py`; live multi-session negative trials are out of scope here and reported as a limitation).
- All 64 catalogue entries present (automated).
- All 8 tasks executed in both conditions, or explicitly marked blocked.
- No critical technical defects (artefact fails to render / fails XML parse) in deliverables declared complete.
- No unsupported claims of rendering or testing by either condition, checked by spot-verifying claimed renders.
- Average improvement >= +10 points out of 100 across scored tasks, with no material regression in usability, accessibility or correctness on any task.
- Verdict vocabulary: Effective / Partially effective / Not effective / Inconclusive. Single-run-per-condition and single-judge-per-task are acknowledged limits: if results are mixed or judge confidence is low, the verdict is at most Partially effective or Inconclusive.

## Known limitations (declared in advance)

- n=1 per condition per task; generation variance is not averaged out.
- One judge per task (an LLM, not a human panel); judge bias is partially mitigated by blinding and randomised A/B order.
- Control and treatment run in the same ecosystem; the treatment prompt necessarily adds the read-the-skill instruction, so some benefit may come from extra steering tokens rather than skill content. Reported, not hidden.
- Live activation-boundary trials (fresh interactive sessions) are not run here.
