# Visual Style Recommendation — Client-Facing Wealth Dashboard (Regulated Private Bank)

## The Choice

**Primary style: Swiss / International Typographic Style (restrained modernism).**
A grid-first, typography-led interface: generous whitespace, a strict modular grid,
flat surfaces, hairline rules, and data presented as quiet, precise tables and charts
rather than decorated cards.

**Supporting influence (one only): classic financial-print editorial.**
Borrow from the visual language of a well-set annual report or broadsheet markets
page: a serif display face for headings and client-facing narrative, tabular
figures, muted rule-based separation. This supplies warmth and heritage without
compromising the Swiss system's clarity.

## Principles Behind It

1. **Trust is conveyed by restraint.** A private bank's clients are not converted by
   novelty; they are reassured by order. Swiss modernism reads as institutional
   competence: nothing moves, flashes, or sells.
2. **The numbers are the interface.** Portfolio value, allocation, performance, and
   fees must dominate visual hierarchy. Decoration competes with figures; this style
   has essentially none, so the data carries the page.
3. **Longevity over fashion.** A regulated bank cannot re-skin annually. Swiss
   principles have been legible for 70 years and will not date between redesign
   cycles or compliance re-reviews.
4. **Regulatory legibility.** Disclosures, risk warnings, and fee breakdowns must be
   genuinely readable, not visually buried. A typographic system treats legal text
   as first-class content with a defined place in the hierarchy.
5. **Calm under bad news.** Portfolios go down. The interface must present a -8%
   quarter with the same composure as a +8% one: neutral surfaces, sober colour
   semantics, no celebratory or alarmist theatrics.

## Rejected Alternatives

1. **Glassmorphism / dark "fintech-neon" (fashionable but unsuitable).**
   The dominant look of trading apps and crypto dashboards: translucent panels,
   glows, gradient meshes on near-black. Rejected because (a) frosted translucency
   routinely fails WCAG contrast on dense numeric tables, (b) it signals
   speculation and day-trading, the opposite of discretionary wealth stewardship,
   and (c) it dates fast — a compliance-approved UI frozen in 2024's trend reads
   as neglect by 2027.

2. **Neumorphism / soft-UI.**
   Embossed controls depend on low-contrast shadow pairs; affordances (what is a
   button, what is pressed) become ambiguous, and contrast ratios collapse for
   low-vision and older clients — a core private-banking demographic. It is also
   nearly impossible to retrofit to WCAG 2.2 AA without destroying the style.

3. **Playful neobank illustration style (rounded mascots, gamified streaks,
   confetti moments).**
   Effective for mass-market acquisition apps, wrong here: gamification cues around
   investing invite regulatory scrutiny (nudging, inducement rules), and the tone
   trivialises seven-figure portfolios. Clients paying advisory fees expect a
   counterpart to their relationship manager, not a cartoon.

## Implementation Notes

**Typography**
- Display/headings: a quiet transitional or modern serif (e.g. a Financier- or
  Tiempos-class face) at 2–3 sizes only.
- UI and data: one grotesque sans (e.g. a Neue Haas / Inter-class face) with true
  **tabular lining figures** for every number; never proportional figures in tables.
- Scale: small, disciplined ramp (12/14/16/20/28/36). Body ≥ 16px; legal and
  footnote text ≥ 12px and never lower-contrast than AA.

**Colour**
- Base: warm off-white surfaces (#FAFAF7-class), ink-dark text (#1A1D21-class);
  optional client-selectable dark theme built to the same contrast budget.
- One institutional accent (deep green, navy, or burgundy per the bank's identity)
  used for structure and interaction only — never to editorialise performance.
- Semantic pair for gains/losses: desaturated green / desaturated red, always
  accompanied by sign and direction glyphs (+ / −, ▲ / ▼) so colour is never the
  sole carrier (colour-blind safe).
- Charts: a 5-step muted categorical palette; no gradients fills, no glows.

**Density**
- Default to *comfortable-dense*: this audience reads statements, so favour one
  screen showing total value, allocation, performance vs. benchmark, and recent
  activity without scrolling on desktop.
- Offer a user-set density toggle (comfortable / compact) persisted per client;
  compact tightens row height ~25% without shrinking type below 14px.
- Hierarchy by whitespace and rules, not boxes: hairline dividers (1px, ~12%
  opacity ink), card chrome only where grouping is semantically necessary.

**Accessibility**
- WCAG 2.2 AA minimum, AAA for body text contrast where feasible; audit both themes.
- Full keyboard operability and visible focus rings (2px accent outline, offset 2px).
- Charts: every visual carries a data-table equivalent (toggle or screen-reader
  table); ARIA live regions announce portfolio refresh, not animations.
- Respect `prefers-reduced-motion`; all motion is ≤200ms opacity/position easing,
  no parallax, no countup number animations.
- Minimum 24px hit targets; test the serif at small sizes with older-user panels
  (large private-bank client cohort is 55+) — if it fails, headings-only serif.

**Guardrail:** every component proposal should answer one question — *does this make
a number easier to trust?* If not, it does not ship.
