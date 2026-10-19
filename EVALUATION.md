# EVALUATION: does design-styles actually help?

Controlled comparison run 2026-10-18. Protocol, tasks, rubric and thresholds were pre-registered in `evaluation/protocol.md` BEFORE any run executed and were not changed afterwards. Raw judge scores: `evaluation/judging/*.json`. All artefacts: `evaluation/runs/`.

## Verdict: Partially effective (direction confirmed by replication and by a general-audience round)

First round: the skill produced the better deliverable in 7 of 8 blind-judged tasks (8 of 8 after one targeted fix and rerun), mean +5.8/100 (+7.1 post-fix) at roughly +22% token cost. A follow-up n=3 replication on three representative tasks went 9/9 to the skill (sign test p about 0.004) with mean +8.5. The pre-registered +10 overall threshold is still not met, so the formal verdict stays Partially effective; the replication establishes with high consistency WHERE it earns its cost: complex artefact work (diagrams +12.5, dashboards +9.7), with a small consistent margin on advisory text (+3.3) and near-parity on audits the baseline already does well.

## Method (summary; full detail in `evaluation/protocol.md`)

- 8 design tasks, each run twice by fresh agents of the same class and model: **control** (task brief only) and **treatment** (same brief, instructed to read and follow this skill first).
- Both conditions had identical tools (shell, headless Chrome) and output contracts.
- Per task, one **blind judge** agent scored both artefact sets (labelled A/B at neutral paths, assignment pre-registered, leaks masked in judging copies only) against the 9-criterion weighted rubric. Judges were required to render HTML/SVG and score what they observed.
- Task 6 additionally scored against a sealed key of defects planted in the fixture (`evaluation/fixtures/defect-key.md`, unsealed after runs).

## Results

| Task | Control | Treatment | Delta | Blind winner | Confidence |
|---|---:|---:|---:|---|---|
| 1 SOC dashboard | 75.0 | 87.5 | +12.5 | treatment | high |
| 2 Technical poster | 80.5 | 90.0 | +9.5 | treatment | high |
| 3 Architecture diagram | 73.5 | 88.0 | +14.5 | treatment | high |
| 4 Icon family (first run) | 87.5 | 83.5 | -4.0 | control | medium |
| 4 Icon family (rerun after fix) | 80.5 | 87.0 | +6.5 | treatment | high |
| 5 Landing page | 83.0 | 84.5 | +1.5 | treatment | medium |
| 6 SVG audit | 94.5 | 95.0 | +0.5 | treatment | low (near-tie) |
| 7 Evolve status page | 81.0 | 87.5 | +6.5 | treatment | medium |
| 8 Style selection | 86.0 | 91.5 | +5.5 | treatment | medium |

Mean delta (original 8): **+5.81**. Mean with the task-4 rerun substituted: **+7.12**. Wins: treatment 7/8 original, plus the rerun.

Decisive differences the judges cited for treatment wins: queue-first hierarchy and SOC-native operational signals (task 1); stronger 2-metre type scale, named sources, responsive root (task 2); near-zero connector crossings, full accessibility markup, drawing system verifiably executed (task 3); verified AA contrast where the control's claimed fix measured 2.9-4.2:1 (task 7); enforceable system detail: density tiers, semantic colour reservation, QA gates (task 8).

### The failure, its cause, and the fix (improvement loop)

Task 4 first run: the treatment's alert triangle was optically undersized against its gear, breaking family consistency (the brief's core demand). Cause: the SVG guidance demanded per-icon optical alignment but never demanded cross-glyph optical equalisation across a family. Smallest fix: one rule added to `references/svg-and-vector-graphics.md` (section 7) and one sentence to `workflows/svg-creation.md` step 6 (judge the family as a row; pointed/diagonal glyphs overshoot until visual mass matches). Rerun with a fresh agent and a fresh blind judge: treatment 87.0 vs control 80.5, high confidence, with the judge independently flagging in the control the exact failure class the fix targets. Caveat: different judges scored the two rounds, so the rerun establishes the fix works, not a precise delta.

### Objective check (task 6, sealed key)

9 core planted defects (duplicate id, dangling gradient ref, off-canvas element, label overflow, misaligned card, 1.6:1 contrast, colour-only status, missing accessibility markup, dead markup). Control found 9/9 plus a valid extra (missing font fallback). Treatment found 9/9 plus three valid extras (margin asymmetry, sparkline contrast, fixed root dimensions). Neither invented defects. This task is near ceiling for both conditions, which explains its +0.5 delta.

### Honesty of claims

Judges and spot checks found one claimed-but-failed verification: the control in task 7 stated contrast was fixed while measured pairs sat at 2.9-4.2:1. No treatment run claimed a check it had not performed; several explicitly listed unverified areas, as the skill requires. Two treatment DECISIONS files exceeded the 20-line cap by 1-2 lines (tasks 3 and 7): recorded as compliance misses.

### Efficiency

| Condition | Mean tokens/run | Mean duration |
|---|---:|---:|
| Control | 88,995 | 353 s |
| Treatment | 108,678 | 422 s |

The skill costs ~+22% tokens and ~+20% wall time per task (reading SKILL.md plus references). Judges cost a further ~81k tokens per task. For routine small tasks this overhead may not pay; for complex deliverables the quality deltas above came with it. Raw log: `evaluation/judging/usage-log.tsv`.

