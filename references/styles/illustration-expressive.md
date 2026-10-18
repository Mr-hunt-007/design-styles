# Illustration and Expressive Styles

Image-making languages with strong authorial character. Each is a craft with its own construction logic, not a filter. Index: `../style-catalogue.md`.

## Vector Art

- **Also known as:** flat vector illustration.
- **Period and origins:** enabled by PostScript-era tools (Adobe Illustrator 1987, documented); matured as a dominant illustration language through the 2000s-2010s web.
- **Philosophy:** drawing with geometry: shapes, not strokes of paint, so the image scales infinitely and edits cleanly.
- **Visual characteristics:** clean Bézier shapes, flat or simply-shaded fills, deliberate palettes, stylised simplification of subjects.
- **Geometry and composition:** shape economy: fewest anchor points that hold the form; consistent corner and curve language.
- **Colour:** flat fills; shading via hue shift, not black overlay; limited palette per scene.
- **Typography:** pairs with geometric/humanist sans; type and illustration share curve language.
- **Materials and finish:** none simulated unless chosen; optional grain/texture layer.
- **Lighting and depth:** stylised: one-step shadows, hue-shifted shade shapes.
- **Motion and interaction:** rigs cleanly for animation (shape layers).
- **Use for:** product illustration systems, icons, onboarding art, editorial spots, anything needing scale and consistency.
- **Avoid when:** photographic emotion or painterly atmosphere is the point.
- **Common mistakes:** anchor-point litter (lumpy curves), inconsistent corner radii across a set, black-multiplied shadows (muddy), style drift between illustrations.
- **Accessibility:** decorative vs informative distinction; informative art needs alt text; palette contrast for meaningful elements.
- **Implementation:** SVG-native; define a style sheet (stroke width, radius, palette, shading rule) before drawing the set.
- **Complements:** Flat, Line Art, Isometric 3D, Mid-Century Modern.
- **Conflicts:** Cinematic, Grunge (unless hybridised deliberately).
- **Transferable principles:** shape economy and a written style sheet per asset family; hue-shift shading. Transfers to icon systems, diagrams and all SVG work in this skill.
- **Brief example:** "HR-platform illustration set: 12 scenes, 6-colour palette, 2px optical strokes, hue-shift shading, one humour note per scene."
- **QA:** curves smooth (no accidental kinks); set shares palette/stroke/radius rules; scales from 48px to poster; shading rule consistent.

## Line Art

- **Also known as:** monoline illustration, contour drawing.
- **Period and origins:** as old as drawing (documented from ancient art onward); modern monoline branding wave c. 2015 onward (interpretation); heritage in etching, Picasso's single-line studies, Matisse contours.
- **Philosophy:** maximum meaning per line: the economy of a single weight forces every stroke to earn its place.
- **Visual characteristics:** uniform (or two-weight) strokes, open compositions, white space as the body of forms, minimal or no fills.
- **Geometry and composition:** line rhythm and interval carry the design; closure left to the viewer's eye.
- **Colour:** often monochrome line plus one accent fill; line colour on brand-ground variants.
- **Typography:** hairline-to-regular sans pairs well; line weight can match type stroke for unity.
- **Materials and finish:** clean digital stroke or honest pen texture: choose one.
- **Lighting and depth:** hatching or line-density only, if at all.
- **Motion and interaction:** line-draw (stroke-dashoffset) animation is the native and overused move: use when drawing order means something.
- **Use for:** premium packaging, wayfinding, icon systems, editorial spots, scientific-adjacent elegance.
- **Avoid when:** small sizes with thin strokes (vanishing lines), audiences needing bold affordance.
- **Common mistakes:** weight wobble across a set, closing every shape (losing the airiness), strokes not converted/tested for scale rendering.
- **Accessibility:** thin lines fail low-vision users at small sizes: set minimum rendered stroke (e.g. 1.5px at smallest use).
- **Implementation:** SVG stroke-based: define stroke width against viewBox so scaling maths is known; caps/joins consistent (round vs butt).
- **Complements:** Minimalism, Japanese Minimalism, Luxury Editorial, Scientific/Technical Illustration.
- **Conflicts:** Maximalism, Clay, Soft 3D.
- **Transferable principles:** interval and rhythm of line as composition; minimum-stroke-at-size rule. Transfers to diagram connectors, map linework, icon grids.
- **Brief example:** "Botanical gin label: single-weight line botanicals, 2pt at print size, one copper accent fill, open contours."
- **QA:** one stroke weight (or documented two-weight system); legible at smallest size; caps/joins uniform; open/closed logic consistent.

