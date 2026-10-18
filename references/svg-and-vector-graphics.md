# SVG and Vector Graphics

SVG is a first-class design and engineering medium in this skill, not an export format. Every SVG is a designed artefact with a visual system, and a piece of source code with structural quality requirements. Review both, always.

Related: `typography-and-graphics.md` (vector composition, type as shape), `cross-disciplinary-design.md` (technical-manual and architectural drawing principles), `accessibility-and-quality.md` (validation gates), `../workflows/svg-creation.md` (step-by-step procedure), `../examples/svg/` (verified examples).

## 1. When SVG is the right tool

Use SVG for: icons, logos, diagrams, flowcharts, maps, technical illustration, data graphics with modest element counts, decorative patterns, anything that must scale crisply or be styled by CSS.

Prefer something else when:

- Thousands of animated or frequently redrawn elements: Canvas or WebGL.
- Photographic or painterly continuous-tone imagery: raster.
- Live, interactive data with axes, tooltips and updates: a visualisation library (which may itself emit SVG).
- Plain rectangles, text and layout: HTML/CSS, which is cheaper and more accessible.

## 2. Document structure

- Root: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 W H">`. The namespace is required for standalone files; inline HTML5 SVG tolerates its absence but include it anyway for portability.
- `viewBox="minX minY width height"` defines the coordinate system. Prefer a clean, human-readable system (0 0 24 24 for icons, 0 0 1200 800 for diagrams) so coordinates stay legible.
- Responsive sizing: omit fixed `width`/`height` on the root (or set `width="100%"`) and let `viewBox` + CSS control size. For email or strict embeds, set explicit dimensions.
- `preserveAspectRatio` defaults to `xMidYMid meet`; change it only deliberately (e.g. `none` stretches, almost never wanted).
- Order is paint order: later elements draw on top. There is no z-index; restructure the document to layer.
- Structure the file like a drawing, not a dump: `<defs>` first, then background layer, then content groups in paint order, labels last. Group semantically (`<g id="connectors">`, `<g id="nodes">`) when it aids comprehension, never as empty nesting.

## 3. Geometry and drawing

- Primitives: `rect` (with `rx` for rounded corners), `circle`, `ellipse`, `line`, `polyline`, `polygon`. Use them when they express the shape; do not convert everything to `<path>`.
- `<path>` commands: M/m move, L/l line, H/V axis lines, C/c cubic Bezier, S smooth cubic, Q/q quadratic, T smooth quadratic, A/a elliptical arc, Z close. Uppercase absolute, lowercase relative.
- Beziers: place control points to keep curvature continuous (S/T reflect the previous control point). Jerky curves usually mean control points fighting the anchor spacing.
- Transforms: `translate`, `scale`, `rotate(a cx cy)`, `skewX/Y`, `matrix`. Transforms compound down the group tree; prefer drawing in final coordinates and reserve transforms for reuse, rotation of symmetric parts, and animation.
- Crisp 1px strokes on integer grids: position the line on the half-pixel (x=10.5) or use `shape-rendering="crispEdges"` sparingly. Icon strokes aligned to the pixel grid read sharper at small sizes.

## 4. Paint: fills, strokes, gradients, masks, filters

- `fill`, `stroke`, `stroke-width`, `stroke-linecap` (butt/round/square), `stroke-linejoin` (miter/round/bevel), `stroke-dasharray`, `stroke-dashoffset` (the pair behind line-draw animation), `fill-rule`/`clip-rule` (nonzero vs evenodd for holes).
- `opacity` composites the whole element; `fill-opacity`/`stroke-opacity` are per-paint. Overlapping semi-transparent strokes double up visibly: design for it or restructure.
- Gradients: `<linearGradient>`, `<radialGradient>` with `gradientUnits` (objectBoundingBox default) and `gradientTransform`. Reuse one definition for many elements; never paste near-identical gradients per shape.
- `<pattern>` for repeating texture (grids, hatching, dots). Blueprint-style grids are one small pattern, not hundreds of lines.
- `<clipPath>` hides geometry outside a shape; `<mask>` applies greyscale alpha (white shows, black hides). Clip for hard crops, mask for soft fades.
- `<filter>` (blur, drop-shadow, colour matrices) is the most expensive feature: each filtered element rasterises offscreen. Prefer pre-drawn shadows (an offset dark shape at low opacity) in anything with many elements; keep `feGaussianBlur` radii small; never animate filters casually.

