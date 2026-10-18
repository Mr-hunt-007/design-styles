# Workflow: New Design Direction

Create a design direction from a problem statement. This is the 10-step decision engine applied end to end.

**Inputs:** problem statement, audience, constraints, expected deliverable (direction, mock, spec, code, brief).
**Outputs:** the deliverable itself plus a short rationale covering direction, system choices and trade-offs.
**Load:** [../references/design-principles.md](../references/design-principles.md), [../references/style-catalogue.md](../references/style-catalogue.md); domain file as classified in step 2; [../references/cross-disciplinary-design.md](../references/cross-disciplinary-design.md) at step 4.

## Steps

1. **Understand the problem.** Write one sentence each for: purpose, user, context of use, business goal, hard constraints. No visual vocabulary allowed yet. If one missing fact materially changes the outcome, ask one focused question; otherwise state assumptions and proceed.

2. **Classify the domain.** UI/UX, product, visual communication, architecture, art, technical visualisation, brand, or a combination. Load the matching discipline reference (ui-ux.md, industrial-design.md, architecture.md, art-and-composition.md, aerospace-and-instrumentation.md, horology.md, typography-and-graphics.md).

3. **Establish criteria.** Pick and reweight the rubric from [../references/design-evaluation.md](../references/design-evaluation.md) for this domain. These weights are the definition of success for everything that follows.

4. **Explore references.** Shortlist 2-4 styles or movements from the catalogue and 1-3 cross-disciplinary principles that plausibly serve the criteria. For each, note the principle it contributes, not its look. Discard any reference that only adds sophistication-signalling.

5. **Select the direction.** One primary direction, at most two supporting influences. Write the sentence: "Primary X because [criterion]; supported by Y for [specific job]; rejected Z because [conflict]." If that sentence cannot be written honestly, the selection is not done.

6. **Define the visual system.** Only the elements this deliverable needs: composition and grid, geometry and proportion, colour palette with roles, typography with scale, materials and texture, lighting and depth, motion and interaction, density and whitespace, component behaviour, accessibility baseline. Each choice traces to a criterion from step 3.

7. **Produce the deliverable.** Build the thing asked for. A direction request gets a direction document with enough specificity to act on (tokens, example compositions). A mock request gets the mock. Do not substitute a description for an artefact.

8. **Self-critique.** Run the critique method from design-evaluation.md section 4 against your own output. Fix the top findings before showing anything.

9. **Validate.** Run the applicable gates from [../references/accessibility-and-quality.md](../references/accessibility-and-quality.md). For visual artefacts, render and inspect ([implementation-verification.md](implementation-verification.md) or [svg-creation.md](svg-creation.md)).

10. **Explain.** Deliver with: the direction sentence from step 5, the 3-5 most consequential system decisions and why, known trade-offs, and what was validated versus unverified.

## Gate

Done only when: the deliverable exists and matches the request; every major visual choice traces to a stated criterion; conflicting styles were named and excluded; validation ran or its absence is documented. If any of these fail, return to the failing step.