## Pixel Art

- **Also known as:** pixel graphics, dot art (dotto-e in Japanese usage).
- **Period and origins:** 1970s-1980s hardware constraint (documented console/arcade history); deliberate aesthetic revival from c. 2000s indie games onward.
- **Philosophy:** the grid is the medium: every pixel is a decision, and constraint breeds character.
- **Visual characteristics:** visible pixels, limited palettes, hand-placed anti-aliasing, dithering gradients, sprite proportions.
- **Geometry and composition:** everything on the pixel grid; consistent "pixel size" (no mixed resolutions in one piece).
- **Colour:** small deliberate palettes (4-32 colours); ramps designed per material; dithering instead of gradients.
- **Typography:** bitmap fonts at native sizes; scale only by integers.
- **Materials and finish:** none: the pixel IS the texture.
- **Lighting and depth:** cluster shading, hue-shifted ramps, selective outlining (sel-out, community technique).
- **Motion and interaction:** frame-by-frame sprite animation; snappy, low frame counts.
- **Use for:** games, retro-tech brands, 8-bit social content, crypto/dev-tool mascots, favicon-scale art.
- **Avoid when:** luxury, medical, or anywhere "game" is the wrong connotation; large-format print (needs integer scaling).
- **Common mistakes:** mixed pixel sizes, non-integer scaling (blurry), jaggies on curves (bad pixel stair-stepping), auto anti-aliasing from tools.
- **Accessibility:** bitmap text below ~8px native is illegible; provide real-text equivalents; high-contrast palettes help.
- **Implementation:** export with nearest-neighbour scaling; CSS image-rendering: pixelated; SVG can host pixel art via shape-rendering crispEdges rects.
- **Complements:** Y2K, Retro, Neo-Brutalism (as accent).
- **Conflicts:** Luxury Editorial, Organic Minimalism, Cinematic.
- **Transferable principles:** constraint as style generator; integer-scaling discipline; palette ramps per material. Transfers to favicon/small-icon craft everywhere.
- **Brief example:** "Dev-conference badge sprite: 32x32, 12-colour palette, 4-frame idle animation, integer-scaled to print."
- **QA:** one pixel size throughout; integer scaling only; palette within budget; curves stair-step cleanly.

## Paper Cutout

- **Also known as:** cut-paper, papercraft style.
- **Period and origins:** craft traditions documented across cultures (Chinese jianzhi, Polish wycinanki, Mexican papel picado); fine-art benchmark in Matisse's cut-outs (1940s, documented); digital emulation common since 2000s.
- **Philosophy:** honest layers: shapes cut from flat sheets, stacked; depth from physical stacking, charm from the hand's imperfection.
- **Visual characteristics:** flat colour layers with soft drop shadows between, slightly irregular edges, visible layer order, torn vs cut edge choices.
- **Geometry and composition:** stage-set layering (foreground/mid/back); silhouette-driven shapes.
- **Colour:** each layer one flat colour; palettes like paper stock sets (5-8 sheets).
- **Typography:** cut-letter display type works for titles; body text stays printed (flat) for legibility.
- **Materials and finish:** paper grain subtle; shadow softness implies sheet separation distance.
- **Lighting and depth:** one top-light; shadow offset/blur consistent per layer gap.
- **Motion and interaction:** layers sliding on parallax; stop-motion jitter for charm.
- **Use for:** children's media, cultural events, craft and food brands, explainer scenes, stage-like heroes.
- **Avoid when:** sleek tech precision is the brief; the charm IS imperfection.
- **Common mistakes:** inconsistent shadow logic (layers float ambiguously), perfectly smooth edges (loses the cut), too many layers muddying depth.
- **Accessibility:** scenes decorative: alt text; layer contrast where meaning lives.
- **Implementation:** SVG layers with feDropShadow or offset duplicates; keep per-layer shadow recipe tokenised; slight edge roughen via subtle path jitter, not filters that blur.
- **Complements:** Handwritten, Collage, Scandinavian (illustration layer).
- **Conflicts:** Glassmorphism, Cyberpunk, Corporate Swiss.
- **Transferable principles:** explicit layer model with consistent inter-layer shadow (transfers to any elevation system, including UI shadow tokens); silhouette-first shapes.
- **Brief example:** "Folk-festival poster: five paper layers (sky, hills, village, dancers, title), one shadow recipe, papel-picado border."
- **QA:** shadow recipe uniform per gap; silhouettes read at distance; edge treatment consistent (cut or torn, chosen once); ≤6 layers.

