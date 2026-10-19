# DECISIONS — Greenfield Saturday Farmers Market, Season Opening poster

## Canvas and format
- Single self-contained SVG: `width="297mm" height="420mm"` (A3 portrait) with `viewBox="0 0 1123 1588"` (A3 at 96 dpi), so 1 user unit is approximately 0.2645 mm. All sizes below are chosen in this unit space and checked against physical size.
- No external references of any kind: no `@font-face`, no linked images, no CSS imports, no filters. Everything is paths, basic shapes and text with presentation attributes, so any rasteriser (resvg, librsvg, Chrome, ImageMagick) produces the same poster.

## Rasterisation safety (no-webfont machine)
- Font stack is `Arial, Helvetica, sans-serif` only. Arial/Helvetica are present on macOS/Windows; Linux rasterisers substitute metrically compatible Liberation Sans or DejaVu Sans via the generic `sans-serif` fallback.
- Every text element is `text-anchor="middle"` on the page centreline (x=561.5), so a substitute font with slightly different metrics re-centres itself instead of drifting off a margin.
- Width budgets assume a wide fallback (DejaVu Bold, approximately 0.72 em per cap): the widest line ("FARMERS" at 168 px) measures about 880 units against 979 units of usable width; the ribbon text measures about 570 against a 680 ribbon. Nothing is fitted tighter than roughly 85%, so substitution cannot overflow a container.
- No `dominant-baseline`/`alignment-baseline` (inconsistent across rasterisers); every baseline is positioned manually. No `textLength` squeezing. Icons are pure stroked paths, so they are font-independent.
- Only universally available glyphs: ASCII plus en dash (8 AM – 1 PM) and middot separators. No em dashes anywhere.

## Hierarchy (legibility from 2 m)
Rule of thumb: comfortable reading at distance needs cap height of roughly 2 mm per metre of viewing distance, i.e. about 4-5 mm caps (15-19 px here) as the floor for 2 m. Everything on the poster clears it:
1. **FARMERS / MARKET** — 168 px bold (caps ~32 mm): readable across a street, not just 2 m.
2. **SEASON OPENING** — 54 px white on a rust ribbon; the ribbon shape makes it the announcement even at thumbnail size.
3. **When/where block** — date 64 px green, time 46 px rust, place 36 px ink: the three facts in strict size order, each one line, each centred.
4. **Six stall cards** — 29 px bold labels (caps ~5.5 mm, above the 2 m floor); icons carry recognition before the words resolve.
5. Smallest type on the poster is 26-27 px (~5 mm caps): the "every Saturday through 30 October" line and the footer, both still legible at 2 m, both secondary by design.

## Content decisions
- Full market name is composed as eyebrow ("GREENFIELD SATURDAY") + hero ("FARMERS MARKET") so the hero words stay enormous while the complete name still reads top-down.
- Dates verified against the real calendar: 1 May 2027 and 30 October 2027 are both Saturdays, so "Saturday 1 May 2027 ... then every Saturday through 30 October" is internally consistent.
- Place is concrete (Greenfield Town Square, High Street — fictional, matching the fictional brief). Time 8 am - 1 pm.
- Six stall categories, exactly: Fresh Produce, Baked Goods, Dairy & Eggs, Flowers & Plants, Honey & Preserves, Crafts & Makers. Each label is split into two short lines so all six cards share one typographic rhythm and no line approaches the card edge.

## Visual system
- Palette: cream paper #F6F0E2, market-awning deep green #1C5436, rust #C44A26 (accent/CTA), harvest gold #E0A73A, ink #2B2B23, muted sage #6B7560. Green on cream is ~9:1 contrast; rust on cream ~5.6:1; cream on green/rust well above 4.5:1.
- Scalloped awning band across the top (alternating green/gold semicircle paths) and a solid green footer band with a gold rule: the two bands frame the sheet and say "market stall" without any imagery download.
- The ribbon is a flat rect with notched darker-rust tails (two polygons) — a classic poster device that isolates "SEASON OPENING" from the hero without competing in size.
- Stall icons are 5 px stroked line icons (carrot, loaf, milk bottle + egg, tulip, honey jar with comb hexagon, thrown vase) on pale sage circles: one weight, one colour, round caps, drawn in a shared 100-unit box so the set reads as a family.
- Grid: 72-unit side margins; three 300-unit cards per row with equal 39.5-unit gutters; middle column sits exactly on the page centreline.

## Verification performed
- Rasterised the SVG with headless Chrome at exactly 1123x1588 and visually inspected the full-page PNG: no clipped or overflowing text, ribbon/tails aligned, icons legible at small size, scallops hang downward as intended, footer text clear of band edges.
