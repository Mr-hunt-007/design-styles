# Design decisions — Aegis SOC Console

- Triage-first hierarchy: KPI strip (open, critical, MTTA, SLA breaches, clients-with-critical) -> 24h trend -> 40-client estate grid -> queue + sticky detail panel; queue is sorted severity-then-age, the analyst's actual working order.
- Dark theme on a validated dark surface set (#0d0d0d page, #1a1a19 panels, ink #f0efec/#c3c2b7/#898781) from the dataviz skill's reference palette; all text wears ink tokens, never severity color.
- Severity uses the fixed status palette (critical #d03b3b, high #ec835a, medium #fab219) plus blue #3987e5 for low (deliberately not green: "low" is not "good"); severity is never color-alone — every use pairs a text label (badges, legend, tooltip, client cells).
- Trend chart: single-axis stacked hourly bars (fixed stack order low->critical so position encodes severity), 2px surface gaps between segments, rounded top on the end segment, 4 hairline gridlines, legend, crosshair + per-severity tooltip. Hand-built SVG, no libraries.
- 40 clients rendered as a scannable grid sorted worst-severity-first, each cell = name, open count, worst severity (color tick + word); clicking filters the queue — the grid doubles as the cross-client navigation.
- Asset context lives in the detail panel (hostname/IP/OS/owner/criticality tier/exposure/tags) beside client context (industry, asset count, agent coverage, correlated alerts) so a triage decision needs no page change.
- Placeholder data is deterministic (seeded PRNG), fictional client names only, one file, zero network requests; vanilla JS state for severity chips, client filter, search, row selection, ack/investigate actions, live UTC clock.
- SLA framing: per-severity ack SLAs; breached new alerts flagged in the age column and detail panel.

## Verification (honest)
- Ran the dataviz palette validator: severity set passes CVD separation (worst adjacent dE 11.3) and 3:1 contrast on #1a1a19; the yellow/orange normal-vision pair measures 13.6 (floor 15). Tested 6 alternative warm steps — all worse — so kept the documented status palette and leaned on the mandated label pairing + fixed stack position as secondary encoding.
- Rendered in headless Chrome at 1440px and 500px (shot-desktop.png, shot-narrow.png): layout, chart geometry, 64 queue rows, 40 client cells and the detail panel verified by eye; DOM dump shows no JS errors. Interactions exercised headlessly via synthetic events (severity chips, client filter + clear, search, row click/Enter selection, acknowledge, chart hover tooltip) — all behaved as designed; not tested in a live interactive browser session. No light-mode variant was built (dark only, per brief).
