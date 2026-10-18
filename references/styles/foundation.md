# Foundation and Functional Styles

Baseline philosophies most other styles extend or react against. Index: `../style-catalogue.md`.

## Minimalism

- **Also known as:** reductive design, less-is-more.
- **Period and origins:** minimal art, c. 1960s United States (Judd, Martin); design lineage runs earlier through Bauhaus functionalism and Japanese aesthetics (interpretation: these streams converged rather than one inventing it).
- **Philosophy:** remove everything that does not serve the purpose; what remains gains weight. Reduction is a means to clarity, not an end.
- **Visual characteristics:** few elements, generous whitespace, restrained palette, no ornament, high craft in what remains.
- **Geometry and composition:** simple underlying grid, large margins, strong alignment, one dominant focal point.
- **Colour:** narrow palette, often neutral base plus one accent; colour used as signal, not filler.
- **Typography:** one or two families, scale does the hierarchy work; often grotesque sans or quiet serif.
- **Materials and finish:** honest single materials; in UI, flat or softly elevated surfaces.
- **Lighting and depth:** minimal; shadow only where it communicates layering.
- **Motion and interaction:** sparse, purposeful transitions; nothing decorative.
- **Use for:** premium products, portfolios, reading experiences, tools where content density is low and focus is high.
- **Avoid when:** information density is genuinely high, users need many simultaneous affordances, or warmth and personality are the brief.
- **Common mistakes:** emptiness mistaken for minimalism (removing needed affordances), grey-on-white illegibility, hiding navigation to look clean.
- **Accessibility:** low-contrast "quiet" palettes often fail WCAG; verify contrast; do not remove visible focus states.
- **Implementation:** cheap to build, hard to design; spacing tokens and a strict type scale are mandatory or it drifts.
- **Complements:** Japanese Minimalism, Swiss, Scandinavian, Dark Luxury.
- **Conflicts:** Maximalism, Memphis, Grunge, Victorian.
- **Transferable principles:** earn every element; whitespace as structure; a small system executed perfectly beats a large one executed loosely.
- **Brief example:** "Landing page for a privacy-first notes app: one headline, one screenshot, one CTA, nothing else competes."
- **QA:** every element has a stated purpose; contrast passes AA; hierarchy survives squint test; removal of any remaining element would hurt the message.

## Maximalism

- **Also known as:** more-is-more design.
- **Period and origins:** recurring tendency across eras (Baroque, Victorian, Memphis); named as a contemporary design position largely in reaction to 2010s flat minimalism (interpretation).
- **Philosophy:** abundance, layering and personality as deliberate meaning; density is the message, but curated density, not accumulation.
- **Visual characteristics:** layered pattern, saturated colour, mixed imagery, filled space, expressive type.
- **Geometry and composition:** still needs a hidden grid; focal points created by contrast of density, scale breaks for breathing points.
- **Colour:** many hues, high saturation; controlled by a dominant family plus accents, or it collapses.
- **Typography:** mixed families and weights allowed; hierarchy must stay unmistakable.
- **Materials and finish:** rich textures, foils, gloss, pattern-on-pattern.
- **Lighting and depth:** layered depth, drop shadows and overlap welcomed.
- **Motion and interaction:** can be lively; respect reduced-motion preferences.
- **Use for:** fashion, music, culture, food, campaigns needing energy and memorability.
- **Avoid when:** task-critical UI, dense data work, accessibility-sensitive audiences, trust-conservative sectors (banking dashboards).
- **Common mistakes:** no hierarchy (everything shouts), clutter without curation, unreadable body text on pattern.
- **Accessibility:** text over pattern needs scrims; motion density can overwhelm; verify contrast per-element.
- **Implementation:** heavy assets; performance budget and art direction per breakpoint required.
- **Complements:** Pop Art, Collage, Memphis, Bohemian, Maximalist Editorial.
- **Conflicts:** Minimalism, Swiss, Corporate Swiss, Aerospace Instrumentation.
- **Transferable principles:** density can be designed; contrast of density creates focus; personality is a legitimate functional requirement.
- **Brief example:** "Festival identity: clashing poster pattern system, but ticket-purchase flow stays calm and conventional."
- **QA:** a clear first-read exists; body text readable everywhere; density is curated (each layer named); performance tested on mobile.

## Swiss / International Typographic Style

