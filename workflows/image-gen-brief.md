# Workflow: Image-Generation Brief

Convert a concept into a precise visual brief or image-generation prompt. Precision of visual language is the whole job.

**Inputs:** the concept, where the image will live, brand or style constraints.
**Outputs:** a structured brief/prompt, plus inspection criteria for the result.
**Load:** [../references/art-and-composition.md](../references/art-and-composition.md), [../references/style-catalogue.md](../references/style-catalogue.md); [../references/typography-and-graphics.md](../references/typography-and-graphics.md) when type appears in the image.

## Steps

1. **Fix the purpose.** What must a viewer feel or understand in the first second, and where will the image sit (hero, thumbnail, poster, editorial inline)? Purpose drives every later field.

2. **Write the brief, field by field:**
   - Subject and intended purpose.
   - Composition and viewing angle (rule-of-thirds placement, eye level or low angle, foreground/midground/background).
   - Design philosophy and style direction (one primary, named precisely).
   - Historical or artistic references, used for principles and verified as real.
   - Geometry and proportions (aspect of key forms, symmetry or deliberate asymmetry).
   - Materials and surface properties (brushed aluminium, matte ceramic, wet asphalt).
   - Colour relationships (dominant, secondary, accent; temperature; contrast strategy).
   - Lighting and shadow (source direction, hardness, time of day, atmosphere).
   - Texture and depth (grain, depth of field, layering).
   - Level of realism or abstraction, stated explicitly.
   - Typography, when needed: typeface character, placement, size relative to frame.
   - Output dimensions and aspect ratio.
   - Exclusions: elements, styles and clichés to keep out.
   - Practical constraints: safe areas, overlay zones for later text, legibility at thumbnail.

3. **Ban vague language.** Replace "premium", "futuristic", "clean", "pop" with observable properties: "premium" might become "low-saturation palette, generous negative space, single directional key light, no gradients steeper than 10% luminance". If a word cannot be drawn, it does not belong in the brief.

4. **Label the artefact class.** A UI image is a **visual mock-up**, not a working accessible interface; say so. An engineering subject is a **conceptual illustration**, not a validated design; say so. Never let a generated image imply tested functionality.

5. **Define acceptance checks** for the returned image: composition matches, palette within range, exclusions absent, any text spelled correctly (generators corrupt type; check letter by letter), aspect and resolution correct.

6. **Inspect the result** against step 5 when the image comes back; iterate the brief on specific failures, not by adding adjectives.

## Gate

Done only when: every field in step 2 is either filled with observable language or consciously marked not applicable; the artefact class is labelled; acceptance checks exist. A brief containing "make it premium" has failed.
