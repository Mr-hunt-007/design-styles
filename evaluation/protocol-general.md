# Evaluation protocol: general-audience round (pre-registered)

Written and fixed 2026-10-19, before any run of this round was executed. Rubric, tasks, A/B key and thresholds below were not changed after seeing results. This round exists because the original 8 tasks skewed towards cybersecurity subject matter; it tests whether the measured effect holds on everyday, general-audience subjects.

## Method

Identical to `protocol.md`: fresh control agent receives the brief only; fresh treatment agent receives the same brief prefixed with an instruction to first read `SKILL.md` and follow it; one run per condition per task; per task one fresh blind judge scores artefact sets at neutral paths A and B against the same weighted rubric (`protocol.md`, "Scoring rubric"), rendering before scoring. The A/B key is fixed below, assigned by recorded coin flips before any run.

## Tasks (briefs given verbatim to both conditions)

- **G1 Home energy dashboard:** a household energy dashboard for the fictional Harper family; single self-contained `energy.html` with inline placeholder data; must communicate current usage, a 7-day usage trend, solar generation versus grid draw, cost this month versus last, the top energy-using appliances, and one actionable alert; must work in light and dark and at 400px width; plus `DECISIONS.md` (max 20 lines).
- **G2 Recycling diagram:** `recycling.svg` (viewBox 0 0 960 600, self-contained, no external references) explaining to a general audience how household recycling is sorted at a materials recovery facility, from kerbside bin to baled output, with grouped stages, labelled connectors and two annotated callouts (what contaminates a batch; where glass ends up); plus `DECISIONS.md`.
- **G3 Farmers market poster:** A3 portrait single self-contained `poster.svg` announcing the season opening of the fictional Greenfield Saturday Farmers Market; must communicate dates, time and place and six stall categories; clear hierarchy readable from 2 m; text must survive rasterisation on a machine without webfonts; plus `DECISIONS.md`.

## A/B assignment key (coin flips recorded before any run; 1 = A is treatment)

Flips: g1=1, g2=0, g3=0. Therefore: **G1: A = treatment, B = control. G2: A = control, B = treatment. G3: A = control, B = treatment.**

## Decision thresholds (fixed in advance)

- All 3 tasks executed in both conditions, or explicitly marked blocked.
- No critical technical defects (render failure, XML parse failure) in deliverables declared complete; no unsupported verification claims (spot-checked).
- Mean improvement >= +10/100 across the 3 tasks with no material regression on any task: "Effective on general-audience tasks". Positive mean below +10: "Partially effective". Otherwise "Not effective" or "Inconclusive".
- Same declared limitations as `protocol.md`: n=1 per condition per task, one LLM judge per task, treatment prompt necessarily adds steering tokens.
