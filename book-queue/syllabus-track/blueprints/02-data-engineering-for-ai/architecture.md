# Learning architecture

**Private Blueprint only. Draft route: `compare-scope`. Evidence: `matched-source`. No sign-off.**

## Proposed measurable outcomes

- Define completeness and event-time invariants for a feed
- Build idempotent ingestion with traceable failures
- Write a point-in-time join that prevents leakage
- Build a small evidence index whose refreshes retain identity and enforce a freshness rule

## Sequencing and final artifact

Establish contracts and raw lineage; build point-in-time transforms, replay and versioned evidence indexes; apply a cost-limited release exercise contrasting correct, stale and withdrawn inputs.

## Assessment and AI Plus One practice

Submit invariant tests and replay diff first unaided; later use optional AI to suggest corrupt cases, then implement independent checks. Grade correctness, time leakage, reproducibility and tradeoff explanation; a held-back feed change tests transfer.

Require a first attempt without AI; document any bounded AI assistance and independently check consequential outputs against evidence. These are original assessment recommendations, not institutional assignments or grading policy.