## 5. Reuse and definitions

- `<defs>` holds non-rendered definitions: gradients, patterns, clip paths, masks, markers, symbols.
- `<symbol id="...">` + `<use href="#...">` for repeated components (nodes in a diagram, icon parts). One definition, many placements: smaller files, consistent geometry, single point of edit.
- `<marker>` attaches arrowheads and dots to path ends/vertices via `marker-start/mid/end`; set `markerUnits` and `orient="auto"` so arrows follow the line direction and scale with stroke width when wanted.
- IDs must be unique in the document, and unique across the page when SVGs are inlined into HTML (prefix IDs per asset: `tb-arrow`, not `arrow`).

## 6. Text

- `<text>` with `x`/`y` (y is the baseline), `text-anchor` (start/middle/end), `dominant-baseline` for vertical trim, `<tspan>` for multi-line (SVG 1.1 has no automatic wrapping: break lines yourself or measure).
- Font availability is not guaranteed: standalone SVGs render with viewer defaults unless fonts are embedded or system-safe stacks used. Keep text editable where practical; convert to outlines only for logos/wordmarks where letterform fidelity is critical, and say so.
- Minimum legible sizes at final rendered scale: roughly 10-11px equivalent for labels, more for low-contrast or dense contexts. Check after scaling, not in the source coordinate system.

## 7. The SVG as a designed artefact

A technically valid SVG can still be visually poor. Before accepting any SVG, check its visual system:

- **Composition and focal point**: where does the eye land first, and is that the subject?
- **Proportion and alignment**: elements relate by a consistent grid or ratio; optical alignment beats mathematical alignment for triangles, circles vs squares, and type (see `typography-and-graphics.md`).
- **Stroke discipline**: one or two stroke weights used consistently; weights chosen for the final display size.
- **Optical corrections**: circles and points need to be slightly larger than squares of equal mathematical size; horizontal bars slightly thinner than vertical to look equal.
- **Cross-glyph equalisation (icon families)**: equal grid size is not equal visual size. Pointed and diagonal shapes (triangles, diamonds, chevrons) read smaller than squares and circles of the same bounding box, so let them overshoot the live area until their visual mass matches. Verify by rendering the whole family side by side at the target size and comparing masses, never one icon at a time.
- **Negative space**: breathing room inside the viewBox; nothing crowding the edges unless bleeding is intentional.
- **Hierarchy**: primary subject, secondary structure, tertiary annotation, distinguished by weight, size and value, not colour alone.
- **Colour**: a small deliberate palette with defined roles; adequate contrast between adjacent fills; works on the backgrounds it will actually sit on (test light and dark when the context is unknown).
- **Detail density**: matched to display size. A 16px icon carries 2-3 ideas, not 10.
- **Scalability**: legible at the smallest intended size, not merely at the authoring size.

## 8. Discipline-informed SVG (use only when it serves the purpose)

From aerospace and technical manuals: precise geometry, grid-based positioning, dimension lines, annotation callouts with leader lines, consistent symbol vocabulary, legible labels, restrained colour coding (one alert colour, used only for alerts), structured information density.

From architectural drawing: spatial hierarchy, structural grids, modular geometry, proportion and rhythm, layered plan/section thinking, line-weight conventions (heavy = cut/primary, medium = edges, light = detail/annotation), deliberate negative space.

These transfer well into cybersecurity diagrams, network maps, technical posters, documentation figures and presentations. Do NOT automatically add grids, dimensions or technical labels to every illustration; include only elements that support the intended purpose. A decorative illustration with fake dimension lines is aesthetic borrowing, not principle transfer (see `cross-disciplinary-design.md`).

## 9. Code quality rules

