# DECISIONS — Greenfield Saturday Farmers Market, Season Opening Poster

Deliverable: `poster.svg`, a single self-contained A3 portrait SVG (viewBox 0 0 842 1191 = A3 at 72 dpi; root sized 297mm x 420mm). Depth tier: **Studio** — a real shipping artefact, full loop solo. No existing design system governs this fictional brand, so the direction was chosen from the brief.

## 1. Problem first

A street/window poster must do two jobs at two distances: announce *farmers market — season opening* at a glance from several metres, and deliver date, time, place and the stall offer to someone who walks up to ~2 m. Everything below follows from that split.

## 2. Direction

Primary direction: **mid-century market/grocery poster** (flat vector shapes, cream paper ground, deep green + tomato red) carried on **Swiss grid discipline** for the information hierarchy. The scalloped awning band is the one pictorial signifier — it says "market" wordlessly and from any distance. Rejected directions: corporate minimalism (too cold for a community market), Didone/luxury type (wrong voice, hairlines fragile in print and rasterisation), textured/grunge "hand-made" styling (hurts legibility and rasterises badly), photographic collage (wrong tool for a self-contained SVG).

## 3. Hierarchy (readable order, top to bottom)

1. FARMERS / MARKET — 148 pt eq., ~37 mm caps, legible from 15 m+.
2. SEASON OPENING — 64 pt eq. in the only saturated accent (red), the announcement itself.
3. Date / time / place — reversed cream on a solid green panel, the highest-contrast block on the sheet (measured 8.8:1), 46 pt eq. for date and time.
4. Six stall categories — icon chips in a 3-column grid, 20 pt eq. labels (~5 mm caps — above the ~2 mm-cap-height-per-metre legibility floor at 2 m).
5. Practicals footer, 16.5 pt eq. (~4 mm caps), walk-up distance only by design.

Skeleton test: stripping the poster to sizes/weights alone still yields "farmers market → season opening → when/where → what's there".

## 4. Grid and spacing

Content column x=64..778 (714 wide); double rule frame at insets 24/4 pt and 34/1.5 pt (≈8.5 mm from trim — inside any realistic print safe area). Category grid: 3 columns of 222 with 24 gutters; two rows on a repeated vertical rhythm (chip centre → label baseline = 62 throughout). Headline leading 146 on 148 caps (no descenders in either line, so near-solid leading reads as one block). Headings attach downward: the 36-unit gap above the green panel is smaller than the 40 above SEASON OPENING.

## 5. Colour

- Paper cream `#F6EFDD`; deep green `#1F4A2C`; tomato red `#C23B22`; straw gold `#D99A2B`; chip white `#FFFDF6`.
- Measured contrast: green on cream **8.8:1** (all body/label text); cream on green panel **8.8:1**; red on cream **4.6:1**, used only at display size (64 pt) and for decorations, never for small text; gold is never a text colour.
- Meaning is never carried by colour alone: every category has an icon *and* a label; the red "SEASON OPENING" is also the largest line after the title.

## 6. Rasterisation without webfonts (explicit requirement)

Three mechanisms, belt and braces:

1. **System-safe stacks only.** Display/labels: `Arial, Helvetica, 'Liberation Sans', 'DejaVu Sans', sans-serif` (metric-compatible fallbacks across macOS/Windows/Linux). The single italic accent line: `Georgia, 'Times New Roman', serif`. No @font-face, no external resources of any kind — the file is fully self-contained.
2. **Width locking.** Every full-width caps line carries `textLength` + `lengthAdjust="spacingAndGlyphs"`, so line width is fixed by geometry, not by whichever font the rasteriser picks; nothing can overflow the frame or the panel. Short chip labels are left natural with ≥20 % width headroom in their columns.
3. **Tolerant layout.** All text is centre-anchored with generous padding; no text is tightly fitted against a box edge; all non-text graphics are flat fills and simple strokes (no filters, masks, or gradients that shift between rasterisers).

Verified by substitution test: re-rendered the whole poster with the sans stack forcibly replaced by Times New Roman — composition, containment and hierarchy held (see §9). Text is kept live/editable rather than outlined; the trade-off is font-dependent letterforms, which the three mechanisms above make safe, and it preserves accessibility and editability.

## 7. Icon system (six stall categories)

Fresh Produce (carrot), Baked Goods (loaf), Dairy & Eggs (bottle + egg), Cut Flowers (tulip), Honey & Jams (jar), Local Crafts (jug). One system: 44-unit grid, flat fills, deep green as the family's base with one warm accent each (red x2, gold x3, cream details), set in 66-unit ringed chips so the row reads as one family. Judged as a row at full and half size (cross-glyph mass check), not glyph-by-glyph. Labels are short single-line names chosen to fit the 222 column across font substitutions.

## 8. Engineering and accessibility

- `role="img"` + `<title>` + `<desc>` carrying the full factual content (dates, time, place, categories) as the textual alternative.
- Prefixed unique IDs (`gm-*`); repeated geometry via `<defs>`/`<use>` (awning unit x13, chip ring x6, diamond ornament); primitives where primitives suffice; no filters; no off-canvas geometry; valid XML (parsed programmatically).
- Content is fictional by design: `.example`-free copy, no real organisation imitated.

## 9. Verification (loop record)

- Pass 1: XML parse OK; no duplicate IDs; rendered via headless Chrome at 842x1191 and 421x596 (an HTML `<img>` harness — direct SVG screenshots crop because the mm root size exceeds the window). Findings: footer sat too close to row-2 labels (read as part of the grid); two stray no-op transforms.
- Pass 2: category block shifted up 14-16 units, footer separated to a 42-unit gap; re-rendered full size — zero confirmed findings; half-size render confirms all text legible and icons distinct at 50 %.
- Robustness pass: full re-render with the sans stack swapped to Times New Roman — no overflow, no clipping; `textLength` locks held every display line to its designed width.
- Unverified: physical print output (CMYK shift, stock) and renderers other than Chromium (resvg/Inkscape/rsvg); the design avoids the features where those diverge (filters, masks, external refs).

## 10. If this continued (top 3)

1. Print package: CMYK-intent colour check and a 3 mm bleed variant for commercial printing.
2. A second accent illustration pass (e.g. produce spot illustrations in the corners) explored against the current restraint — only if it survives the 2 m hierarchy test.
3. Derivative formats from the same system: A6 handbill (type sizes re-cut, not scaled) and a social square.
