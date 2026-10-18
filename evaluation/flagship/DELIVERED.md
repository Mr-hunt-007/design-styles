# Flagship delivery record

Crew run, 2026-10-18: SCOUT wrote the pre-registered brief (BRIEF.md); three MUSEs designed in isolation (candidates/a typographic specimen, b technical drawing, c catalogue field); the orchestrator ran the PIXEL pass (identical renders, 1280px and 400px dark card); ROAST judged blind under neutral labels and committed the ranking (COLLAPSE.md): candidate c won 8.50 vs 8.40 (a) vs 8.05 (b).

FORGE fixes applied to the winner after the collapse, per ROAST's findings: mark grid re-pitched from 80px cells at 16px margin to 75px cells at 53.5px symmetric margins so corner marks clear link-card corner rounding (all 64 transforms rewritten programmatically, XML re-validated); kicker changed to the README-verbatim "PRINCIPLES, NEVER PRESETS" (ROAST's one fold-in). PIXEL re-verified: clean at 1280x640 and as a 400px rounded card on GitHub dark.

Delivered: docs/assets/social-preview.svg (source) and docs/assets/social-preview.png (1280x640 raster for GitHub's social preview setting). Losing candidates and all rationales kept in candidates/ as the record of why this direction.

Unverified: non-Chromium rasterisers; GitHub's own card renderer (uses the PNG, so font drift is moot).
