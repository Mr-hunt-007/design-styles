# BRIEF: GitHub social preview banner for design-styles

SCOUT · Flagship tier · This brief is the contract for three parallel MUSE directions. 2026-10-18.

## Purpose, audience, context
One image, 1280x640, is the project's face everywhere the repo link travels: GitHub link cards (scaled to roughly 400px wide, corners rounded, glanced at for under two seconds in a feed), and the header of search results. The audience is developers who run AI coding agents, who have seen a wave of "design skill" repos and are rightly skeptical. The banner's job is double: state what the project is (design intelligence for coding agents: it reasons about the problem first and verifies its output by rendering it), and BE the evidence. This banner is a design artifact produced by a design skill; a generic or sloppy banner falsifies the project on sight. It must read instantly at 400px and reward a second look at 1280px.

## Hard constraints (violating any one = rejected, whatever the score)
1. Self-contained SVG, viewBox 0 0 1280 640: no external images, fonts or scripts; text must survive PNG rasterisation on a host without webfonts (system font stack with stated fallbacks, or text outlined to paths). Identical render everywhere.
2. Carries the project name (styled as the repo spells it: `design-styles`) and a one-line value proposition.
3. Honesty: no claim the README does not make. No "best", no superlatives, no invented or rounded metrics, no stars/badges/fake UI chrome implying endorsement. The evaluation verdict is "partially effective"; numbers from it may NOT appear stripped of that context, so the safe move is no numbers at all. No Anthropic/Claude/GitHub logos or trade dress.
4. Legibility floor: project name clearly readable at 400px wide; value proposition readable at 400px or, at minimum, at 640px with the name still carrying the message alone at 400px.
5. Opaque background supplied by the banner itself (no transparency reliance); all critical content inside a 64px safe margin on every edge (link-card cropping and corner rounding).

## Preferences (trade away only for stated reasons)
- Self-demonstrating craft: the banner should visibly embody one of the project's own ideas (problem-first reasoning, the 64-style catalogue, the render-and-verify loop) rather than decorating around them.
- One primary direction per candidate; no style collage. Avoid the AI-slop register: stock gradient meshes, neon glow, glassmorphism chrome, mock terminal screenshots with fake output.
- Should sit comfortably beside both GitHub themes (its own background does the work; test the composition against light and dark page surrounds).
- Tone: confident, exact, a little austere; the README's voice is evidence-over-hype.

## Weighted success criteria (reweighted from references/design-evaluation.md; judge each candidate 1-10 per criterion)
| Criterion | Weight | What it measures here |
|---|---:|---|
| Instant legibility at link-card scale (functional suitability) | 25% | Name + proposition land at ~400px in <2s; hierarchy survives downscaling |
| Originality and differentiation | 20% | Distinguishable from template OSS banners and AI-gradient slop; has a defensible identity |
| Visual hierarchy and composition | 15% | Eye lands name → proposition → supporting form; disciplined use of the 2:1 canvas |
| Craft, precision and consistency | 15% | Spacing rhythm, optical alignment, clean SVG source; 1px faults are findings |
| Message accuracy and brand fit | 10% | Value prop faithful to README; tone matches the project's evidence-first voice |
| Technical robustness | 10% | Rasterises identically without webfonts; sane at 2x; valid, minimal SVG |
| Accessibility | 5% | Text contrast ≥ 4.5:1 against its own background; meaning never by colour alone |

Override rule: an honesty violation or an unreadable name at 400px makes a candidate "not acceptable until fixed", whatever its weighted total. Judges render every candidate at 1280px AND ~400px before scoring; no scoring from source.

## Depth confirmation
Flagship confirmed: this is the project's single public face and direction-defining work. Three parallel MUSE directions, each a genuinely different primary direction (not palette swaps of one idea), each delivered as a rendered comp with a two-line rationale; ROAST/judging collapses to one. Cost justified: the artifact is seen thousands of times and is itself the project's proof of competence; one wrong direction here costs more than two spare explorations.

## Assumptions (no blocking question exists)
- No existing logo, wordmark or design system for this repo was found in README/SKILL; MUSEs may set type freely but must not invent a mascot-style logo that future surfaces would be stuck with.
- The value proposition is drafted by each MUSE from README line 1 territory, e.g. "Design intelligence for AI coding agents" / "Reason first. Render to verify." Any phrasing must pass constraint 3.
- Final deliverable downstream: the winning SVG plus its PNG export at 1280x640; verification loop (render, inspect at both scales, fix) applies before any candidate reaches judging.
