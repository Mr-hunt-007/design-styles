# Audit: `evaluation/fixtures/defective-status-board.svg`

**Artefact:** 640x360 service status board SVG (header, 3 service cards, uptime sparkline panel, open-incidents panel, legend).
**Assumed intent:** an at-a-glance operational status board for the Northbeam infrastructure team; success = correct status readable in seconds, by everyone, with no ambiguity.
**Original file not modified.** A corrected version is provided as `fixed.svg` in this directory.

## Method (what was actually run)

1. **Source review** of the full SVG (47 lines).
2. **XML validation:** `python3 -I -c "import xml.etree.ElementTree as ET,...` → parses ("XML valid").
3. **Contrast computation** (WCAG 2.x relative-luminance formula, scripted in Python) for every text/background and mark/background pair; ratios quoted below are computed, not eyeballed.
4. **Render in headless Chrome** (`--headless --screenshot`, the SVG embedded via `<img>` in a minimal page) at 640x360 and at 50% (320x180); both rasters visually inspected.
5. **Geometry measurement in headless Chrome** via a JS harness calling `getBBox()` on every `text`, `rect`, `circle`, `polyline` to get exact text extents and detect out-of-canvas geometry.

Each finding below is marked **CONFIRMED** (observed in source, render, or measurement) or **PLAUSIBLE**. Severity: critical > major > minor.

---

## Confirmed defects

### Structural

