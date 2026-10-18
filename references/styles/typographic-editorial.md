# Typography, Editorial and Communication Styles

Communication-first systems built on type, pacing and evidence. Index: `../style-catalogue.md`.

## Editorial Design

- **Also known as:** publication design, magazine design.
- **Period and origins:** magazine tradition matured through the 20th century (Brodovitch at Harper's Bazaar 1930s-50s, Fleckhaus's Twen 1960s, documented); grid theory formalised by Swiss school.
- **Philosophy:** reading as a designed journey: pacing, hierarchy and voice guide a reader through long-form content without fatigue.
- **Visual characteristics:** strong mastheads, drop caps, pull quotes, varied spread rhythms, image-text interplay, folios and running heads.
- **Geometry and composition:** baseline grid + column system; spreads alternate density (loud opener, quiet body, punctuating pull-quotes).
- **Colour:** restrained body environment; colour as section coding and accent.
- **Typography:** serif body for sustained reading (or well-set sans), display family for voice; hierarchy of 4-6 defined levels; real typographic detail (ligatures, hanging punctuation, smart quotes).
- **Materials and finish:** paper stock logic even on screen: texture of restraint.
- **Lighting and depth:** flat; photography provides depth.
- **Motion and interaction:** digital editions: scroll pacing, sticky figures, progressive disclosure.
- **Use for:** magazines, long-form web features, annual reports, documentation that must be read not scanned.
- **Avoid when:** task UIs; editorial pacing slows task completion.
- **Common mistakes:** no pacing (every spread equal), line lengths beyond ~75 characters, hierarchy with too many levels, pull quotes repeating adjacent text verbatim.
- **Accessibility:** reading order logical; body ≥16px digital; heading semantics real (h1-h4); line-height ≥1.4.
- **Implementation:** baseline grid in CSS requires discipline (consistent line-height multiples); define the 6-level type scale as tokens.
- **Complements:** Luxury Editorial, Swiss, Typography-Driven, Data-Driven.
- **Conflicts:** Neo-Brutalism (fights its care), Memphis.
- **Transferable principles:** pacing as design material (loud/quiet rhythm transfers to decks, dashboards' overview-to-detail, onboarding flows); line-length discipline everywhere text lives.
- **Brief example:** "Threat-intel annual report: 8-column grid, serif body 10.5/15, loud chapter openers, quiet data spreads, red section coding."
- **QA:** measure 45-75 chars; 4-6 hierarchy levels used consistently; spread rhythm varies; typographic details (quotes, dashes) correct.

## Luxury Editorial

- **Also known as:** fashion editorial, high editorial.
- **Period and origins:** haute-couture magazine lineage (Vogue, Harper's Bazaar art direction through the 20th century, documented); digital luxury sites adopted the codes 2010s.
- **Philosophy:** restraint as wealth: scarcity of elements, abundance of space and flawless detail signal that nothing here is accidental.
- **Visual characteristics:** vast whitespace, hairline rules, high-contrast serifs, small letterspaced caps, full-bleed photography, near-absent UI chrome.
- **Geometry and composition:** symmetry or poised asymmetry; enormous margins; single-item focus per view.
- **Colour:** ivory, black, charcoal; one precious accent (gold, oxblood, forest) used almost never.
- **Typography:** Didone display (high contrast), refined text serif or spare grotesque; letterspaced small caps for labels; impeccable kerning is the brand.
- **Materials and finish:** implied: uncoated stock, foil restraint, silk matte.
- **Lighting and depth:** photographic; interface itself flat and silent.
- **Motion and interaction:** slow fades, no bounce; the pace of confidence.
- **Use for:** fashion, jewellery, hotels, private banking, premium editorial.
- **Avoid when:** approachability, urgency or information density is needed; it whispers.
- **Common mistakes:** Didone at tiny sizes (hairlines vanish), letterspacing lowercase (never), filling the whitespace under commercial pressure, fake-luxury gold gradients.
- **Accessibility:** thin display faces need size floors; grey-on-ivory often fails AA: test; hover-only interactions excluded keyboards, fix.
- **Implementation:** variable fonts with optical sizes solve the Didone-small problem; letterspacing tokens per case style.
- **Complements:** Minimalism, Dark Luxury, Cinematic, Art Deco (heritage flavour).
- **Conflicts:** Clay, Memphis, Grunge, Neo-Brutalism.
- **Transferable principles:** scarcity economics of attention (fewer, better, bigger); detail quality as trust signal. Transfers to premium product pages and award documents.
- **Brief example:** "Jewellery maison site: one piece per viewport on ivory, Didone numerals, letterspaced caps nav, 200ms fades only."
- **QA:** display faces above size floor; AA contrast despite softness; kerning hand-checked on display settings; accent colour nearly absent.

## Typography-Driven Design

- **Also known as:** type-led design, typographic design.
- **Period and origins:** continuous tradition: Constructivist and Dada type experiments (1920s), Swiss rationalism (1950s), Carson's deconstruction (1990s), contemporary type-only branding (documented strands; grouping is interpretation).
- **Philosophy:** type IS the image: when words are the content, letterforms can carry structure, emotion and identity without illustration.
- **Visual characteristics:** oversized type, type as texture/pattern, kinetic scale contrast, almost nothing non-typographic.
- **Geometry and composition:** letterforms as compositional masses; counters and rags become the "imagery"; grid or expressive placement, chosen deliberately.
- **Colour:** often two-tone (type/ground); colour inside letterforms as the one event.
- **Typography:** everything: one family pushed hard (weights, widths, optical sizes) usually beats many families; variable fonts are the native instrument.
- **Materials and finish:** none; ink logic.
- **Lighting and depth:** flat, or type given physical treatment (emboss, shadow) as the single effect.
- **Motion and interaction:** kinetic type sibling (see below); hover weight-shifts via variable axes.
- **Use for:** studios, foundries, conferences, posters, brands with strong verbal identity.
- **Avoid when:** audience needs imagery to understand (abstract type-only fails low-literacy or multilingual contexts).
- **Common mistakes:** display setting with text-type defaults (loose spacing at huge sizes: tighten), decorative illegibility where the words matter, five families doing one family's job.
- **Accessibility:** giant type still needs semantic structure; justified walls and all-caps paragraphs hurt dyslexic readers.
- **Implementation:** variable fonts, optical sizing, careful kerning at display sizes; SVG type outlines for locked compositions.
- **Complements:** Swiss, Editorial, Kinetic Typography, Brutalism.
- **Conflicts:** Skeuomorphism, Soft 3D (as co-leads; fine as accent pairs).
- **Transferable principles:** scale contrast as hierarchy engine; one-family-pushed-hard economy. Transfers to slide design, OOH, hero sections.
- **Brief example:** "Type-foundry specimen site: one variable family, 12px to 40vw range, black/white, weight animates on scroll."
- **QA:** kerning tightened at display sizes; hierarchy from scale/weight only; semantics intact; words legible where meaning lives.

## Kinetic Typography

- **Also known as:** motion type, animated typography.
- **Period and origins:** film title design (Saul Bass 1950s, documented) through music-video lyric culture to web animation APIs; variable-font animation is the current frontier (dated note, 2020s).
- **Philosophy:** time as a typographic dimension: rhythm, speed and transformation give words voice, emphasis and emotion.
- **Visual characteristics:** words entering/exiting with intent, scale and weight pulses, per-character choreography, text synced to audio.
- **Geometry and composition:** motion paths as layout; the frame is a stage with entrances and exits.
- **Colour:** simple grounds, type carries the event.
- **Typography:** sturdy forms survive motion blur; variable axes (weight/width) animate meaning.
- **Materials and finish:** none; timing is the material.
- **Lighting and depth:** optional z-moves (push in = emphasis).
- **Motion and interaction:** easing IS tone (snappy = wit, slow = gravitas); hold times must allow reading (roughly 0.3s + 0.1s/word minimum, interpretation from readability practice).
- **Use for:** title sequences, lyric videos, product launches, social ads, conference openers.
- **Avoid when:** reference content users must re-read; motion-sensitive audiences without alternatives.
- **Common mistakes:** animating everything (no hierarchy of motion), reading-time violations, easing mismatched to tone, text baked into video without captions/transcript.
- **Accessibility:** flashing limits (≤3 flashes/second, WCAG, documented); reduced-motion alternative; transcript for meaning.
- **Implementation:** per-character spans or SVG <text>; GSAP/CSS/Framer in web contexts; prerender for guaranteed timing.
- **Complements:** Typography-Driven, Motion Graphics, Cinematic.
- **Conflicts:** Luxury Editorial stillness, dense Data-Driven surfaces.
- **Transferable principles:** choreography hierarchy (one mover at a time), hold-time maths, easing-as-voice. Transfers to UI micro-interactions and slide builds.
- **Brief example:** "Keynote opener: one sentence, word-by-word weight-pulse entrances synced to beat, 0.5s holds, final lockup freezes."
- **QA:** every word readable in its hold; one choreographic idea; reduced-motion version exists; flash limits respected.

## Handwritten

- **Also known as:** hand-lettered, script style.
- **Period and origins:** script traditions span manuscript culture to signpainting (documented crafts); digital hand-made wave c. 2010s as anti-digital warmth (interpretation).
- **Philosophy:** the visible hand: imperfection certifies a human made this, building intimacy and informality.
- **Visual characteristics:** lettering (drawn words) vs calligraphy (written) vs handwriting fonts (typed): three different crafts; wobble, ink texture, personal quirks.
- **Geometry and composition:** organic baselines, bounce lettering, flourishes framing composition.
- **Colour:** ink-on-paper instincts; chalk, marker, brush palettes.
- **Typography:** hand elements for display/accent; pair with a quiet typeface for body; never set paragraphs in script.
- **Materials and finish:** tooth of paper, ink bleed, chalk dust; honest tool marks.
- **Lighting and depth:** flat; subtle paper shadow at most.
- **Motion and interaction:** write-on animation (mask reveals following stroke order).
- **Use for:** food, craft, kids, personal brands, greeting moments (thank-you states), signage warmth.
- **Avoid when:** authority/precision contexts; legal, medical, enterprise dashboards.
- **Common mistakes:** a handwriting font repeating identical letters (the tell: real hands never repeat), script in all-caps (unreadable), flourish soup, fake quirk on corporate messages.
- **Accessibility:** script is hard reading: display only, generous sizes; real text alternatives for lettering-as-image.
- **Implementation:** commission or draw lettering as SVG paths; write-on via stroke-dashoffset along the true ductus (stroke order).
- **Complements:** Paper Cutout, Bohemian, Organic Minimalism, Mid-Century accents.
- **Conflicts:** Swiss, Aerospace Instrumentation, Corporate Swiss, Futuristic.
- **Transferable principles:** imperfection as trust signal (dose-controlled); tool-truth (marks should look like a real tool made them). Transfers to annotation styles in diagrams and empty-state warmth.
- **Brief example:** "Bakery brand: brush-lettered logotype (drawn, not font), flour-white on charcoal, quiet humanist sans for menus."
- **QA:** repeated letters vary (or real lettering used); body text never script; tool texture consistent; alt text for lettered images.

## Duotone

- **Also known as:** two-colour design; duotone printing (origin craft).
- **Period and origins:** two-ink printing economy (documented print history); digital revival landmark: Spotify's duotone campaign era c. 2015 (documented campaign, widely analysed).
- **Philosophy:** constraint as unifier: mapping all imagery to two colours makes diverse sources feel like one voice, cheaply and boldly.
- **Visual characteristics:** photos mapped shadow-to-colour-A, highlight-to-colour-B; flat two-colour graphics; riso-print energy.
- **Geometry and composition:** the colour treatment unifies; composition free underneath.
- **Colour:** one dark anchor + one bright carry works best; near-complement pairs give maximum pop; test skin tones for dignity.
- **Typography:** third "colour" via ground/knockout type; bold sans holds its own against loud imagery.
- **Materials and finish:** riso/screenprint texture optional and honest to the heritage.
- **Lighting and depth:** source-photo contrast becomes the entire tonal structure: pick contrasty sources.
- **Motion and interaction:** palette-swap transitions between sections.
- **Use for:** music, events, campaign systems unifying messy photo libraries, budget-print projects.
- **Avoid when:** product-accurate colour matters (e-commerce goods), medical imagery.
- **Common mistakes:** low-contrast source photos (mud), unflattering skin mappings, two mid-value colours (no tonal anchor), inconsistent mapping across a set.
- **Accessibility:** ensure text/ground pair passes AA; meaning never by the duo alone for colour-blind users (values differ: good).
- **Implementation:** SVG feComponentTransfer or CSS blend recipes; define the exact mapping curve once, apply everywhere.
- **Complements:** Pop Art, Swiss, Typography-Driven, Grunge (riso strand).
- **Conflicts:** Luxury Editorial naturalism, Skeuomorphism.
- **Transferable principles:** mapping discipline (one transform applied uniformly) transfers to any multi-source unification; constraint as identity.
- **Brief example:** "Film-festival system: navy/coral duotone over archival stills, knockout white titles, one mapping curve for all 40 posters."
- **QA:** one mapping curve everywhere; source contrast sufficient; skin tones dignified; text pair passes AA.

## Monochromatic

- **Also known as:** single-hue design, tonal design.
- **Period and origins:** perennial (ink painting traditions, blueprint cyanotypes documented); periodic digital fashion waves.
- **Philosophy:** one hue, many values: removing hue contrast forces value structure to do all the work, yielding instant cohesion and controlled mood.
- **Visual characteristics:** tints/shades/tones of one hue; value steps as hierarchy; texture gaining importance.
- **Geometry and composition:** value contrast replaces colour contrast as the focal tool.
- **Colour:** build a 7-10 step value ramp of the hue; neutrals derived from the hue (warm/cool greys), not pure grey.
- **Typography:** value steps assign type hierarchy; reversed type on dark steps.
- **Materials and finish:** texture differentiates same-value areas.
- **Lighting and depth:** fully available: light/shadow reads naturally in one hue.
- **Motion and interaction:** value shifts for states (hover = one step up).
- **Use for:** moody brand sites, photography portfolios, data-viz single-metric emphasis, blueprint aesthetics.
- **Avoid when:** multi-category data needs hue coding; alarm/severity systems (red must exist).
- **Common mistakes:** too few value steps (flat mush), the hue drifting across elements (one hue means one hue), forgetting a true-dark anchor.
- **Accessibility:** value contrast conveniently aligns with WCAG contrast; verify steps used for text pairs; colour-blind safe by construction.
- **Implementation:** generate the ramp in a perceptual space (OKLCH, dated tooling note 2026) so steps are even; tokenise steps.
- **Complements:** Minimalism, Dark Luxury, Line Art, Cinematic grading.
- **Conflicts:** Memphis, Pop Art, Maximalism.
- **Transferable principles:** value structure as the skeleton beneath every palette (check any design in greyscale); perceptual ramp construction transfers to all data-viz sequential scales.
- **Brief example:** "Architecture portfolio: ink-blue ramp, 9 steps, photography duplexed into the hue, white type on steps 7-9."
- **QA:** single hue verified (no drift); ≥7 even perceptual steps; text pairs AA; greyscale version still reads.

## Cinematic

- **Also known as:** filmic design.
- **Period and origins:** borrows a century of film grammar (documented craft: composition, grading, titles); as web/product aesthetic, prominent in premium storytelling sites 2010s onward.
- **Philosophy:** frame, light and grade tell the story before a word lands; the viewer is an audience, not a user, for a moment.
- **Visual characteristics:** widescreen ratios (2.39:1 crops), letterboxing, colour grading (teal-orange and its alternatives), atmospheric haze, shallow depth of field, title-sequence type.
- **Geometry and composition:** film blocking: thirds, leading lines, headroom/lookroom; sequence thinking (shots, not pages).
- **Colour:** grade as emotional signature; lifted blacks or crushed contrast as chosen voice; consistent LUT-like treatment.
- **Typography:** restrained title-case serifs or extended sans; letterspaced caps as "titles"; subtitles idiom for captions.
- **Materials and finish:** grain, bloom, anamorphic flare: dose like seasoning.
- **Lighting and depth:** motivated light (it comes from somewhere), practical glows, volumetric atmosphere.
- **Motion and interaction:** slow push-ins, parallax dolly, cut-on-scroll; pacing curves like editing.
- **Use for:** film/TV promos, automotive, premium product stories, game sites, brand films.
- **Avoid when:** utility and speed matter; cinematic weight slows task UIs and bloats pages.
- **Common mistakes:** grading everything teal-orange by default, letterboxing content that users need to read, autoplay heavy video punishing bandwidth, drama with no narrative spine.
- **Accessibility:** captions for all video; contrast within graded imagery for overlaid text; motion sensitivity respected.
- **Implementation:** heavy media: lazy-load, poster frames, compressed loops; CSS filters can approximate grades on images.
- **Complements:** Luxury Editorial, Surreal, Dark Luxury, Motion Graphics.
- **Conflicts:** Flat utility surfaces, Neo-Brutalism, Clay.
- **Transferable principles:** motivated lighting and grade-consistency transfer to all imagery systems; sequence pacing transfers to scroll-telling and onboarding.
- **Brief example:** "EV launch page: 2.39:1 hero loop, dusk grade, headlight practicals, letterspaced title reveals on scroll beats."
- **QA:** one grade across all media; text over imagery AA via scrims; captions present; page weight budgeted.

## Motion Graphics

- **Also known as:** mograph, animated graphic design.
- **Period and origins:** title-design lineage (Bass, Binder, documented), broadcast packages, After Effects era (1993 onward, documented tool history), web animation APIs current.
- **Philosophy:** graphic design in time: movement explains relationships, directs attention and gives brands a voice words cannot.
- **Visual characteristics:** animated shapes/type/icons, explainer language, transitions as meaning, lottie-style vector motion.
- **Geometry and composition:** staging and timing replace static layout; motion paths are compositional lines.
- **Colour:** brand systems in motion; colour changes as state narrative.
- **Typography:** kinetic type subset; lockups built to animate (layer logic).
- **Materials and finish:** flat vector dominant; textures must survive compression.
- **Lighting and depth:** faux depth via parallax, scale and blur layers.
- **Motion and interaction:** the 12 animation principles apply (squash/stretch dosed for brand tone); easing library = brand voice; 200-500ms UI range vs 1-3s narrative beats.
- **Use for:** explainers, logo stings, UI micro-interactions, social content, data storytelling.
- **Avoid when:** motion adds no information and costs attention; reference material users revisit.
- **Common mistakes:** everything moving (no hierarchy), linear easing (dead), duration uniformity (robotic), decorative motion demonstrating skill not serving content.
- **Accessibility:** reduced-motion variants mandatory; flashing limits; no meaning carried by motion alone.
- **Implementation:** SVG/Lottie for vector motion; transform/opacity for performance; FLIP techniques for layout moves.
- **Complements:** Kinetic Typography, Flat, Data-Driven, Soft 3D.
- **Conflicts:** Luxury Editorial stillness, print-first systems.
- **Transferable principles:** choreography hierarchy, easing-as-voice, motion-explains-spatial-change. Transfers to every interactive product this skill touches.
- **Brief example:** "Feature explainer: 45s, three scenes, one brand easing curve, icons morph to show data flow, captions baked and SRT."
- **QA:** one easing voice; one primary mover per beat; reduced-motion build; informs rather than decorates (state what each move explains).

## Data-Driven / Infographic Design

- **Also known as:** information design, data visualisation.
- **Period and origins:** Playfair's charts (1780s), Minard's Napoleon map (1869), Neurath's Isotype (1920s), Tufte's codification (1983 onward), all documented landmarks.
- **Philosophy:** evidence rendered honestly: the data is the hero, design maximises accurate comprehension per unit of attention.
- **Visual characteristics:** charts, diagrams, pictograms, annotation layers, small multiples, restrained chrome.
- **Geometry and composition:** position > length > angle > area > colour as encoding accuracy ranking (documented perception research, Cleveland/McGill 1984); grids aligning multiples.
- **Colour:** functional: sequential ramps for magnitude, diverging for signed, categorical ≤7 distinguishable hues; grey as structural default, colour as signal.
- **Typography:** quiet sans, strong numerals (tabular figures), annotation hierarchy (title = finding, not topic).
- **Materials and finish:** none; ink-ratio discipline (maximise data-ink, interpretation of Tufte's principle).
- **Lighting and depth:** flat; 3D charts distort perception, avoid.
- **Motion and interaction:** transitions preserving object constancy; tooltips as annotation layer; animation for time only when it aids comparison.
- **Use for:** dashboards, reports, journalism, scientific communication, posters with real evidence.
- **Avoid when:** no reliable data (decoration pretending to be evidence is the cardinal sin).
- **Common mistakes:** truncated axes exaggerating effects, dual axes implying false correlation, rainbow ramps, pie charts beyond 3 slices, legends when direct labelling fits, decorating instead of annotating.
- **Accessibility:** colour-blind-safe palettes, patterns/labels beyond hue, data tables as alternatives, contrast on all marks.
- **Implementation:** honest scales documented; SVG-native charts; annotation layer as first-class content.
- **Complements:** Swiss, Scientific/Technical Illustration, Aerospace Instrumentation, Editorial.
- **Conflicts:** Maximalism, Surreal, Grunge (as chart treatments).
- **Transferable principles:** encoding-accuracy ranking, data-ink discipline and finding-first titles transfer to every dashboard, report and diagram this skill produces.
- **Brief example:** "Breach-trends spread: small-multiple lines per sector, direct labels, finding-as-title, grey structure with one alarm hue."
- **QA:** axes honest (zero or stated), encodings match data types; colour-blind check passed; titles state findings; every pixel of ink justified.