1. Coherent, predictable coordinate system; round numbers where the design allows.
2. Suitable `viewBox` and a deliberate responsive sizing strategy.
3. No unnecessary groups, duplicate definitions or redundant elements.
4. Repeated geometry through `<defs>`/`<use>`, not copy-paste.
5. Unique IDs; all `url(#...)`/`href` references valid.
6. Gradients, masks, filters and clips used intentionally, each earning its cost.
7. No expensive filter chains or oversized blur regions.
8. Strokes and fine details legible at expected sizes.
9. No accidental clipping, off-canvas elements or wrong transforms (verify by render, not by eye on code).
10. Readable, maintainable source: indentation, semantic grouping, comments only where the geometry is non-obvious.
11. Semantic grouping where it improves comprehension.
12. Text kept editable where practical; note font-dependency when it matters.
13. Primitives where primitives express the shape; paths where paths are needed; no pointless point-soup.
14. Valid XML: quoted attributes, closed elements, escaped `&`, `<` in text.
15. Rendered and inspected in the intended environment when tools allow; otherwise explicitly reported as unverified.

## 10. Accessibility

- Meaningful SVG: `role="img"` plus `<title>` (first child) and, for complex graphics, `<desc>`; reference them with `aria-labelledby` where inline. Provide a textual alternative near the graphic when the content is data.
- Decorative SVG: `aria-hidden="true"`, no title, `focusable="false"` for old IE/Edge inline cases.
- Never encode meaning by colour alone: pair colour with shape, position, pattern or label (severity = icon + colour, line style + colour).
- Contrast: labels and essential strokes meet the same contrast expectations as UI text (see `accessibility-and-quality.md`).
- Interactive SVG: real focus states, keyboard operability, target sizes comparable to HTML controls; prefer wrapping in buttons/links over scripting raw shapes.

## 11. Interaction and animation

- States: hover, focus-visible, active, disabled, drawn as deliberate designs, not browser accidents.
- Line-draw: `stroke-dasharray` + `stroke-dashoffset` transition. Movement: CSS transforms on groups (`transform-box: fill-box; transform-origin: center` to rotate around the element). SMIL exists but CSS/JS is the maintainable default.
- Respect `prefers-reduced-motion`: provide a reduced or static variant.
- Animate transforms and opacity (cheap); avoid animating filters, paths' `d` (except via dedicated techniques), or anything forcing layout.
- Motion must clarify relationships, communicate state or guide attention. Never animate to demonstrate ability.

## 12. Optimisation

Optimise when the design is validated, not before: keep readable source through iteration.

- Remove editor metadata, empty groups, default-value attributes, unused defs.
- Reduce path precision to what the display size needs (1 decimal is usually plenty at icon scale).
- Collapse transforms into coordinates where it simplifies.
- Merge paths sharing identical paint, when it does not destroy semantics or animation hooks.
- Check gzip/brotli size, not just raw bytes; repetitive SVG compresses extremely well.
- SVGO or equivalent for the final asset; diff-render before and after, because optimisers occasionally change appearance.

## 13. Rendering environment notes

- Browsers differ at the margins: filter fidelity, font fallback, `dominant-baseline` support, and CSS-in-SVG scope (external SVG via `<img>` ignores external CSS and scripts; inline SVG inherits page CSS, including unintended rules).
- SVG referenced by `<img>`/CSS background: no interactivity, no external resources, animations vary. Inline for interaction, external for cacheable static assets.
- Export to raster (for mail, social, thumbnails) via headless Chrome screenshot or resvg; verify the raster, since font and filter rendering can shift.

## 14. Verification procedure (mandatory for delivered SVGs)

1. Validate XML: `python3 -I -c "import xml.etree.ElementTree as ET,sys; ET.parse(sys.argv[1]); print('valid')" file.svg`.
2. Static checks: viewBox present; no element geometry outside the viewBox unless intended; IDs unique; every `url(#id)`/`href="#id"` resolves.
3. Render: headless Chrome `--headless --screenshot=out.png --window-size=WxH file.svg` (wrap in a minimal HTML page to control background and displayed size), or the environment's browser tooling.
4. Inspect the raster: composition, spacing, clipping, stroke weights, label legibility, contrast, proportions.
5. Re-render at the smallest intended size and on light AND dark backgrounds when the destination is unknown.
6. Fix defects, re-render, re-inspect.
7. Report precisely what was checked and what remains unverified. Never claim a render that did not happen.
