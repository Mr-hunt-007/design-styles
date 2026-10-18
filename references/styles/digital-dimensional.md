# Digital and Dimensional Styles

Depth, material and dimension effects native to screens. All of these are surface languages: they need an information architecture underneath. Index: `../style-catalogue.md`.

## Glassmorphism

- **Also known as:** frosted-glass UI.
- **Period and origins:** named c. 2020 (term popularised by Michal Malewicz, interpretation); precedents in iOS 7 translucency (2013) and Microsoft Fluent's acrylic (2017), documented.
- **Philosophy:** layered translucency communicates depth and context: you see where a surface sits because the world shows through it.
- **Visual characteristics:** background blur, semi-transparent white/dark fills, 1px light borders, floating cards over colourful backdrops.
- **Geometry and composition:** layered planes; needs a vivid backdrop to exist (glass over white is invisible).
- **Colour:** backdrop supplies colour; glass itself near-neutral with low-alpha fills.
- **Typography:** high-contrast type on the glass; blur behind must never bleed into letterforms.
- **Materials and finish:** simulated frosted glass; border highlight implies edge lighting.
- **Lighting and depth:** blur radius + overlay opacity + border = perceived elevation; keep one consistent recipe per level.
- **Motion and interaction:** parallax between layers sells the material; subtle only.
- **Use for:** media UIs, overlays, music players, hero panels, OS-adjacent aesthetics.
- **Avoid when:** dense text UIs, low-end devices (blur is expensive), unpredictable user content behind the glass.
- **Common mistakes:** glass on flat backgrounds (reads as grey box), text under the AA line because backdrop varies, stacking five blur layers (GPU cost, visual mud).
- **Accessibility:** contrast is backdrop-dependent: enforce a minimum overlay opacity or scrim behind text; respect prefers-reduced-transparency.
- **Implementation:** CSS backdrop-filter (check browser support), SVG feGaussianBlur fallback; test on low-end hardware.
- **Complements:** Aurora (ideal backdrop), Dark Luxury, Futuristic.
- **Conflicts:** Brutalism, Flat (philosophically), Paper Cutout.
- **Transferable principles:** depth as context (you see through to where you came from); material recipes per elevation level. Transfers to layered map UIs and overlay systems.
- **Brief example:** "Music player: aurora gradient backdrop, one frosted card, 60% white overlay minimum under text, 1px top-light border."
- **QA:** text AA against worst-case backdrop; one blur/opacity recipe per level; performance tested; reduced-transparency fallback exists.

## Liquid Glass

- **Also known as:** Apple's Liquid Glass design language.
- **Period and origins:** introduced by Apple at WWDC, June 2025, across OS 26 releases (documented, recent: verify current guidance before platform work).
- **Philosophy:** interface chrome as a dynamic refractive material: controls behave like lensing liquid glass that responds to content, motion and light, receding when content leads.
- **Visual characteristics:** refraction and lensing at edges (not just blur), specular highlights that shift with motion, morphing control shapes, concentric corner radii.
- **Geometry and composition:** floating control layers above content; capsule and superellipse geometry; controls cluster into glass islands.
- **Colour:** material is near-clear; tint comes from content beneath plus system accent; avoid heavy opaque fills.
- **Typography:** system type over glass needs vibrancy/legibility layers; follow platform tokens.
- **Materials and finish:** simulated optical glass: refraction, dispersion hints, edge highlights.
- **Lighting and depth:** dynamic speculars respond to device motion/scroll; depth from lensing more than shadow.
- **Motion and interaction:** fluid morphs between control states; motion is part of the material definition.
- **Use for:** native Apple-platform apps, OS-adjacent concepts, premium product marketing of such apps.
- **Avoid when:** cross-platform products needing one identity, accessibility-first services, web recreations where the effect costs more than it communicates.
- **Common mistakes:** recreating it with plain blur (that is glassmorphism, not lensing), glass-on-glass stacking, ignoring Apple's legibility/accessibility adaptations.
- **Accessibility:** platform provides reduced-transparency and increased-contrast adaptations: honour them; never hand-build a variant that lacks them.
- **Implementation:** on-platform use native materials/APIs; on web, approximation needs displacement maps or SVG filters and is costly: date-check current support before promising it.
- **Complements:** Spatial/Immersive, Aurora, Futuristic.
- **Conflicts:** Neo-Brutalism, Flat, Grunge.
- **Transferable principles:** material defined by behaviour (motion + light response), not a static texture; chrome recedes so content leads. Transfers to any overlay/control-layer design.
- **Brief example:** "iOS 26 utility app concept: content edge-to-edge, one floating glass toolbar island, system vibrancy for labels."
- **QA:** platform legibility adaptations honoured; no glass stacked on glass; verified against Apple's current HIG (date-check); performance on target devices.

