# Chapter specifications

**Private Blueprint only. Draft route: `compare-scope`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Find entities and boundaries

- **Observable capability:** Name stable domain concepts and system boundaries
- **Teaching blocks:** entities; lifecycles; relationships; actors
- **Original worked example to write:** A library holds system with two copies
- **Assessable practice:** Distinguish a title identifier from a copy identifier

## 2. Prototype a modeled interaction

- **Observable capability:** Convert one state transition into a small independently testable implementation
- **Teaching blocks:** object responsibilities; persistent data; UI state; design patterns
- **Original worked example to write:** A pretend library checkout form updates one copy record
- **Assessable practice:** Write a trace and prove the checkout cannot change a second copy

## 3. Describe scenario behavior

- **Observable capability:** Turn one scenario into a sequence
- **Teaching blocks:** happy path; alternatives; messages; invariant
- **Original worked example to write:** Two patron requests and one available copy
- **Assessable practice:** Write an alternate path with expected response

## 4. Model state explicitly

- **Observable capability:** Predict transitions from initial conditions
- **Teaching blocks:** state machine; guards; time; exceptions
- **Original worked example to write:** A hold expires before pickup
- **Assessable practice:** Find an illegal transition and correct it

## 5. Trace and challenge a design

- **Observable capability:** Reconcile multiple views against a requirement
- **Teaching blocks:** traceability; tests; mismatch; AI suggestion critique
- **Original worked example to write:** A sequence permits a forbidden transition
- **Assessable practice:** Record mismatch, correction and independent test
