# Decisions

- System: 24x24 grid, 2px stroke, fill none, round caps/joins, 2px corner radii, currentColor.
  Live area ~4..20 with 2px safe margin; one stroke weight across the family.
- Optical equalisation: pointed/diagonal glyphs read smaller than rectilinear ones at equal
  bounds, so the alert triangle (x 2.3..21.7) and asset cube (x 3..21) overshoot the live area
  until their visual mass matches scan, report, settings and user. Judged as a row, not per glyph.
- Metaphors: scan = corner brackets + sweep line; alert = triangle + exclamation; report =
  document with folded corner + text lines; asset = isometric cube; settings = three sliders
  (clearer than a gear at 16px with this stroke weight); user = head + shoulders.
- Legibility fix after first render: report originally held three chart bars, which merged into
  a solid blob at 16 and 24px; replaced with two horizontal lines, re-rendered, now clean.
- Delivery: icons.svg is a pure symbol sheet (symbol + use, per-symbol titles). preview.html
  inlines a copy of the sheet because external use fragments do not resolve over file://;
  icons.svg stays the canonical asset for app embedding.
- Verified: XML parses (python ElementTree), ids unique, no dangling references; headless
  Chrome renders of preview.html at 1x and 2x device scale inspected at 16/24/48px on the
  light and dark panels. Not verified: non-Chromium browsers, sub-16px sizes, printed output.
