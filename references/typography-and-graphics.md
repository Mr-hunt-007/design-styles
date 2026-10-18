# Typography and Graphic Design

Typography is the craft of making language visible with precision and intent. Most visual communication is mostly type; whoever controls hierarchy, spacing and alignment controls the message.

## Typeface classification

Working taxonomy (enough to reason with, not a full history):

- **Humanist serifs** (calligraphic roots, warm, long-form reading).
- **Transitional and rational serifs** (higher contrast, more formal authority).
- **Didone / high-contrast serifs** (fashion, luxury, display; fragile at small sizes).
- **Slab serifs** (sturdy, mechanical, assertive).
- **Grotesque / neo-grotesque sans** (neutral, systematic, the Swiss default).
- **Humanist sans** (open apertures, friendly, highly legible at small sizes and on screens).
- **Geometric sans** (constructed, modern, can be cold; watch ambiguous letterforms).
- **Monospace** (code, data, technical voice).
- **Scripts and display faces** (single-purpose voices; never for running text).

Choose by job first (sizes, media, languages, data vs prose), voice second. Two families are usually enough; one family with a strong range of weights is often better.

## Letterform anatomy

Know the vocabulary because it names what you are judging: baseline, x-height, cap height, ascender, descender, counter, aperture, bowl, stem, terminal, stroke contrast. The practical levers:

- **x-height**: larger reads bigger and sturdier at the same point size; affects pairing and sizing.
- **Aperture**: open apertures survive small sizes and poor rendering.
- **Counters**: tight counters clog in small sizes, dark modes and low-quality print.

## Kerning, tracking and leading

- **Kerning** (pairs): display sizes expose bad pairs; headlines above ~24 px deserve a manual pass (AV, To, Wa, r., quotation marks).
- **Tracking** (overall): slightly negative for large display, neutral for body, positive for small caps and all-caps labels. Never track lowercase body text wide.
- **Leading** (line spacing): body text roughly 1.4 to 1.6 times the size, tightening as size grows; display lines can approach 1.0 to 1.1. Longer measures need more leading.
- **Measure**: 45 to 75 characters per line for comfortable reading; outside that, change size, columns or layout.

## Optical alignment

Mechanical alignment is not visual alignment:

- Hang punctuation and bullets outside the text block so the text edge looks straight.
- Round shapes and pointed shapes must overshoot flat edges slightly to look aligned (the same overshoot type designers build into O and A).
- Icons beside text align to the text's optical centre (roughly x-height centre), not the bounding box.
- Centre by visual mass, not by geometry: a triangle centred geometrically looks off-centre.

## Typographic hierarchy

- Build hierarchy from few sizes with clear jumps (a modular scale) plus weight, case, colour and space. Six sizes are almost always enough.
- Space above a heading exceeds space below it: headings attach to what they introduce.
- One voice per level: do not express the same level two different ways on one page.
- Hierarchy test: strip the content to its skeleton; a reader should reconstruct the outline from appearance alone.

## Grid systems

- A grid is a decision-saving machine: columns, gutters, margins, and a baseline rhythm that vertical spacing snaps to.
- Choose column count from content variety: editorial work with mixed elements wants more columns (8 or 12) so elements can span varied widths; simple documents want fewer.
- The grid is felt through consistent alignment and consistent violation: break it deliberately for emphasis, never accidentally.
- Margins are part of the composition, not leftovers; generous margins are the cheapest upgrade in most layouts.

## Editorial pacing

- A publication is a journey with tempo: openers, dense spreads, breathers. Alternate density and rest; a relentless layout exhausts.
- Pull quotes, drop caps, section breaks and full-bleed images are pacing instruments, spent deliberately.
- Front-load orientation: readers decide in seconds whether to commit; the opening must state subject and promise structure.

## Print production vs digital rendering

- Print: CMYK vs spot colour, paper absorbency (dot gain), minimum type sizes for reversed-out text, bleed and safe margins, ink coverage limits. Thin hairlines and tight counters die on uncoated stock.
- Digital: hinting and rasterisation vary by platform; verify at real sizes on real screens. Variable fonts offer weight precision; font loading affects layout shift (see `ui-ux.md`).
- Reversed (light-on-dark) text blooms: use slightly lighter weights and looser tracking in dark themes.

## Language and script considerations

- Scripts differ in rhythm, joining behaviour, vertical metrics and justification rules; a Latin-centric layout imposed on Arabic, Devanagari or CJK text usually fails. Line length, line height and emphasis conventions (no italics in many scripts) must be rethought per script.
- Plan for expansion: translations run long; all-caps tracking, tight buttons and fixed-width labels break first.
- Hyphenation and justification are language-specific; ragged-right is the safe default for multilingual systems.

## Vector composition and SVG

Typography's disciplines apply directly to vector graphics, and vice versa (see `svg-and-vector-graphics.md`):

- **Type as shapes**: converting text to outlines freezes rendering (no font dependency) but loses editability and accessibility; keep live text where possible, outline only for final locked artwork, and always keep an editable source.
- **Optical corrections at small sizes**: like type designers, icon designers thicken strokes, open counters and simplify detail for small renditions; one drawing rarely survives from 16 px to 512 px. Design per size band or test ruthlessly.
- **Grid-locked vs optically adjusted**: start on the pixel/module grid for consistency, then make optical corrections (overshoots, visual centring, stroke-end adjustments) deliberately and consistently. A purely grid-locked icon set looks mechanical; a purely optical one looks lawless.
- **Stroke discipline**: a vector system picks a stroke-weight scale the way typography picks a type scale, and sticks to it.
- Letterform anatomy trains the eye for vector craft: counters become negative space, apertures become gap sizes, terminals become stroke endings.

## Quality checklist

1. Scale: are all sizes from the declared scale, with clear jumps between levels?
2. Measure and leading within comfortable ranges; headings attached to their content?
3. Kerning pass done on display headlines; tracking correct per case and size?
4. Optical alignment: punctuation hung, icons visually centred, edges visually straight?
5. Hierarchy skeleton test passes?
6. Reversed text, small text and low-contrast pairs checked in the real medium?
7. Longest realistic strings and at least one non-Latin script (when in scope) tested?

## Transferable principles

- The modular scale and baseline rhythm transfer to any system of sizes: icons, spacing, charts, architectural drawings.
- Optical over mechanical alignment is a universal craft rule for icons, logos, diagrams and UI components.
- Editorial pacing structures decks, reports, landing pages and onboarding flows.
- Grid discipline from Swiss typography is the backbone of dashboards and technical documents.
- "One voice per level" is a rule for any coding of meaning: chart colours, map symbols, alert severities.

## Domain-specific constraints that do NOT transfer

- Print production numbers (dot gain, ink limits, bleed) do not inform screen work beyond general caution with fine detail.
- Reading-typography ranges (measure, leading) do not govern display lockups, logos or kinetic type, which obey composition instead.
- Script-specific typographic rules must come from that script's tradition, not extrapolated from Latin habits.
