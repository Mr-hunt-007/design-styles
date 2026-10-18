# Workflow: Implementation Verification

Confirm that shipped or built design work actually matches its intent, by exercising the real artefact. The counterpart to green-tests complacency: check real output before calling anything done.

**Inputs:** the built artefact (page, app, SVG, PDF, deck, image) and its spec or design intent.
**Outputs:** a pass/fail report per check, defects fixed or logged, an honest unverified list.
**Load:** [../references/accessibility-and-quality.md](../references/accessibility-and-quality.md) (gates per medium), [../references/design-evaluation.md](../references/design-evaluation.md).

## Steps

1. **Render or run the real thing.** The browser for web, headless Chrome screenshots for SVG and print CSS, the PDF itself (not the HTML source) for PDFs, the actual export for decks and images. Never verify from source code alone when a renderer exists.

2. **Compare against the spec, element by element.** Layout, spacing, type sizes, colours, states, content. Differences are findings even when they "look fine": either the implementation or the spec must be corrected so the two agree.

3. **Exercise, not just view** (interactive work): primary flows by pointer and keyboard, resize across breakpoints, trigger loading/empty/error states, test the actual download or export path when one exists (export pipelines introduce their own defects, e.g. effects that rasterise wrongly).

4. **Run the medium's quality gates** from accessibility-and-quality.md section 5: contrast computed, targets measured, page-overflow probed for fixed formats, SVG parse plus render, image text proofread letter by letter.

5. **Spot-check accessibility** beyond the gates: tab through, check focus visibility, confirm meaning survives greyscale, headings and labels make sense read aloud in order.

6. **Fix and re-verify.** Each fix is confirmed in the rendered artefact, not in the diff. A fix that was not re-rendered is unverified by definition.

7. **Report in three lists** (the honest-reporting rule): checked and passed (with method), failed (fixed or open), unverified (and why: missing device, no screen reader, no renderer). Scope every claim to what ran: "verified at 1280px and 360px in Chrome" rather than "fully responsive".

## Gate

Done only when: the real artefact was rendered or run (or impossibility documented); spec and implementation agree or the disagreement is logged; all fixes were re-verified in the output; the three-list report exists. "Tests pass" or "the code looks correct" does not pass this gate.