- **Also known as:** International Style (graphic), Swiss Design.
- **Period and origins:** Switzerland, c. 1950s; Basel and Zürich schools; Josef Müller-Brockmann, Armin Hofmann, Emil Ruder; roots in Bauhaus and Constructivism.
- **Philosophy:** objective, impersonal clarity: the designer serves the information. The grid is the instrument of order.
- **Visual characteristics:** mathematical grids, asymmetric layouts, flush-left ragged-right text, photography over illustration, abundant structured whitespace.
- **Geometry and composition:** modular grid governs everything; alignment carries the aesthetic; diagonal or scale tension within strict order.
- **Colour:** restrained; black, white, one or two flat signal colours (classically red).
- **Typography:** grotesque sans (Helvetica, Univers lineage); hierarchy by size, weight and placement, not decoration.
- **Materials and finish:** flat ink on paper sensibility; in UI, flat surfaces and hairline rules.
- **Lighting and depth:** none; the plane is the medium.
- **Motion and interaction:** grid-respecting transitions; type can move, order must survive.
- **Use for:** wayfinding, reports, dashboards, enterprise identity, technical documentation, posters with real information.
- **Avoid when:** warmth, nostalgia or handcraft is the emotional brief.
- **Common mistakes:** grid worship producing monotony; Helvetica as costume with no grid logic underneath; whitespace without rhythm.
- **Accessibility:** naturally strong (high contrast, clear hierarchy); keep body sizes generous, grotesques can blur at small sizes.
- **Implementation:** translates directly to CSS grid and design tokens; the cheapest style to systematise.
- **Complements:** Corporate Swiss, Data-Driven, Aerospace Instrumentation, Minimalism, Architectural Modernism.
- **Conflicts:** Grunge, Bohemian, Handwritten, Memphis.
- **Transferable principles:** the grid as reasoning tool; hierarchy from placement not ornament; objectivity as a designable quality. Transfers to reports, slides, diagrams, SVG layout.
- **Brief example:** "Quarterly threat report: 12-column grid, Univers-class sans, black/white/red, every chart on the same baseline grid."
- **QA:** every element sits on the grid or breaks it for a stated reason; hierarchy readable at arm's length; one type family suffices; colour used only as signal.

## Bauhaus

