What This Repository Must NOT Become
====================================

This anti-pattern manifesto defines forbidden directions for the cognitive architecture and sets boundaries for future contributors and autonomous agents.

1. Role collision: blending kernel authority with policy presentation in a single component or persona.
2. Role collision: allowing agent personas to both author and adjudicate kernel truths without separation of concerns.
3. Governance vs decision-making: letting governance artifacts dictate runtime decisions instead of constraining and auditing them.
4. Governance vs decision-making: using policy layers to override or shadow kernel facts rather than to frame visibility and formatting.
5. Testable vs non-testable behavior: introducing behaviors that cannot be validated through deterministic inputs and observable outputs.
6. Testable vs non-testable behavior: coupling emergent heuristics without harnesses that pin them to measurable acceptance criteria.
7. Architecture sprawl: adding cross-cutting features that bypass established layers instead of routing through explicit contracts.
8. Documentation drift: treating architectural contracts as advisory commentary rather than normative specifications enforceable by tests and reviews.

Red line: The core invariant is that the kernel remains the single source of truth, with policy layers only shaping visibility and format, never altering or diluting kernel facts.
