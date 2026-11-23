# Chapter specifications

**Private Blueprint only. Draft route: `ready-for-draft-review`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Start with the Baseline

- **Observable capability:** Make evaluation independent of architecture preference.
- **Teaching blocks:** dataset splits; decision trees; metrics; error analysis
- **Original worked example to write:** A public-use plant-image fixture comes with noisy labels.
- **Assessable practice:** Define a naive and a stronger baseline and predict failure cases.

## 2. Dense Models and Their Diagnostics

- **Observable capability:** Tune and diagnose a small model with reproducible data splits.
- **Teaching blocks:** feedforward layers; loss; regularization; learning curves
- **Original worked example to write:** A model predicts public bus delay categories from tabular features.
- **Assessable practice:** Show one intervention improving held-out performance or explain why none did.

## 3. Architectures for Sequence and Space

- **Observable capability:** Choose inductive structure matching the fields of the problem.
- **Teaching blocks:** recurrent sequence models; convolution; receptive field; comparison
- **Original worked example to write:** A toy dataset pairs short motion sequences and rendered diagram images.
- **Assessable practice:** Assign appropriate models and compare on the same sample budget.

## 4. Attention and Lightweight Adaptation

- **Observable capability:** Test whether adapting a small pretrained model adds value.
- **Teaching blocks:** attention; transfer; fine-tuning; leakage checks
- **Original worked example to write:** An adapted tiny model labels synthetic help-desk requests.
- **Assessable practice:** Compare against a simple classifier and check label contamination.

## 5. Generative Models and Failure Evidence

- **Observable capability:** Evaluate model families without comparing unlike tasks.
- **Teaching blocks:** diffusion intuition; world-model contrast; evaluation; limitations
- **Original worked example to write:** A toy generator produces simple icon geometry while a sequence model predicts the next move in a grid.
- **Assessable practice:** Select one appropriate metric for each and explain why they cannot be ranked by a single score.
