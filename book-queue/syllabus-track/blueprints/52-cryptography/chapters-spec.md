# Chapter specifications

**Private Blueprint only. Draft route: `ready-for-draft-review`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. What must remain true?

- **Observable capability:** Distinguish the security properties a system actually needs
- **Teaching blocks:** confidentiality; integrity; authenticity; trust assumptions
- **Original worked example to write:** A club posts a public results file that must be attributable but need not be secret.
- **Assessable practice:** Select properties for four records and explain why encryption alone is not the answer.

## 2. Small arithmetic, clear boundaries

- **Observable capability:** Evaluate a toy modular expression and explain the teaching boundary
- **Teaching blocks:** congruence; exponents; modular equivalence; toy vs production parameters
- **Original worked example to write:** Two teams compute a tiny modular arithmetic identity by different routes.
- **Assessable practice:** Show hand calculations, then state why the example supports arithmetic and not system security.

## 3. Choose a primitive for a purpose

- **Observable capability:** Connect ordinary protection goals to a reviewed primitive family
- **Teaching blocks:** hashes; authenticated encryption; signatures; established libraries
- **Original worked example to write:** A school archive needs integrity checking for a catalog and protected transport for a private draft.
- **Assessable practice:** Label primitive roles, what each cannot prove, and the evidence required to approve a design.

## 4. Trace who is trusted

- **Observable capability:** Explain identity proof and certificate relationships from a fixture
- **Teaching blocks:** certificate role; trust roots; authentication vs authorization; validity checks
- **Original worked example to write:** A fictional service owner's diagram mixes client identity with access rights.
- **Assessable practice:** Trace the asserted identity and flag what evidence is still absent to authorize a request.

## 5. Manage trust across changes

- **Observable capability:** Decide how to handle a key lifecycle event and prove the safe outcome
- **Teaching blocks:** key scope; rotation; revocation; dependency evidence
- **Original worked example to write:** A synthetic library application retires a service credential after an ownership handoff.
- **Assessable practice:** Draw the change timeline and build a checklist that catches lingering use without touching a real service.
