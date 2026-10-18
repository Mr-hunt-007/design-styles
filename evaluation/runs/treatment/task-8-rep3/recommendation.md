# Visual Style Recommendation: Client-Facing Wealth Dashboard, Regulated Private Bank

## The choice

**Primary: Corporate Swiss** (Swiss/International-Typographic clarity industrialised for enterprise trust) —
**with one supporting influence: Luxury Editorial**, applied only at the surface layer (type voice, whitespace,
numeral treatment), never at the structural layer.

In one sentence: a systematic, grid-and-token-driven Swiss foundation carries the data, the regulation and the
longevity; a restrained luxury-editorial accent supplies the private-bank register that pure enterprise
neutrality cannot, each influence doing a named job at a named level.

## Why: the criteria, then the principles

The problem defines the style, so the criteria come first:

1. **Credibility with risk-averse wealthy clients.** Nothing may look experimental, playful or trend-bound.
2. **Dense financial data, calmly presented.** Portfolio values, allocations, performance series and documents
   must scan quickly without reading as a trading terminal.
3. **Regulatory-grade accessibility and auditability.** WCAG AA minimum is a compliance obligation, not taste;
   every figure shown is a statement the bank is accountable for.
4. **Longevity.** A private bank's interface should age in decades, not redesign cycles.
5. **Differentiation within restraint.** It must feel like *this* bank, not any enterprise SaaS.

Corporate Swiss satisfies 1–4 almost by definition: neutral grotesque typography, an 8pt spacing grid,
predictable page architecture, a semantic colour set with accessibility-grade pairs baked into tokens, and
motion only as feedback. Its documented weakness is criterion 5 — neutrality drifts into anonymity. That is
precisely the job of the supporting influence: Luxury Editorial's scarcity economics (fewer, better, bigger;
abundant whitespace; flawless typographic detail as the trust signal) gives the dashboard its private-bank
voice. The influence is strictly budgeted: it may set the display serif on the portfolio headline, the generous
margins, and the quality of the numerals. It may never reduce data contrast, hide controls behind elegance, or
slow a task. Where the two conflict, Swiss wins: structure, legibility and semantics are load-bearing; luxury
is finish.

Two transferred principles complete the system without becoming styles of their own: from data-visualisation
practice, grey carries structure and colour carries meaning, with position/length encodings preferred over
area and angle; from instrumentation practice, alarm-class hues (red, amber, green) are reserved exclusively
for semantic states — a red that sometimes decorates can never again mean "your portfolio fell".

## Rejected alternatives

**1. Glassmorphism (fashionable, and unsuitable — the trend trap).** Layered translucency is the current
premium-fintech costume, and it fails every hard criterion here. Text and figures over translucent panels have
unguaranteed contrast against whatever sits beneath, which is untenable where AA is a compliance floor and the
content is money. Blur effects tax rendering on the mid-range tablets many clients actually use. Most
damningly, it is datable: a dashboard that looks like 2024's trend tells a client the bank chases fashion with
their interface, and invites the question of whether it chases fashion with their capital.

**2. Dark Luxury.** Superficially the obvious "private bank" answer: near-black grounds, champagne hairlines,
chiaroscuro. It is rejected because it is a showroom language, not a working-tool language. Dark premium
grounds suit one hero object per view; a wealth dashboard is daylight utility with dense tables, where thin
light-on-dark text punishes older and astigmatic eyes — a material share of this clientele. Its codes may
survive only in marketing surfaces and print statements, never in the working dashboard.

**3. Neo-Brutalism.** Thick borders, hard offset shadows, candy fills: energetic, cheap to build, and
currently everywhere in indie fintech. Rejected on register: its charm is deliberate rawness and toy-mechanical
play, the exact opposite of fiduciary gravitas, and it handles dense tabular data poorly. It is also already
trend-saturated, failing the longevity criterion twice over.

Also excluded as conflicts with the chosen direction: handwritten/organic warmth cues (imprecision reads as
negligence in custody of money) and cockpit-instrumentation costume (operator-stress aesthetics alarm the very
clients the bank is paid to reassure — we borrow its semantic-colour discipline, not its look).

## Implementation notes

**Typography.** One workhorse grotesque with a broad range (e.g. a neutral sans of the Helvetica/Inter class)
for all UI, labels and tables; body 16px+, line-height ≥1.4. **Tabular lining numerals everywhere money
appears** — figures must align in columns and not jitter on update. The single Luxury Editorial allowance: a
high-quality text serif for the client's name, total-wealth headline and section display heads, at sizes well
above hairline-failure floors. Two families total, fixed roles, no exceptions.

**Colour.** Light, warm-neutral ground (ivory-tinted greys, not pure white); ink-dark text; one brand hue used
sparingly for identity and primary actions; a semantic set in which green/red appear *only* as
positive/negative performance and status — never decoratively. Gains/losses are additionally coded by sign and
icon, never by hue alone. All text/ground pairs are pre-approved AA (AAA for figures) and stored as tokens, so
no screen can compose a failing combination. One precious accent (deep forest or oxblood, not gold gradients)
reserved for rare brand moments.

**Density.** Calm overview, dense detail: the landing view holds few, large, confident numbers with generous
margins (the luxury register); drill-down views may tighten to true tabular density on the 8pt grid, grouped
into zones rather than hidden behind interaction. Line lengths for any prose ≤75 characters. Every chart earns
its ink: honest axes (zero-based or explicitly stated), direct labels over legends, no 3D, no decoration
pretending to be evidence. Data recency is shown ("as of 17:30 CET"); a stale figure is marked stale, never
silently displayed.

**Accessibility.** AA contrast is the floor, AAA targeted for all monetary figures; full keyboard operability
with visible focus states designed in the system's language; real semantic structure (headings, tables with
headers) so screen readers can read a portfolio aloud correctly; charts accompanied by data-table
alternatives; motion limited to 150–300ms feedback transitions with a reduced-motion variant; touch targets
≥44px for the tablet-first client. Test with the actual audience in mind: 60+ eyesight, varying device
quality, high stakes.

**Governance.** The entire direction ships as tokens (colour, space, type, elevation, motion) with the
serif-accent and precious-hue budgets written into the system docs — the restraint must survive a thousand
future hands, because in private banking the consistency *is* the brand.
