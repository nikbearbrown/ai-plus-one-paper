# Engentic Web Development (AI Plus One): learning architecture

**Private Blueprint only. Draft route: `compare-scope`. Evidence: `matched-source`. No sign-off.**

## Proposed measurable outcomes

1. Trace an existing browser-to-store path, identify repository conventions and constraints, and document the baseline before asking an agent to change anything.
2. Write observable acceptance cases for semantic and keyboard access, responsive layout, state transitions, valid HTTP input, and expected failure or recovery.
3. Delegate an edit with allowed files and a stop condition; compare the resulting diff against scope, explain cross-layer effects, and reject unrelated changes.
4. Verify request, response, and persistence behavior independently, including a refresh, a rejection, and an ambiguous retry, using synthetic fixtures.
5. Propose or, where separately authorized in a teaching environment, build an isolated preview from a named revision; record the results and make an explicit human release or hold decision.

## Sequencing and final artifact

Establish what is there in chapters 1–2: inspect the repository, trace document and browser state, and capture an unaided baseline. Build a vertical slice in chapters 3–4: specify the API and data contracts and make the smallest independently testable changes. Apply in chapter 5: review the cumulative diff, test an isolated preview, and defend release or hold with evidence. The final artifact is a fictional repair café booking feature plus its constraint map, acceptance matrix, scoped task records, annotated diff, test results, and preview or explicit preview blocker.

## Assessment and AI Plus One practice

Write the baseline and predicted outcomes before consulting the agent. Assess semantic keyboard use, correct state and stored records, negative cases, controlled edits, and the link from each acceptance criterion to independently inspected evidence. Use a learner-authored held-out case the agent did not see. If a familiar framework test passes but the user-visible behavior fails, the case fails. Document any agent assistance, what the developer rejected, and why. No AI self-report, green build, or preview URL alone earns a pass. This is a proposed book rubric, not course grading policy.
