# Chapter specifications

**Private Blueprint only. Draft route: `ready-for-draft-review`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. A reading is not yet usable data

- **Observable capability:** Track one measurement across the device and service boundary
- **Teaching blocks:** telemetry; units; time; provenance
- **Original worked example to write:** A simulated greenhouse monitor reports temperature after a battery replacement.
- **Assessable practice:** Specify a message schema with units, observation time, and explicit missing values.

## 2. The network goes away

- **Observable capability:** Design behavior when device connectivity is interrupted
- **Teaching blocks:** buffering; retries; duplicate events; acknowledgments
- **Original worked example to write:** A fictional greenhouse loses connectivity for twelve minutes while values accumulate.
- **Assessable practice:** Trace a reconnect fixture and show how a duplicate reading is prevented from double-counting.

## 3. Manage a device like a lifecycle

- **Observable capability:** Specify onboarding, ownership, replacement, and end-of-life boundaries
- **Teaching blocks:** device identity; configuration version; privacy; maintenance
- **Original worked example to write:** A retired sensor is replaced but the old inventory entry remains active.
- **Assessable practice:** Write a lifecycle decision table and evidence checks for a safe replacement.

## 4. Define the service boundary

- **Observable capability:** Specify a small testable contract between device-side and application-side components
- **Teaching blocks:** schema evolution; adapter behavior; error codes; compatibility fixtures
- **Original worked example to write:** A simulated greenhouse switches controller components and the old service does not recognize a new status field.
- **Assessable practice:** Propose a compatible message change and produce acceptance examples for both versions.

## 5. Test the whole path

- **Observable capability:** Explain evidence for correct end-to-end operation under two failures
- **Teaching blocks:** sensor-to-dashboard map; service contracts; recovery tests; visible staleness
- **Original worked example to write:** All displayed values look valid although a mock field unit is disconnected.
- **Assessable practice:** Submit a trace, status design, and passing/failing recovery cases based on known fixtures.
