# COLLAPSE: flagship banner judging

ROAST · 2026-10-18 · Blind collapse of three parallel MUSE candidates against BRIEF.md. Judged from the delivered renders (full.png at 1280x640, card-dark.png at ~400px on GitHub dark) and SVG source. Every text claim was checked against README.md, EVALUATION.md and LICENSE. Contrast ratios computed (WCAG relative luminance); cand-2's printed "1152" measure checked against actual ink extents in the render (ink spans x≈65 to x≈1215 ≈ the 64..1216 measure: true as rendered).

---

## Candidate 1 — "the catalogue field" (64 marks above/below a calm clearing)

### Gate check: PASS
1. Self-contained SVG, viewBox 0 0 1280 640, no external refs, system font stacks with fallbacks. PASS.
2. `design-styles` present (124px mono bold) + one-line proposition. PASS.
3. Honesty: "64 STYLES" = README's 64-style catalogue (a catalogue count, not an evaluation number); "PRINCIPLES, NOT PRESETS" paraphrases README's "principles, never presets"; tagline is README line-1 territory; no evaluation numbers, no badges, no logos. PASS.
4. Name clearly readable at 400px (~39px rendered); proposition readable at 400px (small but legible in card-dark.png). PASS.
5. Opaque #F5F2EA ground; name/prop/kicker all inside the 64px margin. The 64-mark field runs to 16px of every edge, but it is texture, not critical content. PASS.

### Scores
| Criterion | Score | Evidence |
|---|---:|---|
| Instant legibility (25) | 9 | Name dominates card-dark.png; tagline still reads at 400px; the two mark bands frame rather than compete |
| Originality (20) | 8 | A countable 64-glyph specimen field is a defensible identity; specimen-sheet genre exists, but the one-mark-per-style conceit is this project's own |
| Hierarchy (15) | 8 | Eye: name → tagline → field; the darker top band pulls first-glance weight slightly before the name at card scale |
| Craft (15) | 8 | Single construction grammar (80px cells, 48px live, stroke 3 throughout, verified in source); accent bar = one mono char cell (0.6023×124≈75); crisp 0.5px-offset hairlines at 160.5/479.5 |
| Message accuracy (10) | 9 | Tagline faithful to README; the field makes the README's central noun literally countable — the banner demonstrates the catalogue instead of describing it |
| Robustness (10) | 9 | No textLength tricks; mono wordmark ends ~x=1035, so even a narrower fallback (Consolas 0.55em advance) stays safely inside the margin; all 64 marks are plain paths |
| Accessibility (5) | 9 | Name 15.9:1, tagline 12.7:1, kicker 6.1:1, marks 6.7:1; meaning never by colour |

**Weighted: 8.50**