## Collage Art

- **Also known as:** photomontage, mixed-media collage.
- **Period and origins:** papier collé in Cubism c. 1912 (Picasso, Braque, documented); Dada photomontage (Höch, Heartfield); punk xerox collage 1970s; digital collage ongoing.
- **Philosophy:** meaning by juxtaposition: fragments keep their origins, and the collision creates a third idea none of the parts contained.
- **Visual characteristics:** cut photo fragments, torn edges, mixed scales, halftone textures, tape/staple artefacts, type scraps.
- **Geometry and composition:** controlled chaos: a dominant anchor fragment, supporting shards, breathing zones.
- **Colour:** inherited from sources; unify with an overlay wash, duotone, or limited-source curation.
- **Typography:** ransom-note mixing allowed; one legible system voice for actual information.
- **Materials and finish:** paper tooth, xerox grit, tape gloss; artefacts are vocabulary.
- **Lighting and depth:** per-fragment shadows (physical stack logic), inconsistent source lighting embraced.
- **Motion and interaction:** stop-motion shuffles, fragment parallax.
- **Use for:** music, zines, editorial opinion, campaigns about complexity/memory/media, youth culture.
- **Avoid when:** clarity-critical information, conservative trust contexts; rights-unclear source imagery is a hard stop.
- **Common mistakes:** fragment soup with no anchor, unlicensed imagery, meaning-free randomness (juxtaposition must argue something), illegible everything.
- **Accessibility:** ensure the actual message exists as clean text somewhere; busy grounds need solid panels.
- **Implementation:** licensing first; unify with a grade/texture pass; keep information layer separate from art layer.
- **Complements:** Grunge, Pop Art, Maximalism, Handwritten.
- **Conflicts:** Minimalism, Corporate Swiss, Neumorphism.
- **Transferable principles:** juxtaposition as argument; source-unification passes (grade/texture) transfer to any multi-source imagery system (e.g. report figures from mixed origins).
- **Brief example:** "Op-ed illustration on surveillance: torn CCTV stills, one red thread anchor, halftone wash unifier, clean caption band."
- **QA:** anchor fragment dominates; every fragment licensed/owned; a unification pass applied; information layer legible and separate.

## Pop Art

- **Also known as:** pop.
- **Period and origins:** UK Independent Group mid-1950s (Hamilton), US explosion early 1960s (Warhol, Lichtenstein, Oldenburg), documented.
- **Philosophy:** mass culture as fine art: advertising, comics and packaging reflected back with repetition, flatness and irony.
- **Visual characteristics:** Ben-Day dots, bold outlines, flat commercial colour, repetition grids, comic frames, product iconography.
- **Geometry and composition:** poster-flat frontal compositions; serial repetition as structure.
- **Colour:** saturated primaries and CMYK-adjacent brights; flat, unmodulated.
- **Typography:** comic display, advertising slabs, speech bubbles; exclamatory scale.
- **Materials and finish:** screenprint flatness, registration-shift charm, newsprint dots.
- **Lighting and depth:** flat with comic shading conventions (dot gradients, hard shadows).
- **Motion and interaction:** frame-pop transitions, onomatopoeia bursts.
- **Use for:** food/beverage, retail campaigns, music, anything commenting on consumer culture with wit.
- **Avoid when:** sincerity or understatement is required; irony can poison earnest messages.
- **Common mistakes:** Lichtenstein pastiche without a reason, dots applied as texture rather than printing logic, trademarked imagery misused.
- **Accessibility:** bold contrast is naturally strong; dotted fields behind text still need checks; exclamatory type needs real-text semantics.
- **Implementation:** Ben-Day via SVG patterns; limit dot scales to plausible screenprint logic.
- **Complements:** Maximalism, Memphis, Collage, Retro (60s).
- **Conflicts:** Luxury Editorial, Japanese Minimalism, Dark Luxury.
- **Transferable principles:** repetition as emphasis; borrowing a vernacular (ads, comics) as commentary; print-process artefacts as palette. Transfers to campaign systems and merch.
- **Brief example:** "Burger launch: comic-frame triptych, Ben-Day shading, flat ketchup red/mustard/cyan, 'POW'-register headline with sincere price line set plain."
- **QA:** print-logic dots (consistent screen angles/scales); outlines uniform; irony intentional and brand-safe; text semantics real.

