# Programmable Logic Controller Design (AI Plus One)

**Order 74.** Planning only; not authorization to draft.

## Vision

Translate a process statement into simulated control logic with independently checked invariants and safe responses.

**Audience and prerequisites:** Engineering learners with elementary logic and circuit notation; no physical PLC access required.

**Source basis:** Queue lists `nikbearbrown/agentic-plc-design` as primary and `nikbearbrown/agentic-plc; nikbearbrown/From-Catalog-to-Circuit` as related. These are queue leads, not independently reviewed sources for this plan.

## Learning architecture and chapter checks

1. **Read the process.** Output: Create I/O and operating-state diagrams for a mock filling line. Check: Identify interlocks and intended default responses conceptually.
2. **Model sequences.** Output: Specify permitted transitions and timing in a simulator. Check: Verify sensor events cannot bypass a stated precondition.
3. **Program and test in simulation.** Output: Create a ladder-style or structured-text toy controller. Check: Run normal, missing-input and delay cases without equipment.
4. **Review and handoff.** Output: Write a traceability and simulated commissioning dossier. Check: Separate simulator evidence from untested physical claims.

## Assessed deliverable

A simulator-only controller for a fictional system with requirements-to-tests trace, abnormal-case log and independent reviewer signoff. No live controls. Begin independently; log any AI assistance and independently verify its claims and outputs.

## Drafting gate

Verify source and review plans with a qualified controls educator; coordinate with #96 and do not treat bench proof as operational approval.
