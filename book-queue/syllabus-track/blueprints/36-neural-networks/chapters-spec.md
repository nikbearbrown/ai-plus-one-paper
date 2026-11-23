# Chapter specifications

**Private Blueprint only. Draft route: `hold-source`. Evidence: `tentative-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Representations and the first network

- **Observable capability:** Calculate a network prediction from inputs and weights.
- **Teaching blocks:** Feature scaling; affine layers; nonlinearity; output interpretation.
- **Original worked example to write:** Manually predict a two-feature public-transit lateness label.
- **Assessable practice:** Compute outputs and show why two linear layers cannot model an XOR decision.

## 2. Loss and the learning loop

- **Observable capability:** Derive and check a parameter gradient.
- **Teaching blocks:** Loss; chain rule; backprop; numerical gradient check.
- **Original worked example to write:** Calculate a single update in a two-layer toy network.
- **Assessable practice:** Implement a gradient check and explain a mismatch.

## 3. Training and generalization

- **Observable capability:** Diagnose overfitting and optimization failures from curves.
- **Teaching blocks:** Splits; batch sizes; optimizer; regularization.
- **Original worked example to write:** Fit simulated handwriting-like geometric strokes with two model sizes.
- **Assessable practice:** Create a split-safe comparison and explain underfit versus overfit.

## 4. Architecture follows structure

- **Observable capability:** Pick a network based on inductions appropriate to data.
- **Teaching blocks:** Dense versus local features; sequence ordering; parameter sharing; memory cost.
- **Original worked example to write:** Contrast a dense model and a tiny convolution on translated geometric shapes.
- **Assessable practice:** Justify a model choice and test it on shifted inputs.

## 5. Evaluate and document a model

- **Observable capability:** Support only the conclusions a controlled experiment can bear.
- **Teaching blocks:** Baselines; class errors; calibration; ablation.
- **Original worked example to write:** Trace a high score to a synthetic background shortcut.
- **Assessable practice:** Produce an ablation table, model limitations, and reproducibility receipt.
