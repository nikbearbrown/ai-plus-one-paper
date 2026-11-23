# Chapter specifications

**Private Blueprint only. Draft route: `ready-for-draft-review`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Represent Business Facts

- **Observable capability:** Translate a workflow into cardinalities and keys.
- **Teaching blocks:** entity and relationship; optionality; grain; keys
- **Original worked example to write:** A maker space loans tools to members.
- **Assessable practice:** Produce an ER diagram with rules for repeat loans.

## 2. Normalize Without Losing Meaning

- **Observable capability:** Detect functional dependencies and repair update anomalies.
- **Teaching blocks:** dependencies; normal forms; lossless decomposition; constraints
- **Original worked example to write:** A tool loan record repeats member contact data.
- **Assessable practice:** Normalize a table and demonstrate one anomaly removed.

## 3. Query and Reconcile

- **Observable capability:** Write and verify filters, joins and aggregates.
- **Teaching blocks:** SQL; nulls; grouping; validation counts
- **Original worked example to write:** A manager asks how many overdue loans each site has.
- **Assessable practice:** Predict results for an edge-case fixture and compare query output.

## 4. Integrity Under Update

- **Observable capability:** Protect operations that must succeed together.
- **Teaching blocks:** transactions; constraints; concurrent updates; migrations
- **Original worked example to write:** Two borrowers reserve the last available drill.
- **Assessable practice:** Demonstrate a transaction test with both valid and rejected outcomes.

## 5. Relational Design Review

- **Observable capability:** Defend choices using schema and workload evidence.
- **Teaching blocks:** indexes; query plans; document tradeoff; design record
- **Original worked example to write:** A catalog has stable inventory facts and varying product attributes.
- **Assessable practice:** Recommend a model and justify it with three expected queries.
