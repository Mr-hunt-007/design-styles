# Decisions

Primary task: "which alert do I handle next?" — so the triage queue is the single focal point; every other panel answers exactly one supporting question (am I under attack now / what changed in 24 h / which of the 40 tenants is hot / what is the asset worth).
Direction: instrument-panel functional density, ranked by consequence, with a strict grid; rejected cockpit styling (bezels, fake telemetry add noise) and consumer-dashboard minimalism (hides density experts need).
Severity uses three channels — colour, text label (CRIT/HIGH/MED/LOW), and row edge weight — so meaning survives greyscale; "low" is demoted to a neutral in the trend chart so critical/high dominate the stack.
Unknown is never zero: stale collectors render as hatched "NO DATA" cells and a dedicated status tile ("coverage unknown, not clean"), visually distinct from quiet-green and from counts.
Position constancy: fixed status band (critical, high, unacked >15 min, SLA, collector health) above the fold; queue sorted severity-then-age, not raw recency.
Dark theme on layered neutrals (#0B0F14 page, #10151C panels); tokens on :root; tabular numerals and a mono face for IDs, timestamps, assets; system font stack, zero network dependencies.
All 40 fictional tenants shown as a 5x8 heat grid that filters the queue; queue filters by severity chips and free-text search; selecting a row fills the context rail (detection, MITRE technique, asset tier/owner/exposure/vuln posture, history) with triage actions that mutate state and feed back.
Keyboard: rows are tabbable, arrow-key navigable, Enter selects; all controls are real buttons with visible focus rings; reduced-motion honoured; empty states designed for queue and detail.
Desktop console by intent: min-width 1180px (an analyst tool, not a phone page) — stated trade-off, not an oversight.

Verification performed: contrast computed (WCAG formula) for every text/mark pair including composite badge tints — all text >=4.5:1, marks/borders >=3:1 (worst: 3.4:1 border, 4.86:1 crit badge on selected row); rendered in headless Chrome at 1440x900, 1440x1150 and 1280x860 and visually inspected over two make-verify-critique passes (pass 1 fixed: legend/chart colour mismatch, sub-3:1 chart neutral and axis, ambiguous fleet legend, em dashes in copy); JS confirmed executing (all panels populate in renders).
Not verified: live keyboard/click walkthrough in an interactive browser, screen-reader output, and greyscale print — labels and layout were designed for them but they were not exercised.
