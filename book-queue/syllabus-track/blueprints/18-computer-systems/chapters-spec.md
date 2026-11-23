# Chapter specifications

**Private Blueprint only. Draft route: `ready-for-draft-review`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Bits and Machine Instructions

- **Observable capability:** Predict the result of an arithmetic and branch sequence.
- **Teaching blocks:** number representation; instruction effects; controls
- **Original worked example to write:** A temperature buffer uses a signed value that overflows its range.
- **Assessable practice:** Predict a trace then correct the representation.

## 2. Memory and Layout

- **Observable capability:** Account for observed addresses and storage lifetimes.
- **Teaching blocks:** regions; layout; addressing; lifetime
- **Original worked example to write:** A toy image loader stores pixels and loop variables in different regions.
- **Assessable practice:** Draw a timeline and explain one lifetime error in a supplied trace.

## 3. Processes and Resource Boundaries

- **Observable capability:** Describe what changes across a process launch and a file call.
- **Teaching blocks:** process abstraction; system calls; descriptors; scheduling
- **Original worked example to write:** Two local programs open a copied text file independently.
- **Assessable practice:** Explain which state is shared and which is not.

## 4. Threads and Shared State

- **Observable capability:** Explain why interleaving changes results and evaluate a synchronization boundary.
- **Teaching blocks:** POSIX thread model; shared data; interleaving; synchronization
- **Original worked example to write:** Two threads update different counters but report one aggregate.
- **Assessable practice:** Predict two interleavings and test a corrected design for the given invariant.

## 5. Measure Before Optimizing

- **Observable capability:** Choose observations that support or challenge a local diagnosis.
- **Teaching blocks:** baseline; elapsed time; memory access; experiment control
- **Original worked example to write:** Two traversals of the same toy array display different runtime.
- **Assessable practice:** Write a reproducible comparison and note what it cannot prove.
