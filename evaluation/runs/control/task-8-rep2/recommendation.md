# Visual Style Recommendation: Client-Facing Wealth Dashboard

**Client:** Regulated private bank
**Surface:** Client-facing wealth dashboard (web, responsive)
**Date:** 2026-10-18

## Recommendation

**Primary style: Swiss / International Typographic Style, applied as quiet editorial minimalism.**
**Supporting influence: classic financial print design (FT / broadsheet market pages) for tabular data and serif display accents.**

The dashboard should read like a beautifully typeset private banking statement that happens to be
interactive, not like a fintech app that happens to show a portfolio.

## Principles behind the choice

1. **Trust is conveyed by restraint.** High-net-worth clients equate visual noise with salesmanship.
   A grid-driven, typography-first layout with generous whitespace signals institutional permanence.
2. **Numbers are the interface.** Swiss design subordinates decoration to information hierarchy,
   which is exactly right when the core content is balances, allocations, and performance deltas.
3. **Neutrality ages well.** A commissioned platform for a regulated bank will live 7 to 10 years.
   Swiss modernism is the lowest-churn style in digital product design; it will not look dated at refresh.
4. **Regulatory fit.** Disclosures, footnotes, and risk warnings must be legible and visually
   first-class, not bolted on. An editorial system treats small print as a designed element.
5. **The print influence adds warmth without risk.** A serif used only for display headings and
   section titles (over a sans workhorse) borrows the authority of financial journalism and
   softens the clinical edge of pure Swiss layouts.

## Rejected alternatives

1. **Glassmorphism / neo-fintech dark gradients (fashionable but unsuitable).**
   The Robinhood-adjacent look of translucent cards, glows, and vibrant gradients reads as
   consumer trading, which is the opposite of discretionary wealth management. Blur and low-opacity
   layers also fail WCAG contrast on dense numeric tables, and the style is already dating quickly;
   it would force a redesign mid-contract.
2. **Skeuomorphic luxury (marble textures, gold foil, serif-everything).**
   Attempts to signal "private bank" literally. It inflates page weight, collapses at data density
   (gold-on-cream numerals are illegible), and dark-gold palettes rarely clear 4.5:1 contrast.
   Luxury in 2026 is communicated through typography and space, not ornament.
3. **Material Design (or any stock component-library look).**
   Safe and accessible, but visually generic: the bank's dashboard would be indistinguishable from
   an internal admin tool. Elevation shadows and FABs carry Android product connotations, and the
   opinionated motion system fights the calm, static confidence this audience expects.

## Implementation notes

### Typography
- **Workhorse sans:** a neutral grotesque (e.g. Neue Haas Grotesk, Suisse Int'l, or Inter as the
  budget option) for all UI, labels, and body copy. Two weights only: Regular and Medium.
- **Display serif (supporting influence):** a Financier/Tiempos-class serif for page titles and
  section headers only. Never for numerals or UI controls.
- **Numerals:** always tabular lining figures (`font-variant-numeric: tabular-nums`) in tables,
  KPIs, and anything that aligns vertically.
- Scale: 4 to 5 steps maximum (e.g. 13 / 15 / 18 / 24 / 34 px). Body minimum 15px.
  Disclosure text no smaller than 12px and never in a lighter grey than secondary text.

### Colour
- Base: warm off-white paper tone (#FAF9F6-range) in light mode; deep charcoal, not black, in dark mode.
- Ink: near-black text (#1A1A1A-range), one secondary grey. Resist multi-grey soup.
- One brand accent (deep green, navy, or burgundy per the bank's identity), used sparingly:
  links, active states, primary action.
- Semantic pair for gains/losses: desaturated green and red chosen to remain distinguishable
  under deuteranopia; always pair with a sign (+/−) or arrow, never colour alone.
- Charts: one sequential ramp of the accent plus greys; avoid rainbow categorical palettes.

### Density
- Default to **comfortable editorial density** on the overview (one clear hierarchy: total wealth,
  then allocation, then movement), and **high density** on holdings/transactions tables
  (32 to 36px rows, hairline dividers, no zebra striping).
- Offer a user-controlled compact/comfortable toggle on tables rather than guessing.
- Hard grid: 12 columns, 8px spacing scale, max content width around 1280 to 1440px so line
  lengths and tables stay scannable on large monitors.

### Accessibility
- WCAG 2.2 AA minimum; target AAA (7:1) for all numeric values and disclosures, since the
  audience skews older and the content is consequential.
- Full keyboard operability and visible focus rings (2px accent outline, never suppressed).
- Charts: every visualisation backed by an accessible table alternative; no information encoded
  in colour alone; respect `prefers-reduced-motion` (motion should be near-zero anyway: fades
  and 150 to 200ms easing only, no celebratory animation on portfolio gains).
- Text resizing to 200% without loss of function; test tables at that zoom explicitly.
- Dark mode is a first-class theme with its own validated contrast pairs, not an inversion filter.

## One-line summary

Swiss typographic minimalism with a financial-print serif accent: the quietest style in the room,
which for a private bank is precisely the point.
