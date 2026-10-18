# Workflow: UI/UX Implementation Audit

Review a built interface and its code for usability, visual consistency, responsiveness, accessibility and technical quality. Evidence-based; changes scoped to findings.

**Inputs:** the running interface (URL or local build) and read access to its code.
**Outputs:** ranked findings with file/line evidence; fixes applied only where asked, never a rewrite of unrelated code.
**Load:** [../references/ui-ux.md](../references/ui-ux.md), [../references/accessibility-and-quality.md](../references/accessibility-and-quality.md), [../references/design-evaluation.md](../references/design-evaluation.md).

## Steps

1. **Run the real thing.** Build and open the actual interface. If it cannot run, audit the code but state that interactive behaviour is unverified.

2. **Walk the primary tasks.** Identify the 2-3 jobs users came for and complete them: pointer, then keyboard only. Record friction, dead ends, missing feedback, surprising states.

3. **Audit states.** Empty, loading, error, success, long-content overflow, zero-data and huge-data. Most interfaces are designed for the happy medium and break at the edges.

4. **Audit consistency.** Spacing rhythm, type scale adherence, colour-role discipline, icon sizing, border radii, component variants that drifted apart. Measure; do not estimate.

5. **Audit responsiveness.** 360px, 768px, 1280px at minimum. Horizontal scroll at phone width, clipped controls, unusable touch targets, layouts that reflow into nonsense.

6. **Audit accessibility** per accessibility-and-quality.md sections 1-3: computed contrasts, focus visibility, keyboard reach, labels, reduced motion.

7. **Audit the code for fragility**, scoped to the UI layer: duplicated style values that should be tokens, magic numbers, z-index wars, state handled in three places, listeners leaking, oversized assets, render thrash. Cite file:line for every claim.

8. **Rank and label.** Consequence order; CONFIRMED vs PLAUSIBLE; defect vs preference (per [critique.md](critique.md)).

9. **Fix within scope.** When fixes are requested, change only what a finding justifies. Match the codebase's existing idiom. Do not reformat, rename or "improve" untouched code; do not replace working functionality to make it prettier.

10. **Re-verify each fix** in the running interface, not just in the diff.

## Gate

Done only when: the interface was actually exercised (or its absence declared); every finding has evidence a reader can check; applied changes map one-to-one to findings; nothing unrelated changed. An audit that proposes a redesign instead of findings has failed.
