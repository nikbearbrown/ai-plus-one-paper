# Chapter specifications

**Private Blueprint only. Draft route: `hold-source`. Evidence: `tentative-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. From Commit to Candidate

- **Observable capability:** Define a pipeline that catches broken builds early.
- **Teaching blocks:** version control; reproducible package; checks; handoff
- **Original worked example to write:** A club event API returns a breaking response shape.
- **Assessable practice:** Set pipeline gates and show which gate detects the regression.

## 2. Declare Environments

- **Observable capability:** Represent repeatable desired infrastructure without leaking credentials.
- **Teaching blocks:** declarative config; environment parity; artifact versions
- **Original worked example to write:** A mock test environment has inconsistent service versions.
- **Assessable practice:** Create a local environment spec and demonstrate repeatable setup.

## 3. Ship and Observe a Change

- **Observable capability:** Use verifiable promotion and smoke tests.
- **Teaching blocks:** staging; release artifact; health checks; telemetry
- **Original worked example to write:** A toy application deploys an unavailable dependency.
- **Assessable practice:** Show which signal blocks promotion and preserve evidence.

## 4. Recover and Learn

- **Observable capability:** Rehearse a rollback and improve the process.
- **Teaching blocks:** rollback; failure timeline; runbook; action checks
- **Original worked example to write:** A migrated demo emits incorrect totals.
- **Assessable practice:** Restore the earlier service and propose a check preventing recurrence.