**S1. Duplicate ID `hdr` — two conflicting gradient definitions. (major, CONFIRMED)**
Evidence: lines 3-5 define `linearGradient id="hdr"` (horizontal, #2d3e50→#34495e); lines 6-8 define a second `linearGradient id="hdr"` (vertical, #777→#999). IDs must be unique in an SVG document. Chrome resolves `url(#hdr)` to the first definition (render shows the dark blue header), silently discarding the second; other renderers are not obliged to pick the same one, so the header colour is renderer-dependent in principle, and the author's intent is ambiguous. Fix: keep exactly one gradient, delete the other, and prefix the ID (`sb-hdr`) so it stays unique if the SVG is ever inlined into HTML.

**S2. Dangling paint reference `url(#missing-grad)` — the uptime panel does not render. (critical, CONFIRMED)**
Evidence: line 30, `<g fill="url(#missing-grad)">` wraps the uptime panel rect (line 31); no element with id `missing-grad` exists anywhere in the file. Chrome treats the unresolvable paint server as not-painted: the 640x360 render shows **no card at all** behind "Uptime, 30 days" — the title and sparkline float directly on the page background, breaking the card system the other panels establish. Fix: paint the rect directly (`fill="#ffffff" stroke="#d5dbe1" stroke-width="1"`) like the incidents panel, and delete the wrapper group.

**S3. Element entirely outside the canvas. (major, CONFIRMED)**
Evidence: line 46, `<rect x="668" y="120" width="120" height="60" .../>` — the viewBox is `0 0 640 360`, so the rect spans x 668-788, fully off-canvas. Measured by the `getBBox()` harness: `OUT-OF-CANVAS <rect> bbox 668,120 120x60`. It renders nowhere, bloats the file, and is a trap for the next editor (an invisible fourth card). Fix: delete it, or if a fourth card was intended, re-lay the card row.

**S4. Dead definition: empty `<g id="unused-stub">` inside `<defs>`. (minor, CONFIRMED)**
Evidence: line 9. An empty group that nothing references. Fix: delete.

**S5. Redundant anonymous nested groups. (minor, CONFIRMED)**
Evidence: lines 16-22, `<g><g> ...3 rects... </g></g>` — two nested groups with no attributes, no semantics, no reuse. Fix: remove, or replace with one semantic group per card (`<g id="sb-svc-api">` holding that card's rect, dot and labels together, which is what actually aids maintenance).

### Visual

**V1. Card 2 label overflows its card and collides with card 3. (critical, CONFIRMED)**
Evidence: line 27, "Dashboard web application front-end service" at x=276, 13px. Measured width 257.3px → the text ends at x=533.3 while its card ends at x=408. It crosses the 24px gutter, enters card 3 (starts x=432), and runs straight through the Jobs status dot (cx=460, r=10) — the 640px render shows the sentence striking through the yellow dot and colliding with the "Jobs" label. On a status board this is a task failure: card 3's status is partially obscured and the row is unreadable. Fix: shorten the label to fit the 180px card ("Dashboard" — the long form belongs in a tooltip/detail view); as a rule, card labels must be measured against card width minus insets.

**V2. Card 2 misaligned with the card row. (major, CONFIRMED)**
Evidence: card 1 and 3 at y=84 (lines 18, 20); card 2 at y=87 (line 19) — 3px lower, with its dot (cy=115 vs 112) and text baseline (y=120 vs 117) dragged along. Visible as a sag in the middle of the row in the render. Fix: y=84, cy=112, baseline y=117 for all three.

**V3. Inconsistent card border weight. (major, CONFIRMED)**
Evidence: card 2 `stroke-width="2.5"` vs `1` on cards 1 and 3 (and default 1 on the incidents panel). The render shows the middle card with a visibly heavier frame — unintended emphasis with no meaning (if the intent was "this one is down", the red dot already says so; a 2.5x border is a second, unexplained channel). Fix: stroke-width 1 everywhere.

**V4. Header title crowds the right edge. (minor, CONFIRMED)**
Evidence: measured end x=632.1 of 640 — an 8px right margin against a 20px left margin; at 50% render the title visually touches the edge. The 69-character title is also doing label-of-everything work. Fix: shorten ("Northbeam Platform Service Status", measured 313.5px wide in the fix) or reduce size/weight; keep left and right clearances matched.

**V5. Asymmetric page margins. (minor, CONFIRMED)**
Evidence: left margin 24px; right margin 28px (cards end at x=612, panels at x=612, canvas 640). Fix: re-space so both are 24px (in `fixed.svg`: cards at x=24/230/436 ending at 616, panels 284px wide ending at 616 — 24px both sides).

### Accessibility

**A1. Open-incident text is nearly invisible: contrast 1.6:1. (critical, CONFIRMED)**
Evidence: lines 38-39, `fill="#c8cdd2"` on the white card; computed ratio **1.6:1** against the 4.5:1 requirement for 12px text. These two lines are the most consequential content on the board (what is broken right now) and they are the least legible thing on it — faint even for full-sighted users in the render. Fix: `#566573` (computed 5.99:1) or darker.

**A2. Status is encoded by colour alone, and the legend has no labels. (critical, CONFIRMED)**
Evidence: the only status signal per service is dot colour (lines 23-25); the legend (lines 41-44) is three unlabelled coloured circles — it defines nothing, for anyone. In greyscale (or for the ~1-in-12 male users with red-green CVD) green #2ecc71 and red #e74c3c dots are near-identical discs. Fix: add a second channel — a status word per card ("Operational" / "Outage" / "Degraded") — and give every legend swatch a text label using the same vocabulary (done in `fixed.svg`).

**A3. No accessible name: missing `<title>`, `<desc>`, `role="img"`. (major, CONFIRMED)**
Evidence: the root element (line 1) carries none; the first child of `<svg>` is `<defs>`. A screen reader gets fragments of positioned `<text>` with no stated structure and no summary. Fix: `role="img"` + `aria-labelledby` pointing at a `<title>` and a `<desc>` that states the three statuses and the open incidents (the picture is a view; the data needs a textual form).

**A4. Status dots fail non-text contrast 3:1. (major, CONFIRMED)**
Evidence (computed, against their white cards): yellow #f1c40f = **1.66:1**, green #2ecc71 = **2.1:1** (red #e74c3c = 3.82:1 passes). The two "calm" states are low-visibility marks. Fix: darker status hues — #1e8449 (4.72:1), #b9770e (3.68:1), #c0392b (5.44:1), all computed ≥3:1.

**A5. Legend caption contrast fails at 11px: 2.36:1. (major, CONFIRMED)**
Evidence: line 41, `#95a5a6` on page background `#f4f6f8`; computed **2.36:1** vs the 4.5:1 requirement for small text. Fix: `#5d6d7e` (computed 4.9:1 on `#f4f6f8`).

**A6. Sparkline contrast marginally fails for a meaningful graphic: 2.91:1. (minor, CONFIRMED)**
Evidence: `#3498db` on `#f4f6f8`, computed **2.91:1** vs the 3:1 requirement for meaningful graphics. Borderline, but it is the only data mark in the panel. Fix: `#2874a6` (computed 4.68:1).

---

## Improvement suggestions (not defects)

1. **The sparkline is unreadable as data.** No scale, no min/max, no current value; "Uptime, 30 days" plus an unlabelled wiggle conveys trend-shape only. Add at least a current-value annotation (illustrative "99.2%" added in `fixed.svg`) or min/max gridlines. The underlying numbers should also exist as text somewhere (caption or table) if this board is the record.
2. **Prefix all IDs** (`sb-hdr`, `sb-legend`...) so the asset survives inlining next to other SVGs on one page.
3. **Consider dropping fixed `width`/`height`** on the root (keep `viewBox`) if the board will be embedded responsively; keep them only for strict embed contexts (email, fixed iframes).
4. **Card borders are decorative at 1.4:1** (#d5dbe1 on white). Acceptable because the white-card-on-grey fill does the grouping work, but a slightly darker border would survive poor displays better.
5. **Reuse:** the three card shells could be one `<symbol>`/`<use>`; at three instances this is optional, but it would have prevented V2/V3 (the misalignment and stroke inconsistency were copy-paste drift, which reuse makes impossible).
6. **Incident rows carry no severity, status or timestamp** — on a real board, each row needs at least a severity mark (colour + label, per A2's rule) and an age.
7. **Chart inset consistency:** sparkline insets are 12px left / 8px right of its panel; align both to the panel's 12px text inset.

## What works and should survive

The information architecture is right: header for identity, a status row first, trend and incidents below, legend last — the reading order matches the priority order of an ops board. The restrained palette (one dark header, white cards on a quiet grey field, one accent per meaning) and the card system with 6px radii and a consistent 1px border (where not drifted) are a sound foundation; the fixes above are repairs to this system, not a redesign.

## Three highest-impact improvements

1. **Make the critical content legible:** fix incident-text contrast (A1) and the card-2 overflow/collision (V1) — these two break the board's core task.
2. **Make status colour-independent:** status words on cards + labelled legend (A2), with the darker dot palette (A4).
3. **Repair the structure so it renders deterministically:** one uniquely-ID'd header gradient (S1), paint the uptime panel directly instead of via the dangling reference (S2), delete the off-canvas rect and dead groups (S3-S5).

All of these are implemented in `fixed.svg`.

## Verification report (honest-reporting rule)

**Checked:**
- XML validity of original and `fixed.svg` (ElementTree parse) — both pass.
- All contrast ratios quoted above — computed with the WCAG relative-luminance formula in Python (original and fix palettes).
- Original rendered in headless Chrome at 640x360 and 320x180; rasters inspected (overflow, missing panel, faint incident text, unlabeled legend all visually confirmed).
- Text extents and out-of-canvas geometry measured via `getBBox()` in headless Chrome (exact numbers quoted in findings).
- `fixed.svg` rendered at 640x360 and re-measured with the same harness: all text within its containers, no out-of-canvas geometry, no dangling references.

**Failed and fixed (in `fixed.svg`):** S1-S5, V1-V5, A1-A6, plus suggestions 1 (current-value annotation, illustrative figure), 2, 5 (semantic per-card groups), 7.

**Unverified:**
- Rendering in non-Chromium renderers (Firefox, Safari, resvg, email clients) — not available in this run; S1's renderer-dependence is asserted from the SVG spec, observed only in Chrome.
- Screen-reader behaviour of `fixed.svg`'s `title`/`desc` — no screen reader in this environment; the markup follows the documented pattern but was not heard.
- Dark-background behaviour — not tested; the board paints its own full-bleed background, so it is self-contained, but a transparent-background variant was not evaluated.
- `fixed.svg` was not re-rendered at 50%; the original's 50% render showed no additional size-dependent defects beyond those listed.
