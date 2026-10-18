# Visual Style Recommendation: Client-Facing Wealth Dashboard for a Regulated Private Bank

## The choice

**Primary style: Corporate Swiss** (Swiss-derived enterprise modernism), carried by
**one supporting influence: Luxury Editorial restraint** — its whitespace economics and
typographic finish, applied at the surface level only. The Swiss system owns structure,
data presentation and interaction; the editorial influence owns the emotional register.

## The problem, before any style

- **Audience:** high-net-worth clients, skewing older, often reviewing on iPad or desktop,
  sometimes alongside an advisor. They are not daily power users; they scan for net worth,
  performance, allocation, and anything that needs their attention.
- **Purpose:** sustain trust in an institution that holds their wealth. Every pixel is read
  as a proxy for operational competence.
- **Constraints:** regulatory scrutiny (figures must be unambiguous, gains/losses honestly
  encoded, nothing resembling marketing spin inside statements), accessibility obligations,
  multi-year lifespan across a product family (statements, advisor tools, mobile).
- **Density:** moderate-to-high. This is a data product, not a brochure — but the data is
  personal and emotionally loaded, so it must never feel like a trading terminal.

## Principles behind the selection

1. **Neutrality as trust.** A regulated bank's interface should feel inevitable, not
   designed-at. Grid discipline, a single workhorse typeface, semantic colour and
   predictable page architecture read as institutional competence — the visual equivalent
   of audited books.
2. **Longevity over fashion.** The dashboard will outlive any trend cycle. A rational
   grid-and-token system ages slowly and can be refreshed at the surface without
   re-architecture; a trend-led skin dates the institution with it.
3. **Numbers are the brand.** Portfolio values, performance deltas and allocations are the
   content. The system is built outward from tabular numerals, chart legibility and honest
   encodings — not from mood.
4. **Scarcity signals wealth.** Where a retail bank fills space, a private bank leaves it.
   The editorial influence contributes generous margins, hairline rules, a refined serif
   reserved for display moments (greeting, section titles), and a pace of slow, confident
   transitions. It is seasoning, never structure: it must not reduce the clarity of a
   single figure.
5. **One signature element.** Pure Swiss neutrality risks anonymity. Differentiation is
   concentrated in one place — a distinctive, house-styled data-visualisation language
   (chart geometry, line weights, annotation style) — so identity lives in the data itself.

## Rejected alternatives

1. **Dark Luxury (fashionable, and unsuitable).** The current fintech-premium default:
   near-black grounds, champagne hairlines, chiaroscuro. It flatters marketing pages but
   fails this brief on mechanics: dense numeric data on dark grounds is a specialist craft
   the style does not supply; thin light text on dark punishes older eyes and astigmatism;
   gold-on-charcoal pairs sit chronically near the contrast floor; and daylight use with
   an advisor across a desk is hostile to a dark-first UI. Acceptable later as an opt-in
   dark theme derived from the token system — never as the foundation.
2. **Glassmorphism (fashionable, and unsuitable).** Frosted translucency needs a vivid
   backdrop to exist, and its text contrast is backdrop-dependent — indefensible where the
   content is someone's net worth and the regulator asks why a loss figure was hard to
   read. Blur is also costly on older devices and muddies layered numeric tables. Depth
   effects here would be decoration competing with data.
3. **Aerospace-style instrumentation.** Tempting because it genuinely masters dense data:
   consequence-ranked hierarchy, strict semantic colour, fixed positions for critical
   values. But its emotional register is operator-under-stress — alarm aesthetics applied
   to a client's life savings read as crisis, not stewardship. We reject the costume while
   transferring three of its principles into the Swiss system: red/amber reserved
   exclusively for genuine warnings, key figures in fixed positions across sessions, and
   honest staleness indicators ("prices as of 17:30 CET") instead of silently old data.

Also excluded on register alone: Neo-Brutalism and any playful dimensional style (clay,
soft 3D) — their charm vocabulary contradicts fiduciary gravitas.

## Implementation notes

**Typography.** One workhorse grotesque/humanist sans with a wide weight range and true
tabular lining numerals (non-negotiable: columns of figures must align) for all UI, data
and body text. One high-quality serif for display only — page greeting, section openers —
with a strict size floor (never below ~24px) so hairlines never thin out. Letterspaced
small caps for labels; sentence case everywhere else. Type scale on a modular ratio;
minimum body 16px.

**Colour.** Light, warm-neutral foundation (ivory-tinted greys, not blue-grey clinical).
One deep brand hue (e.g. ink navy or forest) for structure and primary actions. A strictly
semantic set: one gain colour, one loss colour, amber for attention, red reserved for
genuine warnings only — never decorative, and never the brand hue doubling as a semantic.
Gains/losses additionally encoded by sign and direction glyph, never colour alone. All
pairs pre-approved in tokens at AA or better; the precious editorial accent (if any)
appears rarely enough to stay precious.

**Density.** Calm-then-deep layering: an overview that breathes (net worth, performance,
allocation, alerts — one hero figure per zone, generous margins), with density increasing
on drill-down into holdings and transactions, where an 8pt spacing grid and disciplined
tables carry high row counts without crowding. Fixed positions for critical figures across
visits so clients build spatial memory. Grouping by zone, not hiding behind interaction:
nothing financially material lives only in a hover.

**Accessibility.** WCAG 2.2 AA minimum, baked into the tokens rather than audited after.
Text and essential numerals at AA with the loss/gain pairs tested specifically for the
common colour-vision deficiencies; charts double-encode with shape, pattern or position.
Full keyboard operability with visible focus states styled within the system; no
hover-only disclosures. Honour reduced-motion preferences (the slow-fade language degrades
gracefully to instant states). Support 200% zoom and large-text settings without layout
collapse — the demographic reality of the audience makes this a core feature, not
compliance. Every chart ships with a data-table alternative, which also satisfies
statement-style regulatory expectations.

**Motion.** Feedback only: 150–300ms standard easings, slow fades for view changes, no
bounce, no celebration animations on gains. Market movement is not an event to dramatise.

The result should feel like a well-set annual report that happens to be live: quiet,
exact, generous with space, and incapable of ambiguity about a number.
