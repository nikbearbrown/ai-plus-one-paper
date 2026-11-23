# Chapter specifications

**Private Blueprint only. Draft route: `ready-for-draft-review`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Build a miniature language model

- **Observable capability:** Train and inspect a small probabilistic next-token predictor.
- **Teaching blocks:** Tokens; distributions; embeddings; held-out loss.
- **Original worked example to write:** Compare character and word segmentation on synthetic maintenance notes.
- **Assessable practice:** Predict token behavior independently, then run both versions and explain two errors.

## 2. Adapt or supply context

- **Observable capability:** Choose a resource-appropriate way to improve an answer.
- **Teaching blocks:** Pretraining limitations; prompt baseline; adaptation sandbox; controlled splits.
- **Original worked example to write:** Teach a tiny assistant unfamiliar citation labels with examples or retrieved guidance.
- **Assessable practice:** Compare prompts, retrieval and adjustment under a fixed compute cap; report accuracy and cost.

## 3. Assemble document evidence

- **Observable capability:** Reconstruct evidence spanning sections, tables and image captions.
- **Teaching blocks:** Chunk boundaries; hierarchy; table preservation; source identifiers.
- **Original worked example to write:** Find whether a fictional equipment part was replaced after a temperature spike by joining logs and chart captions.
- **Assessable practice:** Return a structured evidence trail and an abstention for one intentionally unresolvable query.

## 4. Evaluate synthesis, not eloquence

- **Observable capability:** Compare retrieval strategies and distinguish claim support from surface quality.
- **Teaching blocks:** Evidence relevance; citation entailment; challenge queries; latency and abstention.
- **Original worked example to write:** Stress a staged safety manual with contradictory old and current revision pages.
- **Assessable practice:** Test a flat baseline and hierarchical method; explain errors attributable to retrieval versus generation.