- **Also known as:** Staatliches Bauhaus (school), Bauhaus style (shorthand).
- **Period and origins:** Germany, 1919-1933 (Weimar, Dessau, Berlin); Gropius, Moholy-Nagy, Albers, Breuer, Bayer; closed under Nazi pressure, diaspora spread it worldwide (documented).
- **Philosophy:** unity of art, craft and industry; form follows function; design for mass production without loss of quality.
- **Visual characteristics:** elementary geometry (circle, square, triangle), primary colours plus black/white, sans-serif type, visible construction.
- **Geometry and composition:** geometric construction, strong horizontals/verticals, functional asymmetry.
- **Colour:** primaries (red, yellow, blue) as system, not decoration; large neutral fields.
- **Typography:** geometric sans (Bayer's universal lettering experiments); lowercase favoured historically.
- **Materials and finish:** tubular steel, glass, honest industrial materials; in 2D, flat unmodulated colour.
- **Lighting and depth:** flat planes; depth via overlap, not shading.
- **Motion and interaction:** geometric, mechanical rhythm suits it.
- **Use for:** education, culture, brand systems wanting constructive optimism, poster and identity work.
- **Avoid when:** softness, luxury texture or organic warmth is required; when primaries would fight the brand.
- **Common mistakes:** treating it as "circles and primary colours" clip-art; ignoring the production-logic core.
- **Accessibility:** primary palette is high-contrast by nature; yellow on white fails, test pairs.
- **Implementation:** simple shapes, light assets; geometric type needs careful spacing at small sizes.
- **Complements:** Swiss, De Stijl lineage, Flat Design, Constructivist-flavoured work.
- **Conflicts:** Victorian, Art Nouveau, Skeuomorphism, Luxury Editorial.
- **Transferable principles:** design for the means of production; elementary forms as vocabulary; workshop unity of disciplines. Transfers to component systems and icon grammar.
- **Brief example:** "Developer-conference identity: three geometric marks from one construction circle, primaries on warm white, DIN-class sans."
- **QA:** forms derive from a stated construction; palette limited to the system; type geometric and legible small; nothing decorative survives without function.

## Brutalism

- **Also known as:** béton brut (architecture), web brutalism (digital).
- **Period and origins:** architecture c. 1950s-1970s (Le Corbusier's Unité 1952, Smithsons' New Brutalism); web revival c. 2014 onward as reaction to templated sameness (interpretation widely held).
- **Philosophy:** raw structural honesty; the material and mechanism exposed without cosmetic mediation; confrontation over comfort.
- **Visual characteristics:** exposed structure, raw surfaces, heavy mass, system defaults (digital: default fonts, visible borders, unstyled-feeling blocks).
- **Geometry and composition:** massive blocks, repetition of structural units, deliberate awkwardness tolerated.
- **Colour:** concrete greys, monochrome plus one aggressive accent; or clashing defaults in web form.
- **Typography:** monospace or default stacks; oversized headings; little typographic nuance on purpose.
- **Materials and finish:** raw concrete, unfinished textures; digital equivalent is the unpolished surface.
- **Lighting and depth:** hard shadow, flat fills; no soft gradients.
- **Motion and interaction:** abrupt, unsmoothed state changes fit the language.
- **Use for:** culture, zines, portfolios, statements against polish; architecture: civic mass and permanence.
- **Avoid when:** users need reassurance, e-commerce conversion, accessibility-critical services; "ugly on purpose" taxes every user.
- **Common mistakes:** confusing it with Neo-Brutalism (which is friendlier and more commercial); randomness mistaken for rawness; broken usability excused as style.
- **Accessibility:** default focus states often survive, good; contrast and target sizes still mandatory; chaos layouts punish screen readers, keep DOM order sane.
- **Implementation:** cheap, fast, resilient; the discipline is in what you refuse to style.
- **Complements:** Monospace/terminal aesthetics, Grunge, Neo-Brutalism, Typography-Driven.
- **Conflicts:** Luxury Editorial, Glassmorphism, Organic Minimalism, Soft 3D.
- **Transferable principles:** honesty about structure; defaults as a palette; mass and repetition as composition. Transfers to data tables and engineering docs that refuse decoration.
- **Brief example:** "Research-lab site: system font, black rules, visible grid lines, raw image dumps with captions."
- **QA:** rawness is consistent (not half-polished); navigation remains findable; contrast passes; DOM order logical.

## Flat Design

- **Also known as:** flat UI; associated with Metro/Modern UI and iOS 7 era.
- **Period and origins:** mainstream c. 2010-2013 (Microsoft Metro 2010, iOS 7 in 2013, documented); roots in Swiss style and modernist flatness.
- **Philosophy:** the screen is a flat medium; remove simulated physicality so content and colour carry the interface.
- **Visual characteristics:** unshaded fills, simple geometric icons, no bevels/gloss/texture, bold colour fields.
- **Geometry and composition:** card and tile layouts, strict alignment, generous padding.
- **Colour:** confident saturated palettes; colour replaces depth as the differentiator.
- **Typography:** large, light-to-medium sans; type carries hierarchy that shadows used to.
- **Materials and finish:** none simulated; pure surface.
- **Lighting and depth:** zero to near-zero; later "flat 2.0" reintroduced subtle shadows for affordance (dated observation, c. 2014+).
- **Motion and interaction:** motion substitutes for depth cues; transitions explain spatial relationships.
- **Use for:** scalable UI systems, icon sets, performance-critical products, SVG-friendly branding.
- **Avoid when:** affordances must be instantly obvious to novice users (pure flat famously hid what was tappable); rich storytelling imagery is the point.
- **Common mistakes:** invisible buttons (no affordance), colour-only state signalling, uniform flatness erasing hierarchy.
- **Accessibility:** affordance loss harms motor/cognitive accessibility; pair colour with shape/label; maintain focus visibility.
- **Implementation:** lightest possible rendering; ideal for SVG and design tokens.
- **Complements:** Swiss, Bauhaus, Material-style elevation (as corrective), Vector Art.
- **Conflicts:** Skeuomorphism, Glassmorphism (philosophically), Steampunk.
- **Transferable principles:** let the medium be itself; motion as spatial explanation; colour as structure. Transfers to diagram and icon systems.
- **Brief example:** "Icon system for a CLI company: 24px grid, 2px stroke-free solid shapes, 6-colour functional palette."
- **QA:** interactive elements visibly interactive; hierarchy survives greyscale; icons legible at 16px; no orphan shadows.

## Skeuomorphism

- **Also known as:** realistic UI, rich UI.
- **Period and origins:** concept ancient (ornament retaining older material forms, documented in archaeology); digital peak c. 2007-2012 (early iOS leather/felt textures), revived selectively in dimensional UI since c. 2020 (interpretation).
- **Philosophy:** borrow the appearance and behaviour of familiar physical objects so the interface explains itself.
- **Visual characteristics:** textures (leather, paper, metal), realistic shadows and highlights, physical metaphors (switches, dials, shelves).
- **Geometry and composition:** object-shaped components; layout follows the metaphor's physical logic.
- **Colour:** material-derived palettes; realism constrains hue freedom.
- **Typography:** often engraved/embossed effects; must stay legible beneath the styling.
- **Materials and finish:** simulated materials are the entire language; quality of simulation decides credibility.
- **Lighting and depth:** single believable light source; consistent shadow direction is non-negotiable.
- **Motion and interaction:** physics-faithful: switches flick, pages curl; behaviour must match the metaphor.
- **Use for:** audio plugins and instruments, onboarding novices, playful products, moments where the metaphor genuinely maps to the function.
- **Avoid when:** the metaphor limits the function (a "tape deck" cannot show a playlist of 10,000), information density is high, or the audience is fluent in abstract UI.
- **Common mistakes:** metaphor without its behaviour (a dial you cannot drag), mixed light sources, decoration that adds no mapping.
- **Accessibility:** textured backgrounds hurt contrast; embossed text often fails AA; ensure controls are real controls to assistive tech, not pictures.
- **Implementation:** heavy assets, hard theming, poor scalability; budget for retina-grade texture work.
- **Complements:** Soft 3D, Clay (as modern descendants), Cinematic.
- **Conflicts:** Flat, Swiss, Brutalism, Minimalism.
- **Transferable principles:** affordance through familiarity; behavioural fidelity to a metaphor; one light source discipline (transfers to all dimensional UI and illustration).
- **Brief example:** "Synth plugin: brushed-aluminium panel, physically draggable knobs with inertia, legible silkscreen labels."
- **QA:** metaphor maps to actual behaviour; one light source throughout; labels pass contrast on texture; controls keyboard-operable.

## Organic Minimalism

- **Also known as:** soft minimalism, warm minimalism.
- **Period and origins:** contemporary synthesis, broadly c. 2015 onward in interiors, branding and UI (interpretation; no single founding moment).
- **Philosophy:** minimalist restraint without minimalist coldness; nature's palette, curves and materials humanise reduction.
- **Visual characteristics:** muted earth tones, rounded geometry, soft shadows, natural textures used sparingly, abundant calm whitespace.
- **Geometry and composition:** curves and superellipses over hard rectangles; asymmetry kept gentle.
- **Colour:** off-whites, sand, clay, sage, terracotta; low saturation, warm greys instead of cold.
- **Typography:** humanist sans or low-contrast serifs; comfortable sizes, airy leading.
- **Materials and finish:** linen, wood, ceramic, matte surfaces; in UI, grain-free soft fills.
- **Lighting and depth:** diffuse, warm; shadows blurred and tinted, never pure black.
- **Motion and interaction:** slow, eased, breathing-pace transitions.
- **Use for:** wellness, skincare, hospitality, lifestyle products, premium consumer apps wanting calm trust.
- **Avoid when:** urgency, technical authority or data density is required; muted palettes read sleepy in ops tooling.
- **Common mistakes:** contrast so low it fails legibility; beige sameness with no focal point; "organic" textures pasted on rigid layouts.
- **Accessibility:** the chief risk is contrast; verify AA on every text/background pair; warm greys mislead the eye.
- **Implementation:** needs careful shadow and radius tokens; superellipse corners need SVG or mask support.
- **Complements:** Japanese Minimalism, Scandinavian, Organic/Biomorphic, Luxury Editorial.
- **Conflicts:** Cyberpunk, Neo-Brutalism, Memphis, Aerospace Instrumentation.
- **Transferable principles:** warmth is a parameter (hue temperature, radius, shadow softness), tunable in any system; calm as a designed outcome.
- **Brief example:** "Meditation app: sand/sage palette, 24px radii, one hero illustration, 300ms eased transitions."
- **QA:** all text passes AA despite muted palette; one clear focal point per screen; radii and shadows from tokens; motion respects reduced-motion.

## Japanese Minimalism

- **Also known as:** Zen aesthetics in design; related concepts: ma (interval), wabi-sabi (imperfect beauty), kanso (simplicity).
- **Period and origins:** rooted in centuries of Japanese tea-ceremony, sumi-e and architectural tradition (documented); the modern design articulation spans 20th-century figures through contemporary practice (e.g. MUJI's no-brand philosophy, c. 1980 onward).
- **Philosophy:** emptiness is content; the interval between elements carries meaning; imperfection and impermanence are honest, not flaws.
- **Visual characteristics:** radical whitespace, asymmetric balance, natural materials, subdued palette, one imperfect human note.
- **Geometry and composition:** asymmetry as default; off-centre focal points; vertical rhythm from traditional formats (interpretation when applied digitally).
- **Colour:** paper whites, ink blacks, muted naturals; a single seasonal accent.
- **Typography:** restrained; generous spacing; mixed Latin/CJK settings need real typographic care (line height, character spacing).
- **Materials and finish:** paper, wood, stone textures referenced with restraint; matte everything.
- **Lighting and depth:** soft natural light logic; shadow as atmosphere (cf. Tanizaki's In Praise of Shadows, 1933, documented essay).
- **Motion and interaction:** very slow reveals; stillness is a state, not a bug.
- **Use for:** craft brands, tea/food, architecture portfolios, editorial about process and patience.
- **Avoid when:** users need speed and density; when "zen" would be costume on an unrelated product (orientalist pastiche risk).
- **Common mistakes:** centring everything (its balance is asymmetric), confusing it with generic minimalism, decorative kanji without meaning.
- **Accessibility:** large empty layouts are screen-reader friendly if landmarks exist; verify ink-grey contrast.
- **Implementation:** demands discipline in spacing scale; asymmetric grids need explicit design, they do not emerge from frameworks.
- **Complements:** Minimalism, Organic Minimalism, Line Art.
- **Conflicts:** Maximalism, Y2K, Graffiti, Victorian.
- **Transferable principles:** the interval as a designed element; asymmetric balance; one imperfection humanising a perfect system. Transfers to pacing of decks, long-form pages and photography sequencing.
- **Brief example:** "Ceramics studio site: one pot per viewport, off-centre, ink-grey captions, 60% empty space."
- **QA:** balance is asymmetric and intentional; whitespace rhythmic not accidental; cultural references accurate and purposeful; contrast verified.

## Scandinavian Design

- **Also known as:** Nordic design, Scandinavian modern.
- **Period and origins:** Nordic countries, c. 1930s-1950s flowering (Aalto, Jacobsen, Wegner; Lunning Prize era, documented); rooted in social-democratic ideals of good design for all.
- **Philosophy:** democratic functionalism with warmth: beautiful, useful objects affordable to ordinary people; light as a precious resource.
- **Visual characteristics:** pale woods, white walls, clean lines softened by craft, functional objects with gentle curves, hygge cosiness.
- **Geometry and composition:** simple volumes, honest joinery logic, uncluttered but lived-in arrangements.
- **Colour:** whites and pale greys warmed by wood tones; muted blues, greens, mustard as accents.
- **Typography:** clean humanist sans; friendly roundness over geometric severity.
- **Materials and finish:** birch, beech, wool, leather; matte and tactile; nothing precious for its own sake.
- **Lighting and depth:** maximising soft daylight; warm artificial light; gentle shadows.
- **Motion and interaction:** modest, friendly micro-interactions.
- **Use for:** furniture and home goods, family products, fintech wanting approachable trust, public-sector services.
- **Avoid when:** drama, luxury exclusivity or technical edge is the brief; it reads modest by design.
- **Common mistakes:** IKEA-pastiche flatness without craft detail; coldness (forgetting the warmth half); grey everything.
- **Accessibility:** strong tradition of inclusive design; keep its naturally good contrast and generous targets.
- **Implementation:** component-friendly; warmth lives in radius, photography and microcopy choices.
- **Complements:** Organic Minimalism, Mid-Century Modern, Minimalism, Flat.
- **Conflicts:** Dark Luxury, Cyberpunk, Steampunk, Maximalism.
- **Transferable principles:** democratic quality (design for everyone as a constraint); warmth through material honesty; light as a design material. Transfers to product strategy and inclusive UI defaults.
- **Brief example:** "Family-banking app: warm white UI, wood-toned illustration, rounded humanist sans, plain-language microcopy."
- **QA:** feels warm not sterile; affordable/attainable tone preserved; contrast and target sizes inclusive; craft detail present somewhere visible.
