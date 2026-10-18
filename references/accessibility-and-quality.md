# Accessibility and Quality Validation

Measurable gates for design deliverables. These are requirements, not finishing touches: run them before calling work done, and report honestly which ones actually ran.

## 1. Contrast

Baseline rules (WCAG 2.x AA levels; the standard evolves, so verify the current version when compliance formally matters, and record the date of the check):

- Body text against its background: at least **4.5:1**.
- Large text (roughly 24px regular or 18.5px bold and above): at least **3:1**.
- UI components and meaningful graphics (icons, chart marks, input borders, focus rings): at least **3:1** against adjacent colours.
- Disabled states are exempt, but do not use "disabled-looking" styling for enabled controls.

Compute, do not eyeball. A quick check without tooling:

```bash
python3 -c "
def lum(h):
    r,g,b=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    f=lambda c: c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4
    return 0.2126*f(r)+0.7152*f(g)+0.0722*f(b)
a,b=lum('1A1A2E'),lum('E8E8F0')
print(round((max(a,b)+0.05)/(min(a,b)+0.05),2))"
```

Text over images or gradients: measure against the lightest and darkest region the text can sit on, or add a scrim and measure against that.

## 2. Colour independence

Never encode meaning by colour alone. Severity, status, category and diff markers need a second channel: icon, label, shape, position or pattern. Test by imagining the design in greyscale; if two states become identical, add a channel. This also covers the roughly 1 in 12 male users with red-green colour vision deficiency: red/green pairs need especially careful secondary coding.

## 3. Interaction accessibility (web and app UI)

- **Focus visibility:** every interactive element has a visible focus state, at least 3:1 against both the component and the background. Never `outline: none` without a replacement.
- **Keyboard:** everything a pointer can do, a keyboard can do, in a sensible order. Modals trap and return focus.
- **Target size:** at least 44x44px touch targets (24x24px minimum with spacing for dense desktop UIs); adjacent targets do not overlap hit areas.
- **Reduced motion:** honour `prefers-reduced-motion`; replace large movements with fades or instant changes. Nothing flashes more than three times per second.
- **Semantics:** native elements over ARIA re-creations; headings nest in order; form fields have labels; live regions announce async results; error messages are associated with their fields.

## 4. SVG accessibility

- Meaningful SVG: `role="img"` plus `<title>` (first child) and, where the content is complex, `<desc>` or an adjacent text alternative. Reference them with `aria-labelledby`.
- Decorative SVG: `aria-hidden="true"` and no title, so screen readers skip it.
- Text in SVG stays real `<text>` where practical; outlined text needs an alternative.
- Diagrams that carry data (architecture, attack paths, charts) need the information available as text somewhere: caption, table or structured list. The picture is a view, not the record.
- Interactive SVG elements follow section 3 rules: focusable, labelled, visible focus.

## 5. Quality gates per medium

**Web UI.** Contrast computed for text, components and states. Keyboard walk of the primary flow. Responsive check at 360px, 768px, 1280px minimum, no horizontal scroll at phone width. Empty, loading, error and success states exist. Fonts load with sane fallbacks. Interactive latency: nothing user-triggered takes more than 100ms to acknowledge.

**SVG.** XML parses (`python3 -I -c "import xml.etree.ElementTree as ET,sys; ET.parse(sys.argv[1])" file.svg`). `viewBox` present; no fixed pixel width/height unless intentional. No elements outside the canvas, no accidental clipping, unique IDs, no dangling `url(#...)` references. Rendered and inspected at intended size and at 50%, on light and dark backgrounds when the placement is unknown. Stroke weights survive the smallest expected size. Accessibility per section 4.

**Print and PDF.** Page fits its fixed dimensions with no overflow (probe the rendered page, do not trust the source). Text at least 8pt body, 6pt captions. Colours checked in the output colour space; near-black rich blacks and sub-1pt hairlines flagged for the print process. Links and reading order survive PDF export when the document is digital-first.

**Image-generation output.** The rendered image matches the brief's composition, palette and exclusions. Text inside generated images is checked letter by letter (generators corrupt type). Aspect ratio and resolution match the placement. Any claim of realism or technical accuracy in the image is labelled as illustrative, not validated engineering.

## 6. Honest reporting rule

Every validation report ends with three lists:

1. **Checked:** each gate that ran, and how (tool, command, manual walk, measurement).
2. **Failed and fixed / failed and open:** defects found, their status.
3. **Unverified:** gates that could not run in this environment (no renderer, no device, no screen reader), stated plainly.

Never summarise this as "fully accessible" or "validated". Claims are only as broad as the checks that actually ran. If the environment allowed no visual rendering, say "source inspected; visual rendering unverified".

Related: [design-evaluation.md](design-evaluation.md) for scoring, [svg-and-vector-graphics.md](svg-and-vector-graphics.md) for SVG construction, [../workflows/implementation-verification.md](../workflows/implementation-verification.md) for the full verification procedure.
