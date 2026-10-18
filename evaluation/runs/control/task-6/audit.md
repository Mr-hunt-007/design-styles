# Audit: defective-status-board.svg

Fixture: `/Users/allwin/Downloads/design-styles/evaluation/fixtures/defective-status-board.svg` (640x360, untouched).
A corrected version is provided at `fixed.svg` in this directory.

## Checks actually run

- `xmllint --noout` for XML well-formedness (passes; the file is well-formed, so every defect below is semantic, visual, or accessibility-related, not a parse error).
- Script scan for duplicate `id` attributes and unresolved `url(#...)` references.
- WCAG relative-luminance contrast calculations (sRGB formula) for every text/background and dot/background pair, for both the original and the fix colors.
- Headless Chrome (`--headless=new`) render of the SVG to a 640x360 PNG, inspected visually.
- Headless Chrome DOM harness measuring `getComputedTextLength()` for every `<text>` element and the computed fill of the broken-reference rect, to confirm overflow/collision with numbers rather than eyeballing.
- The same render + measurement pass was re-run on `fixed.svg` to confirm the fixes.

Not run: no screen-reader (VoiceOver) pass, no non-Chrome renderer (Safari/Firefox/librsvg/Inkscape) comparison. Cross-renderer claims below are based on spec behavior, flagged as such.

---

## Confirmed defects

### Structural

**S1. Duplicate `id="hdr"` on two different gradients (lines 3-8).**
Evidence: script scan found `ids: ['hdr', 'hdr', 'unused-stub']`. Two `<linearGradient id="hdr">` elements are defined with different geometry and colors (dark blue horizontal vs grey vertical). Duplicate IDs are invalid in XML/SVG documents. Chrome resolves `url(#hdr)` to the first definition (verified via `getElementById` in the harness: first stop `#2d3e50`), so the grey gradient is silently dead -- but ID resolution order with duplicates is not something any renderer or toolchain guarantees; an SVG optimizer or a different renderer can legally pick the other one and turn the header grey.
Fix: keep one gradient. If the grey one is intentional for another use, rename it (`id="hdr-alt"`); otherwise delete it.

**S2. Broken paint reference: `fill="url(#missing-grad)"` on the uptime card group (line 30).**
Evidence: script scan reports `missing: ['missing-grad']`; the harness confirms the computed fill is still the unresolved `url("#missing-grad")`. In the Chrome render the 280x110 uptime card rect is simply not painted: the "Uptime, 30 days" label and sparkline float on the page background with no card behind them, unlike the matching "Open incidents" card at the same row. A reference to a non-existent paint server with no fallback makes the element unpainted in SVG 1.1; some renderers treat it as an error.
Fix: `fill="#ffffff" stroke="#d5dbe1"` to match the sibling card (or define the gradient). If a `url()` fill is kept, always provide a fallback: `fill="url(#grad) #ffffff"`.

**S3. Dead content outside the viewBox (line 46).**
Evidence: `<rect x="668" y="120" width="120" height="60" .../>` -- the viewBox is `0 0 640 360`, so the rect's left edge starts 28 units past the right boundary. It is invisible in the render but still parsed, hit-testable in some contexts, and counted in the bounding box by tools that ignore the viewBox (export pipelines, `getBBox`-based fit logic).
Fix: delete it, or move it inside the canvas if it was meant to be a fourth card.

**S4. Dead markup: empty `<g id="unused-stub"></g>` in `<defs>` (line 9) and a doubly nested attribute-less `<g><g>...</g></g>` around the status cards (lines 16-22).**
Evidence: direct source inspection; neither group carries any attribute, transform, or semantics. Pure weight and misdirection for the next editor.
Fix: remove the stub and flatten to a single (or zero) wrapper group.

### Visual

**V1. Middle status card text overflows its card and collides with the third card's label.**
Evidence: measured `getComputedTextLength()` for "Dashboard web application front-end service" = 257.3px starting at x=276, so its right edge is at **x=533.3**, while its card ends at x=228+180=**408** and the third card starts at x=432. The text crosses its own border, the gap, the third card's border, its status dot (cx=460), and overlaps the "Jobs" label (x=480-507.5 at nearly the same baseline). Clearly visible as garbled text in the render.
Fix: shorten the label (e.g. "Dashboard", with the full name in a `<title>` child for hover/AT), or clip/ellipsize; a 180px card at 13px Arial fits roughly 20 characters after the dot.

**V2. Middle status card is misaligned and inconsistently styled with its siblings.**
Evidence: cards 1 and 3 sit at y=84 with `stroke-width="1"`; card 2 sits at y=87 with `stroke-width="2.5"` (lines 18-20). Its dot (cy=115 vs 112) and text baseline (y=120 vs 117) carry the same 3px offset. Visible in the render as a dropped, heavier-bordered middle card.
Fix: y=84, stroke-width=1, cy=112, text y=117, matching the siblings.

