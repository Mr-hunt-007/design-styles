# DECISIONS — recycling.svg

## Narrative and layout
- The diagram reads as a serpentine: row 1 left-to-right (collection → pre-sort → screens), a vertical drop on the right, row 2 right-to-left (magnet/eddy → optical → baler), then down to a full-width "baled output" strip. This matches the brief's arc (kerbside bin to baled output) and fits six stages legibly in 960×600 without shrinking type below 10px.
- The two callouts sit in a band *between* the rows, directly under the stages they annotate, so their pointer tails are short and never cross a flow connector. Contamination points at stage 2 (pre-sort, where it is caught); glass points at stage 3 (screens, where it drops out).
- A closing output strip lists the six bale types as chips (with faint "strap" lines so they read as bales) plus a visually distinct dashed chip for glass cullet, reinforcing the glass callout's "never baled" point.

## Grouping, connectors, callouts
- Every stage is a `<g id="stage-n">` with its own `<title>`; connectors and callouts are also named groups, so the SVG is structured, accessible and editable.
- All six connectors are labelled with what *moves* along them ("tipped onto conveyors", "cleaner mix moves on", "containers roll onward", "what's left: plastics", "sorted by material", "ready to ship") rather than restating stage names. Labels are short two-line stacks sized to fit the 76px gaps; one shared arrowhead marker keeps the flow language consistent.
- Callouts use speech-bubble tails (filled triangle over the card edge) instead of long dashed leaders, because the targets are adjacent; each gets its own colour family (amber for the contamination warning, teal for glass) so they read as annotations, not stages.

## Visual system
- Single green family for the process (#2F7A52 accent, #3E6B57 connectors, #1B3A2D/#44584C text on white cards over #F3F6F2), with teal reserved for everything glass (falling shards in the screens icon, bottle icon, cullet chip) so the glass story is traceable across the sheet.
- Icons are hand-drawn stroke glyphs (bin, pre-sort belt with picker, disc screen with falling shards, horseshoe magnet with cans, optical camera with IR beam, strapped bale) at one stroke weight, no external symbols.
- Type is a generic Helvetica/Arial stack (no webfonts, keeping the file self-contained); hierarchy: 24px title, 14px stage titles with numbered badges, 11px body, 10.5px italic connector labels.
- One soft `feDropShadow` lifts cards off the background; everything else is flat 1.5px strokes.

## Copy
- Written for a general audience: "spinning discs", "air jets blast", "one bad bin can send a whole truckload to landfill". UK-flavoured to match "kerbside" (nappies, aluminium).
- No em dashes anywhere; colons/commas used instead, per standing copy rules.
- A small footnote flags that real facilities vary, since the sheet is a simplification.

## Self-containment
- No external images, fonts, scripts or hrefs; styles are an internal `<style>` block plus `<defs>` markers/filter. Root `<title>`/`<desc>` describe the diagram for assistive tech.

## Verification
- XML well-formedness checked by parsing the file; rendered at 960×600 in headless Chrome and visually inspected the bitmap for text overflow, connector/label collisions and callout tail alignment.
