# Decisions — architecture.svg

- Layout: request path reads top-to-bottom through three horizontal zone bands (edge → application → data),
  with clients above and monitoring as a side panel so telemetry reads as orthogonal to the request flow.
- Coordinate system: viewBox 0 0 1240 920; nodes sit on three shared column centers (285 / 525 / 765) so
  verticals align across zones; all connectors are orthogonal with 8px rounded elbows and zero crossings.
- One card geometry (180x64, rx 10, white on #F7F9FC ground) defined once in <defs> and reused via <use>
  for all 11 components; the accent icon tile is tinted through currentColor so one definition serves all zones.
- Icons: 12 symbols on a 24-unit grid, single 1.8-unit stroke, round caps/joins — one visual weight family.
- Color roles: slate for flow lines/arrowheads, blue/violet/teal zone accents at low-opacity fills with
  stronger strokes, amber reserved for telemetry; dashed stroke (not color alone) distinguishes telemetry,
  and a legend states both line meanings.
- Typography: 24px title, 13.5px/600 node names, 11px muted roles, 10.5px edge labels with a ground-colored
  halo (paint-order) so labels stay legible where they sit on zone tints or cross the gutters.
- Accessibility: role="img" with <title>/<desc>; label contrast measured, DATA and MONITORING captions
  darkened to #0F766E / #B45309 after computing ~3.5:1 and ~3.0:1 for the brighter accents (now ≥4.7:1);
  muted slate text measures ~4.5:1.
- Verified: XML parse, no duplicate IDs, all href/url(#) references resolve; rendered via headless Chrome at
  1240px on white and 620px on a dark page, both inspected (one label-collision defect found and fixed).
- Not verified: screen-reader behavior, print output, and non-Chrome renderers.
