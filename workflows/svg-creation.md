# Workflow: SVG Creation and Verification

Produce an SVG that is both structurally sound and visually intentional. Applies to icons, diagrams, illustrations, logos and data graphics.

**Inputs:** purpose, display context (sizes, backgrounds, medium), style direction.
**Outputs:** the SVG file, plus a verification report (what rendered, what was checked, what remains unverified).
**Load:** [../references/svg-and-vector-graphics.md](../references/svg-and-vector-graphics.md) (mandatory), [../references/accessibility-and-quality.md](../references/accessibility-and-quality.md) section 4.

## Steps

1. **Design intent first.** One sentence: what must this communicate, at what sizes, on what backgrounds? Confirm SVG is the right tool (not Canvas, raster or a chart library).

2. **Plan the coordinate system.** Choose a `viewBox` with round numbers matched to the artefact (24x24 icon grid, 1200x800 diagram). Define the grid, stroke weight scale, corner radii and palette roles before drawing. Decide what becomes a reusable `<defs>` symbol.

3. **Build.** Compose with the planned system: consistent stroke weights, optical alignment over mathematical where shapes demand it, unique IDs, semantic `<g>` grouping, `<use>` for repetition, no element outside the canvas. Keep source readable; no premature minification.

4. **Validate syntax programmatically.**
   ```bash
   python3 -I -c "import xml.etree.ElementTree as ET,sys; ET.parse(sys.argv[1]); print('valid XML')" file.svg
   ```
   Also grep for dangling `url(#...)` and duplicate `id=` values.

5. **Render.** Headless Chrome gives a faithful render:
   ```bash
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --screenshot=/path/out.png --window-size=1200,800 --default-background-color=FFFFFFFF file.svg
   ```
   Render once at target size and once at roughly half size; for icons, also at 2x. When background is unknown, render on light and dark (`--default-background-color`).

6. **Inspect the renders** with the Read tool (they are images): composition and focal point, spacing, accidental clipping, stroke legibility at the small size, contrast on each background, proportion errors, text overlap. For an icon family, additionally render all glyphs side by side at the target size and compare visual masses across the set: pointed and diagonal shapes must overshoot the grid until they match squares and circles optically (see cross-glyph equalisation in the SVG reference). A family is judged as a row, never one glyph at a time.

7. **Fix defects, re-render, re-inspect.** Loop until the small-size render is clean, not just the large one.

8. **Finish.** Add `<title>`/`<desc>` and `role="img"` (or `aria-hidden="true"` if decorative). Optimise only now if delivery needs it: collapse redundant groups, round coordinates sensibly, keep the readable version alongside if the source will be maintained.

9. **Report.** State which checks ran (parse, render sizes, backgrounds) and which did not. If no renderer was available, say "source inspected; visual rendering unverified", never "validated".

## Gate

Done only when: XML parses; renders were visually inspected at target and reduced size (or their impossibility documented); accessibility markup matches the SVG's role; the verification report distinguishes checked from unchecked. "The code looks right" does not pass this gate.
