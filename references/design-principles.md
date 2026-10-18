# Durable Design Principles

Twenty permanent principles, a method for resolving conflicts between them, and rules for keeping knowledge current. These are the stable core of the skill; everything in `style-catalogue.md` and `design-history.md` is reference material that serves them.

## The twenty principles, expanded

**1. Function informs form, but emotional meaning matters too.**
Start from what the artefact must do, then ask what it must mean. A hospital wayfinding sign optimised purely for legibility but rendered in a cold institutional voice fails the frightened visitor it serves. Braun radios work no better for their proportions, yet the proportions are why people kept them for decades.

**2. Aesthetic simplicity does not require functional simplicity.**
A calm surface can govern deep capability. A search box backed by a sophisticated query engine is the canonical case: one field, enormous function. The error is the inverse, stripping capability to achieve a minimal look.

**3. Every visual element should have a defensible purpose.**
In review, challenge each element: what breaks if it is removed? If nothing, remove it or admit it is decoration and justify the decoration. A divider line that separates nothing is noise; the same line separating billing from shipping is structure.

**4. Whitespace is an active compositional element.**
Space assigns importance, groups related items and paces reading. The margin around a headline is doing work; halving it changes the headline's rank. Budget space deliberately, as the Japanese concept of ma treats interval as content (see `design-history.md`).

**5. Contrast should establish hierarchy, not merely decoration.**
Every contrast (size, weight, colour, position) is read as a signal of importance. Decorative contrast that outranks the actual priority misleads the reader: a bright promotional badge louder than the error message is a hierarchy bug, not a style choice.

**6. Material choices affect both performance and perception.**
A material (or its digital analogue: texture, blur, shadow, motion) carries connotation and cost simultaneously. Translucent glass layers read premium but tax contrast and rendering. Choose materials for both what they do and what they say, and never fake one that must perform.

**7. Proportion can matter more than ornament.**
A plain rectangle at the right ratio outperforms an ornamented one at the wrong ratio. Watch dials and classical facades (see `horology.md`, `architecture.md`) demonstrate that perceived quality lives mostly in relationships between dimensions. Fix proportion before reaching for decoration.

**8. Consistency creates coherence, but excessive uniformity can remove character.**
Systems need rules and need sanctioned exceptions. If every card, page and chart is identical, nothing can be emphasised and the product loses voice. Define where the system bends (hero moments, empty states, campaign surfaces) as explicitly as where it holds.

**9. Accessibility is a design requirement, not a finishing step.**
Contrast, target size, focus order, motion tolerance and semantics shape layout and palette decisions, so they must enter at the first sketch. Retrofitting accessibility is more expensive and usually visibly worse than designing with it. Standards live in `accessibility-and-quality.md`.

**10. Engineering constraints should inform creative decisions early.**
Tolerances, rendering budgets, CMS realities and manufacturing methods are design inputs, not obstacles discovered at handoff. Thonet's chair and the Eames shells are celebrated precisely because the process constraint generated the form.

**11. Historical references are sources of principles, not templates to copy.**
Study why a movement worked, then apply the reasoning to today's problem. Copying the artefact produces pastiche dated to the year of copying. Each entry in `design-history.md` ends with an "apply without imitation" note for this reason.

**12. Novelty is not the same as innovation.**
Innovation solves a real problem in a new way; novelty is difference for its own sake. A new navigation pattern that users must learn, with no payoff, is novelty wearing innovation's clothes. Test: what improves, for whom, measurably?

**13. Expensive-looking design is not necessarily good design.**
Gloss, depth effects and premium cues can mask weak hierarchy and poor flows. Judge against task success and longevity, not perceived production cost. Dark Luxury styling on a confusing checkout is lipstick on a funnel leak.

**14. A beautiful interface that fails its users is unsuccessful.**
Usability outranks aesthetics whenever they genuinely conflict (they rarely do when the work is good). The rubric in `design-evaluation.md` enforces this: no visual score compensates for task failure.

**15. A technically correct product can still fail through poor communication.**
Accuracy without hierarchy, naming or narrative loses the user anyway. A correct chart with an unreadable legend communicates nothing. Design the explanation as part of the artefact.

**16. Different contexts demand different definitions of quality.**
A cockpit display, an art poster and a children's app each weight legibility, expression and safety differently. Fix the quality criteria per project before judging anything (step 3 of the operating loop in `../SKILL.md`).

**17. The absence of decoration can be as intentional as decoration itself.**
Restraint is a decision with reasons, not a default to hide behind. Be able to say why the surface is quiet (focus, trust, longevity), or the minimalism is just emptiness. See Minimalism versus emptiness in `styles/foundation.md`.

**18. Design decisions should be reversible where uncertainty is high.**
When evidence is thin, prefer choices that are cheap to change: tokens over hard-coded values, a theme over a rebrand, a pilot over a rollout. Spend irreversibility only on validated certainty.

**19. The best design may be invisible when it makes a difficult task feel effortless.**
If users cannot say why something felt easy, the design is working. Resist adding visible cleverness that claims credit at the cost of friction.

**20. Long-term relevance comes from sound principles, not resistance to all change.**
Timelessness is not stasis. Rams-era Braun endures because the reasoning holds, not because it refused every new material. Update expressions freely; change principles only with evidence.

## Resolving conflicts between principles

Principles collide constantly (consistency vs character, simplicity vs capability, expression vs accessibility). Resolve by requirement, not by taste:

1. **Restate the actual requirements.** Who uses this, for what, under what constraints, with what success measure? Most "principle conflicts" dissolve here because one principle turns out not to apply.
2. **Order the non-negotiables.** Safety, legal and accessibility requirements rank first, always. Task success ranks above brand expression; brand expression ranks above personal preference.
3. **Name the trade-off explicitly.** "Larger type improves legibility but costs one row of data per screen" is decidable; "cleaner vs richer" is not.
4. **Prefer the resolution that satisfies both partially over the one that satisfies one totally,** unless a non-negotiable forces totality. A slightly denser Swiss grid often beats choosing between density and order.
5. **Check reversibility (principle 18).** Under uncertainty, pick the option that is cheaper to unwind, and say so.
6. **Record the decision and its reason** so the next person inherits the rationale, not just the artefact.

## Knowledge maintenance: durable versus time-sensitive

Treat these two classes differently in every answer.

**Durable knowledge** (apply with confidence, rarely changes):
- Colour relationships: hue contrast, value structure, simultaneous contrast, the primacy of value over hue for legibility.
- Proportion and composition: grids, ratios, optical correction, focal hierarchy.
- Human factors fundamentals: reach, legibility distance, reaction time, cognitive load, error-prevention patterns.
- Manufacturing fundamentals: tolerance thinking, material behaviour classes, assembly logic.
- Accessibility principles: perceivable, operable, understandable, robust as goals.
- The historical record itself (what happened), as distinct from its fashion.

**Time-sensitive knowledge** (verify before relying; date every claim):
- Current interface conventions and platform guidelines (iOS/Android/web norms shift in years, not decades).
- Specific standards versions and legal thresholds (e.g. WCAG version in force, regional regulations): name the version you are applying and check for updates when stakes are high.
- Material and component availability, pricing, lead times.
- Tool and library capabilities, browser support tables.
- Trends and style popularity. A new trend is not automatically an improvement; evaluate it against the durable principles above before adopting it.

Rules: when research tools are available, verify time-sensitive claims rather than recalling them; write "as of <date>" on any claim likely to expire; never present interpretation as documented fact; and never claim this skill's knowledge is permanent or unlimited. When a reference here conflicts with a current verified standard, the verified standard wins and this file should be updated.
