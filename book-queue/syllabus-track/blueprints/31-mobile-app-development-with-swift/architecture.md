# Learning architecture

**Private Blueprint only. Draft route: `hold-source`. Evidence: `matched-source`. No sign-off.**

## Proposed measurable outcomes

- Prototype a mobile task in Figma with reusable states for success, loading, empty and error.
- Hand off the prototype as a language-neutral interaction and state specification.
- Build the same behavior in one chosen stack; explain what the platform handles and what the app must own.
- Demonstrate accessibility, new and restored state, and recovery when the network fails.

## Sequencing and final artifact

Follow a fictional shuttle app from a user task to a Figma prototype, then to one runnable implementation. The final artifacts are an inspectable Figma file, an editable app in the learner’s chosen stack, and reproducible test evidence. Swift/iOS is an optional path alongside Kotlin/Android or a cross-platform implementation. The prototype describes intent; the runnable app proves behavior.

## Assessment and AI Plus One practice

The learner defines state and acceptance cases first. An agent can draft a view or persistence routine in the selected stack, but the learner checks the diff against the Figma handoff and tests the result independently. Apply the same behavior rubric across stacks. Grade accessible interaction, correct state and recovery rather than fidelity to one toolkit.
