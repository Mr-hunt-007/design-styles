# Visual Style Recommendation: Client-Facing Wealth Dashboard, Regulated Private Bank

## The problem before any style word

- **Audience:** high-net-worth clients, broad age range, many 55+, often reviewing on
  iPad or phone alongside an adviser. Not operators; not traders.
- **Purpose:** convey portfolio state, performance and allocation with total clarity,
  and make the bank feel trustworthy, discreet and expensive.
- **Constraints:** regulated environment (WCAG-level accessibility expected by policy,
  figures must be unambiguous, no implied performance theatre), moderate-to-high data
  density, product lifespan of 5-10 years across many teams' hands.
- **Emotional register:** calm authority. Trust first, prestige second, novelty last.

Selection criteria derived: (1) credible to risk-averse wealth clients for a decade,
not a season; (2) carries tables, charts and numerals at real density; (3) WCAG AA
minimum enforceable in tokens; (4) scales across a large org and component library;
(5) still reads as a private bank, not a generic SaaS admin panel.

## Choice

**Primary: Corporate Swiss.**
**Supporting influence: Luxury Editorial** (one influence only, with a narrow job).

Selection sentence: Corporate Swiss because it is the only candidate that meets all
five criteria — systematic grids, tabular numerals, token-driven semantic colour and
the strongest accessibility posture in the catalogue; Luxury Editorial supports the
one thing Corporate Swiss cannot do, which is signal private-bank prestige, applied
only at the surface level (display serif for headings and large figures, generous
margins, near-absent chrome); rejected styles below.

## Principles behind the choice

1. **Neutrality is the trust signal.** Wealth clients read restraint as competence;
   the content (their money) carries the page, the style stays invisible.
2. **One signature element rescues neutrality from anonymity** (Corporate Swiss's own
   rule): here, the editorial serif on headline figures is the signature. Everything
   else stays in the workhorse grotesque.
3. **Semantic colour reservation**, a principle transferred from Aerospace
   Instrumentation without its costume: red and amber appear only as loss/alert
   semantics, never decoratively, so a red number always means exactly one thing.
4. **Scarcity economics of attention** from Luxury Editorial: fewer, better, bigger.
   One hero figure (total wealth) per view; everything else subordinate.
5. **Longevity over fashion.** The International Style corporate lineage has held
   since the 1960s; a regulated bank cannot rebrand its dashboard every trend cycle.

## Rejected alternatives

1. **Glassmorphism** (the fashionable one). Frosted panels over gradient backdrops
   are everywhere in 2024-26 fintech concepts, and unsuitable here: contrast is
   backdrop-dependent, which is untenable where AA on every figure is a compliance
   requirement, not a preference; its own entry warns against dense text UIs and
   low-end devices; and translucency reads as consumer-app novelty, not fiduciary
   gravity. It would also date the product within one OS cycle.
2. **Dark Luxury.** Tempting for "private bank" — but the catalogue's own avoid-when
   is decisive: dense data on dark grounds is a different craft, daylight utility
   suffers (clients review statements in offices and in sunlight), thin light text
   punishes older and astigmatic eyes, and gold-on-near-black AA is fragile across a
   whole data UI. Right register, wrong medium. A dark *mode* can come later as a
   token theme; it must not be the design's foundation.
3. **Aerospace Instrumentation.** It handles density and semantic colour superbly,
   but its register is legibility under stress for trained operators. Alarm
   hierarchies, zoned panels and mission-control affect would make clients feel
   their wealth is in an emergency room. We take its colour-reservation principle
   (above) and leave the style; adopting it whole would be costume.

(Also excluded as conflicts with the chosen pair: Neo-Brutalism, Memphis, Grunge —
each named as a conflict in the Luxury Editorial or Corporate Swiss entries.)

## Implementation notes

**Typography.**
- Workhorse: one large-range grotesque (Inter-class or the bank's licensed
  equivalent) for all UI, labels, tables; letterspaced small caps for section labels.
- Signature: a refined high-contrast serif for page titles and hero figures only,
  with optical sizing so hairlines never render below their size floor (~28px).
  Never letterspace lowercase; never set the serif at table sizes.
- **All financial figures in tabular lining numerals**, grotesque only, so columns
  align and values scan. Scale: 12/14/16/20/28/40, 8pt-grid line heights.

**Colour.**
- Neutral core: ivory-white ground (not stark #FFF), ink text, two structural greys.
- One brand hue (deep navy or forest) for interactive elements and selected states.
- Semantic set, reserved absolutely: green = gain, red = loss/alert, amber =
  attention; these hues appear nowhere else — no red marketing accents, ever.
- One precious accent (champagne/brass) used almost never: hairline rules, the
  active-tab marker. If it appears more than twice per view, it is being misused.

**Density.**
- Two-tier architecture: overview pages are editorial-sparse (one hero figure,
  3-4 summary cards, vast margins); drill-down pages (holdings, transactions) run
  full Swiss table density with zoning by grouping, never by hiding data a
  regulated client is entitled to see.
- Fixed positions for critical data (total value, as-of timestamp) across all views.
- Show data freshness explicitly ("as of 18 Oct 2026, 16:00 CET"): stale-data
  honesty is both a trust feature and a regulatory expectation.

**Accessibility.**
- WCAG 2.2 AA as a token-level guarantee: every foreground/background pair
  predefined and contrast-tested, including the gain/loss greens and reds and the
  brass accent (the usual failure points). Target AAA on body-size figures.
- Never encode gain/loss by colour alone: pair with +/− signs and directional
  glyphs (colour-blind clients hold portfolios too).
- Full keyboard and screen-reader paths; charts carry data-table equivalents;
  no hover-only disclosures; motion limited to 150-300ms feedback easing and
  disabled under prefers-reduced-motion.
- Minimum 16px body on data screens; the 55+ audience is the median user, not an
  edge case.

**QA gates before ship:** semantic hues appear only as semantics; serif never below
its size floor; AA verified on measured swatches, not assumed; one signature element
and one accent event per view; tabular numerals in every money column.