## Neumorphism

- **Also known as:** soft UI, neo-skeuomorphism.
- **Period and origins:** named c. December 2019 (term from Jason Kelley via Michal Malewicz discourse, interpretation); flared and faded as mainstream UI trend c. 2020.
- **Philosophy:** interface elements as soft extrusions of one continuous surface: the control and the background share material.
- **Visual characteristics:** same-colour element and background, dual shadows (light top-left, dark bottom-right), pillowy embossed/debossed states.
- **Geometry and composition:** rounded rectangles and circles; generous spacing because shadows need room.
- **Colour:** one low-saturation base (greys, off-whites, desaturated pastels); accents sparse.
- **Typography:** must supply the contrast the surfaces lack; medium+ weights.
- **Materials and finish:** extruded soft plastic/rubber feel; matte.
- **Lighting and depth:** fixed global light source; depth = extrusion height via paired shadows; pressed = inverted shadows.
- **Motion and interaction:** press-in transitions are the signature; keep them fast.
- **Use for:** small calm utilities (audio controls, smart-home toggles), concept work, single-purpose dashboards with few controls.
- **Avoid when:** many controls or states (disabled/focus/error become indistinguishable), accessibility-critical products, dark multi-brand theming.
- **Common mistakes:** low-contrast everything (its famous flaw), no focus states, using it for entire products instead of control clusters.
- **Accessibility:** inherently borderline: add real contrast via type, icons and accent rings; focus indicators must be explicit, shadows alone fail.
- **Implementation:** two box-shadows per state; dark mode requires re-derived shadow pairs, not inverted colours.
- **Complements:** Organic Minimalism, Soft 3D, Monochromatic.
- **Conflicts:** Brutalism, Maximalism, Data-Driven (dense).
- **Transferable principles:** consistent global light source; state as physical displacement (pressed/raised grammar). Transfers to icon relief and tactile toggle metaphors anywhere.
- **Brief example:** "Smart-thermostat panel: one warm-grey surface, extruded dial, pressed-in presets, orange accent ring for focus/active."
- **QA:** focus state visible without shadow reliance; AA met via type/accents; one light source everywhere; state pairs (raised/pressed) distinct at a glance.

## Soft 3D

- **Also known as:** friendly 3D illustration; overlaps "big tech 3D" c. 2019-2022 (interpretation, community term).
- **Period and origins:** contemporary, broadly c. 2018 onward as real-time and Blender-era rendering reached brand teams (interpretation).
- **Philosophy:** dimensional warmth: 3D's believability with toy-like friendliness instead of realism's coldness.
- **Visual characteristics:** rounded inflated forms, matte materials, pastel-to-mid palettes, soft studio lighting, floating compositions.
- **Geometry and composition:** bevelled everything, isometric-ish or gentle perspective hero scenes, objects hovering with soft contact shadows.
- **Colour:** cheerful mid-saturation palettes, gradient-lit surfaces.
- **Typography:** 2D type beside 3D scenes; keep type flat for legibility.
- **Materials and finish:** matte plastic, soft rubber, occasional glass accents.
- **Lighting and depth:** large soft key light, ambient fill, blurred shadows; no harsh speculars.
- **Motion and interaction:** slow floats, squash-stretch micro-loops.
- **Use for:** SaaS hero art, fintech onboarding, empty states, explainer scenes.
- **Avoid when:** data precision or gravitas is needed; already a saturated look, differentiation suffers (dated observation c. 2021+).
- **Common mistakes:** inconsistent light rigs across a set; 3D type (legibility death); scenes decorating rather than explaining.
- **Accessibility:** illustration-only meaning must have text alternatives; busy scenes behind text need scrims.
- **Implementation:** real 3D (Blender/Spline) or faux-3D vector gradients; a faux-3D SVG recipe keeps assets light.
- **Complements:** Clay, Gradient Mesh, Organic Minimalism.
- **Conflicts:** Brutalism, Grunge, Scientific/Technical Illustration.
- **Transferable principles:** one light rig per asset family; friendliness via radius/matte/palette dials. Transfers to icon relief and empty-state systems.
- **Brief example:** "Payments onboarding: three floating scenes (card, shield, graph), one key-light rig, brand pastels, flat captions."
- **QA:** light direction identical across set; contact shadows consistent; scenes explain the step; text never 3D.

