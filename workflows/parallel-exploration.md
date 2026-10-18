# Workflow: Parallel Exploration (superposition and collapse)

For direction-defining work, do not bet on the first idea. Hold several genuinely different directions open at once, develop each to the point where it can be judged on evidence, then collapse to one. The metaphor is quantum; the mechanics are parallel agents and a blind-ish judging pass. It buys breadth with tokens, so it is reserved for Flagship-tier work or an explicit user request (see [design-loop.md](design-loop.md)).

**Inputs:** a sharp brief (SCOUT's output or equivalent) with weighted criteria.
**Outputs:** one chosen direction with comps, a ranked comparison with reasons, and the rejected directions kept as records.
**Load:** [../agents/README.md](../agents/README.md), [../references/design-evaluation.md](../references/design-evaluation.md).

## Steps

1. **Define the spread.** Choose 2-4 candidate directions that are genuinely different answers to the brief, not shades of one idea (different primary principle, not different accent colour). Name each in one sentence. If only one credible direction exists, say so and skip this workflow; forcing a spread wastes the user's tokens.

2. **Fan out.** One MUSE per direction, spawned in parallel, each with the same brief and ONLY its own direction. Each commits fully: visual system plus a real comp (HTML/SVG), self-verified structurally. MUSEs do not see each other's work; convergence now is contamination.

3. **Render everything.** PIXEL (or the orchestrator applying the PIXEL discipline) renders all comps identically: same sizes, same backgrounds, side-by-side sheet where practical.

4. **Collapse.** ROAST judges the candidates against the brief's weighted criteria, on the renders plus source, and commits to a ranking with evidence. Where the brief allows, present candidates to the judge with neutral labels so the ranking argues from the work, not its authorship. PENNY weighs in only where business trade-offs separate close candidates.

5. **Decide and fold in.** Pick the winner (the user picks when they are present; otherwise recommend with the ranking attached). Fold in at most one or two specific strengths from losing candidates ONLY where they serve the winner's principle; grafting features from every candidate rebuilds the compromise this workflow exists to avoid.

6. **Continue in the loop.** The winning direction enters the standard design loop ([design-loop.md](design-loop.md)) for build and refinement. Keep the losing comps and the ranking in the record: they are the proof of why this direction, and the first place to return if it fails.

## Gate

Done only when: each candidate was a real rendered artefact (never a description), the ranking cites evidence per criterion, the choice names what it rejected and why, and the total agent spend was declared at the start. Two candidates judged well beats four candidates judged lazily.
