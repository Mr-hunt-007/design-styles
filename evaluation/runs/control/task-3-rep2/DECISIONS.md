# Design decisions: architecture.svg

- Left-to-right request flow (Clients → Edge → Application → Data) on a 1480x860 canvas; monitoring as a full-width bottom plane since it spans all zones.
- Three tinted, color-coded zones (edge blue, app violet, data green, monitoring amber) with badge labels and one-line zone captions; node icons reuse the zone accent so membership reads at a glance.
- Edge is a vertical chain (CDN → WAF → LB) with labeled hops (HTTPS, cache miss, clean traffic); LB fans out to the three services via an elbow "bus" to avoid steep diagonals.
- Async path modeled explicitly: services publish to the Message Queue, Worker Pool consumes, workers write results to PostgreSQL and artifacts to Object Storage (w-1/w-2/w-n chips suggest autoscaling).
- Data connectors assigned semantically: Web Frontend → Redis (sessions/cache), API + Auth → PostgreSQL (SQL); data nodes ordered (Redis, Postgres, Storage) so no connector lines cross.
- Telemetry drawn as dashed gray arrows from each zone into Monitoring (Metrics/Logs/Traces/Alerting chips), with a legend distinguishing solid data paths from dashed telemetry.
- Self-contained: inline hand-drawn stroke icons, system font stack, no external refs or scripts; connector labels use a background-colored halo (paint-order) to stay legible over lines.
- Replica counts (x3/x4/x2) and sub-labels are illustrative placeholders, not from any real system; no vendor names beyond generic PostgreSQL/Redis.
- Omitted a CDN → Object Storage "static origin" link deliberately: routing it across all three zones added crossings that hurt readability more than the link informed.

## Verification

- Rendered the SVG twice with headless Chrome (file:// → PNG at 1480x860) and visually inspected the screenshots: checked component presence (all 10 + clients), label legibility, arrowheads, and overlap; fixed one arrow that clipped the PostgreSQL node corner.
- Did not test other renderers (Firefox, Inkscape, <img> embedding) or dark backgrounds; the SVG paints its own light background rect, so it should be safe when embedded.
