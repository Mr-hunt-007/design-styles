# Decisions — task-3-rep3 (architecture.svg)

- Layout: top-to-bottom request flow across three horizontal zone bands (EDGE / APPLICATION / DATA),
  matching how traffic actually moves; monitoring is a cross-cutting right-side panel fed by dashed
  telemetry arrows from each zone, so it reads as observability rather than a request hop.
- Flow: Users -> CDN -> WAF -> LB (labeled edges), LB fans out orthogonally to the 3 services;
  services -> queue -> worker pool for async work; services + workers reach the data tier via a
  shared "reads/writes" bus with junction dots, which keeps 5-to-3 data access legible instead of
  drawing 15 crossing lines. One representative "jobs" arrow stands in for all services publishing.
- Zones are tinted rounded containers (blue/violet/green/orange) with letterspaced labels; node
  borders and hand-drawn stroke icons (globe, shield, lock, cylinder, bucket, pulse...) inherit the
  zone hue so membership is readable even in grayscale shape terms.
- Self-contained: system font stack, no external refs, inline markers/filters; explicit width/height
  plus viewBox; solid #f8fafc background so it renders on any viewer background.
- Worker pool drawn as stacked cards to signal N replicas; legend explains solid vs dashed vs
  junction-dot conventions.
- Verification: rendered twice via headless Chrome at 1500x940 and visually inspected the PNGs;
  fixed two label collisions found in the first render (APPLICATION subtitle, DATA subtitle vs SQL
  riser). Checked in Chrome only; no other renderers tested, and not checked at small sizes.
