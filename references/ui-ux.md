# UI/UX Design

Judge an interface by what users accomplish, not by screenshots. A screen is evidence of a design; task completion is the design. Every evaluation and every new design starts from the question: what is the user trying to do, and what stands in the way?

## Information architecture

- Structure follows the user's mental model, not the org chart or the database schema.
- Name things in the user's vocabulary. If a label needs a tooltip to be understood, the label failed.
- Depth vs breadth: shallow hierarchies with clear scent beat deep "tidy" trees. Users follow trails, they do not read maps.
- Every screen should answer: where am I, what can I do here, where can I go next.
- Search is not an excuse for bad structure; it is a parallel path for users who already know the name of the thing.

## User journeys and task completion

- Design the journey before the screens: entry point, steps, decisions, exits, failure branches.
- Measure success as task completion: did the user achieve the outcome, in how many steps, with how many errors and how much hesitation.
- Identify the one primary task per screen. Everything else is secondary and must look secondary.
- Shorten the happy path first. Then make the unhappy paths survivable: undo, retry, save progress.
- Journeys cross sessions and devices. State the user built up must survive both.

## Cognitive load

- Each element on screen rents attention. Charge it rent: does it help the current task?
- Recognition beats recall: show options, previous choices, defaults, examples.
- Progressive disclosure: reveal complexity when the task requires it, not before.
- Consistency reduces load; every novel pattern is a tax. Spend novelty only where it buys real value.
- Group by meaning (proximity, alignment, shared containers), not by decoration.

## Visual hierarchy

- Hierarchy is the order in which the eye should visit things. Decide that order explicitly, then enforce it with size, weight, contrast, position and whitespace.
- One focal point per view. Two equal focal points means none.
- If everything is bold, highlighted or coloured, nothing is. Reserve the strongest treatments for the rarest, most important states.
- Test: squint or blur the screen. The remaining shapes should still tell the right story.

## Affordances and feedback

- Interactive elements must look interactive; non-interactive elements must not. Ambiguity here is a defect, not a style choice.
- Every action gets a reaction within ~100 ms, even if it is only an acknowledging state change.
- Feedback must say what happened, where, and what to do next if anything.
- System status is always visible for long operations: progress, remaining work, cancellation.

## Interaction states

Every component ships with all of its states designed, not just the resting one:

- Default, hover, focus, active, disabled, selected.
- Empty: the first-run screen is a teaching moment, not a blank table. Say what will appear here and how to create it.
- Loading: skeletons or progress, preserving layout so content does not jump.
- Success: confirm the outcome in the user's terms, offer the natural next step.
- Failure: say what failed, why if known, what the user can do, and preserve their input. Never dead-end.
- Partial data, stale data, permission-denied and offline are states too. Unknown is not the same as zero or clean; render it as unknown.

## Accessibility

- Accessibility is a requirement of the design, not a retrofit. See `accessibility-and-quality.md` for the full checklist.
- Minimums that are never negotiable: keyboard operability for every action, visible focus, text contrast at or above WCAG AA, meaning never carried by colour alone, touch targets large enough to hit, reduced-motion respected.
- Screen-reader order must follow visual order; labels must describe purpose, not appearance.

## Responsive behaviour

- Design the content's priority order first; breakpoints merely re-flow that order.
- Test the extremes: narrowest supported width, longest realistic strings, largest font settings, slowest network.
- Touch and pointer are different instruments: hover-only affordances must have touch equivalents.

## Error prevention and recovery

- Prevent before you apologise: constraints, sensible defaults, confirmation only for destructive or irreversible actions.
- Validate early, inline, and in human language. Point at the field, keep the user's input.
- Destructive actions: undo beats confirm. If undo is impossible, make the confirmation describe the consequence, not just repeat the verb.
- Autosave anything a user would be upset to lose.

## Design systems and component reuse

- A design system is a set of decisions made once: tokens (colour, type, spacing, radius, elevation), components with all states, and usage rules.
- Reuse is a hierarchy: token before component before pattern before new invention.
- A component used for an unintended purpose will be redesigned by its misuse. Document intent, not just appearance.
- Excessive uniformity removes character; the system should define where expression is allowed (illustration, hero areas, empty states) and where it is not (forms, tables, alerts).

## Performance and implementation quality

- Perceived speed is part of the design: optimistic UI, skeletons, cached last-known-good data labelled as such.
- Layout shift, jank and late-loading fonts are design defects, not engineering trivia.
- The implemented interface is the real design. Audit the build, not the mock-up.

## Practical audit checklist

1. State the primary task of the screen in one sentence. Can a new user find and complete it unaided?
2. Walk the happy path counting steps, inputs and decisions. What can be removed?
3. Trigger every failure you can: bad input, no network, no permission, empty data, huge data. Is each state designed?
4. Tab through the entire screen. Is focus visible, ordered, and able to reach every action?
5. Check contrast on real backgrounds, including text over images and disabled states.
6. Blur test: does hierarchy survive? Is there exactly one focal point?
7. Look for meaning carried only by colour, hover-only affordances, and unlabelled icons.
8. Resize to the narrowest width and inflate text size. What breaks?
9. Check consistency against the system: tokens, spacing rhythm, component variants, label vocabulary.
10. Read every error message aloud. Does each say what happened and what to do?
11. Measure or estimate load behaviour: what does the user see at 0.5 s, 2 s, 10 s?
12. List the three highest-impact fixes, separating defects from preferences.

## Transferable principles

- Task-first evaluation applies to any artefact with a reader: a poster, a report and a dashboard all have a "primary task".
- One focal point per view, and hierarchy as a deliberate eye-path, transfer to posters, slides, documents and diagrams.
- State thinking (empty, loading, error, partial) transfers to data visualisation and reporting: unknown must look different from zero.
- Progressive disclosure structures long documents and technical manuals as well as apps.
- Token thinking (decide once, reuse everywhere) is the basis of every coherent visual system, print or digital.

## Domain-specific constraints that do NOT transfer

- Interactivity conventions (hover, focus, tap targets) have no meaning in static media; do not "design states" for a poster.
- Web performance tactics (lazy loading, skeletons) are irrelevant to print and can be misapplied as decoration.
- A/B-test-driven iteration assumes live traffic; one-off artefacts need judgement, not experiments.
