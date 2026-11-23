# Chapter specifications

**Private Blueprint only. Draft route: `ready-for-draft-review`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Transform Records as Values

- **Observable capability:** Write and explain an effect-free typed transformation.
- **Teaching blocks:** expressions; immutability; types; total inputs
- **Original worked example to write:** Normalize fictional bicycle trips into a typed record.
- **Assessable practice:** Hand-compute outputs then test null-equivalent cases.

## 2. Spark Execution and Laziness

- **Observable capability:** Predict which user actions trigger work.
- **Teaching blocks:** transformations/actions; pipeline lineage; partition
- **Original worked example to write:** A trip pipeline filters a season before counting.
- **Assessable practice:** Annotate when data is read and validate input/output equality.

## 3. Aggregation That Combines Safely

- **Observable capability:** Select a mergeable aggregate and reason about partitions.
- **Teaching blocks:** map/reduce; associativity; empties; grouping
- **Original worked example to write:** A service reports regional average ride lengths.
- **Assessable practice:** Expose why averaging partition averages can fail.

## 4. Joins, Shuffles and Skew

- **Observable capability:** Interpret execution evidence and adjust a bottleneck.
- **Teaching blocks:** join shape; shuffle; skew; partition diagnostics
- **Original worked example to write:** A tourist district dominates event volume.
- **Assessable practice:** Compare two strategies on the same fixture and report both time and correctness.

## 5. A Reproducible Pipeline

- **Observable capability:** Deliver trusted outputs with checks and an execution record.
- **Teaching blocks:** schema; validation; repeatability; measurements
- **Original worked example to write:** Daily route snapshots feed a usage summary.
- **Assessable practice:** Submit the local/Spark reconciliation, resource observations and a runbook.
