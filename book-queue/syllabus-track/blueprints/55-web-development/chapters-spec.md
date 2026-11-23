# Chapter specifications

**Private Blueprint only. Draft route: `compare-scope`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. The browser still needs a document

- **Observable capability:** Create an operable sketch before styling it
- **Teaching blocks:** semantic structure; forms; navigation; adaptive layout
- **Original worked example to write:** A campus repair café page needs a workshop filter and booking intent form.
- **Assessable practice:** Write and keyboard-test a compact form with labels and a clear error location.

## 2. Where state lives

- **Observable capability:** Explain the state owning each part of a browser interaction
- **Teaching blocks:** local vs shared state; rendering; events; pending status
- **Original worked example to write:** A workshop filter is reset when a registration is saved.
- **Assessable practice:** Draw the state ownership table and define when filtering should or should not persist.

## 3. Design a truthful request boundary

- **Observable capability:** Specify successful and unsuccessful mutation contracts
- **Teaching blocks:** HTTP request roles; validation; response semantics; retry behavior
- **Original worked example to write:** A fictional attendee submits an already-full session request.
- **Assessable practice:** Produce a request/response contract and expected UI outcomes for three fixtures.

## 4. Persist and reconcile

- **Observable capability:** Verify data survives a refresh with consistent expected behavior
- **Teaching blocks:** records; identity and schema; server truth; repeated submission
- **Original worked example to write:** A booking is shown as pending after a simulated timeout.
- **Assessable practice:** Write a deterministic test that distinguishes unknown result from rejection and prevents duplicate display.

## 5. Release a small vertical slice

- **Observable capability:** Defend evidence that the feature works across boundaries
- **Teaching blocks:** accessibility; test coverage; deployment isolation; evidence receipts
- **Original worked example to write:** A mock repair café needs an enrollment demo without real accounts.
- **Assessable practice:** Submit a browser-to-store trace and three verified failure cases; distinguish demonstration from production readiness.
