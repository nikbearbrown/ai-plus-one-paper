# Chapter specifications

**Private Blueprint only. Draft route: `hold-source`. Evidence: `no-usable-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Represent noisy text

- **Observable capability:** Explain what a preprocessing choice removes
- **Teaching blocks:** Unicode; segmentation; normalization; label policy
- **Original worked example to write:** Toy multilingual campus help messages
- **Assessable practice:** Demonstrate two tokenization errors on fixed strings

## 2. Set a meaningful baseline

- **Observable capability:** Implement and check a deterministic baseline
- **Teaching blocks:** features; split boundaries; metrics
- **Original worked example to write:** Synthetic maintenance ticket topic labels
- **Assessable practice:** Compare majority and keyword baselines on a held-out set

## 3. Engineer an error slice

- **Observable capability:** Report class- and context-specific errors
- **Teaching blocks:** imbalance; ambiguous labels; examples; confidence
- **Original worked example to write:** Toy negation and code-switching slice
- **Assessable practice:** Correct two mislabeled cases and justify exclusions

## 4. Evaluate a change

- **Observable capability:** Trace a regression to a pipeline stage
- **Teaching blocks:** controlled comparison; frozen data; rollback
- **Original worked example to write:** Synthetic spelling-variation update
- **Assessable practice:** Propose a reproducible regression gate
