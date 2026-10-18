# Design Evaluation: Rubric and Critique Method

How to score design work and deliver critique that improves it. Use this file whenever the task is CRITIQUE, AUDIT, DECIDE, or the self-review step of any creation workflow.

## 1. Default scoring rubric

Score each criterion 1-10, multiply by its weight, sum for a weighted total out of 10. The weights below are a starting point, not universal truths.

| Criterion | Default weight | What it measures |
|---|---:|---|
| Functional suitability | 20% | Does the design achieve its stated purpose for its actual users? Task completion, fitness for context, correctness of priorities. |
| Visual hierarchy and composition | 15% | Does the eye land where it should? Order of reading, grouping, balance, use of space. |
| Usability and accessibility | 15% | Can real people, including those with impairments, use it? Contrast, affordances, feedback, error tolerance. |
| Originality and differentiation | 15% | Is this distinguishable from a template or a competitor? Does it have a defensible identity? |
| Craft, precision and consistency | 10% | Alignment, spacing rhythm, geometric consistency, finish quality, absence of sloppy detail. |
| Context and brand alignment | 10% | Does the visual language fit the product, audience, culture and brand system it lives in? |
| Technical feasibility and performance | 10% | Can it be built and maintained? Rendering cost, responsiveness, implementation fragility. |
| Longevity and maintainability | 5% | Will it survive the current trend cycle? Can it be extended without collapse? |

## 2. Reweight by domain

Adjust weights before scoring, and state the adjusted weights in the assessment. Three worked examples:

**Safety-critical instrumentation** (cockpit displays, medical monitors, industrial control):

| Criterion | Weight |
|---|---:|
| Functional suitability | 30% |
| Usability and accessibility | 25% |
| Visual hierarchy and composition | 20% |
| Technical feasibility and performance | 15% |
| Craft, precision and consistency | 10% |
| Originality and differentiation | 0% |
| Context and brand alignment | 0% |
| Longevity and maintainability | 0%* |

*Longevity folds into feasibility here; originality is actively dangerous when it breaks operator expectations.

**Expressive art poster** (gallery, festival, cultural event):

| Criterion | Weight |
|---|---:|
| Originality and differentiation | 30% |
| Visual hierarchy and composition | 25% |
| Context and brand alignment | 15% |
| Craft, precision and consistency | 15% |
| Functional suitability | 10% |
| Usability and accessibility | 5% |
| Technical feasibility and performance | 0%** |
| Longevity and maintainability | 0% |

**A poster must still be legible at viewing distance and reproducible by the intended print process; fold those checks into functional suitability.

**Enterprise SaaS product**:

| Criterion | Weight |
|---|---:|
| Functional suitability | 25% |
| Usability and accessibility | 20% |
| Technical feasibility and performance | 15% |
| Longevity and maintainability | 15% |
| Visual hierarchy and composition | 10% |
| Craft, precision and consistency | 10% |
| Context and brand alignment | 5% |
| Originality and differentiation | 0-5% |

The pattern: move weight towards the consequences of failure. When failure harms people, function and usability dominate. When failure is forgettability, originality dominates.

## 3. Assessment requirements

Every scored assessment must:

1. **Explain each score.** One or two sentences per criterion. A number without a reason is noise.
2. **Cite observable evidence.** Point at the artefact: "the severity badge and the status chip use the same red", "body text measures 11px over a photograph", "the third card breaks the 8px spacing rhythm". Never score from a general impression.
3. **Name the three highest-impact improvements.** Ranked, specific, and actionable. If the reviewer cannot name three, say so rather than padding.
4. **Separate critical defects from subjective preference.** A critical defect breaks function, safety, accessibility or comprehension. A preference is a judgement call another competent designer could reasonably reverse. Label them differently and never mix them in one list.
5. **Never present aesthetic judgement as precise science.** Scores on originality, composition and brand fit are structured opinion. Say so. Contrast ratios, tap target sizes and render costs are measurable. Treat the two kinds of claim differently.
6. **Apply the override rule.** A high visual score never compensates for a serious safety, usability or functional failure. If such a failure exists, the overall verdict is "not acceptable until fixed", whatever the weighted total says. State the total anyway, then state the override.

## 4. Critique method

Order of work when critiquing an existing design:

1. **Establish intent first.** What was this trying to do, for whom? Critique against its own goals, not against the reviewer's taste. If intent is unknowable, state the assumption being used.
2. **Inspect before judging.** Look at the actual artefact, at real size, in its real context (device, print, distance, lighting) where possible. For implementations, interact with it; a screenshot hides half the defects.
3. **Collect findings, then rank by consequence.** Lead with what loses users, money or safety. Spacing nitpicks come last, however satisfying they are to spot.
4. **Write concrete fixes, not adjectives.** Not "the hierarchy feels weak" but "the page title (18px/400) is lighter than the card headings (16px/600); either promote the title or demote the cards". Every finding names the element, the problem, the consequence and at least one fix.
5. **Mark confidence.** CONFIRMED: verified by measurement, interaction or reproduction (a contrast ratio computed, a broken flow walked through, a clipped element rendered). PLAUSIBLE: visible in inspection but not verified end to end, or dependent on context the reviewer lacks. Never report a PLAUSIBLE finding in CONFIRMED language.
6. **Acknowledge what works.** One short paragraph. Not flattery: it tells the designer what to preserve while fixing the rest, which is operationally useful.
7. **Close with the three highest-impact improvements** (section 3.3) and, where scoring was requested, the reweighted rubric table with the override rule applied.

## 5. Anti-patterns in critique

- Scoring without looking (critique from the description of a design rather than the design).
- Laundry lists with no ranking, forcing the reader to guess what matters.
- Taste presented as defect ("I would have used a serif").
- Vague praise or vague damnation ("feels premium", "looks dated") with no evidence.
- Rewriting the designer's intent instead of evaluating against it.
- Inflating confidence: reporting unverified suspicions as findings.
- Letting beauty excuse failure, or failure excuse ignoring genuinely good craft.

Related: [accessibility-and-quality.md](accessibility-and-quality.md) for measurable gates, [../workflows/critique.md](../workflows/critique.md) for the step-by-step procedure.
