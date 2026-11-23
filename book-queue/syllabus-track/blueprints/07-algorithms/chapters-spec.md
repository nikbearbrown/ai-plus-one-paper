# Chapter specifications

**Private Blueprint only. Draft route: `existing-book`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Write the contract and count the work

- **Observable capability:** Separate correct output, invariants and cost claims.
- **Teaching blocks:** input promises; invariants; asymptotic bounds; arrays and priority queues
- **Original worked example to write:** Compare min-pair finding at two dataset sizes with known operation counts.
- **Assessable practice:** Give a bound and a trace that would falsify the implementation’s claim.

## 2. Represent reachability and cost

- **Observable capability:** Choose a representation and frontier policy from constraints.
- **Teaching blocks:** adjacency; BFS/DFS; Dijkstra; edge-weight assumptions
- **Original worked example to write:** Route fictional library book transfers with weighted stair/elevator links.
- **Assessable practice:** Hand-compute a case where fewest edges is not cheapest and explain the algorithm change.

## 3. Earn the greedy choice

- **Observable capability:** Establish invariant or exchange conditions and repair a false one.
- **Teaching blocks:** interval scheduling; tie cases; cut ideas; counterexample
- **Original worked example to write:** Schedule shared rehearsal-room requests with different overlaps.
- **Assessable practice:** Prove earliest-finish choice on a new fixture; break earliest-start with a minimal graph-free case.

## 4. Combine solutions across subproblems

- **Observable capability:** Select divide-and-conquer or DP and justify recurrence.
- **Teaching blocks:** sorting and merge; recurrences; overlapping states; DP reconstruction
- **Original worked example to write:** Compare independent runs of a merge-based count with a small constrained route dynamic program.
- **Assessable practice:** Solve the recurrence for the split and reconstruct the DP result using a hidden tie case.

## 5. Explain why a choice is hard

- **Observable capability:** Use a reduction to separate model change from implementation change.
- **Teaching blocks:** decision counterpart; reduction direction; verification; optional approximation boundary
- **Original worked example to write:** Turn a fictional club conflict-selection problem into a graph encoding.
- **Assessable practice:** Map a tiny instance both ways and explain why failing an instance does not prove hardness.

## 6. Benchmark what the proof does not predict

- **Observable capability:** Explain constant factors and memory via reproducible tests, not proof replacement.
- **Teaching blocks:** timing; cache/data shape; peak memory; holdout
- **Original worked example to write:** Compare graph-search frontiers on generated wide and deep structures.
- **Assessable practice:** Submit one proof, independent tests and a capacity recommendation with evidence.
