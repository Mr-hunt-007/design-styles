# Decisions — Northbeam status page

Changed:
- Replaced the mixed-font (Verdana/Georgia/Trebuchet) look with a single system font stack, a small
  token palette, and a 720px column on a soft grey background with white cards.
- Component table became a card list with colored status pills (dot + tinted background), so state is
  readable by color, text, and shape; incident status moved into badges (Investigating/Monitoring/Resolved).
- Overall banner now says "Some systems are experiencing issues" with an amber accent: the original
  "All Systems Operational (mostly)" contradicted the partial outage and degraded rows shown below it.
- "SUBSCRIBE!!" became "Subscribe"; email input got type=email, a hidden label, focus styles, and short
  explanatory copy. Fixed 900px width replaced with responsive layout (viewport meta, wrapping, 480px query).
- Semantic HTML (header/main/article/ul/form, h3 for incident titles); meta text contrast raised from #b5b5b5.

Preserved:
- All six components and their exact statuses; both active incidents' IDs, full wording, and timestamps;
  the past-incident entry; the "7 days" framing; section order; Northbeam navy brand color; footer details.

Verification: rendered with headless Chrome at 1280px and inside a 390px iframe (Chrome's headless minimum
window width prevented a direct 390px capture); inspected both screenshots — no overflow, media query and
footer wrapping confirmed. No JS behavior to test; the form intentionally remains non-functional, as before.
