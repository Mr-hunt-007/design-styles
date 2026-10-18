# Decisions — 6-icon interface family

- Grid: 24x24, live area ~18x18 (3..21 on stroke centerline); pointed shapes (alert apex,
  asset cube tips) overshoot ~0.5px for optical size balance against flat-edged glyphs.
- Stroke: 1.75px, round caps + round joins everywhere; fill:none; color via currentColor.
- Corner language: 2px radius on all hard corners (scan brackets, alert triangle, report doc);
  asset cube uses 1.8px, scaled with the glyph so rounding reads identical.
- Metaphors: scan = viewfinder brackets + scanline; alert = triangle + exclamation (dot drawn
  as `h.01` with round cap); report = document with fold + column chart; asset = isometric
  cube; user = head + shoulders.
- Settings uses three sliders instead of a gear: a gear's teeth alias to mush at 16px with a
  1.75 stroke, and sliders keep the family's pure line/circle vocabulary. Rails and knobs are
  edge-aligned left (x3.5) and right (x20.5) across the three rows.
- icons.svg is the canonical sheet: <symbol> defs + a <use> row so it previews when opened
  directly. preview.html inlines a verbatim copy of the symbols because Chrome's external
  <use href="icons.svg#id"> is unreliable over file://; edit icons.svg first, then re-sync.
- Verified: rendered preview.html in headless Chrome at 2x (light + dark, 16/24/48px, inline
  16px text row) and icons.svg at ~64px/glyph; checked joints, alignment, 16px legibility by
  eye from screenshots. Not verified: Safari/Firefox, non-retina 1x hardware, icon fonts.
