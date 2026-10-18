# Meridian: Design Decisions

## The two styles
1. **Swiss / International Typographic Style**: strict grid with exposed hairline rules, huge uppercase
   Helvetica-stack headlines, flat off-white/near-black/signal-red palette, numbered sections, no ornament.
2. **Technical instrument / blueprint aesthetic**: monospaced metadata (FIG. numbers, bearings, UTC
   timestamps, confidence scores), registration-mark corners, graph-paper panels, and hand-built SVG
   instruments (perimeter radar, attribution graph, exposure ladder, drift log) instead of stock art.

## Why they cohere
Both are grid-first, functional, and anti-decorative, so they share one skeleton: Swiss sets the macro
layer (layout, headline scale, color discipline); the instrument style fills the micro layer (annotations,
diagrams, data chrome). One red does double duty, poster accent and "threat" semantic, binding the two
registers. The pairing argues the product: Swiss order is the clarity delivered, readouts the telemetry.

## Verification performed
Rendered in headless Chrome at 1440px (full page + hero close-up) and at true 390px/320px via an iframe
harness (Chrome's ~485px minimum window first faked a mobile overflow); fixed a clipped SVG label and mobile
headline size from screenshots; confirmed scrollWidth equals viewport at 390/320 and zero external URLs.
Not tested: Safari/Firefox, real devices, screen readers.
