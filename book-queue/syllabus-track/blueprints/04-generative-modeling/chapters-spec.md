# Chapter specifications

**Private Blueprint only. Draft route: `ready-for-draft-review`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Learn a distribution before generating

- **Observable capability:** Use empirical frequency and likelihood to construct a sampler.
- **Teaching blocks:** training/held-out split; mode count; likelihood; seed
- **Original worked example to write:** Fit a small mixture of fictional points with an empirical histogram.
- **Assessable practice:** Generate samples from two baselines and count absent regions.

## 2. Generate one decision at a time

- **Observable capability:** Trace an autoregressive factorization and exposure to prefix changes.
- **Teaching blocks:** conditioning; factorization; decoding; temperature
- **Original worked example to write:** Generate a tiny fictional rhythm sequence from transitions.
- **Assessable practice:** Compute two conditional probabilities and test the effect of replacing an early symbol.

## 3. Represent, reconstruct, sample

- **Observable capability:** Explain why reconstruction alone does not establish generative quality.
- **Teaching blocks:** latent representation; bottleneck; prior; diversity
- **Original worked example to write:** Encode two clouds of toy geometric symbols and interpolate between them.
- **Assessable practice:** Compare reconstruction error with coverage on a hidden pattern and diagnose a disagreement.

## 4. Compare generator objectives

- **Observable capability:** Contrast reconstruction-plus-regularization and discriminator feedback on a controlled synthetic example.
- **Teaching blocks:** VAE objective; generator versus discriminator; sample diversity; convergence caveats
- **Original worked example to write:** Compare two tiny precomputed sample sets for three shapes against known modes.
- **Assessable practice:** Diagnose whether a sample set is sharp, diverse or neither using labeled held-out fixtures.

## 5. Extension: remove noise step by step

- **Observable capability:** Hand-trace simplified iterative generation and expose schedule choices.
- **Teaching blocks:** forward corruption; denoising; sampling schedule; budget
- **Original worked example to write:** Track three noisy steps on synthetic two-dimensional points.
- **Assessable practice:** Compare alternate step counts with a fixed noise draw and record cost and quality separately.

## 6. Test failures before choosing a model

- **Observable capability:** Evaluate a model using coverage, quality and reproducibility.
- **Teaching blocks:** mode collapse; nearest-neighbor check; repeat seeds; limits
- **Original worked example to write:** Compare two samplers for synthetic shapes with identical means.
- **Assessable practice:** Submit protocol, counterexample, repeat-run metrics and model recommendation.
