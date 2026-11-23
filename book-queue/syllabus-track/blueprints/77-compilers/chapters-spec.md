# Chapter specifications

**Private Blueprint only. Draft route: `ready-for-draft-review`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. From text to tree

- **Observable capability:** Produce a parse tree for expressions
- **Teaching blocks:** tokens; precedence; associativity; grammar
- **Original worked example to write:** Toy calculator expression
- **Assessable practice:** Find a case where precedence changes the answer

## 2. Check meaning before running

- **Observable capability:** Distinguish syntax from type failures
- **Teaching blocks:** scope; type rules; diagnostics
- **Original worked example to write:** Toy boolean/arithmetic expressions
- **Assessable practice:** Create one minimal failing program per error class

## 3. Lower to an intermediate form

- **Observable capability:** Translate and preserve meaning
- **Teaching blocks:** instructions; temporaries; control flow
- **Original worked example to write:** Toy conditional calculation
- **Assessable practice:** Trace a compiled branch against the interpreter

## 4. Optimize without changing behavior

- **Observable capability:** Use an equivalence test to validate a transformation
- **Teaching blocks:** constant folding; tests; counterexample; limits
- **Original worked example to write:** Constant subexpressions in toy programs
- **Assessable practice:** Show a correct transformation and a counterexample

## 5. Liveness and Register Pressure

- **Observable capability:** Solve a small backward dataflow problem and check the allocation against simultaneous live ranges.
- **Teaching blocks:** Use/def sets, backward fixed point, interference, allocation and spilling.
- **Original worked example to write:** Trace liveness for a four-block arithmetic program built for this book.
- **Assessable practice:** Give live-in/live-out sets for a changed branch; supply an allocation or justify a spill without changing behavior.
