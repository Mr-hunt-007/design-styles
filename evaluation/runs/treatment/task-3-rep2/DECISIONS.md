# architecture.svg - decisions

- Coordinate system: 1200x780 viewBox, round numbers; three horizontal zone bands (EDGE, APPLICATION, DATA) tracing the request path top to bottom, plus a full-height MONITORING panel on the right because observability spans every tier.
- One connector weight (1.6) with three line grammars, each with its own arrowhead marker and a legend: solid gray = request/data flow, dashed violet = async jobs, dotted amber = telemetry. Meaning is carried by line style plus label, never color alone.
- Orthogonal routing only; the load-balancer fan-out and the enqueue path are drawn as buses to avoid line spaghetti. Exactly two perpendicular crossings remain (cache line over the job bus and over the results channel); worker-to-data lines route through the 30px inter-zone channel.
- Nodes are white cards (rx 8) with a fixed anatomy: 20px accent-stroke icon, 14.5px semibold title, 11px role sub-label. The service chip icon is one symbol reused three times. Each zone has a tinted fill, a tinted card stroke, and one accent hue (blue/violet/green/amber) used for its icons and zone label.
- Connector labels get a background-colored halo (paint-order stroke) so they stay legible where they sit near lines.
- Worker pool drawn as a container with three chips to show it is a scaled set, not a single box; narrative edges chosen for legibility (API->Postgres, Auth->Redis, workers->Postgres/object storage) rather than every realistic link.
- Accessibility: role="img" with title/desc; text kept as editable text on a system font stack.
- Verified: XML parsed programmatically; ids unique and all url()/href references resolve (grep); rendered via headless Chrome at 1200px and at 600px on a dark page (the file carries its own background) and both rasters visually inspected - no clipping, no overlaps found after two fixes (removed a duplicated Monitoring title; darkened the MONITORING label).
- Contrast measured, not assumed: every text pair now 4.80:1 or better (two labels darkened after measuring 3.35:1 and 4.08:1); lines 3.35-5.66:1 against the 3:1 graphics bar. Not verified: non-Chrome renderers and print output.
