# Design decisions — SOC triage dashboard

- Primary direction: Aerospace Instrumentation as principle transfer (consequence-ranked hierarchy, semantic colour reservation, fixed-position critical data, unknown-is-not-zero), supported by Corporate Swiss (token architecture, 8px rhythm, tabular numerals, controlled vocabulary). Rejected Cyberpunk/Futuristic (decorative alarm hues destroy severity semantics) and Dark Luxury (hostile to dense data).
- One question per panel: KPI strip = "how bad is this shift"; queue = "what do I triage next" (the single primary task, largest region, sorted severity-then-age); context panel = "what is this alert on"; trend = "what changed over 24h"; 40-cell estate grid = "which clients are hot".
- Alarm hues reserved strictly: red/amber/yellow appear only as severity/state; interactive affordances use a separate blue accent; green only for healthy feeds.
- Monochrome survival: severity = colour + shape (triangle/diamond/square/circle) + text label; statuses and estate cells carry text/counts; trend stack uses an opacity ramp so lightness orders severity in greyscale.
- Unknown is not zero: stale feeds (dashed), silent client (hatched, "no data ≠ no threat"), telemetry-coverage KPI, and a per-alert warning when the client's feed is degraded.
- Triage is operable: working filters (severity/status/client/search), row selection, Acknowledge/Escalate/Suppress with undo toast, j/k/a/e keyboard flow, visible focus, reduced-motion respected; unacked-critical pulse is the only animation.
- Dark theme engineered, not styled: elevated grey surfaces (no pure black), severity hues checked ≥4.5:1 on panels, 13px dense type with mono tabular numerals for values.
- All data is inline fictional placeholder (40 neutral org names, RFC5737/private IPs); zero external requests.

Verification performed: rendered in headless Chrome at 1600×1000, 1600×1400, and a true 390px viewport (via iframe harness after finding headless Chrome's 500px window floor faked an overflow); 18 scripted DOM assertions for selection, ack/escalate/suppress+undo, filters, keyboard and estate-cell filtering all pass; greyscale render inspected for severity survival; grep confirmed no external URLs.
Not verified: real screen-reader pass (semantics/ARIA written but untested), Safari/Firefox rendering, and contrast ratios were computed, not instrument-measured.
