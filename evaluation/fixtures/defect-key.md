# Sealed answer key: defective-status-board.svg (planted defects)

1. Duplicate id `hdr` (two linearGradients share it; second silently ignored or wins depending on renderer).
2. Dangling reference `url(#missing-grad)` on the uptime card group (card renders unfilled/black depending on renderer).
3. Off-canvas element: rect at x=668 outside viewBox width 640.
4. Text clipping/overflow: header title (20px, starts x=20) wider than 640 canvas; incident card at 332 with ~260px-wide text okay, but card-2 label "Dashboard web application front-end service" (13px from x=276) overflows its 180-wide card ending at 408.
5. Misaligned geometry: middle status card y=87 vs 84; its dot cy=115 vs 112; its label y=120 vs 117; stroke-width 2.5 vs 1 inconsistency.
6. Low contrast: incident text #c8cdd2 on #ffffff (approx 1.6:1), far below any threshold.
7. Meaning by colour alone: status dots green/red/yellow with no shape/label distinction; legend has colours but no text labels next to swatches.
8. No accessibility markup: no title/desc/role on root.
9. Empty/unused defs: `<g id="unused-stub">` plus the duplicate gradient; empty nested `<g><g>` around status cards.
10. Fixed width/height on root alongside viewBox (blocks responsive scaling; minor, counts as improvement not defect if flagged as such).

Scoring: recall = confirmed planted defects found (1-9 core; 10 counts either way). False positives noted but not penalised unless factually wrong.
