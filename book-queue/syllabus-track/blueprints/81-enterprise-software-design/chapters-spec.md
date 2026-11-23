# Chapter specifications

**Private Blueprint only. Draft route: `hold-source`. Evidence: `no-usable-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Map organizational boundaries

- **Observable capability:** Define services by responsibility
- **Teaching blocks:** actors; bounded contexts; handoffs
- **Original worked example to write:** Synthetic campus purchase approvals
- **Assessable practice:** Propose two boundaries and justify one

## 2. Make integration contracts explicit

- **Observable capability:** Design checkable APIs and data ownership
- **Teaching blocks:** schemas; versions; events; ownership
- **Original worked example to write:** Toy purchase requests and receipts
- **Assessable practice:** Construct a backwards-compatibility fixture

## 3. Reason through failure

- **Observable capability:** Defend a safe recovery behavior
- **Teaching blocks:** timeouts; retries; idempotency; compensation
- **Original worked example to write:** Duplicate mock receipt event
- **Assessable practice:** Show how a test catches double counting

## 4. Review the redesign

- **Observable capability:** Trace a business constraint to architecture
- **Teaching blocks:** decision records; tradeoffs; change reversibility
- **Original worked example to write:** Simulated separate purchasing teams
- **Assessable practice:** Submit a bounded migration decision and checks
