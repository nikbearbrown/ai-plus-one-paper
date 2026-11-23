# Chapter specifications

**Private Blueprint only. Draft route: `ready-for-draft-review`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Testable quality claims

- **Observable capability:** Turn broad requirements into measurable acceptance signals.
- **Teaching blocks:** Quality attributes; defects versus failures; risk matrix; acceptance oracles.
- **Original worked example to write:** Specify reliability and recoverability for a library hold queue.
- **Assessable practice:** Convert three ambiguous requirements into checks; justify their risk ordering.

## 2. Partitions and boundary attacks

- **Observable capability:** Choose test inputs using behavioral equivalence.
- **Teaching blocks:** Input classes; threshold boundaries; state transitions; test data privacy.
- **Original worked example to write:** Exercise a discount threshold with cents, refunds, and midnight.
- **Assessable practice:** Produce 12 cases that kill at least three provided boundary mutants.

## 3. Layers and contracts

- **Observable capability:** Place different tests at the cheapest credible layer.
- **Teaching blocks:** Unit, integration and acceptance; test doubles; contract checks; service errors.
- **Original worked example to write:** Check whether a room-booking API rejects conflicting reservations.
- **Assessable practice:** Design checks that distinguish a client bug from an unavailable service.

## 4. Properties, regression and CI

- **Observable capability:** Use invariants and reproducible fixture runs.
- **Teaching blocks:** Property tests; seed tracking; mutation score; flaky test diagnosis.
- **Original worked example to write:** Verify that merging two waitlists cannot silently drop an item.
- **Assessable practice:** Repair a flaky test and write a repeat-run receipt.

## 5. Release evidence and escaped defects

- **Observable capability:** Issue a go/no-go recommendation grounded in defects and residual exposure.
- **Teaching blocks:** Defect lifecycle; test traceability; severity and likelihood; release gate.
- **Original worked example to write:** Decide whether a stubbed payment sandbox supports release of a campus marketplace.
- **Assessable practice:** Write a release recommendation after triaging a hidden regression and missing coverage.