## Clay Style

- **Also known as:** claymorphism (UI variant, term c. 2021, interpretation).
- **Period and origins:** contemporary 3D illustration trend c. 2020 onward; heritage in claymation (Aardman lineage as cultural reference, documented studio history).
- **Philosophy:** handmade digital: chunky clay-like forms promise approachability, play and zero intimidation.
- **Visual characteristics:** thick rounded shapes, visible softness, inner+outer shadow combo (UI variant), pastel palettes, stubby proportions.
- **Geometry and composition:** everything inflated; big radii; characters and objects with toy proportions.
- **Colour:** pastels and candy mids; low contrast between surfaces, accents carry signal.
- **Typography:** rounded sans pairs naturally; keep type 2D.
- **Materials and finish:** matte clay, fingerprint-soft; no gloss.
- **Lighting and depth:** soft top light; UI cards use large blurred outer shadow plus subtle inner highlight.
- **Motion and interaction:** squash-and-stretch is native; playful bounces.
- **Use for:** kids and education, casual games, community products, playful onboarding.
- **Avoid when:** authority, security gravitas or dense data; investors rarely trust claymation dashboards.
- **Common mistakes:** clay UI with hairline type (weight mismatch), pastel-on-pastel text, play aesthetics on serious legal/medical flows.
- **Accessibility:** pastel contrast traps; bump text contrast beyond the palette; large targets come naturally, keep them.
- **Implementation:** 3D renders or SVG with layered radial gradients; inner-shadow recipes for UI cards.
- **Complements:** Soft 3D, Handwritten, Flat (for type layer).
- **Conflicts:** Dark Luxury, Cyberpunk, Swiss, Aerospace Instrumentation.
- **Transferable principles:** proportion as tone (stubby = friendly); material softness as an anxiety-reduction dial. Transfers to mascot systems and error-state design.
- **Brief example:** "Kids' reading app: clay mascot set, candy palette, chunky rounded buttons with inner-light recipe, bold rounded sans."
- **QA:** text contrast exceeds palette softness; one softness recipe across components; targets ≥44px; tone-appropriate for content.

## Isometric 3D

- **Also known as:** isometric illustration; technically often "dimetric/pseudo-isometric" in practice (interpretation).
- **Period and origins:** axonometric projection from engineering drawing (19th-century formalisation, documented); pixel-game isometrics 1980s; flat-vector isometric boom 2010s.
- **Philosophy:** explain space and systems without perspective distortion: parallel lines stay parallel, so everything stays measurable and comparable.
- **Visual characteristics:** 30° axes (2:1 pixel ratio variant), no vanishing points, stacked modular scenes, cutaways and exploded views.
- **Geometry and composition:** strict axis discipline; scenes built from repeatable unit cubes; z-stacking for hierarchy.
- **Colour:** three-face shading rule (top lightest, two sides stepped) creates volume without gradients.
- **Typography:** labels stay flat/screen-aligned for legibility; axis-aligned type only for decoration.
- **Materials and finish:** flat fills with facet shading; optional line overlay.
- **Lighting and depth:** implied single light via the three-face rule; consistent across every object.
- **Motion and interaction:** axis-constrained movement reads beautifully; build-up animations explain assembly.
- **Use for:** architecture/infra diagrams, network maps, product explainers, data-centre and city scenes, games.
- **Avoid when:** emotional close-up storytelling (it is inherently distant), or when true scale/perspective matters.
- **Common mistakes:** mixed angles in one scene; objects off-grid; shading faces inconsistently; labels rotated into illegibility.
- **Accessibility:** diagrams need reading order and text alternatives; colour-coded systems need labels/patterns too.
- **Implementation:** SVG-native via skew/rotate transforms or axonometric grids; define the unit cube once, reuse everywhere.
- **Complements:** Scientific/Technical Illustration, Flat, Data-Driven, Low Poly.
- **Conflicts:** Cinematic, Surreal, Grunge.
- **Transferable principles:** projection choice as honesty (measurable space); unit-module scene construction. Transfers directly to attack-surface and architecture SVGs.
- **Brief example:** "Cloud-security explainer: unit-cube server blocks, 30° grid, three-face shading, flat callout labels with leader lines."
- **QA:** one projection angle everywhere; all objects on grid; face-shading rule constant; labels horizontal and AA-legible.

