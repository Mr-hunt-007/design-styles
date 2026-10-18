# Workflow: Cross-Disciplinary Principle Transfer

Borrow a principle from one discipline to improve a design in another, without surface imitation.

**Inputs:** a design task in progress, plus the suspicion that another discipline has solved a structurally similar problem.
**Outputs:** adapted principles woven into the design, with the transfer decisions explained.
**Load:** [../references/cross-disciplinary-design.md](../references/cross-disciplinary-design.md) (mandatory), plus the source-discipline reference (aerospace-and-instrumentation.md, architecture.md, horology.md, art-and-composition.md, industrial-design.md, typography-and-graphics.md).

## Steps

1. **Understand the actual problem.** What is failing or missing in the current design: prioritisation, rhythm, precision, atmosphere, trust, density management?

2. **Name the requirement, not the discipline.** "Operators must spot the one abnormal value among forty in under a second" is a requirement. "Make it feel aerospace" is not.

3. **Identify candidate source disciplines.** Which fields have solved this requirement under harsher constraints? Use the worked mappings in cross-disciplinary-design.md as a starting point, then look beyond them; the mappings are examples, not a menu.

4. **Extract the principle.** State it in one medium-neutral sentence. Example: cockpit design yields "normal state is visually quiet; only deviation earns colour and motion", not "add bezels and warning stripes".

5. **Adapt to the target medium.** Translate the principle into the target's native elements (CSS states, grid columns, stroke weights, type scale). The adaptation must be unrecognisable as costume and recognisable as logic.

6. **Run the anti-forcing check.** Answer honestly: (a) does this transfer solve the step-1 problem better than a conventional approach? (b) does it add implementation or cognitive complexity? (c) would removing it make the design worse? If (a) is no or (c) is no, drop the transfer. Simple tasks usually need zero transfers; forcing influences into a plain icon or a basic form is a failure mode of this skill.

7. **Check coherence.** Multiple transfers must resolve into one visual system with one hierarchy. If the result reads as several styles placed together, cut transfers until it reads as one design.

8. **Explain.** Report only the transfers that survived: source principle, why it fits, how it was adapted. Do not catalogue the influences considered and discarded unless asked.

## Principle transfer vs aesthetic borrowing

- **Transfer (default):** the source's reasoning improves the target's function. Invisible as a reference, visible as quality.
- **Borrowing (exception):** the source's look is itself the point (a retro-futurist poster, a cockpit-themed game UI). Legitimate only when the intended identity calls for it, and it must still pass usability gates.

Label which one you are doing. Mixing them unawares produces themed clutter.

## Gate

Done only when: each surviving transfer maps requirement → principle → adaptation; the anti-forcing check ran; the result reads as one coherent system. A deliverable that needs its influences listed to be understood has failed the coherence check.
