# architecture.svg — key design decisions

- Top-down request flow (clients → edge → application → data) as three full-width tinted zone bands;
  the vertical axis itself encodes trust/depth, so zone membership is readable without a key.
- Technical-drawing discipline per the skill's SVG reference: one node grammar (190×64 rounded rect,
  24px stroke icon, title + role sub-label), two stroke weights, round-number 1240×880 coordinate grid.
- Column alignment carries meaning: each service sits above the datastore it owns
  (Auth→Redis, API→Postgres, Media→Object Storage), yielding zero connector crossings.
- Async path is a distinct sub-row (queue → worker pool) inside the application zone; workers' writes
  curve back into the data zone ("job results", "artifacts") to show fan-in without clutter.
- Monitoring drawn outside all zones as an amber rail fed by dashed telemetry taps from each zone —
  dashed vs solid distinguishes telemetry from request flow (legend provided; never colour alone).
- Restrained per-zone hue coding (blue/violet/teal, tints + darkened label colours) paired with text
  labels; Clients drawn dashed as an external actor. Edge labels get a white halo for legibility.
- Icons are shared <symbol>/<use> defs with unique arch- prefixed IDs; accessibility via role="img",
  <title>, <desc>. Deliberate omission: CDN→object-storage origin pull, to keep one readable flow.

Verification performed: XML parsed (ElementTree), duplicate-ID and dangling-reference grep (clean),
rendered via headless Chrome at 1240×880 and 620×440 and visually inspected; two label/line collisions
found and fixed (zone descriptors vs connector verticals), then re-rendered and confirmed clean.
Not verified: dark-background embedding (the SVG carries its own opaque canvas), screen-reader output.
