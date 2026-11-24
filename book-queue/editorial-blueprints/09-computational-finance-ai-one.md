# Computational Finance (AI Plus One)

**Queue #9 · ready · proposed curriculum Blueprint · no approval**

## Source basis

Primary: `nikbearbrown/mba-computational-finance`. Related: `nikbearbrown/computational-finance-with-ai`; `nikbearbrown/computational-finance`; `nikbearbrown/Corporate-Finance-with-Excel-Python-and-LLMs`; `nikbearbrown/Computational_Finance_with_Python`; `nikbearbrown/claude-for-finance`. These are catalog-listed sources, not a claim that this Blueprint reproduces the manuscript or that its material is cleared for reuse.

## Reader and purpose

**Audience and prerequisites:** MBA or advanced undergraduate learners comfortable with returns, present value and one of Excel or introductory Python.

**Teaching spine:** Use instruments, valuation, risk and portfolio questions to teach model construction with an agent and independent financial verification.

## Proposed chapter progression

1. **Measure returns from imperfect inputs.** Produce a total-return and annualization model; reconstruct a two-period path and state how missing values were handled.
2. **Price a bond from dated cash flows.** Model discounting and duration; verify that a one-year cash flow of 105 at 5% prices at 100 and the price falls at a higher rate.
3. **Model uncertainty explicitly.** Estimate sampling variability and drawdown on a synthetic sequence; hand-check the max drawdown for a short path.
4. **Value an option in a small tree.** Work a one-step replication and pricing model; test a payoff bound and explain model assumptions without live trading.
5. **Construct and stress a portfolio.** Compute weights, covariance and scenario impacts; independently verify feasibility and show the effect of a changing correlation.
6. **Connect statements to model assumptions.** Translate a fictional set of accounts into forecast inputs; reconcile the balance and label the valuation driver most vulnerable to error.

## Assessed deliverable

Analyst model packet on synthetic instruments: specification, an agent-assisted workbook or script, inputs and provenance, independent benchmark and sensitivity checks, and a decision interpretation. Reject a model with inconsistent timing even if its charts are plausible.

Require a first unaided attempt and a checked revision. Any AI assistance is optional unless the source-verified teaching scope specifically calls for it; assess learner judgment from a separate calculation, trace, or test.

## Drafting gate

Expand computational-finance.md; compare candidate variants only for independently checked, rights-cleared examples. Map modules to the 13-chapter source, retain model techniques specific to Computational Finance and exclude identifiable student work.

Do not treat this compact plan as a manuscript, an approval, or a change to the listed stage.
