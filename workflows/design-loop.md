# Workflow: The Design Loop and Dynamic Depth

Design work here is never one pass. Every deliverable moves through a loop, and the loop's depth scales to the stakes, chosen deliberately and said out loud.

**Inputs:** the brief (or workflows/new-design.md output), the chosen depth.
**Outputs:** the deliverable plus a loop record: what each pass found and changed, and the gate result.
**Load:** [../references/design-evaluation.md](../references/design-evaluation.md); for crew work, [../agents/README.md](../agents/README.md).

## The loop

1. **Make** the artefact (or the next revision of it).
2. **Verify**: structural validation, then render and inspect (the PIXEL discipline: target size and smaller, light and dark when destination is unknown).
3. **Critique** against the brief's weighted criteria (the ROAST discipline): findings by consequence, confirmed vs taste.
4. **Decide**: fix and loop again, or stop. Stop when the gate passes, or when a full pass produces only taste-level findings (diminishing returns), or when a constraint (time, budget) is hit, stated honestly.
5. **Record** one line per pass: what the render exposed, what changed. The record is the proof the loop ran.

Two consecutive passes with no confirmed findings means stop; polishing past that point is vanity, not quality.

## Depth tiers (dynamic by stakes, not by enthusiasm)

| Tier | When | What runs |
|---|---|---|
| **Sketch** | small, reversible, low-stakes: an icon tweak, a colour swap, a quick opinion | one pass, self-verified; no crew, no ceremony |
| **Studio** | a real deliverable one person will ship: a page, a diagram, an icon set, a poster | the full loop solo, 2-4 passes; crew only if one station is genuinely weak (e.g. spawn RAMP for a compliance-bound UI) |
| **Flagship** | brand-defining, expensive to reverse, or the user asked for the works | SCOUT brief first; parallel exploration ([parallel-exploration.md](parallel-exploration.md)) for direction; FORGE builds; PIXEL, ROAST and RAMP verify in parallel; PENNY signs off the trade-offs |

Choose the tier in one line at the start ("Studio depth: shipping artefact, moderate stakes") so the user can override it. Upgrading a tier mid-task is fine when findings justify it; silently running Flagship ceremony on a Sketch task is a defect. Agent spawning follows the cost discipline in `../agents/README.md`.

## Gate

The loop is done only when: the final pass's confirmed findings are zero or explicitly accepted by the user; the loop record exists; and anything unverified is named. A deliverable with no loop record did not go through this workflow.
