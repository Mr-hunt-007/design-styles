# Contemporary and Specialist Styles

Current specialist languages and discipline-rooted aesthetics. Where a style has a discipline file (aerospace, architecture, industrial design), that file holds the engineering truth; this entry holds the visual language. Index: `../style-catalogue.md`.

## Cyberpunk

- **Also known as:** high-tech low-life aesthetic.
- **Period and origins:** 1980s fiction (Gibson's Neuromancer 1984, Blade Runner 1982, documented); game/film visual canon since; neon-noir digital trend ongoing.
- **Philosophy:** technological saturation plus social decay: density, noise and commercial glare as a critique worn as style.
- **Visual characteristics:** neon on wet black, glitch artefacts, CJK signage layers, HUD overlays, scanlines, chrome and decay together.
- **Geometry and composition:** vertical urban density, layered signage depth, asymmetric HUD framing.
- **Colour:** magenta/cyan neon, acid accents on near-black; sodium-vapour oranges.
- **Typography:** condensed techno sans, glitched display, fake-system monospace readouts.
- **Materials and finish:** wet reflections, emissive glow, grime over chrome.
- **Lighting and depth:** practical neon sources, volumetric haze, bloom.
- **Motion and interaction:** glitch stutters, scan reveals, flicker (dose carefully).
- **Use for:** games, esports, music, fiction marketing, cybersecurity brands accepting the cliché knowingly.
- **Avoid when:** genuine security-operations UIs (noise fights analysis), accessibility-critical products, brands avoiding dystopian connotations.
- **Common mistakes:** glow on everything (no darkness left to contrast), unreadable glitch type on information, cyberpunk-as-default for anything "tech".
- **Accessibility:** neon-on-black often passes contrast but bloom halos hurt legibility; flicker must respect photosensitivity limits.
- **Implementation:** glow = layered shadows/blurs, budget GPU; glitch via clip-path/channel-shift snippets.
- **Complements:** Futuristic, Y2K, Retro-Futurism, Aurora (calmed).
- **Conflicts:** Scandinavian, Organic Minimalism, Luxury Editorial.
- **Transferable principles:** practical-light logic (glow comes from sources, not styles); density layering with one readable channel. Transfers to dark-mode drama done with discipline.
- **Brief example:** "Esports tournament identity: wet-asphalt black, two neon hues only, glitch reserved for the logotype sting, clean schedule tables."
- **QA:** ≤2 neon hues; information layer glitch-free; flicker within safety limits; darkness preserved for contrast.

## Futuristic

- **Also known as:** sleek-tech, advanced-tech aesthetic.
- **Period and origins:** perennial moving target; each era's "future" dates fast (interpretation); current register (2020s): dark gradients, precision hairlines, AI-glow motifs.
- **Philosophy:** communicate "ahead": precision, speed and novel capability, without committing to a named fiction.
- **Visual characteristics:** dark or ultra-clean grounds, hairline geometry, abstract tech motifs (particles, meshes, orbits), restrained glow.
- **Geometry and composition:** engineered alignment, wide aspect compositions, isometric or orbital abstract diagrams.
- **Colour:** deep navy/graphite bases, electric accent (cyan, violet), white space variant for "lab clean".
- **Typography:** extended or geometric sans (Eurostile lineage risks cliché: consider neutral grotesques), tabular numerals, generous tracking on caps.
- **Materials and finish:** glass, brushed metal, light itself.
- **Lighting and depth:** controlled glow, rim lights, depth-of-field renders.
- **Motion and interaction:** precise fast easing, data-stream reveals, scanning beams sparingly.
- **Use for:** deep-tech, AI, aerospace-adjacent brands, concept vehicles, product launches.
- **Avoid when:** warmth/trust for consumers matters more than edge; futurism ages: date-stamp your choices.
- **Common mistakes:** sci-fi prop clutter (fake coordinates, meaningless hex), glow inflation, Eurostile-by-default, dark mode with AA failures.
- **Accessibility:** thin hairlines on dark fail low-vision users: minimum stroke/contrast floors; decorative data noise confuses screen readers, hide it.
- **Implementation:** hairlines need device-pixel alignment; particle/mesh backgrounds budgeted and pausable.
- **Complements:** Aerospace Instrumentation (honest version), Aurora, Dark Luxury, Glassmorphism.
- **Conflicts:** Handwritten, Bohemian, Victorian.
- **Transferable principles:** precision as credibility (alignment tolerance, consistent radii); abstraction over fake data. Transfers to any brand wanting engineered feel without fiction.
- **Brief example:** "AI-platform launch: graphite ground, one violet accent, hairline orbital diagram of real architecture, grotesque caps."
- **QA:** no fake data/labels; contrast floors met on dark; one accent hue; motifs map to real product concepts.

## Dark Luxury

- **Also known as:** dark premium, noir luxury.
- **Period and origins:** contemporary synthesis (interpretation): luxury-editorial codes moved onto near-black grounds, prominent in spirits, audio, automotive and fintech-premium since c. 2015.
- **Philosophy:** scarcity in shadow: darkness frames the few precious elements; restraint plus one tactile richness signals expense.
- **Visual characteristics:** near-black grounds (not pure #000), hairline gold/brass rules, high-contrast serifs or spare grotesques, dramatic product lighting.
- **Geometry and composition:** vast dark margins, centred or poised asymmetric focus, one hero per view.
- **Colour:** charcoal/ink bases, champagne/brass/copper accents, deep accent hue (oxblood, forest) optional.
- **Typography:** Didone display or refined grotesque; letterspaced caps labels; numerals matter (prices, vintages).
- **Materials and finish:** implied leather, stone, metal; matte darkness with one specular event.
- **Lighting and depth:** chiaroscuro product light, soft falloff, no flat black voids behind subjects.
- **Motion and interaction:** slow confident fades, metallic sheen sweep once.
- **Use for:** spirits, watches, audio, automotive, private banking, premium SaaS tiers.
- **Avoid when:** approachability, daylight utility, dense data (pure dark data UIs are a different craft: see Aerospace Instrumentation).
- **Common mistakes:** pure black + pure gold text failing AA, gold gradients everywhere (casino effect), thin serifs dissolving on dark, no texture variance (flat void).
- **Accessibility:** dark modes punish astigmatism with thin light text: weight up; AA on gold tones carefully measured.
- **Implementation:** elevated-surface tokens (dark greys stepping), bloom control on light text, true-black OLED considerations.
- **Complements:** Luxury Editorial, Art Deco, Cinematic, Monochromatic.
- **Conflicts:** Clay, Scandinavian, Memphis, Pop Art.
- **Transferable principles:** darkness as frame (not fill); one-specular-event discipline. Transfers to premium dashboard skins and award sites.
- **Brief example:** "Single-malt site: ink ground, one bottle in chiaroscuro, champagne hairline rules, letterspaced caps, serif numerals for age statements."
- **QA:** text AA on measured swatches; one metallic event per view; black is elevated greys not void; weight compensation for dark mode applied.

## Organic / Biomorphic

- **Also known as:** biomorphism, nature-derived form.
- **Period and origins:** biomorphic abstraction in 20th-century art (Arp, Miró, documented), Aalto's curves, contemporary parametric/generative nature forms; blob UI waves periodically.
- **Philosophy:** forms grown, not drawn: nature's curves, branching and gradients of density read as alive, humane and non-mechanical.
- **Visual characteristics:** blob shapes, branching structures, cell/membrane textures, flowing dividers, asymmetric soft masses.
- **Geometry and composition:** no straight lines doctrine (dosed); curvature continuity (G2 smoothness) distinguishes elegant from lumpy.
- **Colour:** natural gradients (leaf, dusk, skin), earth-to-vivid ranges.
- **Typography:** humanist forms echo the curves; avoid rigid geometrics.
- **Materials and finish:** membrane translucency, organic texture, soft matte.
- **Lighting and depth:** soft form shadows implying volume; subsurface hints.
- **Motion and interaction:** blob morphs, breathing idles, growth animations.
- **Use for:** health/bio brands, wellness, environmental orgs, section dividers humanising tech products.
- **Avoid when:** precision/engineering credibility is core; blobs can read unserious in finance/ops.
- **Common mistakes:** lumpy Béziers (kinked curvature), blob-as-default decoration with no meaning, organic shapes fighting rectangular content grids.
- **Accessibility:** irregular containers complicate text wrapping: keep text in regular regions; contrast on gradient grounds verified.
- **Implementation:** SVG paths with smooth handles (mirror tangents), CSS border-radius tricks for simple blobs, morph via flubber-like interpolation or CSS paths.
- **Complements:** Organic Minimalism, Soft 3D, Gradient Mesh, Art Nouveau (ancestor).
- **Conflicts:** Brutalism, Swiss hardline, Pixel Art.
- **Transferable principles:** curvature continuity as craft metric; growth/branching as diagram metaphor for genuinely organic systems (org charts are not trees of steel). Transfers to divider systems and bio-data visualisation.
- **Brief example:** "Biotech brand: membrane-gradient hero blob (G2-smooth), humanist sans, cell-texture section dividers, text on calm panels."
- **QA:** curves G2-smooth (no kinks); blobs carry meaning or structure; text in regular containers; gradient contrast verified.

## Maximalist Editorial

- **Also known as:** expressive editorial, anti-minimal publication design.
- **Period and origins:** lineage from Twen and 1990s Ray Gun through 2020s expressive web editorial (interpretation); density with craft, distinct from chaotic Maximalism.
- **Philosophy:** abundance under discipline: a real grid and type system pushed to loud density, energy without losing the read.
- **Visual characteristics:** oversized headlines colliding with images, mixed type families, dense spreads, marginalia, stickers/stamps, saturated accents.
- **Geometry and composition:** strong grid deliberately violated at focal moments; the violation IS the hierarchy.
- **Colour:** bold editorial accents on functional grounds; section coding loud.
- **Typography:** 2-3 families in open conflict but fixed roles; extreme scale contrast; text columns stay sacred (readable).
- **Materials and finish:** print artefacts, highlighter strokes, tape and annotation layers.
- **Lighting and depth:** flat with collage-depth moments.
- **Motion and interaction:** scroll-triggered collisions, marquee strips; body text never moves.
- **Use for:** culture magazines, campaign microsites, fashion editorial, youth-facing reports.
- **Avoid when:** scanning efficiency or conservative trust is required.
- **Common mistakes:** violating the grid everywhere (then there is no grid), body text sacrificed to expression, density without pacing (no quiet spreads).
- **Accessibility:** reading order must survive the chaos (DOM/semantic discipline); body contrast and size protected.
- **Implementation:** needs a stricter underlying system than minimal design, not looser; tokens for the "violence" (rotation angles, overlap offsets).
- **Complements:** Maximalism, Editorial, Typography-Driven, Collage.
- **Conflicts:** Minimalism, Corporate Swiss, Neumorphism.
- **Transferable principles:** rule-break budgeting (count and place violations); loud/quiet pacing. Transfers to launch pages and annual reports wanting energy with control.
- **Brief example:** "Music-magazine feature: 12-col grid, headline overlapping hero at 8°, two quiet text spreads per loud opener, highlighter annotation layer."
- **QA:** grid exists and violations counted/placed; body text untouched by effects; pacing alternates; semantics/reading order intact.

## Neo-Brutalism

- **Also known as:** neubrutalism, neo-brutalist UI.
- **Period and origins:** web/UI trend c. 2020 onward (interpretation; popularised via design-tool communities and startup sites); softened, commercial descendant of web brutalism.
- **Philosophy:** honest blocks with a wink: flat raw surfaces, hard borders and unapologetic structure, but friendly colour and playfulness replace brutalism's hostility.
- **Visual characteristics:** thick black borders, hard offset shadows (no blur), flat saturated fills, visible structure, chunky components, slight rotations.
- **Geometry and composition:** card-block construction, exaggerated padding, deliberate slight misalignments as charm.
- **Colour:** cream/white grounds, saturated primaries and candy brights, always with black structure.
- **Typography:** bold grotesques, mono accents, oversized weights; underlines thick.
- **Materials and finish:** none: flat fills and hard edges are the material.
- **Lighting and depth:** faux depth via solid offset shadows (x/y offset, zero blur).
- **Motion and interaction:** snappy press-down (shadow collapses), hover lifts; toy-mechanical feel.
- **Use for:** dev tools, indie SaaS, portfolios, Gen-Z products, hackathon/ community brands.
- **Avoid when:** premium gravitas or dense enterprise data; trend saturation risk (dated note: heavily used 2021-2024).
- **Common mistakes:** borders inconsistent widths, soft shadows sneaking in (breaks the language), black-on-saturated text failing AA, quirk without system.
- **Accessibility:** naturally high contrast if enforced; focus states fit the language (thick outlines); check saturated fills under black text.
- **Implementation:** trivially cheap: border/box-shadow tokens; SVG-friendly; press states = transform + shadow swap.
- **Complements:** Brutalism, Flat, Pixel accents, Typography-Driven.
- **Conflicts:** Luxury Editorial, Glassmorphism, Liquid Glass, Organic Minimalism.
- **Transferable principles:** one shadow grammar used totally; charm through systematic quirk (tokenised rotation/offset). Transfers to sticker systems and playful component kits.
- **Brief example:** "API-tool site: cream ground, 3px black borders, 6px offset shadows, lime/violet fills, mono code blocks, press-collapse buttons."
- **QA:** border width single token; shadows hard (zero blur) everywhere; text/fill pairs AA; quirks tokenised not random.

## Corporate Swiss

- **Also known as:** enterprise modernism, Swiss-derived corporate design.
- **Period and origins:** International Style's corporate adoption (1960s-70s identity programmes: Rand, Unimark lineage, documented) through today's enterprise design systems.
- **Philosophy:** Swiss clarity industrialised: neutrality, consistency and scale-safety for organisations where design must work in a thousand hands.
- **Visual characteristics:** restrained grotesques, systematic grids, generous white, limited accent palette, structured iconography, photography over illustration.
- **Geometry and composition:** token-driven spacing scales, 8pt-grid discipline, predictable page architectures.
- **Colour:** neutral core + one brand hue + semantic set (success/warn/error); accessibility-grade pairs predefined.
- **Typography:** one workhorse family with large range (text to display), tabular numerals for data, no display theatrics.
- **Materials and finish:** flat, clean; depth only as elevation tokens.
- **Lighting and depth:** standardised shadow levels (component elevation scale).
- **Motion and interaction:** 150-300ms standard easing set; motion as feedback only.
- **Use for:** enterprise SaaS, banks, B2B platforms, design systems, documentation.
- **Avoid when:** differentiation is the goal (its virtue is neutrality: brands drown in it without a signature element).
- **Common mistakes:** sameness (indistinguishable from every other enterprise product), grey-on-grey hierarchy, system worship blocking needed exceptions, accent hue overused until meaningless.
- **Accessibility:** typically strongest style here: bake WCAG pairs into tokens; focus/keyboard complete.
- **Implementation:** design-token architecture is the style; component library governance; theming contracts.
- **Complements:** Swiss, Data-Driven, Minimalism, Aerospace Instrumentation (ops screens).
- **Conflicts:** Memphis, Grunge, Bohemian, Y2K.
- **Transferable principles:** token architecture and semantic colour discipline transfer to every product this skill designs; "one signature element" rule rescues neutrality from anonymity.
- **Brief example:** "B2B security platform: Inter-class family, 8pt grid, navy brand hue + semantic set, one signature element (data-viz accent style) for identity."
- **QA:** tokens cover colour/space/type/elevation; WCAG pairs enforced in tokens; one signature element named; semantic colours never decorative.

## Scientific / Technical Illustration

- **Also known as:** technical drawing, scientific visualisation (illustration strand).
- **Period and origins:** anatomical and botanical plates (Vesalius 1543, Audubon, documented), engineering drafting conventions (ISO/ANSI standards, documented), cutaway/exploded-view tradition (mid-20th century industrial illustration).
- **Philosophy:** accuracy first, beauty through clarity: every line answers a question about structure, scale or function; nothing invented.
- **Visual characteristics:** precise linework, labelled parts, leader lines, exploded views, cutaways, ghosted housings, scale indicators, stipple/hatch shading.
- **Geometry and composition:** orthographic or axonometric projections; alignment to datum; consistent line-weight hierarchy (object > hidden > dimension lines).
- **Colour:** restrained functional coding; monochrome tradition with selective colour for systems (hydraulic red, electrical blue conventions, documented practice varies by field).
- **Typography:** neutral sans labels, consistent sizes, horizontal orientation, callout numbering systems.
- **Materials and finish:** paper-plate cleanliness; rendering only where it informs.
- **Lighting and depth:** conventionalised (stipple density, hatching), not atmospheric.
- **Motion and interaction:** exploded-view assembly animations; layer toggles.
- **Use for:** manuals, patents, product pages, education, security architecture diagrams.
- **Avoid when:** emotional branding; accuracy unknowable (never fake precision: a diagram implies measurement).
- **Common mistakes:** decorative gradients on technical drawings, inconsistent line weights, labels overlapping geometry, invented internal details presented as fact.
- **Accessibility:** label text sizes enforced; figure + caption + data-table alternatives; colour coding doubled with patterns.
- **Implementation:** SVG-native craft; line-weight tokens (e.g. 2/1.25/0.75px hierarchy); leader-line rules (no crossings, one bend max as convention).
- **Complements:** Data-Driven, Isometric 3D, Line Art, Aerospace Instrumentation.
- **Conflicts:** Surreal, Grunge, Clay.
- **Transferable principles:** line-weight hierarchy, leader/callout grammar and "drawn = claimed" honesty transfer to every diagram and attack-surface SVG this skill makes.
- **Brief example:** "Zero-trust architecture plate: axonometric network, 3-weight linework, numbered callouts with legend, one accent coding trust zones."
- **QA:** projection consistent; 3-tier line weights; no invented detail; labels horizontal, non-overlapping, legible at delivery size.

## Aerospace Instrumentation

- **Also known as:** cockpit/avionics aesthetic; mission-control style.
- **Period and origins:** instrument-panel standardisation through the 20th century ("basic T" arrangement, documented aviation human-factors history), glass cockpits (1980s onward), mission control rooms; as a borrowed digital style, ongoing.
- **Philosophy:** legibility under stress: information prioritised by consequence, states unambiguous, nothing decorative competes with a warning. See `../aerospace-and-instrumentation.md` for the engineering substance; this entry is the visual language.
- **Visual characteristics:** dark neutral grounds, high-contrast readouts, bezel/zone grouping, alarm colour hierarchy (red/amber/green conventions, documented in avionics standards), tape gauges, tabular numerics.
- **Geometry and composition:** functional zoning (scan patterns), fixed positions for critical data, density managed by grouping not hiding.
- **Colour:** strict semantic reservation: red = warning, amber = caution, green = normal (aviation convention, documented); greys carry structure; no decorative use of alarm hues.
- **Typography:** instrument-grade legibility (open apertures, tabular lining numerals, generous x-height); size by criticality not aesthetics.
- **Materials and finish:** matte panel neutrality; glow only as state.
- **Lighting and depth:** flat with disciplined state-glow; night-mode dimming logic.
- **Motion and interaction:** state changes announce (blink conventions for unacknowledged alarms); values move smoothly (needle logic) so change is perceivable.
- **Use for:** SOC/NOC dashboards, monitoring, trading, medical ops, industrial HMIs; borrowed for credibility in tech branding (then it is costume: label it so).
- **Avoid when:** consumer friendliness is the goal; and never fake it on safety-critical claims: styling is not certification.
- **Common mistakes:** sci-fi greeble clutter, red used decoratively (destroys alarm meaning), everything blinking, density without zoning, dark theme failing contrast floors.
- **Accessibility:** contrast floors above AA for critical text; alarms multi-coded (colour + icon + position + sound where applicable); colour-blind-safe severity scales.
- **Implementation:** semantic colour tokens locked; fixed layout regions; latency of data shown (stale indicators): honesty features.
- **Complements:** Swiss, Data-Driven, Corporate Swiss, Monochromatic.
- **Conflicts:** Maximalism, Clay, Bohemian, Memphis.
- **Transferable principles:** consequence-ranked hierarchy, semantic colour reservation, fixed-position critical data, stale-data honesty. Transfers to every dashboard; this is the canonical principle-transfer source.
- **Brief example:** "SOC overview: zoned panel layout, grey structure, red reserved for active critical alerts only, tabular numerals, stale-feed indicators."
- **QA:** alarm hues appear ONLY as semantics; critical values fixed-position; AA+ contrast; every state (normal/caution/warning/stale/unknown) visually distinct.

## Industrial Product Design

- **Also known as:** product-design aesthetic; Rams-lineage functionalism (one strand).
- **Period and origins:** industrial design profession from early 20th century (Behrens at AEG, documented); Braun/Rams functionalism (1950s-80s, "ten principles" documented); Apple's hardware language as contemporary heir (interpretation widely argued).
- **Philosophy:** the object as servant: usefulness, honesty, longevity; as little design as possible, but every detail resolved. See `../industrial-design.md` for discipline depth.
- **Visual characteristics:** when borrowed as 2D style: product-photo cleanliness, functional colour coding, honest materials, precise radii, control-panel logic, labelled affordances.
- **Geometry and composition:** radii families (consistent corner language), alignment to physical logic, grid from the object's structure.
- **Colour:** neutral bodies, one functional accent (the Braun orange dot logic), material-true greys.
- **Typography:** engraved/printed label sensibility: small neutral sans, meticulous alignment.
- **Materials and finish:** honest material rendering (aluminium reads as aluminium), matte bias.
- **Lighting and depth:** studio product lighting, soft but revealing form.
- **Motion and interaction:** mechanical honesty: switches toggle, dials rotate with detents.
- **Use for:** hardware brands, product pages, design-system philosophies, premium tool UIs.
- **Avoid when:** expressive emotion is the brief; restraint reads cold if unmatched to audience.
- **Common mistakes:** minimal-looking but unresolved details (inconsistent radii betray it), fake materials, accent colour promoted to decoration.
- **Accessibility:** physical lineage helps (affordances labelled); keep control metaphors operable by keyboard.
- **Implementation:** radius/spacing tokens from a declared family; product renders with one light rig.
- **Complements:** Minimalism, Swiss, Corporate Swiss, Scandinavian.
- **Conflicts:** Maximalism, Grunge, Steampunk.
- **Transferable principles:** every-detail-resolved standard; functional accent discipline; honesty of affordance. Transfers to UI component craft and icon metaphors.
- **Brief example:** "Audio-hardware site: aluminium-true renders, one orange functional accent, label-grade sans, control metaphors that behave mechanically."
- **QA:** radii from one family; accent only on functional elements; materials honest; details resolved at zoom.

## Architectural Modernism

- **Also known as:** modernist architecture aesthetic; International Style (architecture).
- **Period and origins:** c. 1920s-1970s (Le Corbusier, Mies van der Rohe, Gropius; "less is more" attributed to Mies, documented usage); principles codified in the 1932 MoMA International Style exhibition (documented). See `../architecture.md` for spatial discipline.
- **Philosophy:** structure as truth: expose the frame, let function shape form, let light and proportion do the ornament's job.
- **Visual characteristics:** when borrowed graphically: exposed grid, module repetition, large glazing-like whitespace planes, concrete/steel/glass palette, plan and section drawings as motifs.
- **Geometry and composition:** structural grid governs; golden-section and Modulor-style proportion systems (Corbusier's Modulor, documented) as optional regulators; horizontal emphasis bands.
- **Colour:** material palette (concrete grey, steel, glass green-edge, white render) + primary accents (De Stijl/Corbusian polychromy strand).
- **Typography:** neutral grotesques, architectural lettering (stencil, DIN lineage), understated.
- **Materials and finish:** honest material textures used flat and unadorned.
- **Lighting and depth:** light as material: strong directional shadow play on flat compositions.
- **Motion and interaction:** reveal by plan/section/elevation logic; measured pacing.
- **Use for:** architecture firms, real estate, institutional identities, grid-driven editorial and web layouts.
- **Avoid when:** cosy or playful briefs; its authority can read austere.
- **Common mistakes:** grid as cage (no hierarchy events), concrete palette becoming lifeless grey soup, plan motifs as decoration with wrong conventions.
- **Accessibility:** grey palettes need contrast care; large plans need described alternatives.
- **Implementation:** CSS grid mirrors structural bays; drawing conventions (line weights, north arrows) used correctly or not at all.
- **Complements:** Swiss, Brutalism, Minimalism, Monochromatic.
- **Conflicts:** Bohemian, Victorian, Y2K.
- **Transferable principles:** module-and-bay rhythm, light-as-material, structure-revealed honesty. Transfers to layout systems, poster composition and whitespace architecture everywhere.
- **Brief example:** "Practice portfolio: bay-rhythm grid, one project per 'floor', long-shadow photography, DIN-class labels, concrete/white/one-primary."
- **QA:** grid rhythm audible (consistent bays); hierarchy events placed; drawing conventions correct; grey palette contrast-verified.

## Sustainable / Circular Design

- **Also known as:** eco-design, circular design.
- **Period and origins:** green design discourse from 1970s (Papanek's Design for the Real World 1971, documented), cradle-to-cradle framework (Braungart/McDonough 2002, documented), circular-economy design ongoing.
- **Philosophy:** longevity, repair and material honesty as both ethics and aesthetics; waste is a design failure; claims must be true (greenwash is the style's cardinal sin).
- **Visual characteristics:** unbleached/recycled material cues, mono-material simplicity, repair-friendly modularity shown proudly, ingredient/impact transparency blocks, restrained ink coverage.
- **Geometry and composition:** functional economy; modular units; visible fastenings (designed-to-disassemble as motif).
- **Colour:** unbleached naturals, soy/eco-ink earthtones, low-coverage layouts; avoid "green = eco" cliché as sole signal.
- **Typography:** efficient workhorse faces, high legibility at small sizes (ingredient panels), honest hierarchy for impact data.
- **Materials and finish:** recycled stocks, mono-materials, debossing over foils, visible fibre.
- **Lighting and depth:** natural, unglossy.
- **Motion and interaction:** lightweight pages as a stated performance/energy choice (dated practice note: carbon-aware web design discourse, 2020s).
- **Use for:** consumer goods with real credentials, repair brands, policy communication, packaging.
- **Avoid when:** claims cannot be substantiated; aesthetic without evidence is greenwashing and a legal risk in several jurisdictions (dated note, 2020s regulation trend: verify current rules).
- **Common mistakes:** leaf-and-kraft clichés replacing evidence, eco-look on wasteful structures, unreadable "natural" low-contrast inks.
- **Accessibility:** recycled-stock contrast drops: compensate ink choices; impact data needs plain-language summaries.
- **Implementation:** specify actual materials/processes with suppliers; digital: performance budgets as sustainability feature.
- **Complements:** Scandinavian, Organic Minimalism, Industrial Product Design, Data-Driven (impact evidence).
- **Conflicts:** Y2K gloss, Dark Luxury excess, Maximalism (material-heavy strands).
- **Transferable principles:** evidence-before-aesthetics; design-for-disassembly thinking (modularity transfers to design systems); efficiency as a visible virtue.
- **Brief example:** "Refill-brand packaging: unbleached board, one-ink print, deboss logo, impact panel with verified numbers, visible reuse instructions."
- **QA:** every claim substantiated; contrast compensated for stock; mono-material/ink economy real; no greenwash clichés standing in for data.

## Generative / Computational Design

- **Also known as:** procedural design, algorithmic art.
- **Period and origins:** pioneers 1960s (Vera Molnár, Georg Nees, Frieder Nake, documented); Processing (2001) and creative-code culture; parametric design in architecture; AI-generative wave 2020s (distinct strand).
- **Philosophy:** design the rules, not the artefact: systems produce families of form, with variation and emergence as the aesthetic.
- **Visual characteristics:** rule-based pattern families, flow fields, recursive structures, data-driven form, seeded variation across applications.
- **Geometry and composition:** parameter spaces; composition emerges from constraints; curation of outputs is the design act.
- **Colour:** algorithmic palettes (sampled, interpolated in perceptual space); seed-consistent across a system.
- **Typography:** usually stable type against generative fields; type itself generative only with legibility guards.
- **Materials and finish:** plotter lines, print grain, or pure digital crispness: declare the output medium.
- **Lighting and depth:** per system; often flat fields with density implying tone.
- **Motion and interaction:** living systems (slow evolution), input-reactive identities.
- **Use for:** brand identities needing infinite variation (events, media), data portraits, architecture facades, album/edition art.
- **Avoid when:** a single fixed mark is required by trademark/regulatory needs; when "generative" is a buzzword for random.
- **Common mistakes:** randomness without constraints (noise, not design), unrepeatable outputs (no seed discipline), demo-ware that cannot ship at brand scale, AI-strand provenance/rights ignored.
- **Accessibility:** generative backgrounds behind text need worst-case contrast guards baked into the rules; motion variants capped.
- **Implementation:** seeds + parameter docs = reproducibility; SVG output natural for plotter/vector systems; guardrail functions (contrast, density caps) are part of the design.
- **Complements:** Data-Driven, Swiss (as stable frame), Organic/Biomorphic, Futuristic.
- **Conflicts:** Handwritten (philosophically opposite provenance), Victorian.
- **Transferable principles:** rules-with-guardrails thinking transfers to design tokens and theming systems (a design system IS a generative system); curation as design act.
- **Brief example:** "Festival identity: flow-field mark generator, 5 locked parameters + seed per edition, contrast guard ≥4.5:1 behind type, plotter posters."
- **QA:** seeded and reproducible; guardrails enforce contrast/density; parameter ranges documented; curated exemplars approved.

## Spatial / Immersive Design

- **Also known as:** spatial computing design, XR/immersive design.
- **Period and origins:** VR/AR research decades old (documented HCI history); consumer wave landmarks: modern VR headsets 2016+, passthrough AR headsets and visionOS-era spatial UI 2023-2024 (documented releases; fast-moving: date-check current platform guidance).
- **Philosophy:** the interface inhabits the user's space: design with depth, scale, embodiment and comfort as first-class materials, not screen conventions floated in 3D.
- **Visual characteristics:** volumetric panels, depth-layered UI, glass materials, environmental anchoring, gaze/hand affordances, spatial audio cues.
- **Geometry and composition:** comfort zones (content ~1-3m, interpretation of platform ergonomics guidance), field-of-view budgets, world-anchored vs head-anchored decisions.
- **Colour:** environment-adaptive; translucent materials over unknown backdrops need adaptive contrast.
- **Typography:** sizes in angular terms (degrees of FOV) not pixels; generous weights; billboarding text toward the viewer.
- **Materials and finish:** platform materials (glass/vibrancy) for coherence; physical-light response.
- **Lighting and depth:** real depth: occlusion, shadow grounding objects, parallax honesty.
- **Motion and interaction:** comfort rules (no camera hijacking, stable horizons, vection limits, documented motion-sickness research); hands/gaze/controller affordances distinct.
- **Use for:** XR apps, spatial product demos, training sims, museum installations, future-facing concepts.
- **Avoid when:** a 2D screen serves the task better (most tasks); immersion is a cost users pay, spend it on genuinely spatial problems.
- **Common mistakes:** 2D screens pasted into space, text too small in angular size, UI pinned to the face (nausea and annoyance), ignoring comfort/safety research.
- **Accessibility:** seated/standing options, one-handed modes, subtitle/caption systems in space, photosensitivity and vection safeguards; vast open research area: state unknowns honestly.
- **Implementation:** platform HIGs are mandatory reading per target (fast-changing: verify current); prototypes in-headset, not on flat mockups.
- **Complements:** Liquid Glass, Futuristic, Soft 3D, Data-Driven (spatial data).
- **Conflicts:** print-native styles applied literally; dense flat dashboards ported 1:1.
- **Transferable principles:** angular-size thinking and comfort budgets transfer back to responsive design (viewing distance awareness); depth as hierarchy transfers to layered 2D UI.
- **Brief example:** "Network-ops spatial view: world-anchored topology volume at 2m, head-anchored alert strip, text ≥1° angular height, seated mode."
- **QA:** text angular size verified in-headset; comfort rules met (no horizon moves); anchoring choices justified; 2D fallback exists.
