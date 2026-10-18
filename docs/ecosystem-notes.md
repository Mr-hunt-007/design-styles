# Ecosystem research notes

Researched 2026-10-18 (web search snapshot; links below). These notes exist so public claims about differentiation stay factual and dated. Re-verify before repeating any figure.

## Landscape

- The Agent Skills standard (SKILL.md packages) was created by Anthropic in October 2025 and published as an open standard in December 2025; it is adopted by Claude Code, Codex CLI, Gemini CLI, Cursor, GitHub Copilot and many other agents. One tracker counted ~24,000 repositories containing skill/plugin definitions by mid-2026.
- Large curated lists exist (ComposioHQ awesome-claude-skills, hesreallyhim awesome-claude-code).
- Design-specific skills are plentiful: Anthropic's own frontend-design skill is the common recommendation for UI work; roundups list style packs such as "Frontend Design Pro" (11 aesthetic styles), "Designer Skills" (63 skills) and "Awesome Claude Design" (28+ DESIGN.md files). A dedicated svg-art skill exists in at least one collection (kv0906/cc-skills).
- A published critique of the category (Superdesign review, 2026): design skills are "static SKILL.md rulebooks: they hand your agent a look and a set of rules, and they cannot see your codebase or their own output".

## Where design-styles genuinely differs (verifiable in this repo)

1. **It inspects its own output.** The SVG/visual verification loop (render via headless Chrome, inspect, fix, re-render) is mandatory workflow, not advice; the bundled examples carry a record of defects the loop actually caught.
2. **Measured, pre-registered evaluation.** `evaluation/protocol.md` fixes tasks, rubric and thresholds before runs; `EVALUATION.md` reports control-vs-treatment results including failures. No other design skill found in this research publishes a controlled comparison.
3. **Principle transfer, not style presets.** The catalogue's 64 entries each carry transferable principles and anti-misuse guidance (when NOT to use, common mistakes); the core method moves principles across disciplines instead of applying looks.
4. **Activation discipline.** Ships strictly opt-in with a tested mode switcher, rather than injecting itself into every design request.
5. **Tested structure.** `../tests/validate_skill.py` enforces links, catalogue coverage, SVG integrity and the entrypoint contract on every change.

## What design-styles does not claim

- Not "the first", "the best" or "the most comprehensive": the ecosystem is large and moves fast.
- Not a replacement for Anthropic's frontend-design skill for pure frontend aesthetics; the overlap is partial and the two can coexist (design-styles is broader and opt-in).
- No implementation, documentation or presentation was copied from the projects above; they were surveyed from search summaries for positioning only.

## Sources (accessed 2026-10-18)

- https://code.claude.com/docs/en/skills
- https://github.com/Human-Codex/skills
- https://www.implicator.ai/the-best-github-tools-for-building-claude-code-skills/
- https://superdesign.dev/blog/design-skills-reviewed
- https://www.bitdoze.com/best-ai-skills-for-web-design/
- https://pasqualepillitteri.it/es/news/578/claude-code-skills-design-uiux-guia
- https://fast.io/resources/awesome-claude-skills-directory-2026/
