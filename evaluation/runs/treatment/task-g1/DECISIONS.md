# DECISIONS — Harper Home Energy (task-g1)

Direction: domestic instrument clarity (aerospace principle transfer: one question per panel, rank by
consequence, glance legibility), warmed for a home context; rejected cockpit styling and glassmorphism
(noise and contrast conflicts for a family glancing at a kitchen phone).

- One question per card, written under each title; the single actionable alert sits first (consequence rank).
- Every number derives in JS from one inline DATA object, so tiles, bars, chart, costs and appliance
  shares reconcile by construction (incl. "Everything else" = today's total minus listed appliances).
- Solar = amber, grid = blue everywhere, but meaning never rides on colour alone: direct labels,
  legends, and a surface-coloured seam between stacked segments (adjacent fills alone are ~1.5:1).
- Tokens on :root; dark via prefers-color-scheme (data-theme override + toggle). All text pairs
  measured >=4.5:1 and chart fills >=3:1 vs surface in both themes (computed, not eyeballed).
- Trend SVG is drawn at the container's real pixel width (redrawn on resize) so labels stay ~11px
  on phones instead of scaling down with a fixed viewBox.
- Cost compares month-to-date vs the same point last month (labelled), not a misleading full-month bill.
- Verified: light+dark renders inspected; 400px via iframe harness with scrollWidth probe (400/400,
  no overflow); contrast computed; sr-only data table backs the chart. Unverified: real screen reader,
  physical devices.
