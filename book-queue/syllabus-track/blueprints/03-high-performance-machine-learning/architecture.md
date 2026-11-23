# Learning architecture

**Private Blueprint only. Draft route: `ready-for-draft-review`. Evidence: `matched-source`. No sign-off.**

## Proposed measurable outcomes

- Measure runtime and memory for an equivalent baseline
- Predict when vectorization or parallelism reduces elapsed time
- Explain synchronization, movement and workload shape overhead
- Test correctness and scaling limits under a recorded benchmark

## Sequencing and final artifact

Establish measurement with fixed seeded inputs; build CPU/vector and accelerator examples where available; apply a budgeted pipeline benchmark with stand-ins when hardware is unavailable.

## Assessment and AI Plus One practice

Predict bottlenecks unaided, benchmark original serial and proposed layouts, and compare tolerance-bound outputs; optional AI suggests bottlenecks only after prediction. Grade measurement controls, correctness, reproducibility and explanation, not raw speed.

Require a first attempt without AI; document any bounded AI assistance and independently check consequential outputs against evidence. These are original assessment recommendations, not institutional assignments or grading policy.
