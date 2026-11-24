# Agentic Search and Graphs (AI Plus One)

**Order 58.** Planning only; not authorization to draft.

## Vision

Treat agentic search as a bounded decision problem over actions, observations and costs.

**Audience and prerequisites:** Programmers comfortable with graphs and basic search; no current vendor tool assumed.

**Source basis:** Queue lists `nikbearbrown/agents-as-graphs-book` as primary and `nikbearbrown/agents-as-graphs; nikbearbrown/info-6205-algorithms; nikbearbrown/agentic-best-practices` as related. These are queue leads, not independently reviewed sources for this plan.

## Learning architecture and chapter checks

1. **Agent states and evidence.** Output: Model a tool-assisted inventory inquiry as a state/action graph. Check: Identify hidden state and evidence limitations.
2. **Budgeted search.** Output: Implement a bounded toy frontier with costs and stopping rules. Check: Compare successful and truncated traces.
3. **Information versus action.** Output: Distinguish observations from actions that change a mock environment. Check: Write a test for a proposal denied by its rules.
4. **Evaluate search behavior.** Output: Use trace and cost summaries on synthetic cases. Check: Explain when a simpler fixed workflow wins.

## Assessed deliverable

A small simulated search agent with replayable traces, route comparisons and bounded stop behavior. Begin independently; log any AI assistance and independently verify its claims and outputs.

## Drafting gate

Verify manuscript pin, authorship and companion role; distinguish from graph traversal foundations and Design of Agentic Systems.
