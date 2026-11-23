# Chapter specifications

**Private Blueprint only. Draft route: `ready-for-draft-review`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Make a baseline worth comparing

- **Observable capability:** Build a repeated timing and memory baseline.
- **Teaching blocks:** warm-up; variance; fixed shapes; identity checks
- **Original worked example to write:** Implement a serial mini-batch nearest-centroid distance pass.
- **Assessable practice:** Propose comparable inputs and diagnose a timing artifact in three runs.

## 2. Multiply work without wasting copies

- **Observable capability:** Explain when vectorization shifts the bottleneck to memory.
- **Teaching blocks:** strides; broadcasting; materialization; numerical tolerance
- **Original worked example to write:** Compare loop, tiled and broadcasted synthetic distance kernels.
- **Assessable practice:** Estimate each temporary array and test accuracy on a boundary shape.

## 3. Schedule work across cores

- **Observable capability:** Measure a real overhead/balance boundary.
- **Teaching blocks:** chunks; serialization; synchronization; speedup
- **Original worked example to write:** Partition a skewed synthetic corpus for parallel counting.
- **Assessable practice:** Show one workload that gets slower and link it to recorded setup cost.

## 4. Measure compute versus transfer

- **Observable capability:** Separate kernel runtime from end-to-end measurement.
- **Teaching blocks:** host/device copies; batching; synchronization; memory cap
- **Original worked example to write:** Profile a toy product on CPU and an available accelerator or use a supplied trace.
- **Assessable practice:** Pick a batch size within the budget and explain two claims not supported by a trace.

## 5. Partition a training step

- **Observable capability:** Explain synchronization and communication costs without treating the fallback trace as live cluster evidence.
- **Teaching blocks:** data partition; gradients; all-reduce intuition; stragglers
- **Original worked example to write:** Trace two fictional workers with equal arithmetic and unequal data-transfer delays.
- **Assessable practice:** Compute the step barrier time with two different partitions and defend a reproducible measurement plan.

## 6. Defend a scaling experiment

- **Observable capability:** Report a fair repeatable comparison with limits.
- **Teaching blocks:** fixed error contract; throughput; memory peak; reproducibility
- **Original worked example to write:** Evaluate serial, tiled and parallel implementations of toy mini-batch inference.
- **Assessable practice:** Produce a report with speed, correctness, memory and a negative reproducible result.
