# Design Recommendation: Client-Facing Wealth Dashboard for a Regulated Private Bank

## The Choice

**Primary style: Swiss / International Typographic Style (quiet modernism).**
**Supporting influence: classical financial print (the typographic language of annual
reports and broadsheet finance pages).**

A strict grid, generous whitespace, restrained colour, and typography doing almost all
of the work. The classical-print influence contributes one serif voice for headings and
figures-first table conventions, lending the warmth and gravitas that pure Swiss
minimalism can lack. The product should feel like a well-set private banking statement
that happens to be interactive.

## Principles Behind It

1. **Trust is conveyed by restraint.** Clients with significant assets read visual
   excess as salesmanship. A calm, orderly surface signals institutional permanence.
2. **Numbers are the interface.** Portfolio values, allocations, and performance deltas
   are the content; the style must subordinate chrome to figures. Swiss grid discipline
   and tabular rigour make numbers scan reliably.
3. **Legibility across an older demographic.** Private-bank clients skew 50+. High
   contrast, large comfortable body sizes, and unambiguous hierarchy are non-negotiable.
4. **Regulatory durability.** Disclosures, risk warnings, and audit-relevant figures
   must never be visually buried. A neutral, low-ornament system keeps mandated content
   first-class rather than an afterthought squeezed around decoration.
5. **Longevity over fashion.** The dashboard will live 5-10 years between redesigns.
   Swiss modernism has not dated meaningfully in 60 years; trend styles age in 3.

## Rejected Alternatives

1. **Glassmorphism / dark "neo-fintech" (fashionable but unsuitable).** Frosted panels,
   neon gradients on near-black, and glowing charts are the current consumer-fintech and
   crypto vernacular. Precisely the wrong association for a regulated private bank: it
   reads as speculative trading, not stewardship. Translucency also wrecks contrast
   ratios (text over blurred backgrounds routinely fails WCAG), and dark-first UIs
   perform poorly for printed statements and older eyes in daylight.
2. **Skeuomorphic luxury (leather, gold foil, engraved textures).** Attempts to signal
   "private bank" literally. In practice it renders heavily, dates instantly, clutters
   data views, and its low-contrast gold-on-dark palettes fail accessibility. Wealth is
   better signalled by space and typography than by rendered materials.
3. **Bento-grid dashboard maximalism.** The "everything in rounded tiles, sparkline in
   each" pattern popular in SaaS analytics. It fragments attention across 12+ competing
   cards, implies all metrics are equally important (they are not: net worth and change
   dominate), and invites decorative mini-charts that are too small to read honestly.
   A client reviews a portfolio; they do not operate a NOC.

## Implementation Notes

### Typography
- **Headings and key figures:** a modern transitional serif with strong tabular numerals
  (e.g. Tiempos, Financier, or Source Serif). This is the classical-print influence.
- **Body, labels, and tables:** a neutral grotesque (e.g. Neue Haas Grotesk, Inter, or
  Suisse Int'l). Two families total; no third.
- **Numerals:** tabular lining figures everywhere numbers align (tables, KPIs). Minimum
  16px body, 14px for secondary labels; key portfolio figures 28-40px.
- Weight carries hierarchy, not colour or boxes: regular / medium / semibold only.

### Colour
- **Base:** warm off-white paper (#FAF9F6 range) with near-black ink (#1A1A1A) for a
  light-first product; a dark theme may follow, never lead.
- **One brand accent** (deep green, navy, or burgundy per the bank's identity), used
  sparingly: primary actions, selected states, the line on the main performance chart.
- **Semantic pair for gains/losses:** a desaturated green and a red-brick red, always
  paired with a sign or triangle glyph, never colour alone.
- Charts use a 4-5 step tonal ramp of the accent plus warm greys; no rainbow palettes.

### Density
- Default to a **medium-low density overview**: one dominant figure (total value and
  period change), one primary chart, then allocation and holdings beneath.
- Holdings and transactions get a **dense tabular mode**: tight rows (40-44px), hairline
  rules, right-aligned numerals; density is a deliberate mode, not the default.
- A consistent 8pt spacing system on a 12-column grid; wide margins at desktop widths
  (max content width ~1200px) to preserve the "set page" feel.

### Accessibility
- WCAG 2.2 AA minimum, target AAA for body text and all monetary figures (7:1 contrast).
- Never encode meaning in colour alone (signs, glyphs, and labels accompany red/green);
  verify the palette under deuteranopia and protanopia simulation.
- Full keyboard operability and visible focus states on all interactive elements,
  including chart point inspection; charts expose underlying data as accessible tables.
- Respect `prefers-reduced-motion`; animation is limited to sub-200ms fades regardless.
- Support 200% text zoom without loss of content; test with screen readers on the
  figures-heavy views, where unlabeled numbers are the most common failure.
- Print stylesheet for statements and disclosures: the design's print heritage should
  make paper output excellent, which also serves compliance archiving.

## Summary

Swiss typographic modernism supplies the order, clarity, and neutrality a regulated
institution needs; classical financial print supplies the warmth and authority that
distinguishes a private bank from a brokerage app. Everything fashionable that was
rejected fails on the same three tests: client trust, accessibility, and ten-year
durability.