### Confirmed defects
- CONFIRMED: corner marks sit 16px from the canvas edge; GitHub link-card corner rounding shaves them, which chips the "exactly 64 complete marks" conceit at the four corners. Fix: pull the four corner cells in, or accept the shave knowingly.
- CONFIRMED: "PRINCIPLES, NOT PRESETS" paraphrases the README's "principles, never presets" — honest in substance, but the verbatim phrase is free and stronger.
- TASTE: the two-tone banding (#ECE8DD strips) is quiet to the point of near-invisibility on some monitors; it reads, but barely.

---

## Candidate 2 — "the measured specimen" (Swiss wordmark + red annotation layer)

### Gate check: PASS (with one renderer-conditional caveat, below)
1. Self-contained, Helvetica/Arial/Liberation stack stated. PASS.
2. Name (178px) + two-line proposition. PASS.
3. Honesty: "64 STYLES · 12 MODES · 1 VERIFICATION LOOP" all verified in README (lines 59, 64); "BLIND-JUDGED VERDICT: PARTIALLY EFFECTIVE" is the recorded verdict stated with its own label and no stripped numbers — this is exactly the compliant form constraint 3 describes; "1152" and "baseline" are self-referential measurements and both are TRUE as rendered (measured); MIT verified in LICENSE. PASS.
4. Largest name of the three (~55px at card scale); proposition clearly readable at 400px. PASS.
5. Opaque ground; all content inside 64..1216 (wordmark ink aligned to the margin via side-bearing offset, confirmed in render). PASS.

### Scores
| Criterion | Score | Evidence |
|---|---:|---|
| Instant legibility (25) | 10 | Best 400px read of the field: name fills the measure, both prop lines legible in card-dark.png |
| Originality (20) | 7 | The red-annotated type specimen is a known genre; the genuinely original stroke is printing the project's own unflattering verdict on its face |
| Hierarchy (15) | 8 | Name → prop is clean; the annotation layer (baseline label, 1152, two meta rows, 4 corners occupied) scatters the second look slightly; upper-middle dead zone is intentional Swiss air but unearned at 2:1 |
| Craft (15) | 9 | Half-pixel hairline discipline (356.5, 64.5/1215.5 ticks), dimension line broken around its label, side-bearing compensation so ink — not glyph boxes — hits the margins; measured and true |
| Message accuracy (10) | 9 | Putting "PARTIALLY EFFECTIVE" on the banner is the purest expression of the README's evidence-over-hype voice; every claim verified |
| Robustness (10) | 6 | The hero hangs on `textLength="1162" lengthAdjust="spacingAndGlyphs"`: where textLength is honored, fallback fonts (Arial/Liberation at 178px) get visibly respaced glyphs; where it is NOT honored (older librsvg-class rasterizers), the ink no longer spans 1152 and the printed "1152" becomes a false measurement — the one honesty claim in the set that a renderer can falsify |
| Accessibility (5) | 9 | Ink 16.6:1, meta 6.8:1, red annotations 5.9:1; annotations also carried by lines, not colour alone |

**Weighted: 8.40**

### Confirmed defects
- CONFIRMED: single-point-of-failure coupling between the "1152" claim and textLength support (source line 36); true in the judged render, unverifiable here on other rasterizers (none installed). Fix: outline the wordmark to paths — the measurement then becomes unconditionally true and the font stack question disappears for the only element that matters.
- CONFIRMED: at 400px the entire annotation layer (the candidate's concept) drops below legibility — the self-demonstration only exists at 1280px; the card-scale viewer sees a plain type banner.
- PLAUSIBLE: cap-height alignment to the top rule shifts across Helvetica Neue/Arial/Liberation metrics; untested on non-mac hosts.

---

## Candidate 3 — "FIG. 1" (technical sheet of the render-and-verify loop)

### Gate check: PASS
1. Self-contained; mono stack with fallbacks; pattern grid, no external refs; `use` carries both `href` and `xlink:href`. PASS.
2. Name (84px mono) + proposition. PASS.
3. Honesty: "64-STYLE CATALOGUE · PRINCIPLES, NEVER PRESETS" verbatim README; body copy faithful ("reasons about the problem before styling, renders the result to verify it, fixes what the render exposes"); loop stations are real skill behaviour; no evaluation numbers; the figure is a diagram, not fake UI chrome. PASS.
4. Name readable at 400px (~26px) — passes, with the least headroom of the three. PASS.
5. Opaque ground; text content inside margins (callout ends ~x=1212). The decorative frame sits at 36px, outside the safe zone. PASS (frame is not critical content).

### Scores
| Criterion | Score | Evidence |
|---|---:|---|
| Instant legibility (25) | 7 | Name smallest of the three and shares the first glance with the diagram; prop legible at 400px, body text and all station labels are not (acceptable as tertiary, but the right half goes mute at card scale) |
| Originality (20) | 9 | The most distinctive artifact of the set; reads like an instrument sheet, nothing like template OSS banners or gradient slop |
| Hierarchy (15) | 7 | Left block vs right figure splits attention near 50/50; at card scale the circuit's mass competes with the wordmark for the first fixation |
| Craft (15) | 9 | Geometry verified from source: station centres sit on the r=164 circuit to 0.05px (√(116²+116²)=164.05); arrow rotations correct for clockwise flow; three disciplined stroke weights; single vermilion accent used only for fault-and-fix |
| Message accuracy (10) | 9 | Literally depicts the loop the README leads with; the red fault found at RENDER, magnified at INSPECT, corrected at FIX is the project's story told in one figure |
| Robustness (10) | 8 | All-mono, no textLength, middle-anchored labels tolerant of metric drift; minor: letter-spacing on middle-anchored labels off-centres by ~1px in some engines |
| Accessibility (5) | 8 | Ink 14.3:1, body 7.2:1, caps 6.0:1, notes 7.8:1, accent 4.6:1 — all pass; loop direction carried by arrowheads, not colour |

**Weighted: 8.05**

### Confirmed defects
- CONFIRMED: the sheet frame (x=36) lives outside the 64px safe zone; link-card corner rounding clips the drawn corners, which on a "technical sheet" conceit reads as a cropped sheet.
- CONFIRMED: at 400px every label on the figure is illegible, so the diagram carries only its silhouette; the candidate's content-rich half contributes shape, not information, at the scale that matters most (25% criterion).
- TASTE: body paragraph in mono at 17px is austere to the point of greyness; it suits the sheet conceit.

---

## Ranking (committed)

**1st — Candidate 1 (8.50). 2nd — Candidate 2 (8.40). 3rd — Candidate 3 (8.05).**

The decisive differences:

1. **Robustness vs. a conditional honesty claim.** Cand-1's layout tolerates any fallback font with ~180px of slack; cand-2's printed "1152" is only true while the rasterizer honors textLength — the single place in the whole field where an honesty claim is held hostage by the rendering engine, on a brief where honesty is a rejection gate. A banner whose proof can silently go false loses to one whose proof is 64 countable paths.
2. **Self-demonstration that survives 400px.** Cand-1's evidence (the catalogue field) is fully present at card scale; cand-2's evidence (the annotation layer) and cand-3's evidence (the labelled loop) both drop below legibility exactly where 25% of the weight sits. Only cand-1 is still demonstrating the project in a feed.
3. **First-glance hierarchy.** Cand-3 gives the name 84px and half the canvas to a figure that competes with it; cand-1 and cand-2 both give the name an uncontested landing. That is what separates 3rd from the top two.

Cand-2 loses by 0.10 — it would win outright with the wordmark outlined to paths.

## Fold-ins to the winner (serving cand-1's own principle: the catalogue is the evidence)

1. From cand-3: replace "PRINCIPLES, NOT PRESETS" with the README-verbatim **"PRINCIPLES, NEVER PRESETS"** — cand-1's principle is evidence-exactness, and the exact claim is free.
2. No second fold. Cand-2's verdict line and annotation layer are its own concept; grafting either onto cand-1's calm clearing adds a second voice the composition was built to avoid.

(Separately, cand-1 should fix its own confirmed defect: the four corner marks vs. card corner-rounding.)

## Confidence

**Medium-high.** High on honesty gates (every text claim checked against README.md, EVALUATION.md, LICENSE), on contrast (computed), on cand-3's geometry and cand-1's mark count (verified in source), and on both provided scales (rendered renders inspected at 1280 and ~400 dark).
Unverified: cross-rasterizer behaviour (no rsvg/resvg/inkscape on this machine) — cand-2's textLength risk and cand-3's letter-spacing centring are PLAUSIBLE, grounded in known engine behaviour but not reproduced here; light-theme GitHub surround was not separately rendered (all three supply opaque cream grounds, so risk is low); no render at 2x was made.
