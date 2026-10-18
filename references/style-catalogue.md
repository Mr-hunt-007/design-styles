# Style Catalogue: Index and Selection Guide

The catalogue holds 64 named styles in six category files under `references/styles/`. Each entry is a self-contained reference: philosophy, characteristics, use cases, limits, mistakes, accessibility, implementation constraints, transferable principles and a QA checklist. Styles are sources of principles, never templates to copy.

## Taxonomy

| Category file | Covers | Core idea |
|---|---|---|
| `styles/foundation.md` | Minimalism, Maximalism, Swiss, Bauhaus, Brutalism, Flat, Skeuomorphism, Organic Minimalism, Japanese Minimalism, Scandinavian | Functional and philosophical baselines most other styles react to |
| `styles/heritage.md` | Victorian, Art Nouveau, Art Deco, Mid-Century Modern, Memphis, Retro, Y2K, Retro-Futurism, Steampunk, Gothic Revival | Historical identities and their revivals |
| `styles/digital-dimensional.md` | Glassmorphism, Liquid Glass, Neumorphism, Soft 3D, Clay, Isometric 3D, Low Poly, Gradient Mesh, Holographic, Aurora | Depth, material and dimension effects native to screens |
| `styles/illustration-expressive.md` | Vector Art, Line Art, Pixel Art, Paper Cutout, Collage, Pop Art, Surreal, Grunge, Graffiti, Bohemian | Image-making languages with strong authorial character |
| `styles/typographic-editorial.md` | Editorial, Luxury Editorial, Typography-Driven, Kinetic Typography, Handwritten, Duotone, Monochromatic, Cinematic, Motion Graphics, Data-Driven/Infographic | Communication-first systems built on type, pacing and evidence |
| `styles/contemporary-specialist.md` | Cyberpunk, Futuristic, Dark Luxury, Organic/Biomorphic, Maximalist Editorial, Neo-Brutalism, Corporate Swiss, Scientific/Technical Illustration, Aerospace Instrumentation, Industrial Product Design, Architectural Modernism, Sustainable/Circular, Generative/Computational, Spatial/Immersive | Current specialist languages and discipline-rooted aesthetics |

Categories overlap deliberately. Swiss Design is both a foundation and an editorial system; Aerospace Instrumentation is both a specialist style and a discipline (see `aerospace-and-instrumentation.md`). When a style has a discipline file, the discipline file holds the engineering truth and the style entry holds the visual language.

## How to select a style (problem first, never style first)

1. State the problem: audience, purpose, medium, constraints, brand context, lifespan.
2. Derive the required qualities: for example "dense data, fast scanning, operator trust" or "emotional warmth, craft credibility".
3. Shortlist 2-4 styles whose *philosophy* matches those qualities. Match philosophy, not surface. Read the full entries.
4. Check every shortlisted entry's **Avoid when** and **Conflicts** fields against the brief.
5. Pick one primary direction. Add supporting influences only if each one solves a named problem.
6. Record what was rejected and why; this is the rationale the user receives.

A style chosen because it is fashionable, or because the user named it without a fit check, must still pass steps 4-5. If it fails, say so and propose the nearest fit.

## Styles cross disciplinary boundaries

Every entry carries a **Transferable principles** field: the discipline-independent lessons the style teaches. Aerospace Instrumentation's failure-state hierarchy improves SaaS dashboards; Architectural Modernism's structural grid paces editorial pages; horology-grade finishing (see `horology.md`) disciplines icon sets. Transfer the principle, not the costume: borrowing cockpit bezels is aesthetic imitation, borrowing alarm-priority logic is principle transfer. Process and worked mappings: `cross-disciplinary-design.md`.

## Extensibility rules

- Add a new style only when it carries a genuinely distinct philosophy or specialist knowledge, not a minor variant (a new gradient fashion is a note under an existing entry, not a new style).
- New entries use the full schema of the existing entries and go in the closest category file; split a file only when it passes ~450 lines.
- Date trend-sensitive claims ("as of 2026..."). Mark interpretation as interpretation.
- Never duplicate a style across files; cross-reference instead.

## Full style index

