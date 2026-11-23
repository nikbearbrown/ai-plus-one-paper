# Chapter specifications

**Private Blueprint only. Draft route: `existing-book`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Start with a decision question

- **Observable capability:** State outcome, unit, horizon and a baseline before viewing results.
- **Teaching blocks:** measurement; data card; bias; success metric
- **Original worked example to write:** Predict whether synthetic fictional distribution shipments will be late.
- **Assessable practice:** Write a baseline choice and a recording plan that could falsify it.

## 2. Make an inspectable dataset

- **Observable capability:** Audit schema, missingness and duplicate records without exposing identifiers.
- **Teaching blocks:** types; cleaning logs; missingness; version IDs
- **Original worked example to write:** Repair a table with impossible service dates and repeated shipment IDs.
- **Assessable practice:** Propose a reversible transform log and document data you would keep unknown.

## 3. Keep test data in the future

- **Observable capability:** Check that splits and feature provenance reflect model use.
- **Teaching blocks:** train/validation/test; groups; leakage; timing
- **Original worked example to write:** Show how a delivery-time field leaks a route’s outcome.
- **Assessable practice:** Correct a deliberately leaky training fixture and compare before/after held-out performance.

## 4. Compare models fairly

- **Observable capability:** Analyze baselines and prediction error under same test design.
- **Teaching blocks:** simple models; curves; calibration; resource budget
- **Original worked example to write:** Compare a toy nearest-neighbor model with a constant baseline.
- **Assessable practice:** Explain model selection if one slice worsens despite better average score.

## 5. Look for structure without labels

- **Observable capability:** Distinguish clustering quality evidence from a persuasive scatterplot.
- **Teaching blocks:** normalization; clustering; dimensionality; stability
- **Original worked example to write:** Group simulated delivery routes whose distance changes with units.
- **Assessable practice:** Compare two scalings on held-out routes and defend one coherent, noncausal interpretation.

## 6. Tell what the result supports

- **Observable capability:** Write decisions and uncertainty for a nontechnical reader.
- **Teaching blocks:** uncertainty; error examples; drift; rerun instructions
- **Original worked example to write:** Prepare a dashboard note for fictional distribution planners.
- **Assessable practice:** Submit a recommendation, a contrary case and a runnable provenance packet.
