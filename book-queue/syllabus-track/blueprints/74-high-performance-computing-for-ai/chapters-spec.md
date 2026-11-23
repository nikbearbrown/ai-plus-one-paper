# Chapter specifications

**Private Blueprint only. Draft route: `hold-source`. Evidence: `no-usable-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Read a workload

- **Observable capability:** Estimate work before running
- **Teaching blocks:** operations; tensor sizes; data motion
- **Original worked example to write:** Synthetic matrix batch
- **Assessable practice:** Compute a bound and identify the largest buffer

## 2. Benchmark fairly

- **Observable capability:** Distinguish setup time from steady state
- **Teaching blocks:** warmup; repeat trials; memory; provenance
- **Original worked example to write:** Two implementations of a small tensor loop
- **Assessable practice:** Submit comparable timed trials and variation

## 3. Select a resource strategy

- **Observable capability:** Defend a budgeted configuration
- **Teaching blocks:** batching; overlap; throughput; latency
- **Original worked example to write:** Fixed-memory synthetic inference batches
- **Assessable practice:** Choose a batch size under a memory ceiling

## 4. Report scaling honestly

- **Observable capability:** Diagnose scaling without overclaiming
- **Teaching blocks:** normalization; speedup; bottlenecks; reproducibility
- **Original worked example to write:** Four toy worker counts with one outlier
- **Assessable practice:** Explain which counter supports one limited claim
