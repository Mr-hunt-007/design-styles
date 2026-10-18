# Workflow: Design Critique

Evaluate an existing design (interface, image, product, layout, SVG) and deliver ranked, evidence-based findings.

**Inputs:** the artefact (file, URL, screenshot, code) and, if available, its intent and audience.
**Outputs:** ranked findings with fixes, a scored rubric when requested, three highest-impact improvements.
**Load:** [../references/design-evaluation.md](../references/design-evaluation.md) (mandatory), [../references/accessibility-and-quality.md](../references/accessibility-and-quality.md), plus the discipline reference matching the artefact.

## Steps

1. **Recover intent.** What is this for, who uses it, what does success look like? Ask the user if unstated and consequential; otherwise record the assumption. Critique against intent, never against personal taste.

2. **Inspect the real artefact.** Open the file, render the page, run the build, zoom the image. For interfaces, interact: click, tab, resize, trigger error states. Note what inspection method was actually available; it bounds the confidence of every finding.

3. **Reweight the rubric** for the domain (design-evaluation.md section 2) and state the weights.

4. **Collect findings across the checklist:** hierarchy, spacing and proportion, geometric consistency, decoration without purpose, generic or derivative styling, contrast and accessibility, interaction clarity, material appropriateness, visual noise, implementation fragility, performance, mismatch between visual language and purpose.

5. **Verify what can be verified.** Compute contrasts, measure spacings, walk flows, reproduce breakages. Mark each finding CONFIRMED or PLAUSIBLE.

6. **Rank by consequence.** Safety and task failure first, then comprehension, then craft. Label each finding as critical defect or preference.

7. **Write fixes.** Element, problem, consequence, concrete fix. No adjectives standing alone.

8. **Score (when requested).** Rubric table with per-criterion reasons and evidence. Apply the override: serious safety, usability or functional failure caps the verdict at "not acceptable until fixed" regardless of the weighted total.

9. **Preserve the good.** One paragraph naming what works and must survive the fixes.

10. **Deliver:** ranked findings, the three highest-impact improvements, scores if asked, and a confidence statement (what was inspected, what could not be).

## Gate

Done only when: every finding cites observable evidence; CONFIRMED and PLAUSIBLE are separated; defects and preferences are separated; the top three improvements are specific enough to act on today. A critique that reads as a list of adjectives has failed this gate.
