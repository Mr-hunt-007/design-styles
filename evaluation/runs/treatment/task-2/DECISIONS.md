# Design decisions — credential-stuffing poster

- Style: Swiss/International Typographic as primary (grid-driven poster with real information is its native use), Data-Driven/Infographic as support (Isotype unit chart, finding-first stats, honest ranges). Rejected cyberpunk/neon "hacker" styling: costs legibility at 2 m and credibility with a professional audience.
- Coordinates: viewBox 0 0 842 1191 = A3 portrait at 1 unit = 1 pt, so type sizes read directly as print points; 52 pt margins, 3-column module (235 pt) for the defence cards.
- Hierarchy tuned for distance: 100 pt title and 42-44 pt stats read from ~5 m; 26 pt section heads and 19 pt step titles from ~2 m; 12.5-14 pt body is deliberate close-reading detail (standard poster progressive disclosure).
- Palette: black/white plus one Swiss signal red (#D7261E), used only for meaning — section numbers, the final attack step, the 1-in-100 dot, the strongest defence. Grey is structure, never signal.
- Narrative structure: 01 attack chain (five numbered steps on a connector spine) → 02 why it works (reversed stat band) → 03 defences (six cards, strongest tagged). The 100-dot unit chart makes the 1% hit rate visceral without a dishonest axis.
- Honesty: statistics carry their sources (Google/Harris 2019, Digital Shadows 2022); success rate stated as the published 0.1-2% range; unit chart labelled "illustrative 1% rate" in the footer; MITRE/OWASP/NIST references in the footer.
- No external fonts: system stack Helvetica/Arial via one embedded <style>; text kept live (editable, accessible), role="img" + <title>/<desc> provided.

## Verification performed

- XML validated (python ElementTree); duplicate-ID grep clean.
- Rendered with headless Chrome at 842x1191, 1684x2382, and 421x596; all three renders visually inspected (render_full.png, render_2x.png, render_half.png kept in this directory).
- Fixed after inspection: overlapping footer lines; STRONGEST tag placement.
- Known artifact: at the 421 px thumbnail size Chrome's minimum-font-size clamp enlarges the sub-10 pt tracked footer/kicker strings so they touch the edge; the 1x and 2x renders confirm clean margins at print scale.
- Not verified: physical A3 print output (CMYK shift, dot gain) and colour-blind simulation tooling; the red/black/grey palette never encodes meaning by hue alone (numbers, tags and labels carry it), so risk is low.
