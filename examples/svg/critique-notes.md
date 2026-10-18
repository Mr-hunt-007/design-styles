# SVG critique and correction: worked example

`critique-before.svg` is a deliberately flawed pipeline-status graphic. `critique-after.svg` is the corrected version. This is the model for the SVG audit workflow (`../../workflows/svg-creation.md`, step "critique"): findings ordered by consequence, each tied to observable evidence, confirmed defects separated from improvements.

## Confirmed defects (before)

1. **Off-canvas element.** `<rect x="430" ...>` lies entirely outside `viewBox 0 0 400 200`: dead weight that will surprise anyone editing the file. Evidence: 430 > 400. Fix: removed.
2. **Meaning by colour alone.** The three status circles differ only in fill (green/red/orange): invisible to colour-blind users and meaningless in forced-colours mode. Fix: each state gets a distinct glyph (check, cross, exclamation) plus a text label; colours darkened to hold 3:1+ contrast against white.
3. **No accessible name.** No `<title>`, `<desc>` or `role`. A screen reader announces nothing useful. Fix: `role="img"` with title and desc.
4. **Misaligned geometry.** Node y-positions are 30, 28, 31 and the connectors slope (52→50, 50→53): reads as sloppiness at any size. Fix: one baseline (y=30), level connectors.
5. **Duplicate definitions.** Three identical gradients `g1 g2 g3`. Fix: one gradient, referenced three times.
6. **Inconsistent stroke weights.** Connectors at 1px and 3px with no semantic difference. Fix: one 2px weight, with arrowheads to show direction (the diagram's actual point).
7. **Low-contrast label.** `#999` 11px text on white is below any reasonable text-contrast threshold. Fix: `#555e6b` at 12px.
8. **Empty nesting.** `<g><g><g>` adds depth without meaning. Fix: one semantic group per layer.

## Improvements (not defects)

- Fixed `width`/`height` on the root blocks responsive scaling; removed so `viewBox` governs.
- Node labels were missing entirely; the graphic said nothing without them.

## Verification

Both files were XML-validated and rendered via headless Chrome; the after version was additionally inspected at 50% size and on a dark backdrop. Node fills and status icons hold on dark; the dark-ink status labels and footer caption are tuned for light backgrounds, which is noted in-source (a dark embedding needs a light-ink variant).
