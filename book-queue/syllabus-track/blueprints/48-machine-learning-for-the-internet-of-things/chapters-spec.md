# Chapter specifications

**Private Blueprint only. Draft route: `hold-source`. Evidence: `tentative-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Can the sensor support the label?

- **Observable capability:** Define a prediction target and audit measurement gaps
- **Teaching blocks:** signal vs label; sampling; missingness; task consequence
- **Original worked example to write:** A synthetic refrigerator sensor stream has a few missing samples around a door opening.
- **Assessable practice:** Design a label guide and flag two windows that must remain ambiguous.

## 2. The split before the score

- **Observable capability:** Choose evaluation partitions that match intended use
- **Teaching blocks:** group split; chronology; leakage; baseline
- **Original worked example to write:** A training set has multiple days from each mock classroom and several duplicate windows.
- **Assessable practice:** Draw an evaluation split for a new classroom and explain why a random row split fails.

## 3. When a threshold causes alarms

- **Observable capability:** Interpret performance and tradeoffs at a chosen operating point
- **Teaching blocks:** false positives; false negatives; thresholds; error slices
- **Original worked example to write:** A fictional condition monitor gives two models equal accuracy with different missed-event costs.
- **Assessable practice:** Compute error tables and justify one threshold for a low-stakes maintenance alert.

## 4. Compare transfer without shopping for a result

- **Observable capability:** Design a fair evaluation of a pretrained time-series model against a simple baseline
- **Teaching blocks:** pretraining boundaries; frozen vs adapted representations; repeated evaluation; uncertainty
- **Original worked example to write:** A fictional maintenance dataset contains repeat device cycles and models with differing validation scores.
- **Assessable practice:** Predeclare comparison metrics and held-out device groups, then draft a claim and a result that would make it false.

## 5. Can it run where it is needed?

- **Observable capability:** Decide edge feasibility and fallback for a bounded model
- **Teaching blocks:** latency and memory; energy measurement; drift; abstention
- **Original worked example to write:** Two pretend edge model profiles show opposite accuracy and memory rankings.
- **Assessable practice:** Write a model card and validate the deployment recommendation against three stated resource budgets.
