# Annotated Cases: Principle Transfer in Practice

Three worked cases showing the decision process, not just the outcome. Each follows the pattern: problem, chosen principles, key decisions, rejections, evaluation, lessons.

---

## Case 1: Security-intelligence dashboard

**Problem.** Analysts triage threat findings across thousands of assets. Sessions run hours; the costly failure is a missed critical finding, the chronic failure is fatigue. Stakeholders asked for something that "looks like a SOC in a movie". Deliverable: dashboard design system and layout.

**Chosen principles.**
- *Aerospace instrumentation:* quiet-by-default. In a cockpit, nominal state is visually silent; colour and motion are reserved for deviation. Transferred as: neutral greys for all healthy/informational rows, saturated colour only for warning and critical, no ambient animation anywhere.
- *Aerospace instrumentation:* glanceable primary scan. Instruments cluster by task, not by data source. Transferred as: one fixed triage strip (new criticals, ageing criticals, coverage gaps) always in the same place, so the analyst's first glance is a trained scan, not a search.
- *Swiss typographic hierarchy:* a strict grid and a 4-step type scale carry all hierarchy; severity is encoded by weight, position and one colour channel plus an icon, never by decorative treatment.
- *Scientific visualisation:* marks encode data, nothing else. Asset-to-threat relationships drawn as a force-directed graph with quantitative edge weights; no glows, no radar sweeps.

**Key decisions.** Dark theme accepted, but justified by long-session eye strain and measured contrast (body text 4.9:1), not by genre. Severity uses colour + icon + position (colour-independence). Density is high by design, with an 8px rhythm keeping it scannable: aerospace tolerates density when alignment is disciplined. All timestamps absolute on hover, relative at rest.

**Rejections, and why.** Cockpit theming (bezels, scanlines, warning stripes, HUD fonts): aesthetic borrowing that adds noise to exactly the channel reserved for deviation. Animated globe: decoration consuming the most valuable screen region. Red/green status pair: fails colour-vision deficiency; replaced with red/neutral plus icons.

**Evaluation** (safety-adjacent reweighting: function 30, usability 25, hierarchy 20, feasibility 15, craft 10). Scored 8+ on function and hierarchy in review; the open weakness was originality, deliberately near zero weight. Override check: no usability failures outstanding. Verdict: acceptable.

**Lessons.** The client's "movie SOC" request was a requirement for *credibility*, satisfied by precision and restraint rather than theming. Principle transfer looked like nothing; it read as quality, not as aerospace.

---

## Case 2: Technical conference poster

**Problem.** A1 poster announcing a systems-engineering conference. Must be read in two stages: theme at 5 metres, programme details at arm's length. Audience: engineers who distrust marketing gloss. Deliverable: one poster composition.

**Chosen principles.**
- *Architectural composition:* massing and circulation. The poster is zoned like a building section: one dominant mass (the title block, roughly one third of the sheet), a circulation path (a single vertical datum line the eye travels down), and service zones (dates, venue, sponsors) kept subordinate. Negative space treated as structural, not leftover.
- *Painterly light:* a single implied light direction across the central illustration gives depth and atmosphere; value structure (not hue) separates foreground subject from background field, borrowed from chiaroscuro value planning.
- *Aerospace annotation:* programme details rendered as a callout system, leader lines with consistent elbow angles, one label grammar (code, title, time), hairline weights exactly half the illustration's stroke weight.

**Key decisions.** Two reading distances made explicit in the type scale: 180pt title, 14pt annotations, almost nothing between, so the hierarchy has no mud in the middle. Palette limited to two inks plus paper, keeping the painterly lighting a matter of value, which also survives cheap reproduction. The annotation grammar was tested by rendering at 25% (simulating 5m viewing): annotations correctly disappear into texture, title holds.

**Rejections, and why.** Full-bleed photographic background: would collapse the value structure that carries depth. Blueprint-blue cliché: aesthetic borrowing signalling "technical" while reducing contrast range. A third accent colour: the two-stage reading needed no third voice.

**Evaluation** (expressive reweighting: originality 30, composition 25, context 15, craft 15, function 10, accessibility 5). Strongest on composition; the honest critique noted originality at 7: the annotation language is distinctive, the title treatment is safe. Accepted trade-off: the audience rewards restraint.

**Lessons.** Three influences stayed coherent because each owned a different layer: architecture owned structure, painting owned depth, aerospace owned detail. Conflicts only arise when two influences compete for the same layer.

---

## Case 3: Watch-inspired interface icon system

**Problem.** 24 interface icons for a precision-positioning product, rendered at 16-24px. The brand word was "instrument-grade". Deliverable: icon grid rules plus the set.

**Chosen principles.**
- *Horological proportion:* a dial's legibility comes from fixed proportional relationships (hand widths to dial diameter, index length to chapter ring). Transferred as a 24px grid with locked ratios: 2px stroke everywhere, interior gaps never below 2px, key forms sized to a 20px live area with a 2px optical margin.
- *Horological finishing:* on a watch, every chamfer is deliberate and consistent across the piece. Transferred as terminal discipline: all stroke ends either squared or rounded, chosen once (rounded), applied to all 24 icons; all corner radii from a 2-value set.
- *Optical alignment over mathematical:* circular icons drawn 1px over the square ones' bounding box, as circular dial elements are, so they read as the same size.

**Key decisions.** Pixel-grid snapping at 16px verified by rendering each icon at 16px on light and dark and inspecting for half-pixel blur. Metaphors kept conventional (gear, pin, layers): precision was expressed in execution, not invention. One accent state (active) by colour swap only; geometry never changes between states, as a dial never rearranges.

**Rejections, and why.** Decorative watch parts (crowns, lugs, guilloché texture, tick marks as framing): aesthetic borrowing that destroys legibility below 24px and turns an instrument claim into a costume. A 1.5px stroke "for elegance": blurs on 1x displays; elegance that fails rendering is not finishing, it is negligence.

**Evaluation** (craft-weighted: craft 25, function 25, usability 20, consistency within context 15, originality 10, longevity 5). Craft and consistency scored highest after the 16px re-render pass caught four blurred icons. Override check: all icons distinguishable in greyscale.

**Lessons.** Horology contributed no visible watch imagery at all; it contributed the *standard* (locked ratios, one finishing decision applied without exception, optical corrections). That is what principle transfer means: the discipline sets the bar, the medium sets the form.
