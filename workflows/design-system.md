# Workflow: Design System Creation

Create tokens, components, rules and governance that let a team ship coherent design without the original designer present.

**Inputs:** product context, brand direction (or the output of [new-design.md](new-design.md)), target platforms, team constraints.
**Outputs:** token definitions, component specifications with states, usage rules, and a handoff document; optionally a reusable design-system SKILL.md package (step 9).
**Load:** [../references/ui-ux.md](../references/ui-ux.md), [../references/typography-and-graphics.md](../references/typography-and-graphics.md), [../references/accessibility-and-quality.md](../references/accessibility-and-quality.md), [../references/design-leadership.md](../references/design-leadership.md).

## Step 0: Check for an existing system first

Search before creating: an installed brand or design-system skill covering this product, token files (design-tokens, tailwind.config, :root custom properties), styleguide pages, brand guideline documents, component libraries. If one exists, this workflow switches to extending and repairing it; never fork a second system for a brand that already has one. If the existing system is another skill, load it and treat its tokens as the source of truth.

## Steps

1. **Inventory reality.** Audit what exists: every colour, type size, spacing and radius actually in use. Systems built against an imagined product die on contact with the real one.

2. **Define primitives.**
   - Colour: raw palette, then semantic roles (background, surface, text-primary, text-muted, border, accent, success, warning, danger). Components reference roles, never raw values. Check every text/background role pair for contrast now, not later.
   - Type: one scale (e.g. 12/14/16/20/24/32), weights with assigned jobs, line heights per size.
   - Spacing: one base unit (4 or 8px) and a named scale; all layout spacing comes from it.
   - Radii, elevation/shadow levels, motion durations and easings, breakpoints.

3. **Specify components.** For each: anatomy, variants, and all states (default, hover, focus, active, disabled, loading, error, selected). A component spec without focus and error states is incomplete. Define content rules (truncation, overflow, empty).

4. **Write usage rules, with prohibitions.** When to use which variant, and what never to do (e.g. "danger colour never appears in charts as a category hue"). Rules earn their place by preventing a specific observed misuse.

5. **Encode decisions, not pixels.** Every token answers "why": the handoff explains the reasoning so future additions extend the logic instead of copying artefacts.

6. **Plan governance.** Who approves new tokens, how exceptions are recorded, how deprecations roll out, where the single source of truth lives (code, not a drawing tool, when the product is software).

7. **Prove it.** Rebuild 2-3 real screens using only the system. Gaps found here are system defects; fix the system, not the screens.

8. **Hand off.** Deliver tokens in the team's format (CSS custom properties, JSON, platform tokens), component specs, usage rules, and the governance note. Include a "how to extend" section with one worked example.

9. **Optional: package the system as a skill.** When the user wants the system available to future agent sessions, generate a standalone design-system skill the host environment can install (for Claude Code: `<brand>-design-system/SKILL.md` with a frontmatter description naming the brand and its surfaces, plus token/reference files). The skill must contain: the tokens as the single source of truth, the semantic role table, type scale, component shapes, usage rules and prohibitions, voice notes if any, and a short QA checklist; instruct consumers to load tokens from the skill rather than improvising values. Keep it opt-in by description scope (its brand), test that it parses, and tell the user where it was installed. design-styles itself then defers to that skill for this brand (see "Design systems: detect, use, create" in SKILL.md).

## Canonical contents

Whether delivered as a handoff document or packaged as a skill (step 9), a generated design system covers this table of contents. Sections may merge for a small product, but a missing section is a stated decision, never an oversight. Component entries below are the minimum set; the real list comes from the step 1 inventory.

- **Readme**: what the system is for, how to consume the tokens, how to extend it (step 8's worked example lives here).
- **Brand**: iconography rules (grid, stroke, optical corrections), logo usage and clear space, voice and tone.
- **Colours**: brand colours; neutrals; secondary and tertiary accents; semantic colours (roles, not raw values); status palette (success, warning, danger, info); surfaces (background, raised, overlay, with both themes where the product has them).
- **Components**: buttons; inputs; cards and stat tiles; status pills and tags; sidebar or primary navigation; data table; at least one chart treatment (e.g. a donut or bar spec with its palette and label rules). Each with anatomy, variants and full states per step 3.
- **Spacing, radii, shadows**: the spacing scale and base unit; the radius set and what each size means; elevation levels and when each applies.
- **Type**: body and mono faces with fallback stacks; display headline treatment; the heading scale with weights and line heights.

## Gate

Done only when: real screens were rebuilt from the system without ad-hoc values; all text/background role pairs pass contrast; every component spec includes focus, disabled and error states; governance names an owner. A token file alone is not a design system.
