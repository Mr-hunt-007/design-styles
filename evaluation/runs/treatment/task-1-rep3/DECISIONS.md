# Decisions — Aegis SOC triage dashboard

- Primary task: "which alert do I work next, and do I have context to act?" The queue dominates; each panel answers one question: under attack now (critical tile), what changed (24h chart), can I trust the picture (coverage), what is this asset (context panel).
- Rank by consequence: criticals hold a fixed top-left tile with red edge; queue is ranked severity-then-SLA-remaining; nothing decorative sits above severity.
- Three severity levels only, each with a defined response printed in the legend (Critical = act now/30min, High = this shift/4h, Moderate = batch/24h); fewer levels fights alarm fatigue.
- Severity is triple-coded (shape glyph + text label + colour): triangle/diamond/circle, so meaning survives greyscale and red-green CVD.
- Unknown is not zero: 2 stale clients show "—" counts with a dashed STALE badge, are excluded from totals, and the coverage tile says "stale ≠ clear"; counts never render a stale client as calm.
- One dataset drives everything (seeded PRNG, 131 alerts, 40 clients): tiles, rail counts, queue and detail agree by construction.
- Dark system: blue-grey surface ramp (#0B0F14→#1C2530), tabular mono numerals, 11px uppercase panel labels, 4/8px rhythm, dense 40px rows for expert scanning; expression confined to the chart and glyphs.
- Destructive action uses undo (suppress → toast + Undo), not confirm; Acknowledge/Escalate mutate state and re-render.
- Keyboard: every control focusable with a 2px visible ring; arrow keys walk the queue; prefers-reduced-motion honoured (no animation to begin with).

Verification actually performed (headless Chrome + Python):
- Contrast computed for 22 token pairs: all text ≥4.5:1 (ink 15.4, secondary 8.8, captions 5.4–5.8; severity inks 6.6/10.1/7.2 incl. on chips); graphics ≥3:1 after fixing two measured failures (moderate chart bar 2.57→4.18, zero-dot 2.87→4.13); hairline panel borders (1.4:1) are deliberately decorative — component boundaries use a ≥3:1 token.
- Rendered and inspected at 1440×900 and 1280×800; 390px and 768px probed via iframe harness: scrollWidth equals viewport (no horizontal overflow), layout stacks, secondary columns drop.
- Functional probe (scripted clicks): severity filter 131→3 rows, clear, row select updates detail, ack → "Ack'd", suppress 131→130 with undo restoring, client filter, stale cell renders "—". No console errors.
- Not verified: real screen readers, real devices/touch, light theme (dark-only by brief); at ≤860px the client rail and detail panel are cut, a stated trade-off for a desktop-first tool.
