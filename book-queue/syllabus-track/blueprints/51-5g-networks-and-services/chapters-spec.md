# Chapter specifications

**Private Blueprint only. Draft route: `hold-source`. Evidence: `tentative-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. From service intent to a budget

- **Observable capability:** Convert contrasting use cases into priorities and acceptance ranges
- **Teaching blocks:** throughput; latency; reliability; device density
- **Original worked example to write:** A venue needs video updates, inventory sensors, and a protected operational notification channel.
- **Assessable practice:** Create three profiles and explain why a single optimization goal is inadequate.

## 2. What the radio layer can trade

- **Observable capability:** Explain how scheduling choices influence access under load
- **Teaching blocks:** New Radio concepts; access scheduling; channel conditions; resource tradeoffs
- **Original worked example to write:** An invented shared radio frame has two traffic classes with conflicting deadline needs.
- **Assessable practice:** Assign slots on a toy timeline and identify the opportunity cost of the chosen arrangement.

## 3. Where the core changes the result

- **Observable capability:** Separate core control events from user data and identify service boundaries
- **Teaching blocks:** radio access and core; control and user planes; virtualization; slicing targets
- **Original worked example to write:** Two simulated clients share access infrastructure but require different service policies.
- **Assessable practice:** Draw two paths and label which plane establishes and which carries traffic.

## 4. Keep a moving session usable

- **Observable capability:** Trace handoff effects through a constrained end-to-end design
- **Teaching blocks:** mobility; session continuity; path transitions; service monitoring
- **Original worked example to write:** A mock campus vehicle crosses coverage regions and experiences a short interruption.
- **Assessable practice:** Interpret a synthetic event trace and propose one check that distinguishes access from core delay.

## 5. Commission a service on paper

- **Observable capability:** Defend a synthetic architecture and test its budget
- **Teaching blocks:** service requirement traceability; capacity scenarios; acceptance tests; residual risk
- **Original worked example to write:** A public event needs a design dossier without access to an operator lab.
- **Assessable practice:** Submit two alternatives, a budget check, and a rollback recommendation for a failed synthetic acceptance case.
