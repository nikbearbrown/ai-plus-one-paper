# Chapter specifications

**Private Blueprint only. Draft route: `hold-source`. Evidence: `no-usable-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. State what improves

- **Observable capability:** Define a measurable baseline and constraints
- **Teaching blocks:** objective; data split; guardrails; claims
- **Original worked example to write:** An offline toy summarizer
- **Assessable practice:** Define correctness, abstention and one prohibited change

## 2. Separate proposer and evaluator

- **Observable capability:** Maintain a fixed test independent of model revisions
- **Teaching blocks:** holdout; leakage; versioning; controls
- **Original worked example to write:** A revised prompt accidentally learns all visible answers
- **Assessable practice:** Describe a clean redo and why scores cannot be compared

## 3. Review and accept one change

- **Observable capability:** Explain why one proposed edit is rejected despite a score
- **Teaching blocks:** human authorization; regressions; scope; rollback
- **Original worked example to write:** A toy punctuation normalizer fails an ambiguity case
- **Assessable practice:** Use a signed-off rubric blank without simulating approval

## 4. Decide when to stop

- **Observable capability:** Show evidence does not support a stronger claim
- **Teaching blocks:** diminishing gains; noise; audit; stop conditions
- **Original worked example to write:** Scores fluctuate on tiny synthetic sample
- **Assessable practice:** Write a qualified decision and frozen next test
