# Chapter specifications

**Private Blueprint only. Draft route: `compare-scope`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Learn a small representation

- **Observable capability:** Compute and interpret one gradient step
- **Teaching blocks:** tensor shapes; layers; losses
- **Original worked example to write:** Two-point nonlinear fit
- **Assessable practice:** Reproduce a hand calculation and numerical check

## 2. Diagnose optimization

- **Observable capability:** Separate numerical issues from underfitting
- **Teaching blocks:** learning rates; initialization; traces; variance
- **Original worked example to write:** Synthetic curve fitting with two step sizes
- **Assessable practice:** Explain one unstable run from a loss trace

## 3. Test generalization

- **Observable capability:** Design an honest train/validation/test split
- **Teaching blocks:** regularization; leakage; held-out slices
- **Original worked example to write:** Toy image shapes with repeated seeds
- **Assessable practice:** Detect a deliberately leaky partition

## 4. Compare and report

- **Observable capability:** Defend a narrower empirical result
- **Teaching blocks:** ablations; compute budgets; uncertainty
- **Original worked example to write:** Fixed-budget tiny classifier
- **Assessable practice:** Report one evidence-backed improvement and one limit

## 5. From Results to a Research Explanation

- **Observable capability:** Produce an ablation claim with explicit uncertainty and a counterexample test.
- **Teaching blocks:** Controlled comparisons, independent holdouts, error slices, replication scope, visualization.
- **Original worked example to write:** Compare two toy image classifiers differing by one intervention and explain why equal average accuracy does not establish equal reliability.
- **Assessable practice:** Specify an ablation and a condition that would refute the claim; use a synthetic dataset and compute the metric without a model assistant.
