# Chapter specifications

**Private Blueprint only. Draft route: `compare-scope`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. State the question

- **Observable capability:** Define a measurable data product
- **Teaching blocks:** unit of observation; source; target; data contract
- **Original worked example to write:** A synthetic bike-share trips table
- **Assessable practice:** Design a check for a changing station ID

## 2. Reason about arrays before vectorizing

- **Observable capability:** Compare loop and vector result under a known shape
- **Teaching blocks:** array shape; dtype; broadcasting; numerical check
- **Original worked example to write:** Normalize synthetic station counts by a daily divisor
- **Assessable practice:** Predict a shape mismatch before using a tool and correct it

## 3. Clean without hiding errors

- **Observable capability:** Separate valid correction from a changed population
- **Teaching blocks:** missing values; duplicates; types; rejected records
- **Original worked example to write:** Departure times in two formats
- **Assessable practice:** Reconcile before/after row counts

## 4. Split before fitting

- **Observable capability:** Build a split and test leakage assumptions
- **Teaching blocks:** time split; transformation fit; identifiers; baseline
- **Original worked example to write:** A future trip field predicts the past
- **Assessable practice:** Remove leakage and verify expected failure

## 5. Package the pipeline

- **Observable capability:** Make a clean rerun explainable
- **Teaching blocks:** configs; deterministic fixtures; tests; summary
- **Original worked example to write:** Two runs with an added station row
- **Assessable practice:** Provide a rerun note and failing input test
