# Chapter specifications

**Private Blueprint only. Draft route: `compare-scope`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Make ownership visible

- **Observable capability:** Assign each service and decision a human owner
- **Teaching blocks:** stakeholders; risk; escalation; interfaces
- **Original worked example to write:** A synthetic campus service desk
- **Assessable practice:** Map failed routing to a responsible person

## 2. Model multiple accountable components

- **Observable capability:** Specify non-overlapping responsibilities and a handoff
- **Teaching blocks:** event contract; routing; shared dependency; operational fallback
- **Original worked example to write:** A mock agent routes and a deterministic service looks up approved FAQ entries
- **Assessable practice:** Trace a delayed lookup and explain who can stop the workflow

## 3. Draw data boundaries

- **Observable capability:** Explain which artifacts can cross each boundary
- **Teaching blocks:** classification; partition; retention; redaction
- **Original worked example to write:** Two fictional departments with distinct records
- **Assessable practice:** Define context and retention rules with toy data

## 4. Compare rollout options

- **Observable capability:** Design one defensible rollout sequence
- **Teaching blocks:** canary; metrics; rollback; exception handling
- **Original worked example to write:** A read-only FAQ assistant with uneven coverage
- **Assessable practice:** State a condition for pausing release

## 5. Operate the service

- **Observable capability:** Design evidence for runtime decisions
- **Teaching blocks:** quality drift; incident signals; escalation; cost
- **Original worked example to write:** A sudden drop in supported answers
- **Assessable practice:** Build a tabletop runbook and trace one alert
