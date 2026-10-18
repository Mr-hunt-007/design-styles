# Meridian landing: style decisions

**Styles combined: Corporate Swiss (primary) + Aerospace Instrumentation (supporting).** The catalogue
lists each as a complement of the other, and both share the same philosophy: clarity under consequence.

**How they cohere:** Corporate Swiss owns the page (white ground, 8pt token scale, one workhorse sans,
one brand blue, generous whitespace, predictable architecture). Aerospace Instrumentation is confined to
the product surfaces: four dark "instrument panels" (hero overview, discovery feed, ranked queue,
evidence card) with mono labels, tabular numerals, zone grouping, stale-feed honesty, and severity hues
(red/amber/green) reserved strictly for severity, never decoration. The panels are the Swiss system's
"one signature element", so the combination is a frame-and-instrument relationship, not a collision.
Rejected: Cyberpunk (catalogue: avoid for genuine security ops), Dark Luxury (conflicts with dense data).

**Verification performed:** rendered with headless Chrome at 1440px (full page, 4 iterations) and at a
true 390px viewport (via iframe harness, since headless Chrome clamps windows to 500px min); confirmed
scrollWidth == 390 with a JS overflow probe (only intentional internal scroll in the evidence block).
Fixed during iteration: inline spans overlapping the queue's grid columns, grid-item min-width overflow,
and the flipped feature putting its panel in the narrow 42fr column. Contrast pairs were checked by
computed estimate (all text at or above ~4.5:1 on both surfaces), not with an automated WCAG tool.
Screen-reader output, keyboard flow and real devices were not tested. No external network dependencies.