**V3. Header title nearly touches the right edge (asymmetric margins).**
Evidence: measured title width 612.1px from x=20, right edge at x=632.1 on a 640-wide canvas -- 20px left margin vs 7.9px right margin. It does not clip (confirmed by measurement; I am not claiming clipping), but any slightly wider font fallback (Arial unavailable -- see A4) pushes it off-canvas, and visually it reads as overset.
Fix: shorten the title (e.g. "Northbeam Platform: Service Status") or reduce the size so the right margin matches the left 20px.

**V4. Sparkline x-spacing is uneven.**
Evidence: polyline x values 36, 80, 124, 168, 212, 256, 296 -- six steps of 44 then a final step of 40 (line 34). For a time series with evenly spaced samples this silently distorts the last interval.
Fix: last point at x=300 (still inside the card, which ends at x=304).

### Accessibility

**A1. Incident text fails WCAG AA text contrast catastrophically.**
Evidence: computed ratio of `#c8cdd2` on the white card = **1.60:1** (AA requires 4.5:1 for 12px text). The two incident lines -- the most operationally important text on a status board -- are the least readable thing on it, and read as "disabled" styling.
Fix: a dark grey such as `#4b5563` (measured 7.56:1). The "Legend:" label `#95a5a6` on `#f4f6f8` also fails at **2.36:1**; `#515e6a` gives 6.14:1.

**A2. Status is conveyed by color alone (WCAG 1.4.1).**
Evidence: each service's state is encoded solely in the dot fill (green/red/yellow, lines 23-25); no status word, pattern, or shape differs. The legend (lines 41-44) makes it worse: three colored dots with **no text labels at all**, so even a sighted user is never told what green/yellow/red mean, and a color-blind user cannot recover the mapping. The red/green pair is the classic deuteranopia confusion pair.
Fix: add a status word per card ("Operational" / "Outage" / "Degraded") and label each legend dot.

**A3. Non-text contrast of the status dots fails WCAG 1.4.11.**
Evidence: computed ratios against their white cards: yellow `#f1c40f` = **1.66:1**, green `#2ecc71` = **2.10:1** (minimum 3:1 for meaningful graphics; red passes at 3.82:1). Against the `#f4f6f8` page background the legend's yellow dot is 1.53:1.
Fix: add a darker 1.5px stroke per dot (`#1e8449` 4.72:1, `#8a6d03` 4.92:1, `#b03a2e` 6.02:1 -- all measured) or darken the fills. (With A2 fixed, the dots become redundant with text, but the strokes keep them legible regardless.)

**A4. No accessible name or structure for the whole graphic.**
Evidence: the root `<svg>` has no `<title>`, no `<desc>`, no `role="img"`, no `aria-*`; none of the texts are associated with the dots they describe. Screen readers announce either nothing or a soup of unassociated strings; the image has no name in an `<img>`-style embedding.
Fix: `role="img"` + `aria-labelledby` pointing at a `<title>`/`<desc>` pair on the root; `<title>` children on each status group.

**A5. No generic font fallback.**
Evidence: `font-family="Arial"` on the root (line 1) with no fallback stack. On systems without Arial (most Linux renderers, many CI rasterizers) the renderer picks an arbitrary default, changing all the metrics this layout already strains (see V1, V3).
Fix: `font-family="Arial, Helvetica, sans-serif"`.

---

## Improvement suggestions (not defects)

1. **Sparkline has no scale.** No axis, min/max, or unit for "Uptime, 30 days"; the line is uninterpretable (is the dip 99.9% or 60%?). Add min/max labels or a baseline gridline.
2. **Card text is not vertically centered.** The dot/label row sits at y~112 inside an 84-154 card (center 119); nudging to cy=119 would balance the cards, especially if a second status line is not added.
3. **Incident rows could carry severity.** Reusing the status-dot language (small dot per incident) would tie the two panels together.
4. **Title hierarchy.** The header is one 20px string; a product name + lighter subtitle split would scan faster on a wall display.
5. **Hygiene:** collapse the `stop` elements' `offset="0"/"1"` to `0%/100%` consistency, and consider `shape-rendering`/`text-rendering` hints only if the board targets low-DPI wall screens.

---

## Fixed version

`fixed.svg` in this directory applies S1-S4, V1-V4, and A1-A5 (plus suggestion 2) with the measured colors above. It was re-rendered and re-measured in the same headless-Chrome harness: no duplicate ids, no unresolved `url()` references, every text right-edge inside its container, and all text/dot contrast pairs at AA or better.
