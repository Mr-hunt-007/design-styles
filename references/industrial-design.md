# Industrial Design and Product Engineering

A product should feel intentional from every viewing angle, at every distance, in the hand and over years of use. Industrial design is the discipline of reconciling what a thing must do, how it is made, and what it means to the person who owns it.

## Form and function

- Function sets the envelope; within that envelope, form carries emotional and cultural meaning. A kettle that pours badly is a failure; two kettles that pour equally well can still differ enormously in what they say about their owner.
- Honest form: the shape should express what the object is and how it works. Fake vents, decorative screws and applied "tech" styling erode trust.
- Reduction is a tool, not a religion. Remove until the object stops working or stops communicating, then restore the last thing.
- Every surface, parting line, radius and transition is a decision. If you cannot defend it, it is noise.

## Ergonomics and human factors

- Design for the hand before the eye: grip diameter, texture where fingers land, weight and balance around the natural hold point.
- Reach and posture: controls fall where the hand already is; frequent actions need no regrip; the object works for small and large hands, left and right.
- Tactile feedback: detents, travel, resistance and click communicate state without looking. A control that feels vague reads as cheap and causes errors.
- Weight is a message: heft can signal quality in a tool and failure in a wearable. Decide what weight should say, then engineer it.
- Test with bodies, not renders: the first physical mock-up (even foam) reveals more than any viewport.

## Materials, finishes and manufacturing

- Choose material for load, wear, temperature, feel and meaning together. Aluminium, polycarbonate, steel, glass and wood each carry cultural readings as strong as their datasheets.
- Finish changes the material's meaning: bead-blasted vs polished aluminium are different products.
- Material honesty: let materials look like what they are. Chrome-painted plastic ages into embarrassment.
- Know the process before drawing the form: injection moulding wants draft angles and uniform wall thickness; machining wants accessible tool paths; sheet metal wants bend radii. The process constraints are design inputs, not later corrections.
- Every cosmetic surface has a cost. Spend finish quality where hands and eyes actually go.

## Assembly, tolerances and serviceability

- Parts must locate themselves: chamfers, keying, asymmetry that prevents wrong assembly.
- Tolerances stack. A gap that is "0.2 mm nominal" will be 0.5 mm somewhere in production; design gaps and shut lines to look intentional at worst case.
- Consistent, even gaps read as precision; varying gaps read as defect, even when functional.
- Serviceability is a design feature: fasteners over glue where repair matters, wear parts accessible, batteries replaceable where the lifecycle demands it.

## Durability, repairability and lifecycle

- Design for the tenth year, not the unboxing: how do the materials wear, scratch, patina, discolour?
- Graceful ageing beats fake permanence: leather and brushed metal improve with use; glossy plastic only degrades.
- Repairability, spare-part availability and disassembly for recycling are lifecycle decisions made at the sketch stage, not the end.
- An object someone wants to keep for decades is the most sustainable object. Desirability is an environmental strategy.

## Product family identity

- A family shares a design language: consistent radii, control logic, materials, graphics and proportional rules, scaled to each product's job.
- Identity lives in the invariants: decide which three or four features make the product recognisable with the logo removed, and protect them across the range.
- Consistency is not cloning: each family member solves its own ergonomic and functional problem inside the shared language.

## Evaluation checklist

1. Pick it up (or imagine the first physical interaction): is the first touch where the design wants it?
2. Walk around it: does any angle look unconsidered or accidental?
3. Question every element: what does this line, vent, radius or graphic do?
4. Check honesty: any material pretending to be another, any functionless styling?
5. Check the process fit: can this form actually be moulded, machined or formed as drawn?
6. Check wear: where will it scratch, stain and dent first, and how will that look?
7. Check the family: would this sit beside its siblings as a relative, not a stranger?

## Common failure modes

- **Render-driven design**: forms that only work from the hero angle; walk the full turntable.
- **Styling applied late**: a functional chassis "skinned" at the end always looks skinned. Integrate from the first sketch.
- **Unresolved junctions**: where two surfaces, materials or radii meet without a decision; junctions are where quality is judged.
- **Radius soup**: many similar-but-unequal radii on one product; define a radius family (e.g. 2, 6, 16 mm) and stay inside it.
- **Feature creep in form**: a crease or chamfer for every function; the strongest products spend their formal moves on one or two ideas.
- **Ignoring the worn state**: products are judged after a year of scratches, grease and sunlight, not in the box.
- **Specification theatre**: quoting materials and processes as marketing rather than engineering; if the material claim does not change the user's outcome, it is decoration.

## Materials as meaning (quick reference)

- Machined aluminium: precision, tool, considered cost.
- Stainless steel: permanence, hygiene, professional duty.
- Polycarbonate / ABS: lightness, affordability; quality lives in texture and wall consistency.
- Glass: honesty and fragility; signals confidence in what is behind it.
- Wood and leather: warmth, domesticity, ageing as a feature.
- Rubber and elastomers: grip, safety, serviceability; degrade fastest, plan replacement.

These are cultural defaults, not laws; subverting them is a legitimate statement when deliberate.

## Transferable principles

- Material honesty transfers to digital surfaces: do not render fake textures, fake depth or fake mechanisms that promise behaviour the product does not have.
- Tolerance thinking transfers to layout: design spacing systems that still look intentional at worst case (long labels, translations, missing images).
- Ergonomics transfers to interfaces: put frequent controls where the hand or thumb already is; make targets and travel feel right, not just look right.
- Parting lines and shut lines teach seam discipline: in UI, the joins between components (borders, radii, spacing) are where quality is read.
- Family identity transfers directly to design systems: define the invariants that survive across screens, documents and media.
- Designing for the tenth year transfers to brands and codebases alike: choose decisions that age, not decisions that launch.

## Domain-specific constraints that do NOT transfer

- Manufacturing constraints (draft angles, wall thickness, tooling cost) are real only for physical production; invoking them for digital work is theatre.
- Physical ergonomics data (grip sizes, forces) must not be dressed up as evidence for on-screen decisions.
- Never claim a concept is manufacturable, structurally sound or certifiable without engineering evidence. A rendering proves appearance, nothing else.
