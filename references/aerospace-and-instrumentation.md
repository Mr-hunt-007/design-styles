# Aerospace Design and Instrumentation

Aerospace design is engineering under consequence: every display, control and label exists because someone needs exact information or exact authority at a specific moment, often under stress. Its lessons travel remarkably well; its authority does not. A dashboard that looks like a spacecraft cockpit is not automatically a good aerospace interface, and is usually a worse software interface.

## Functional hierarchy

- Information is ranked by consequence and frequency: what must be seen always, what must be seen on demand, what must interrupt. Nothing earns screen or panel space by being interesting.
- Primary flight information follows fixed positions so scanning is trained into muscle memory; position constancy beats layout novelty every time.
- One glance answers one question: instruments are designed around the question they answer, not the data they contain.

## Human factors

- Design for the degraded human: tired, stressed, task-saturated, interrupted, wearing gloves, in vibration or glare. If it works then, it works.
- Consistency of direction and meaning: up/increase, green/safe conventions are never locally violated, because habits transfer between contexts and will be executed under stress.
- Control-display compatibility: the control sits near, and moves in the same sense as, the thing it controls.
- Guard against both missed alarms and alarm fatigue: an alert that cries wolf trains people to silence it.

## Reliability and fault tolerance

- Assume failure: every indicator can fail, so the system distinguishes "value is zero", "value unknown", and "sensor failed", and shows them differently. A dead gauge must not look like a calm gauge.
- Graceful degradation: when part of the system fails, the remainder keeps presenting a coherent, prioritised picture.
- Failure states are designed with the same care as nominal states, because they are the states that matter most.

## Clear labelling

- Every control and value is labelled with what it is and its units; abbreviations come from a controlled vocabulary, applied identically everywhere.
- Labels state function, not implementation; they survive the stress test of being read aloud over a radio.
- Modes are always indicated: the most dangerous state is the operator believing the system is in a different mode than it is.

## Information density

- Density is not the enemy; undisciplined density is. Expert-facing displays can be dense when layout, grouping and position constancy carry the structure.
- Clutter is removed by ranking, layering and decluttering modes (showing less during critical phases), not by deleting data experts need.

## Instrument legibility

- Legibility is engineered for the worst case: viewing angle, distance, vibration, lighting from darkness to direct sun.
- High-contrast figures, generous stroke weights, unambiguous numerals, and scales designed so the needed precision is readable without interpolation guesswork.
- Colour is a secondary code: meaning survives in monochrome; colour reinforces, never solely carries, a distinction.

## Environmental and material constraints

- Temperature, vacuum, vibration, radiation, mass and power budgets shape every aerospace artefact; mass is paid for in fuel, so everything justifies its weight. The design mindset: every element pays rent.

## Maintainability

- Equipment is designed for inspection and replacement: access, standard fasteners, connectors that cannot be mated incorrectly, documentation that matches the hardware exactly.

## Verification and traceability

- Nothing is assumed to work; it is demonstrated. Requirements trace to tests; changes trace to approvals; documents trace to revisions.
- The design-review culture transfers directly: claims need evidence, and "it looked fine" is not evidence.

## Worked transfer: security operations dashboard

How the principles above reshape a typical SOC or threat-intelligence dashboard, as principle transfer rather than cockpit styling:

- Rank by consequence: active critical incidents hold a fixed, always-visible position; trend charts and inventories live below or behind them. Nothing animated or decorative sits above the severity rank.
- One question per panel: "are we under attack now", "what changed since yesterday", "what needs a human decision" each get their own panel, rather than one chart trying to answer all three.
- Unknown is not zero: unscanned assets, stale feeds and failed collectors render as distinct "no data" states, never as a reassuring green or an empty chart (incomplete enumeration must never be presented as a total).
- Alert philosophy: three severity levels at most, each with a defined response; anything that fires daily without action is demoted by design.
- Position constancy and controlled vocabulary: the same metric keeps its name, unit and location across every view and report.
- Monochrome survival: print the dashboard in greyscale; if severity vanishes, the encoding is colour-only and must be fixed.

## Transferable principles (use these freely)

These improve cybersecurity dashboards, SaaS products, monitoring systems, technical posters, reports and diagrams:

1. **Rank by consequence**: decide what must always be visible, what interrupts, what waits. Severity drives position and weight.
2. **Alert philosophy**: few alert levels, consistently styled, each with a defined operator response; design against alarm fatigue.
3. **Unknown is not zero**: render missing, stale and failed data as distinct states (see also `ui-ux.md`).
4. **Position constancy**: stable layouts that reward the trained eye; do not reshuffle dashboards per release.
5. **Glance legibility**: each panel answers one question at a glance; worst-case contrast and sizing.
6. **Controlled vocabulary**: one name per concept, everywhere, including units.
7. **Meaning survives monochrome**: colour reinforces, never solely encodes.
8. **Graceful degradation**: partial data still presents a coherent, prioritised picture.
9. **Declutter modes**: progressive density rather than deletion of expert detail.
10. **Verification culture**: review the implemented artefact against its requirements; record what was checked.

## Instrumentation-inspired design checklist

1. Can the operator answer the top three questions within one glance each?
2. Is every value labelled with name and unit, from a controlled vocabulary?
3. Do unknown, stale, zero and failed states all look different?
4. Does meaning survive greyscale printing?
5. Are alert levels few, consistent, and each tied to a defined response?
6. Has the layout stayed stable across versions, or does every release reshuffle the trained eye?
7. Under worst-case conditions (small screen, glare, stress, partial data), what breaks first?

## Domain-specific constraints that do NOT transfer

- Certification, airworthiness, human-rating, redundancy architectures and safety cases are regulated engineering processes. Never claim or imply that a design "meets aerospace standards", is "flight-ready" or is safety-validated; this skill can apply aerospace-inspired principles, not aerospace assurance.
- Real instrument conventions (e.g. specific flight-deck layouts and colour codes) are trained standards for certified crews, not a style kit; copying them into consumer software misleads rather than helps.
- Aesthetic borrowing (bezels, warning stripes, fake switch guards, decorative telemetry) is styling, legitimate only when the brief genuinely calls for that identity; it adds noise to real operational tools. State the difference explicitly when a client asks for "cockpit style".
