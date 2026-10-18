# Design decisions - architecture.svg

- Vertical tier flow (edge -> app -> data, top to bottom) mirrors the request path; users enter at left into the edge band.
- Three tinted zone containers with hue coding: blue = edge, violet = app, green = data; node icon chips reuse the zone hue so membership reads twice.
- Monitoring sits outside the zones (right column) since it is cross-cutting; amber dashed connectors tap each zone edge rather than individual nodes to avoid a spider web.
- Connector semantics carried by line style and a legend: solid grey = synchronous request path, grey dashed = async queue traffic, amber dashed = telemetry.
- Orthogonal elbow routing with reserved vertical lanes between row-2 boxes (x=700, 760 for API; 1100 for Auth) keeps data-tier connectors from passing through the queue/worker boxes; exactly one line crossing remains (workers->Postgres over API->Redis), which I judged acceptable.
- LB fan-out drawn as a shared stem splitting at y=330 with one label ("HTTP, least connections") instead of three.
- Every edge labelled with protocol or purpose (HTTPS, cache miss, filtered, REST/JSON, enqueue, consume, SQL, cache, sessions, results, artifacts); labels get a background-colored halo (paint-order) so they stay legible over lines.
- Hand-drawn 20px stroke icons (globe, shield, fan, braces, lock, cylinder, bolt, bucket, pulse) - no external assets; system font stack, drop-shadow via inline SVG filter; fully self-contained file.
- Realistic details without clutter: node subtitles (OWASP rules, DLQ, primary + replica, S3-compatible), zone captions (public ingress, private subnets, encrypted at rest), footer AZ note.
- Verification: rendered the SVG twice with headless Chrome at 1560x1000 and visually inspected the PNGs; first pass caught a "telemetry" label clipped under the Monitoring card (removed, legend covers it). Checked only this one rasterizer at one size; no other viewers, zoom levels, or accessibility checks were tested.