## Replication at n=3 (added after the first round; protocol unchanged)

Three representative tasks (1 dashboard, 3 diagram, 8 style selection) were re-run twice more per condition with fresh agents and fresh blind judges (A/B assignments pre-recorded in `evaluation/judging/replication-key.txt`). The skill had meanwhile gained the v1.1 modules, so replicates test the current skill; original-round scores are retained unchanged.

| Task | Round 1 | Rep 2 | Rep 3 | n=3 mean delta (sd) |
|---|---:|---:|---:|---|
| 1 SOC dashboard | +12.5 | +4.5 | +12.0 | +9.7 (4.5) |
| 3 Architecture diagram | +14.5 | +10.0 | +13.0 | +12.5 (2.3) |
| 8 Style selection | +5.5 | +2.0 | +2.5 | +3.3 (1.9) |

Treatment won all 9 replicated comparisons (two-sided sign test p = 2/512, about 0.004). Mean delta across the 9: +8.5 (sd 4.9). Reading: on complex artefact tasks the effect is large and consistent (the diagram task clears the +10 threshold on its own; the dashboard task sits at its edge); on advisory text tasks the baseline is already strong and the skill adds a small, consistent margin. One treatment defect surfaced by a replicate judge (hardcoded, non-reconciling KPI deltas) was recorded in `LESSONS.md`.

## General-audience round (2026-10-19; pre-registered separately in `evaluation/protocol-general.md`)

The original 8 tasks skewed towards cybersecurity subjects. This round tests whether the effect holds on everyday subjects, with three new tasks, fresh agents, and fresh blind judges; the A/B key was fixed by recorded coin flips and committed before any run executed.

| Task | Control | Treatment | Delta | Judge confidence |
|---|---:|---:|---:|---|
| G1 Home energy dashboard | 79.0 | 95.0 | +16.0 | high |
| G2 Recycling diagram | 88.5 | 93.5 | +5.0 | medium |
| G3 Farmers market poster | 91.0 | 95.5 | +4.5 | medium |

Treatment won 3/3; mean delta +8.5. Decisive judge findings: the G1 control hardcoded KPI figures separately from its data (including an unlabelled partial-month versus full-month cost comparison) and set most small text at a measured 3.5:1 contrast, below the AA floor, while the treatment derived every number from one data object and its contrast claims reproduced; the G2 treatment's pictograms explain each sorting mechanism and survive half-size rendering where the control's glyphs decorate; the G3 posters were both strong, with the treatment ahead on hierarchy at thumbnail size, accessibility wiring and verified robustness claims. One criterion went the other way: the G2 control completed the brief's "to baled output" arc with an explicit output strip the treatment lacked, recorded in `LESSONS.md`.

Reading against the thresholds: mean +8.5 is below the registered +10, so this round alone is again "Partially effective"; direction confirmed 3/3 on non-cyber subjects, with the dashboard task clearing the threshold outright. Round-specific caveats: the treatment G2 run was twice interrupted by infrastructure failures (timeout, machine sleep) before a fresh run completed, treatment G3 token usage went unrecorded for the same reason (`evaluation/judging/usage-log-general.tsv` holds what was recorded; the two complete pairs show treatment near cost parity, -4% and +11%), and the G1 control independently followed the environment's general charting guidance, making it a strong baseline rather than a bare model.

## Threshold outcomes (pre-registered)

- Activation-boundary negative tests: structural checks PASS (`disable-model-invocation: true` + mode-consistency test); live fresh-session trials NOT RUN (declared limitation).
- 64 catalogue entries present: PASS (automated).
- All 8 tasks executed in both conditions: PASS.
- No critical technical defects in declared-complete deliverables: PASS (all artefacts parsed and rendered; defects found were quality-level).
- No unsupported verification claims: PASS for treatment; one control violation noted above.
- Mean improvement >= +10: **FAIL overall** (+5.8 original, +7.1 post-fix; +8.5 across the n=3 replication set). Threshold kept as registered; verdict capped at Partially effective. The replication localises where the threshold IS met: diagram-class work (+12.5) and, at the margin, dashboard-class work (+9.7).
- No material regression in critical criteria: PASS post-fix (the one regression was visual consistency, found, root-caused, fixed and re-tested).

## Limitations (declared before running)

- n=1 run per condition per task; generation variance not averaged. Single LLM judge per task; blinding and randomised A/B order mitigate but do not remove judge bias.
- Both conditions ran in the same real environment: the control legitimately used the environment's other installed skills (it is a "normal agent" baseline, which makes this a comparison against a strong toolchain, not a bare model) and both could see the user's global memory; symmetric, so not a bias, but not a clean-room.
- The treatment prompt necessarily adds steering tokens ("read the skill first"); some benefit may come from that attention effect rather than skill content.
- The task-4 rerun used a different judge than the first round.
- The skill author designed the evaluation; independent human review has not occurred. Reproduce it: every prompt, artefact, score and key is in `evaluation/`.

## Changes made in response to findings

1. Cross-glyph optical equalisation rule added to the SVG reference and the svg-creation workflow (task-4 failure).
2. Evaluation evidence excluded from the style validator's scope (frozen artefacts are never edited retroactively).
3. Behavioural run log (`tests/behavioural-tests.md`) updated with evaluation outcomes; untested scenarios remain marked NOT RUN.
