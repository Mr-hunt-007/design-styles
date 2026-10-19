# Decisions: Harper energy dashboard

- Built with the dataviz skill procedure: form first, color by job, palette validated, marks spec'd, hover layer, a11y pass, render check.
- Current usage is the one hero figure (48px, system sans, proportional figures); solar-now and month cost are plain stat tiles.
- Cost this month vs last is a stat-tile delta ("$148, ▼16% vs September"), not a two-bar chart: two numbers are not a chart.
- 7-day trend: single-series line + 10% area wash, slot-1 blue, endpoint direct-labeled, no legend (single series).
- Solar vs grid: stacked bars (part-to-whole per day); solar = slot-2 orange, grid = slot-1 blue, assigned in fixed palette order.
- Two-slot palette validated with scripts/validate_palette.js: all checks pass, light (ΔE_cvd 24.7) and dark (26.8) modes.
- Top appliances: single-hue horizontal HTML bars (identity is the row label, not color), values at bar tips.
- Alert uses the reserved status warning color as icon + left border only; text stays in ink tokens, and it carries one concrete action.
- Mark specs followed: 2px line, ≥8px markers with 2px surface ring, bars ≤24px with 4px rounded data-end, 2px surface gap in stacks, solid hairline grid.
- Hover layer: crosshair + snap tooltip on the line, whole-column hit targets with an all-series tooltip on stacks; same tooltips on keyboard focus.
- Every chart has a table-view twin (<details>); tabular-nums only in tables and axis ticks.
- Dark mode is selected, not flipped: dark-stepped series hexes and dark chrome under both prefers-color-scheme and a data-theme toggle (Auto/Light/Dark, persisted best-effort).
- 400px: KPI tiles and chart cards stack via auto-fit/one-column grids; SVGs re-render to container width (ResizeObserver) so type never shrinks with the viewport; x-labels thin out below 480px.
- Placeholder data is internally consistent: solar + grid sums to each day's total; appliance sum (115.3) is stated as 67% of the week's 172.8 kWh.
- Tooltip/legend/table text inserted via textContent only.
