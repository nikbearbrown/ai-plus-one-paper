# Chapter specifications

**Private Blueprint only. Draft route: `hold-source`. Evidence: `tentative-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. The difference that matters

- **Observable capability:** Distinguish semantic drift from formatting noise
- **Teaching blocks:** desired state; observed state; invariants; evidence
- **Original worked example to write:** Two intentionally reordered configurations represent the same synthetic teaching-room inventory.
- **Assessable practice:** Write a comparison table and isolate the only functional difference.

## 2. Will the second run do anything?

- **Observable capability:** Determine whether a fixture transformation is idempotent
- **Teaching blocks:** plan and apply distinction; state convergence; retries; edge cases
- **Original worked example to write:** Two fictional automations label demo machines, one duplicating the label after every run.
- **Assessable practice:** Trace first and second runs and propose a test that fails the duplicate behavior.

## 3. Review the change before applying

- **Observable capability:** Construct a human review packet for a state change
- **Teaching blocks:** scope; staged rollout; test oracle; approval
- **Original worked example to write:** A fictional campus service wants to change configuration on one cohort before others.
- **Assessable practice:** Define preconditions, a limited proof step, and a measurable stop threshold without executing anything.

## 4. Evidence during rollout

- **Observable capability:** Connect synthetic monitoring signals to one clear continuation or rollback decision
- **Teaching blocks:** preflight tests; event receipts; alerts; state postconditions
- **Original worked example to write:** A mock batch configuration reports success while a read-only fleet snapshot contains one stale member.
- **Assessable practice:** Explain the inconsistency and define which evidence should block the next simulated rollout.

## 5. Recover to a known state

- **Observable capability:** Specify rollback and audit a change record
- **Teaching blocks:** rollback vs roll-forward; checkpoints; unknowns; evidence receipts
- **Original worked example to write:** A synthetic receipt shows half of a teaching fleet updated before a failure.
- **Assessable practice:** Produce a recovery decision and write a peer-verifiable verification checklist.
