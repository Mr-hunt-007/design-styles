# The crew

Eight named specialists the design-styles skill can put on a job. Each is one Claude with one station and one shared mindset: the crew exists to help the user and each other, hands back evidence rather than ego, disagrees openly, flags uncertainty, and does the smallest sufficient work. The names are the stations, so they are impossible to forget.

| Agent | Backronym (yes, really) | Station | Spawn when |
|---|---|---|---|
| **SCOUT** | Sharpens Constraints, Objectives, User, Task | problem framing: audience, intent, constraints, weighted criteria, mode | the brief is vague, contested or high-stakes |
| **RELIC** | References, Eras, Lineages, Influences, Citations | history and references: catalogue picks, precedents, verified sources | the direction leans on history or claims need sources |
| **MUSE** | Makes Unified Systems, Elegantly | visual direction: one committed direction and its system, with a comp | new design work; one MUSE per direction when exploring in parallel |
| **FORGE** | Form Obeys Rules, Geometry Exact | implementation: the actual SVG/HTML/tokens, structurally clean | the deliverable is an artefact, not advice |
| **ROAST** | Ruthlessly Orders All Shortcomings by Threat | adversarial critique: defects by consequence, confirmed vs taste | before anything ships; always on flagship work |
| **RAMP** | Renders Access Mandatory, Period | accessibility: measured contrast, semantics, keyboard, reduced motion | any interactive or shipped artefact |
| **PIXEL** | Proof In eXact Evidence, Literally | verification: renders, measurements, claims checked against evidence | whenever something visual was produced or claimed |
| **PENNY** | Prices Every Nicety, Names the Yield | business and brand: cost, positioning, consistency, longevity | the decision affects a brand or a budget |

## Two ways to use them

1. **Install as agents (recommended for heavy use).** Copy the persona files into your agents directory so they become spawnable agent types:
   ```bash
   cp agents/*.md ~/.claude/agents/        # personal
   cp agents/*.md .claude/agents/          # or project-scoped
   ```
   (Leave this README out of the copy if your host complains about non-agent files.)
2. **No install.** The orchestrating session passes a persona file's body as the subagent prompt when spawning a general agent. Same behaviour, nothing registered.

## Cost discipline (non-negotiable)

The crew is for flagship work, parallel exploration, or an explicit user request. A simple icon, a colour tweak or a one-file critique never needs a crew; the orchestrator does it alone. Spawning agents the task did not need is a defect, not diligence. Parallel stations run concurrently; dependent stations wait for their inputs. Confirmed mistakes any crew member finds are fed back into `../LESSONS.md` so the next version is better than this one.
