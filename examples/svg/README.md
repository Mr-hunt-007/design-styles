# Verified SVG examples

Five example sets demonstrating the standards in `../../references/svg-and-vector-graphics.md`. All were built with the verification loop in `../../workflows/svg-creation.md`.

| File | Demonstrates |
|---|---|
| `illustration-lighthouse.svg` | Clean flat vector illustration: limited palette, focal hierarchy, layered composition, reusable gradient, title/desc accessibility. |
| `diagram-order-journey.svg` | General-audience technical diagram (an online order's journey) with connectors, arrow markers, `<symbol>`/`<use>` node reuse, grid pattern, zone layering, line-weight conventions, callouts encoded by colour + shape + label, legend and technical-manual title block. Neutral example data (Examplo Ltd). |
| `icon-shield-scan.svg` | 24px-grid interface icon: 2px stroke discipline, round caps, `currentColor` theme adaptation, optical centring. |
| `composition-artdeco-sunburst.svg` | Distinctive style study (Art Deco): one ray defined, placed by rotation; symmetric ziggurat skyline; clipped frame; restrained two-colour palette. |
| `critique-before.svg` / `critique-after.svg` / `critique-notes.md` | Full audit-and-correct workflow: 8 confirmed defects, fixes, and the findings write-up. |

## Verification record (2026-10-18)

- **XML validity:** all six SVGs parsed clean with Python `xml.etree` (run via `../../tests/validate_skill.py` and directly).
- **Internal references:** unique IDs and resolving `url(#)`/`href` references confirmed by `../../tests/validate_skill.py`.
- **Rendering:** all six rendered via headless Chrome screenshots and visually inspected. Defects found and fixed in the loop: finding-label overflow in the diagram (boxes widened), asymmetric skyline notch cutting the sun in the Art Deco piece (profile made symmetric). Both re-rendered clean.
- **Size/theme checks:** icon inspected at 24/48/96px on light and dark (passes both via `currentColor`); critique-after inspected at 100% and 50% and on a dark backdrop (icons hold; dark-ink labels are light-background assets, noted in-source).
- **Unverified:** rendering in Firefox/Safari; print output; screen-reader announcement (markup follows the documented pattern but was not tested with assistive technology).
