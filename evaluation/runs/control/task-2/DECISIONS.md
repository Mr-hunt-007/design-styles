# Design decisions — credential stuffing poster

- Canvas: 842×1191 viewBox (A3 portrait at 72 dpi points), so pt-equivalent sizes map directly to print.
- Dark navy ground (#0A1120) with a semantic colour code: red = attack, amber = why-it-works/risk,
  cyan/green = defence (detect/prevent), amber = respond. One gradient bar ties them together at the top.
- Hierarchy for 2 m readability: stacked 64 pt title, 34–42 pt stat numerals, 21 pt section heads,
  14.5 pt step titles; body copy never below 10.5 pt and is meant for close reading.
- Narrative structure: 3 headline stats → numbered 5-step attack chain (vertical, dotted connector) →
  "why it works" side panel (one key opening three padlocks) → 3×2 defence card grid tagged
  PREVENT / DETECT / RESPOND → single takeaway banner ("assume every password is already breached").
- Self-contained: no external fonts or assets; system stack 'Helvetica Neue'/Helvetica/Arial only,
  all icons are inline stroke paths in <defs>. Stats are hedged ranges with a source footnote;
  no em dashes in copy per house style.
- Framed as OWASP OAT-008 for conference credibility; no vendor branding (neutral deliverable).

## Verification performed
- Rendered poster.svg in headless Chrome at 2× (1684×2382 PNG) and visually inspected the full page:
  no text overflow, clipping, or element collisions; contrast and hierarchy read correctly at thumbnail size.
- Not done: physical A3 print test, other renderers (Inkscape/Preview/rsvg), or a measured 2 m legibility test;
  font metrics assume Helvetica/Arial is present (true on macOS/Windows; generic sans fallback elsewhere).
