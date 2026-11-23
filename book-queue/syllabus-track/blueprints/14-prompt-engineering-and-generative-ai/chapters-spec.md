# Chapter specifications

**Private Blueprint only. Draft route: `existing-book`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Describe the task before writing prompts

- **Observable capability:** Turn ambiguity into input and output requirements.
- **Teaching blocks:** task boundaries; output schema; success criteria; abstention
- **Original worked example to write:** Write a contract for summarizing a fictional archive return request.
- **Assessable practice:** Produce tests for missing records, contradictory inputs and out-of-scope requests.

## 2. Compare prompt patterns on the same job

- **Observable capability:** Measure one change against a named baseline.
- **Teaching blocks:** examples; decomposition; formatting; controlled comparison
- **Original worked example to write:** Classify toy catalog entries with direct versus worked-example prompts.
- **Assessable practice:** Define expected outputs before running and explain one failure not fixed by examples.

## 3. Ground answers in evidence

- **Observable capability:** Require exact support, provenance and refusal where missing.
- **Teaching blocks:** retrieval; citation checks; source separation; unsupported claims
- **Original worked example to write:** Answer a practice question from a three-record fictional library policy fixture.
- **Assessable practice:** Test an ambiguous claim; mark support and missing evidence without asking the model to judge itself.

## 4. Bound what a tool-using agent may do

- **Observable capability:** Design a typed action and a stop rule with explicit human approval.
- **Teaching blocks:** tool inputs; explicit state and optional memory; stop/approval; trace
- **Original worked example to write:** Create a toy agent that reads a local inventory and suggests a change without applying it.
- **Assessable practice:** Show the trace proves no write occurred; test retry, stale state and an out-of-scope suggestion.

## 5. Build a repeatable prompt evaluation

- **Observable capability:** Compare prompt variants on held-out data and report limits.
- **Teaching blocks:** sampling; held-out tests; effect sizes; error taxonomy
- **Original worked example to write:** Evaluate two prompt versions for a fictional reading assistant.
- **Assessable practice:** Deliver code or spreadsheet of evidence, explain one timeout or failure, and defend a revision.
