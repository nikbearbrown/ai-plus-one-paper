# Chapter specifications

**Private Blueprint only. Draft route: `ready-for-draft-review`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Frame obligations before drawing boxes

- **Observable capability:** State how users see correctness and deadlines.
- **Teaching blocks:** goals; workload; failure policy; nonrequirements
- **Original worked example to write:** Translate a civic repair queue request into acceptance scenarios.
- **Assessable practice:** Write normal, overloaded and partial-failure outcomes, including what users are told.

## 2. Size from an explicit workload

- **Observable capability:** Estimate capacity with units, ranges and bottleneck bounds.
- **Teaching blocks:** throughput; latency; high-water marks; storage
- **Original worked example to write:** Size a fictional feed used by differently active campuses.
- **Assessable practice:** Calculate optimistic and conservative budgets and show a sensitive assumption.

## 3. Choose who owns mutable facts

- **Observable capability:** Write data ownership and read/write guarantees.
- **Teaching blocks:** transactions; cache invalidation; eventual reads; contracts
- **Original worked example to write:** Trace request state across a write API and public dashboard.
- **Assessable practice:** Find a stale read that matters and define a better caller contract.

## 4. Design for partial failure

- **Observable capability:** Predict safe behavior from dependency outage and recovery.
- **Teaching blocks:** idempotency; explicit limits; queue replay; observability
- **Original worked example to write:** Simulate retry of a repair request when acknowledgments fail.
- **Assessable practice:** State observable invariants under a failed message and test with a tabletop trace.

## 5. Defend competing architectures

- **Observable capability:** Compare alternatives under the same workloads and failures.
- **Teaching blocks:** bottleneck test; simplicity; costing; revision evidence
- **Original worked example to write:** Compare one SQL service with a distributed queue and read replica.
- **Assessable practice:** Submit a decision memo with arithmetic, reject rationale, and alternate-workload reversal.