## Surreal Design

- **Also known as:** surrealism (applied); dream imagery.
- **Period and origins:** Surrealist movement founded 1924 (Breton's manifesto, documented; Dalí, Magritte, Ernst); advertising and digital art have borrowed it continuously since.
- **Philosophy:** the impossible rendered plausibly: dream logic bypasses rational filters and makes an idea unforgettable.
- **Visual characteristics:** impossible scale/gravity/material swaps, realistic rendering of unreal scenes, uncanny juxtapositions, vast empty dreamscapes.
- **Geometry and composition:** classical composition holding irrational content (the tension is the point); deep perspective stages.
- **Colour:** often naturalistic with one wrong note; or saturated dream grading.
- **Typography:** restrained, letting the image carry strangeness; type-as-object plays (melting, floating) sparingly.
- **Materials and finish:** convincing render of the impossible: material fidelity sells the trick.
- **Lighting and depth:** coherent light within the impossible scene (the realism rule).
- **Motion and interaction:** physics violations executed smoothly; morph transitions.
- **Use for:** campaign heroes, album/book covers, editorial concepts, brand films; one unforgettable image per message.
- **Avoid when:** instructions, data, trust-critical products; surrealism explains nothing, it provokes.
- **Common mistakes:** random weirdness without a conceptual spine; render quality too low to sell the illusion; stacking ten tricks where one lands.
- **Accessibility:** purely conceptual imagery needs strong alt text; uncanny content warnings where appropriate.
- **Implementation:** photo-composite or 3D craft is high; AI-assisted generation common now, verify rights and disclose per policy (dated note, 2026).
- **Complements:** Cinematic, Collage, Maximalism.
- **Conflicts:** Data-Driven, Aerospace Instrumentation, Flat.
- **Transferable principles:** one impossible thing, rendered with total craft; concept-first image making (the idea audit: what does the impossibility argue?). Transfers to hero-image art direction anywhere.
- **Brief example:** "Cloud-storage campaign: a filing cabinet as a monsoon cloud raining folders over a calm sea, golden-hour light, one-line caption."
- **QA:** exactly one impossibility, serving the stated concept; light/materials internally coherent; render quality sells it; caption anchors meaning.

## Grunge

- **Also known as:** dirty design; 90s alternative aesthetic.
- **Period and origins:** early 1990s, tied to grunge music culture and David Carson's Ray Gun typography experiments (documented); xerox-punk ancestry 1970s.
- **Philosophy:** anti-polish authenticity: distress, noise and broken rules as honesty against corporate slickness.
- **Visual characteristics:** distressed textures, overprinted layers, torn/dirty edges, degraded type, photocopier artefacts, splatter.
- **Geometry and composition:** deliberate misalignment, collision layouts, density over order; still needs a focal hierarchy to function.
- **Colour:** muddy neutrals, black-heavy, bruised accents (oxblood, mustard, olive); occasionally acid brights.
- **Typography:** eroded faces, typewriter, hand-scrawl, overlapping and clipped type; Carson-style expressive setting.
- **Materials and finish:** grit, grain, tape, stains; texture IS structure.
- **Lighting and depth:** flat, photocopied deadness or harsh flash-photo feel.
- **Motion and interaction:** jitter, frame-drop stutters, glitch cousins; sparingly.
- **Use for:** music, streetwear, bars/venues, counterculture editorial, horror-adjacent media.
- **Avoid when:** legibility-critical or trust-critical products; finance/medical almost never.
- **Common mistakes:** texture dumped over a clean layout (grunge is structural, not a filter), total illegibility with no entry point, stock-brush sameness.
- **Accessibility:** eroded type for display only; keep one clean information channel; contrast still law.
- **Implementation:** real scanned textures beat stock brushes; SVG roughen filters exist but raster texture reads truer; keep info layer separate.
- **Complements:** Collage, Graffiti, Brutalism, Punk-zine aesthetics.
- **Conflicts:** Luxury Editorial, Corporate Swiss, Clay, Glassmorphism.
- **Transferable principles:** controlled degradation (decide what stays clean); authenticity through process artefacts. Transfers to texture passes and anti-corporate campaign voices.
- **Brief example:** "Venue gig-poster system: scanned xerox texture, eroded headline face, clean gig-details strip at base, two-colour riso palette."
- **QA:** one clean information zone survives; textures original/licensed; distress consistent in process logic; focal hierarchy exists despite chaos.

## Graffiti

- **Also known as:** street art lettering (graffiti writing specifically centres letterform).
- **Period and origins:** modern writing culture from Philadelphia/New York late 1960s-1970s subway era (documented); global vocabulary since; ancient wall-marking precedents acknowledged.
- **Philosophy:** letterform as gesture, identity and claimed space; style is earned through flow, not applied.
- **Visual characteristics:** tags, throw-ups, wildstyle pieces; arrows, bits, fills, outlines, forcefields; spray textures and drips.
- **Geometry and composition:** letter flow and connection; balance of positive letter mass and negative cuts; piece composition on a wall plane.
- **Colour:** fill + outline + 3D/shadow + background logic; high-contrast combos; chrome-and-black economy of throw-ups.
- **Typography:** the letters ARE the art; hierarchy: tag (signature), throw-up (speed), piece (mastery).
- **Materials and finish:** spray softness, drips, wall texture, marker gloss.
- **Lighting and depth:** block 3D or cast shadow conventions; forcefield glows.
- **Motion and interaction:** draw-on reveals mimicking painting order; drip physics.
- **Use for:** streetwear, music, sports, urban events, youth campaigns; municipal walls (commissioned).
- **Avoid when:** corporate contexts where it reads as costume; cultural appropriation risk when faked without respect for the craft (interpretation, widely voiced within the culture).
- **Common mistakes:** "graffiti font" defaults (writers spot fakes instantly), illegible wildstyle where communication needed, clean vector drips that defy gravity.
- **Accessibility:** wildstyle is display-only; pair with plain text; spray contrast on busy walls needs testing.
- **Implementation:** commission real writers where authenticity matters; vector pieces need pressure-varied strokes, not uniform paths.
- **Complements:** Grunge, Pop Art (lineage debates aside), Collage.
- **Conflicts:** Luxury Editorial, Scandinavian, Corporate Swiss, Neumorphism.
- **Transferable principles:** flow and connection between letterforms (transfers to logotype design); earned-style humility: imitating a living culture badly is a brand risk.
- **Brief example:** "Basketball-court event identity: commissioned throw-up wordmark, chrome/black fill, clean sans schedule block."
- **QA:** letter flow continuous; drips obey gravity; authenticity sourced (commissioned or honestly stylised); plain-text companion present.

## Bohemian

- **Also known as:** boho, boho-chic.
- **Period and origins:** named for 19th-century bohemian counterculture (documented usage); as interiors/graphic style, a late-20th-to-contemporary eclectic blend of folk, travel and craft references.
- **Philosophy:** curated wanderlust: layered pattern, handcraft and natural materials express individual, collected-over-time identity.
- **Visual characteristics:** layered textiles and patterns (kilim, ikat, macramé references), botanical motifs, sun/moon iconography, warm earthy abundance.
- **Geometry and composition:** relaxed, layered, asymmetric; pattern-on-pattern with tonal glue.
- **Colour:** terracotta, ochre, rust, olive, cream, dusty rose; sun-faded saturation.
- **Typography:** organic serifs, brushy scripts, letterpress textures; airy spacing.
- **Materials and finish:** woven texture, rattan, linen, dried botanicals, kraft.
- **Lighting and depth:** golden-hour warmth, soft natural shadow.
- **Motion and interaction:** gentle sway, fabric physics; unhurried.
- **Use for:** wellness, weddings, travel, artisan food, interiors, festival brands.
- **Avoid when:** precision/tech credibility needed; pattern sources used shallowly risk cultural flattening (name and respect sources).
- **Common mistakes:** pattern soup without tonal unification, "ethnic" clip-art with no provenance, beige mush with no focal point.
- **Accessibility:** low-contrast earthy palettes trap text: verify; patterned grounds need solid text panels.
- **Implementation:** real textile scans or honest vector homage; pattern library with named sources; texture weight budgeted.
- **Complements:** Organic Minimalism, Handwritten, Mid-Century (70s strand), Victorian (lightly).
- **Conflicts:** Cyberpunk, Swiss, Flat, Aerospace Instrumentation.
- **Transferable principles:** tonal glue unifying diverse patterns (transfers to any multi-source visual system); provenance-respect as design ethics.
- **Brief example:** "Retreat brand: ochre/cream palette, one ikat-inspired pattern credited to its tradition, brush-script accent over airy serif system."
- **QA:** patterns tonally unified; sources credited/respectful; text on solid grounds, AA met; one focal point per layout.