## Low Poly

- **Also known as:** low-polygon art.
- **Period and origins:** 1990s real-time 3D constraint (documented hardware history); embraced as deliberate aesthetic c. 2013 onward in illustration and games (interpretation).
- **Philosophy:** reduction with facets: a form simplified until its triangles show, honesty about digital construction becoming beauty.
- **Visual characteristics:** visible triangular facets, flat-shaded planes, crystalline landscapes and animals, gradient skies behind faceted subjects.
- **Geometry and composition:** triangle meshes; silhouettes matter more than surface detail; strategic edge placement defines character.
- **Colour:** per-facet flat fills stepping through a gradient; hue-shifted shadows.
- **Typography:** clean geometric sans contrast the facets; never triangulate text.
- **Materials and finish:** matte facets; optional subtle grain.
- **Lighting and depth:** faux lighting via facet value steps; one light direction.
- **Motion and interaction:** facet-by-facet builds, crystalline shatters.
- **Use for:** game art, posters, hero illustrations, environmental storytelling, award visuals.
- **Avoid when:** softness/organic warmth is the brief, or detail precision is required (faces, products).
- **Common mistakes:** uniform triangle sizes (dead rhythm: vary density by detail need), noisy facets destroying silhouette, gradient banding.
- **Accessibility:** decorative mostly; ensure text alternatives; facet contrast can create visual noise behind text, use scrims.
- **Implementation:** genuinely SVG-friendly (polygons with flat fills); Delaunay tools exist but hand-placed edges read better.
- **Complements:** Isometric 3D, Gradient Mesh (as sky), Futuristic.
- **Conflicts:** Organic Minimalism, Handwritten, Luxury Editorial.
- **Transferable principles:** detail density proportional to importance (more facets where it matters) transfers to all illustration and data design; silhouette-first thinking.
- **Brief example:** "Trail-running event poster: faceted mountain fox, dawn gradient facets, dense triangles on the head, sparse on the body."
- **QA:** silhouette reads at thumbnail; facet density varies with importance; one light direction; no stray vertices/gaps.

## Gradient Mesh

- **Also known as:** mesh gradients, freeform gradients.
- **Period and origins:** named after Adobe Illustrator's gradient-mesh tool (introduced 1998, documented); aesthetic mainstream in branding c. 2017 onward (Stripe-era gradients, interpretation).
- **Philosophy:** colour as atmosphere: smooth multi-hue fields give flat media depth, temperature and emotion without literal imagery.
- **Visual characteristics:** multi-point colour blends, soft organic colour clouds, dimensional blobs, vibrant backgrounds behind sharp UI.
- **Geometry and composition:** colour placement IS the composition: warm/bright pulls focus; shapes optional.
- **Colour:** 3-5 anchor hues max; adjacent hues blend clean, complements make mud unless buffered.
- **Typography:** sharp type over soft fields: strong contrast pairing.
- **Materials and finish:** airbrushed smoothness; optional grain to kill banding.
- **Lighting and depth:** implied glow and volume purely through colour temperature and value.
- **Motion and interaction:** slow hue drift backgrounds; performance-test them.
- **Use for:** brand backdrops, hero sections, event identities, album art, gradient-lit product renders.
- **Avoid when:** information graphics (gradient fields behind data mislead), print without colour management.
- **Common mistakes:** muddy complement blends, banding on export, gradients behind body text, trend-copying a famous brand's exact palette.
- **Accessibility:** text over gradients needs worst-case-point contrast checks; provide solid fallbacks.
- **Implementation:** true mesh is not native SVG (SVG 2 meshes unimplemented in browsers as of knowledge cutoff: date-check); approximate with stacked radial gradients + blur, or raster export; add noise to prevent banding.
- **Complements:** Aurora (sibling), Holographic, Futuristic, Typography-Driven.
- **Conflicts:** Brutalism, Pixel Art, Scientific/Technical Illustration.
- **Transferable principles:** colour temperature as focal control; atmosphere as a separable background layer. Transfers to data-viz background discipline (what NOT to put behind charts).
- **Brief example:** "AI-conference identity: indigo-magenta-amber mesh fields, grain overlay, stark white grotesque type."
- **QA:** no muddy zones; banding checked at export size; text contrast at worst-case point; palette ≤5 anchors.

