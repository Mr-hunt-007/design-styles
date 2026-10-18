# Design decisions — Sentry Grid SOC dashboard

1. Triage-first layout: severity KPIs on top act as filters; the alert queue owns ~70% of width because the queue is the analyst's unit of work; right rail = context (asset detail, 24h trend, client load).
2. Severity is triple-encoded (color, pill text, left accent bar on KPIs) so it survives glance-reading and mild color-vision deficiency; monospace numerals for all metrics/IDs/IPs.
3. SLA breach is a first-class signal: dedicated KPI, red age + "SLA" marker per row, computed from per-severity targets (15m/1h/4h/24h) against unacknowledged alerts.
4. 40-client scale handled three ways: client column + dropdown filter, "clients affected / of 40" KPI, and a top-10 "client load" panel (sorted criticals-first, stacked severity bars, quiet-client count) that acts as a cross-filter on click.
5. Asset context panel answers "does this host matter?": crown-jewel badge, role/owner/site, exposure tags (internet-facing, edr:stale), alert narrative, mini-timeline, related-open-alerts count, and Acknowledge/Escalate/Contain actions that mutate state live.
6. Trend = hand-drawn SVG stacked hourly bars (no chart lib, zero dependencies) with a highlighted spike window whose annotation is computed from the same window as the data spike.
7. Dark theme built from one token set (near-black blue base, 4 severity hues, teal accent); default selection is the newest open critical so the context panel is never empty.
8. Data: 96 deterministic seeded alerts over 18 realistic detection types with MITRE technique tags, fictional client names only.

## Verification (honest)
- Rendered in headless Chrome at 1600x1000 and 1600x1500; screenshots inspected visually; no JS console errors. Two issues found and fixed this way: spike annotation/shading mismatched the data window, and clipped axis labels.
- Scripted DOM smoke test (headless): severity KPI filter (87 -> 6 rows, all critical), text search, client cross-filter, filter reset — all passed. Acknowledge/Escalate/Contain buttons were code-reviewed but not click-tested (default selection was already acknowledged). Not tested: real browsers other than Chrome, narrow viewports (<1100px uses min-width scroll by design).
