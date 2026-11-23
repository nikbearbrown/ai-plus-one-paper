# Chapter specifications

**Private Blueprint only. Draft route: `ready-for-draft-review`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Partial Failure from the Client’s View

- **Observable capability:** Trace retries under delayed outcomes.
- **Teaching blocks:** timeouts; partial failure; delivery vs execution
- **Original worked example to write:** A reservation reaches a server twice after a delayed reply.
- **Assessable practice:** Mark which observations do and do not prove a reservation exists.

## 2. Ordering Without a Shared Clock

- **Observable capability:** Draw causal edges for a concurrent history.
- **Teaching blocks:** local sequence; send and receive; causal order
- **Original worked example to write:** Two kiosks update different inventory records while a relay waits.
- **Assessable practice:** Construct two valid event orders and explain which edges constrain both.

## 3. Replication and Visible History

- **Observable capability:** Compare permitted reads under a stated contract.
- **Teaching blocks:** replicas; visibility; consistency contracts
- **Original worked example to write:** Two copies of a library availability count temporarily disagree.
- **Assessable practice:** Produce one permitted and one forbidden read trace.

## 4. Coordinate Commit Without a Single Local Transaction

- **Observable capability:** Exhibit the effect of delayed participants on an all-or-nothing update.
- **Teaching blocks:** atomic commitment; coordinator decision; participant failure; blocking
- **Original worked example to write:** A fictional makerspace schedules a room and an instructor together.
- **Assessable practice:** Produce two traces with the same successful outcome and one blocking trace; identify the assumption that differs.

## 5. Recovery and Verification

- **Observable capability:** Test a bounded recovery claim reproducibly.
- **Teaching blocks:** deduplication; replay; failure experiments
- **Original worked example to write:** A toy ticket service restarts after saving a reservation but before replying.
- **Assessable practice:** Submit a deterministic failure test and a limitation statement.