## Holographic / Iridescent

- **Also known as:** holo, iridescent foil aesthetic.
- **Period and origins:** holographic foil in security printing and packaging (late 20th century, documented); fashion/graphic trend wave c. 2016 onward (interpretation).
- **Philosophy:** instability as delight: colour that refuses to sit still signals novelty, play and futurity.
- **Visual characteristics:** spectral sweeps (pink-cyan-mint-lavender), foil textures, chrome type with rainbow speculars, soap-bubble surfaces.
- **Geometry and composition:** simple geometry carries it best; the material is the event.
- **Colour:** full-spectrum pastel sweeps; anchor with neutral (white/silver/black) grounds.
- **Typography:** bold simple forms take holo fills; thin type disappears in the shimmer.
- **Materials and finish:** diffraction foil, pearlescent plastic, oil-slick chrome.
- **Lighting and depth:** angle-dependent colour implies environment; speculars mandatory.
- **Motion and interaction:** hue-rotation on scroll/hover is the native move; subtle, with reduced-motion fallback.
- **Use for:** beauty, music, fashion drops, event badges, sticker/merch, card finishes.
- **Avoid when:** longevity or sober trust is the brief; spectral noise behind content kills reading.
- **Common mistakes:** holo on everything (it needs neutral ground to shimmer against), text set in iridescent fills, print without actual foil planning.
- **Accessibility:** spectral fills fail contrast structurally: keep text solid; shimmer motion needs reduced-motion variant.
- **Implementation:** CSS/SVG via layered linear gradients + hue-rotate, or conic gradients; print requires foil stock or pearlescent inks (plan with printer).
- **Complements:** Y2K, Aurora, Gradient Mesh, Futuristic.
- **Conflicts:** Scandinavian, Gothic Revival, Corporate Swiss.
- **Transferable principles:** reserve the spectacular material for one hero element; angle-dependence as interactivity metaphor. Transfers to accent systems and award/badge design.
- **Brief example:** "Music-festival badge: solid black card, one holo foil blob behind white logotype, spectral edge on hover for digital version."
- **QA:** holo on one element class only; all text solid and AA; motion variant for reduced-motion; print foil specced with vendor.

## Aurora

- **Also known as:** aurora gradients, northern-lights backgrounds.
- **Period and origins:** contemporary UI trend c. 2020 onward (blurred colour-blob backdrops behind glass/dark UI, interpretation; popularised across OS wallpapers and SaaS heroes).
- **Philosophy:** atmosphere without image: soft drifting light fields give calm depth and brand colour while staying out of content's way.
- **Visual characteristics:** large blurred colour blobs, dark or deep-toned bases, glow pools, often paired with glassmorphism.
- **Geometry and composition:** blobs placed like stage lighting: one key glow near the focal content, falloff elsewhere.
- **Colour:** 2-4 hues, often analogous (teal-violet-magenta) on near-black or deep navy; dark-mode native.
- **Typography:** high-contrast white/near-white type floats above; glow never behind long text blocks.
- **Materials and finish:** pure light; no texture beyond optional grain.
- **Lighting and depth:** the background IS lighting; content panels gain depth by glow occlusion.
- **Motion and interaction:** very slow drift (60s+ loops); must be pausable/reduced-motion aware.
- **Use for:** dark-mode SaaS heroes, dashboards' ambient backdrops, AI-product branding, event screens.
- **Avoid when:** light-mode-first products, dense reading surfaces, printing (gamut and banding pain).
- **Common mistakes:** blobs under data charts (false colour cues), oversaturated neon soup, banding on large screens, motion that distracts.
- **Accessibility:** verify text contrast at brightest blob point; charts need solid panel grounds; reduced-motion honoured.
- **Implementation:** CSS radial-gradients + blur, or SVG feGaussianBlur blobs; add grain; GPU cost of huge blurs is real, pre-render where possible.
- **Complements:** Glassmorphism, Dark Luxury, Futuristic, Gradient Mesh.
- **Conflicts:** Paper Cutout, Scandinavian, Victorian.
- **Transferable principles:** background as stage lighting (focus via glow placement); ambient layers strictly separated from information layers. Transfers to dashboard theming done safely.
- **Brief example:** "Security-platform hero: navy base, one teal-violet glow behind the product screenshot, grain at 3%, static fallback."
- **QA:** glow placement directs to focal point; no glow under data/text blocks; banding and contrast checked on large dark displays; motion pausable.
