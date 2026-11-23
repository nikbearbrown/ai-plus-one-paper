# Chapter specifications

**Private Blueprint only. Draft route: `ready-for-draft-review`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. From Domain Rules to Responsibilities

- **Observable capability:** Assign behavior to a cohesive set of classes.
- **Teaching blocks:** objects; invariants; responsibility; boundaries
- **Original worked example to write:** A community tool-lending desk has reservations and borrowing rules.
- **Assessable practice:** Draw responsibility assignments for three contested actions.

## 2. Contracts at Object Boundaries

- **Observable capability:** Define behavior clients can rely on independent of implementation.
- **Teaching blocks:** interfaces; input/output conditions; abstraction; error cases
- **Original worked example to write:** Two storage implementations share a reservation repository contract.
- **Assessable practice:** Write contract tests both stores must pass.

## 3. Composition and Substitution

- **Observable capability:** Select an extension mechanism and test substitutability.
- **Teaching blocks:** composition; inheritance; delegation; coupling
- **Original worked example to write:** A lending service changes its overdue policy by membership type.
- **Assessable practice:** Implement the change twice and compare the blast radius.

## 4. Collaboration Under a New Use Case

- **Observable capability:** Use interactions to preserve consistency across objects.
- **Teaching blocks:** message sequence; ownership; dependencies; collaborators
- **Original worked example to write:** A return updates availability and records a repair inspection.
- **Assessable practice:** Trace normal and exceptional paths and implement a minimal variation.

## 5. Refactor with Evidence

- **Observable capability:** Improve design while retaining the same externally visible results.
- **Teaching blocks:** characterization tests; refactoring; documentation; tradeoffs
- **Original worked example to write:** A report formatter is separated from lending policy.
- **Assessable practice:** Submit an independent prediction, regression tests and a design rationale.

## 6. Isolate Construction

- **Observable capability:** Let callers use products without choosing concrete classes.
- **Teaching blocks:** factory responsibility; constructor contracts; configuration boundaries
- **Original worked example to write:** An export component selects a formatter from a supported set.
- **Assessable practice:** Add a formatter without changing callers, with tests for invalid choices.

## 7. Represent Requests as Objects

- **Observable capability:** Separate requesting work from executing it.
- **Teaching blocks:** commands; shared interface; outcomes and undo boundaries
- **Original worked example to write:** A notes tool queues formatting operations for review.
- **Assessable practice:** Implement a reversible command and prove state restoration.

## 8. Combine Behaviors

- **Observable capability:** Use wrapping where behavior layers vary independently.
- **Teaching blocks:** decorator; composition order; invariants
- **Original worked example to write:** An output stream can count rows and annotate warnings independently.
- **Assessable practice:** Test two wrapper orders and justify which is valid.

## 9. Choose, Combine, or Remove

- **Observable capability:** Defend a maintainable pattern portfolio under change.
- **Teaching blocks:** tradeoff matrix; design review; regression evidence
- **Original worked example to write:** A volunteer scheduler adds one new reminder workflow.
- **Assessable practice:** Compare two designs and remove one unneeded abstraction.
