# DECISIONS — recycling.svg

Task: a 960x600 self-contained SVG explaining, to a general audience, how household recycling is sorted at a materials recovery facility (MRF), kerbside bin to baled output, with grouped stages, labelled connectors and two annotated callouts.

Process: iterative (build, render, critique, fix, re-render). No governing design system applies to this piece (it is a neutral public explainer, not a branded asset), so the direction was chosen from the brief.

## Direction

**Primary: technical-manual explainer** (principle transfer from aerospace/technical documentation): numbered stages, one consistent symbol vocabulary, annotation callouts with dashed leader lines ending in a dot on the referenced panel, restrained colour coding where each accent has exactly one meaning. **Supporting: editorial infographic warmth** (paper-tone ground, rounded panels, friendly copy) so it reads as public communication, not an engineering drawing.

Excluded as conflicting: isometric illustration (depth cues cost more legibility than they add at 960x600 with six stages plus two callouts); flat corporate "blob" illustration (decorative, weak at conveying mechanism); skeuomorphic realism (detail density a 230px-wide panel cannot carry).

## Structure

- **S-flow on a 2x3 grid.** Six stage panels (230x148, x = 40/365/690, rows y = 86/364), read left-to-right then right-to-left, following the arrows. The serpentine keeps a six-step process at a comfortable panel size inside 960x600 and creates a middle band that the two callouts legitimately occupy, adjacent to the stages they annotate.
- **Grouped stages.** Each panel is one `<g>`: numbered chip, title, pictogram, two-to-three-line caption. Panel = stage is the grouping the brief asked for; `<g id>` names make the source navigable.
- **Labelled connectors.** Five arrows (one per hand-off), each with a short italic label naming what moves: trucked in, by conveyor, containers move on, non-metals, sorted streams. Labels name the material flow, not the machine, because the audience follows the stuff, not the plant.
- **Callouts in the middle band**, each pointing at the stage where the fact happens: contamination at pre-sort (stage 2), glass at screening (stage 3). Leader = dashed line + terminal dot, visually distinct from solid flow arrows so annotation is never mistaken for flow.

## Visual system

- viewBox 0 0 960 600; coordinates on whole or half units; panels share one geometry.
- **Stroke discipline:** 2px ink for all pictogram geometry, 1.5px for secondary lines (panel borders, motion arcs, leaders), one small-arrow and one flow-arrow marker. Motion is always a dashed grey arc (cardboard off the trommel, eddy-current fling, air-jet eject): one vocabulary, three uses.
- **Palette with roles:** ink #2b3445 (structure/text), paper #f6f4ee (ground), white panels, #e9e4d8 passive fill, amber (#b45309 family) = contamination only, teal (#137a6e family) = glass only. Meaning is never colour-alone: both callouts also carry an icon and a title, glass is also named in stage 3's caption.
- **Type:** system humanist stack (Avenir Next/Segoe UI fallback chain); 23px title, 13.5px stage titles, 11px body, 10.5px connector labels: nothing below ~10.5px at authored size. Text kept editable (no outlines); font-dependency noted as acceptable for a general-audience graphic.
- **Reuse:** conveyor roller and bale defined once in `<defs>` and placed with `<use>`; ids prefixed `rc-` for safe inlining.

## Content decisions (accuracy vs. simplicity)

- Six stages compress a real single-stream MRF honestly: collection, tipping floor + manual pre-sort, size screening (where glass is deliberately broken and drops out), ferrous magnet + eddy current, optical (NIR) sorting with air jets, baling. Fibre screening is folded into "screening" and flagged in the footer caption ("paper and cardboard are screened off alongside the container line; exact machinery varies by facility") rather than claiming a precision the diagram does not draw.
- Contamination callout names the real offenders (food-soiled packaging, bagged recycling, nappies, hoses/film) and the two real consequences: tangles jam screens; one bad load can condemn a bale.
- Glass callout answers the question people actually have (why no glass in the bales): crushed on purpose, falls through as cullet, leaves by a separate route.

## Accessibility

`role="img"` with `aria-labelledby` pointing at `<title>` and a full-sequence `<desc>`; colour paired with icon/label everywhere; smallest text ~10.5px at authored size; callout text measures ≳5:1 contrast on its tinted fills, body text ≳8:1 on white (hex pairs chosen against WCAG thresholds; not instrument-measured).

## Verification log

- XML parses (`python3 -I` ElementTree); no duplicate ids; all `url(#)`/`href` references resolve (grep).
- Rendered headless Chrome at 960x600 (1x), 1920x1200 @2x, and 480x300 (half size); all three rasters inspected.
- Defects found by render and fixed: stage 3 hopper collided with its caption (assembly raised 4-6px); cardboard exit used a detached straight arrow inconsistent with the dashed-arc motion vocabulary (replaced); glass callout icon read as fir trees (redrawn as broken jar + shard).
- Half-size render: structure, titles, numbers, connectors and callout headings legible; 11px body text at 50% is at the legibility floor, acceptable since 960px is the intended minimum display width.
- Unverified: physical print output; screen-reader pass with real AT; exact contrast instrumentation.

## If work continued (top three)

1. Per-material colour keys on the output bales (paper/plastic/metal) tied to a small legend.
2. A subtle tinted band tracing the main material path through all six panels, so the eye can ride the stream itself.
3. Localised variants (bin colours and terminology differ by country; "kerbside" copy is UK-leaning).
