# AI-Assisted Software Engineering (AI Plus One)

**Order 59.** Planning only; not authorization to draft.

## Vision

Teach the software engineering lifecycle around AI proposals rather than tool-specific prompt tricks.

**Audience and prerequisites:** Engineers who can use Git and write automated tests.

**Source basis:** Queue lists `nikbearbrown/ai-for-coding-a-practitioners-guide` as primary and `nikbearbrown/Foundational-AI-for-Software-Engineering; nikbearbrown/codex-for-students; nikbearbrown/claude-code-for-students; nikbearbrown/github-copilot-cli-for-students; nikbearbrown/stem-project-review` as related. These are queue leads, not independently reviewed sources for this plan.

## Learning architecture and chapter checks

1. **Frame a small change.** Output: Write acceptance tests and a scoped change request. Check: Show which requests require clarification.
2. **Review an implementation.** Output: Inspect a minimal implementation against tests and code ownership. Check: Find one plausible silent regression in a fixture.
3. **Test and maintain.** Output: Add regression and maintenance checks after simulated requirements drift. Check: Demonstrate that malformed inputs fail safely.
4. **Govern the handoff.** Output: Produce a reviewable patch and explicit operational assumptions. Check: Give a peer enough evidence to repeat the checks.

## Assessed deliverable

A small repository change package with tests, review record, provenance and maintenance notes; compare assisted and independent first passes. Begin independently; log any AI assistance and independently verify its claims and outputs.

## Drafting gate

Verify canonical source and audience; keep distinct from Order 60 only if manual engineering craftsmanship and teams own the main assessment.
