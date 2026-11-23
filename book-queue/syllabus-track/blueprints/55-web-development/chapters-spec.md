# Engentic Web Development (AI Plus One): chapter specifications

**Private Blueprint only. Draft route: `compare-scope`. Evidence: `matched-source`. No sign-off.**

Each chapter revisits one original, fictional repair café booking feature. Agent instructions, acceptance tests, and changes are proposed examples, not syllabus assignments.

## 1. Inspect the repository and make the document operable

- **Observable capability:** Locate the route, component, styles, existing tests, and constraints; describe the baseline before delegating an accessibility fix.
- **Teaching blocks:** Repository orientation and in-scope files; semantic HTML and form labels; responsive CSS; keyboard acceptance checks.
- **Original worked example to write:** The booking-intent form has placeholder text instead of a label. Trace where it is rendered, record the keyboard baseline, and ask for only the markup and associated style change.
- **Assessable practice:** Predict and test focus order, labels, and error focus with and without the patch. Annotate the diff and reject an unrelated dependency update.

## 2. Trace browser state and bound the interaction change

- **Observable capability:** Identify the owner and lifetime of local, shared, and persisted state, then review a patch against explicit transitions.
- **Teaching blocks:** Events and render flow; state ownership; pending and stale responses; focused component diffs.
- **Original worked example to write:** Saving a reservation clears the workshop filter and a late response restores an old selection. Specify which state should persist and give the agent one component or reducer to edit.
- **Assessable practice:** Hand-draw an event/state table. Reproduce a late response with a learner-authored fixture, compare the expected and actual transitions, and explain why a large state refactor is unnecessary.

## 3. Specify the HTTP contract before writing the endpoint

- **Observable capability:** Design observable success and failure cases and constrain the change to a named API boundary.
- **Teaching blocks:** HTTP request and response semantics; server-side validation; safe error handling; contract tests and diff review.
- **Original worked example to write:** A fictional attendee tries to book an already-full workshop. Design distinguishable outcomes for malformed input and a valid request denied for capacity, with no change to records in either case.
- **Assessable practice:** Draft three cases before the agent sees the task. Inspect the endpoint-only diff, then send the requests independently and check both the response and intended UI outcome.

## 4. Test persistence when the result is uncertain

- **Observable capability:** Show that a refresh and a retry cannot invent or duplicate a booking; defer a change if the data contract is unclear.
- **Teaching blocks:** Record identity and schema; server source of truth; transaction or uniqueness boundary; reconciliation tests.
- **Original worked example to write:** A simulated timeout occurs after a booking is stored. The client must distinguish an unknown outcome from rejection and reconcile against the stored result without creating another record.
- **Assessable practice:** State the invariant in plain language, delegate one named persistence change, review the diff for unwanted migration or schema changes, and use a separately written test to check record count and UI after refresh.

## 5. Verify the vertical slice and retain release control

- **Observable capability:** Produce a reproducible evidence packet and justify a human release or hold decision.
- **Teaching blocks:** End-to-end trace and keyboard review; revision-pinned preview with synthetic data and no live write credentials; regression evidence and cleanup; explicit human release and rollback decision.
- **Original worked example to write:** The local booking flow passes but the isolated preview has an incorrect API configuration. Verify it from a fresh browser, document the blocker, and keep production untouched.
- **Assessable practice:** Review the cumulative diff, then submit an acceptance matrix, browser-to-store trace, one held-out negative case, and preview receipt or documented blocker. Explain what was not tested and who is authorized to release or roll back. A passing preview never triggers production deployment automatically.
