# Computational Finance (AI Plus One)

**One textbook, queue #9.** Finance supplies the questions, assumptions, and methods. The AI agent helps implement the model in Excel, Python, or another suitable tool. The learner checks whether the result answers the financial question and whether the result is correct.

- Start from the [MBA Computational Finance book](https://github.com/nikbearbrown/mba-computational-finance): returns and risk, securities, valuation, options, portfolios, asset pricing, and financial statements.
- Compare the [AI variant](https://github.com/nikbearbrown/computational-finance-with-ai), [methods draft](https://github.com/nikbearbrown/computational-finance), and [Excel/Python/LLM draft](https://github.com/nikbearbrown/Corporate-Finance-with-Excel-Python-and-LLMs) for distinct explanations, checked examples, and lab ideas. Use only authorized material and document where it came from. The [student Python course](https://github.com/nikbearbrown/Computational_Finance_with_Python) is a curriculum comparison unless its contributors explicitly clear material for reuse. None is a separate AI Plus One title.
- Keep **Corporate Finance (AI Plus One)** separate for company financing and investment decisions. Reuse a relevant model only where it supports a distinct learning outcome.

## One problem, two implementations

For a bond-valuation lab, specify cash flows, compounding convention, price date, and units before asking an agent to build anything. Have it implement the same model in Excel or Python; use the other implementation as an optional cross-check. Require a simple benchmark: a one-year zero-coupon bond paying 105, discounted at 5% per year, is worth 100. Then test that price falls when the discount rate rises, and inspect timing and units if the tools disagree. Grade the setup, validation, and interpretation, not the software choice. Use synthetic or authorized data; no live trading.

This note sets drafting scope. It is not a finished book, rights clearance, or a change to any source repository. Follow the [drafting handoff](../codex-handoff.md).
