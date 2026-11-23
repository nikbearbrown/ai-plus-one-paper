# Chapter specifications

**Private Blueprint only. Draft route: `hold-source`. Evidence: `no-usable-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. What Counts as a Correct Result?

- **Observable capability:** State a behavioral oracle for a function.
- **Teaching blocks:** contracts; examples; boundaries; ambiguity
- **Original worked example to write:** A toy conversion service rounds near threshold values.
- **Assessable practice:** Write expected outputs for five carefully chosen boundaries.

## 2. Behavior Across Interfaces

- **Observable capability:** Separate local unit concerns from integration contracts.
- **Teaching blocks:** unit tests; state; dependency boundaries; interface tests
- **Original worked example to write:** A mock delivery service retries a delivery request.
- **Assessable practice:** Propose separate unit and interface checks and predict the failure location.

## 3. Tests That Detect Regressions

- **Observable capability:** Show that chosen tests detect specific plausible defects.
- **Teaching blocks:** negative cases; regression; coverage interpretation
- **Original worked example to write:** A refund calculator switches its comparison at one threshold.
- **Assessable practice:** Introduce a benign seeded fault and show which test detects it.

## 4. Make the Release Case

- **Observable capability:** Communicate verified behavior and remaining risks.
- **Teaching blocks:** test evidence; flaky tests; unexplored cases; recommendation
- **Original worked example to write:** A tiny scheduler passes deterministic cases but has one unstable fixture.
- **Assessable practice:** Produce a reproducibility report and justified decision.
