# Decisions — Northbeam status page

Direction: Corporate Swiss (grid-driven clarity for information-rich, trust-critical communication), with one principle
transferred from aerospace instrumentation: the top-level annunciator must report the worst active condition.
Rejected decorative directions (gradients, dark hero, illustration) — a status page earns trust through restraint.

Changed:
- Banner no longer contradicts the page: "All Systems Operational (mostly)" became an honest amber state with an icon
  and a summary derived from the incidents below. This is the page's single focal point.
- Status was colour-only text; added dots as a redundant channel and recoloured all states to pass WCAG AA on white
  (every text/background and dot pair computed, 4.58:1-14.76:1; original #f39c12/#ccc/#b5b5b5 failed badly).
- One type family (system stack) replacing the Verdana/Georgia/Trebuchet mix; consistent 4/8px spacing, card system.
- Fixed 900px wrap became max-width 720px + fluid padding; component rows stack under 480px.
- Incident state (Investigating/Monitoring/Resolved) promoted from buried meta text to a badge; semantic HTML
  (lang, viewport, header/main/article, labelled email input, visible focus rings); "SUBSCRIBE!!" → "Subscribe".

Preserved: every component and its status, both active incidents verbatim (IDs, copy, timestamps), the past incident,
subscribe purpose, footer contacts, and the brand blue #1b4f72.

Verified: contrast ratios computed (script); rendered in headless Chrome at 1280px and at a true 360px viewport
(iframe probe — headless Chrome silently clamps windows to 500px wide), no horizontal overflow, layouts inspected.
Not verified: real devices, screen readers, keyboard walk (focus styles present but untested interactively).