| Style | File | Use when |
|---|---|---|
| Minimalism | foundation | the content must carry everything and noise is the enemy |
| Maximalism | foundation | abundance, personality and density ARE the message |
| Swiss / International Typographic | foundation | objective, grid-driven clarity for information-rich communication |
| Bauhaus | foundation | form from function, geometry and primary contrast with craft unity |
| Brutalism | foundation | raw structural honesty should confront, not comfort |
| Flat Design | foundation | fast-rendering, scalable UI with no depth illusions |
| Skeuomorphism | foundation | familiarity with real objects lowers the learning curve |
| Organic Minimalism | foundation | calm restraint that still feels warm and human |
| Japanese Minimalism | foundation | emptiness, asymmetry and imperfection as active values |
| Scandinavian Design | foundation | democratic warmth: function plus light, wood and comfort |
| Victorian | heritage | layered ornament and period richness are the point |
| Art Nouveau | heritage | flowing organic line unifying structure and decoration |
| Art Deco | heritage | geometric glamour, luxury and machine-age optimism |
| Mid-Century Modern | heritage | optimistic functional warmth, c. 1945-1969 vocabulary |
| Memphis Design | heritage | playful rule-breaking colour and pattern clash |
| Retro | heritage | a specific named past era evokes trust or nostalgia |
| Y2K | heritage | glossy techno-optimism of c. 1997-2004 |
| Retro-Futurism | heritage | yesterday's vision of tomorrow, hopeful or ironic |
| Steampunk | heritage | Victorian mechanics reimagined as fantasy technology |
| Gothic Revival | heritage | verticality, pointed structure and moral seriousness |
| Glassmorphism | digital-dimensional | layered translucency communicates depth without weight |
| Liquid Glass | digital-dimensional | dynamic refractive material language (Apple, 2025-) |
| Neumorphism | digital-dimensional | soft extruded surfaces, low-stakes tactile UI |
| Soft 3D | digital-dimensional | friendly dimensional illustration for product storytelling |
| Clay Style | digital-dimensional | chunky matte 3D warmth, approachable mascots and scenes |
| Isometric 3D | digital-dimensional | systems and spaces explained without perspective distortion |
| Low Poly | digital-dimensional | faceted geometry as deliberate stylised reduction |
| Gradient Mesh | digital-dimensional | smooth multi-hue colour fields and dimensional blends |
| Holographic / Iridescent | digital-dimensional | spectral shimmer signalling novelty and play |
| Aurora | digital-dimensional | soft blurred colour atmospheres behind calm UI |
| Vector Art | illustration-expressive | crisp scalable illustration with flat colour logic |
| Line Art | illustration-expressive | single-weight economy of line, elegance through restraint |
| Pixel Art | illustration-expressive | grid-constrained charm, gaming and retro-digital identity |
| Paper Cutout | illustration-expressive | layered physical craft feel, handmade warmth |
| Collage Art | illustration-expressive | juxtaposition of found fragments creates new meaning |
| Pop Art | illustration-expressive | mass-culture imagery, bold repetition and irony |
| Surreal Design | illustration-expressive | impossible imagery that makes an idea unforgettable |
| Grunge | illustration-expressive | distressed texture and anti-polish authenticity |
| Graffiti | illustration-expressive | street energy, letterform as gesture and territory |
| Bohemian | illustration-expressive | eclectic layered pattern, travel and handcraft spirit |
| Editorial Design | typographic-editorial | long-form reading with pacing, structure and voice |
| Luxury Editorial | typographic-editorial | fashion-grade whitespace, serifs and restraint signal prestige |
| Typography-Driven | typographic-editorial | type IS the image; nothing else competes |
| Kinetic Typography | typographic-editorial | moving words carry rhythm, emphasis and emotion |
| Handwritten | typographic-editorial | personal, human, imperfect marks build intimacy |
| Duotone | typographic-editorial | two-colour discipline unifies mixed imagery |
| Monochromatic | typographic-editorial | one hue, many values: cohesion and mood control |
| Cinematic | typographic-editorial | film grammar: wide frames, light, grade and narrative |
| Motion Graphics | typographic-editorial | animated explanation and brand expression |
| Data-Driven / Infographic | typographic-editorial | evidence rendered honestly as the hero content |
| Cyberpunk | contemporary-specialist | high-tech dystopia: neon, noise and density as identity |
| Futuristic | contemporary-specialist | forward-looking sleekness without a named fiction |
| Dark Luxury | contemporary-specialist | near-black restraint with precious accents |
| Organic / Biomorphic | contemporary-specialist | nature-derived curves and grown-not-drawn forms |
| Maximalist Editorial | contemporary-specialist | dense expressive publication energy under a real grid |
| Neo-Brutalism | contemporary-specialist | flat raw blocks, hard borders, unapologetic UI honesty |
| Corporate Swiss | contemporary-specialist | Swiss clarity tuned for enterprise trust at scale |
| Scientific / Technical Illustration | contemporary-specialist | accuracy-first drawing that explains how things work |
| Aerospace Instrumentation | contemporary-specialist | life-critical legibility, alarm hierarchy, operator trust |
| Industrial Product Design | contemporary-specialist | Rams-lineage object logic applied as a visual language |
| Architectural Modernism | contemporary-specialist | structure, module and light as compositional law |
| Sustainable / Circular Design | contemporary-specialist | material honesty, longevity and repair as aesthetics |
| Generative / Computational | contemporary-specialist | rules and systems produce the form |
| Spatial / Immersive | contemporary-specialist | 3D environments, AR/VR and volumetric interfaces |
