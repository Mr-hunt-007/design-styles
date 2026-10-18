# LESSONS

Confirmed mistakes, their causes, and the rules they produced. Append-only; newest at the top. Load this file at the start of any Studio or Flagship task: it is how each version of this skill is better than the last. When a lesson generalises, promote it into the proper reference or workflow file and note the promotion here; LESSONS is the inbox, the references are the law.

Format per entry: date, the mistake (observed, not hypothetical), root cause, the rule, where it now lives.

---

**2026-10-18 · KPI numbers that do not reconcile with the data they summarise.** A dashboard's headline tiles carried hardcoded delta constants that disagreed with its own 22-row queue; a blind judge caught it as the submission's main blemish. A second run showed the fix pattern: derive every displayed number from the one seeded dataset so tiles, chart, queue and detail agree by construction. Rule: a summary number is computed from the records it summarises, never typed in; reconciliation is part of the technical pass. Lives here; promote to `references/ui-ux.md` if it recurs.

---

**2026-10-18 · Icon families judged one glyph at a time.** An icon set lost a blind comparison because its alert triangle read optically smaller than its gear: each glyph was aligned individually, never compared as a row. Cause: guidance demanded per-icon optical alignment but not cross-glyph equalisation. Rule: a family is judged as a row at target size; pointed and diagonal glyphs overshoot the grid until visual mass matches. Promoted to `references/svg-and-vector-graphics.md` section 7 and `workflows/svg-creation.md` step 6. Verified by rerun: the fixed guidance flipped the comparison.

**2026-10-18 · Headless Chrome fakes mobile overflow.** Multiple runs "found" horizontal overflow at 390px that did not exist: headless Chrome clamps window width to roughly 500px, so naive narrow screenshots clip. Rule: test narrow viewports via an iframe harness or device emulation, and confirm with a scrollWidth probe before reporting overflow. Lives in the PIXEL persona (`agents/pixel.md`); promote to the SVG reference if it recurs.

**2026-10-18 · "Contrast fixed" without numbers.** A run claimed its contrast problems were fixed; a judge measured 2.9-4.2:1 on the "fixed" pairs. Cause: claim written from intention, not measurement. Rule: a verification claim requires the measured value next to it; otherwise write "unverified". Lives in the honesty rules (`SKILL.md`) and `agents/pixel.md`.

**2026-10-18 · External `<use>` fragments over file://.** Symbol sheets referenced as `icons.svg#id` do not resolve in Chrome over file://, so previews rendered empty. Rule: for local previews, inline the sheet and keep the external file canonical, noting the duplication. Observed independently by two runs; lives here until it recurs outside previews.

**2026-10-18 · Source review misses what a render catches.** An Art Deco composition passed source inspection but rendered with an asymmetric skyline notch cutting the sun; a diagram's labels overflowed their boxes by a few pixels. Cause: geometry errors invisible in coordinates, obvious in pixels. Rule: no visual deliverable ships on source review alone; the render loop is mandatory, and the render is inspected, not just produced. Lives in `workflows/svg-creation.md` and `workflows/design-loop.md`.

**2026-10-18 · Relative links written from the wrong directory.** Several docs referenced `tests/validate_skill.py` from folders where that path cannot resolve. Rule: every cross-file link is written relative to ITS OWN file and the validator checks all of them; run `python3 -I tests/validate_skill.py` after touching any doc. Enforced by `tests/validate_skill.py`.
