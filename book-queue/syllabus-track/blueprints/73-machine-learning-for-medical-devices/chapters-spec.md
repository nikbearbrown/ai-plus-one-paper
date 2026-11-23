# Chapter specifications

**Private Blueprint only. Draft route: `hold-source`. Evidence: `no-usable-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Define an observable model boundary

- **Observable capability:** Draw a verification boundary
- **Teaching blocks:** nonclinical status; input/output contracts; ground truth
- **Original worked example to write:** Synthetic fan-speed status flag
- **Assessable practice:** Identify three testable interface assumptions

## 2. Test predetermined failures

- **Observable capability:** Design a reproducible test suite
- **Teaching blocks:** missing input; malformed fields; fixtures; expected flags
- **Original worked example to write:** Simulated empty status frame
- **Assessable practice:** Write a test that distinguishes an input fault from a scoring fault

## 3. Monitor a threshold offline

- **Observable capability:** Evaluate toy alert behavior
- **Teaching blocks:** drift versus jitter; false alerts; simulated shifts
- **Original worked example to write:** Replay synthetic temperature-status measurements
- **Assessable practice:** Compare two thresholds on the same fixed toy trace

## 4. Make the evidence auditable

- **Observable capability:** Document limits and traceability
- **Teaching blocks:** test receipts; nonclinical environment; ownership
- **Original worked example to write:** Synthetic monitoring review board
- **Assessable practice:** Reconcile one failed test with the requirement and limit the claim
