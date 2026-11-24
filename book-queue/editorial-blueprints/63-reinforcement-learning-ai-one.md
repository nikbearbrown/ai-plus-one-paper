# Reinforcement Learning (AI Plus One)

**Order 63.** Planning only; not authorization to draft.

## Vision

Teach the mathematics of learning policies from interaction by using playable games to reveal what the math predicts.

**Audience and prerequisites:** Programmers with introductory probability and Python who know basic game loops.

**Source basis:** Queue lists `nikbearbrown/Reinforcement-Learning-for-Agentic-AI` as primary and `nikbearbrown/Reinforcement-Learning-for-Agentic-AI-Theory-Practice-LLMs; nikbearbrown/Agentic-Reinforcement-Learning; local:game-reinforcement-learning; nikbearbrown/info-6205-algorithms` as related. These are queue leads, not independently reviewed sources for this plan.

## Learning architecture and chapter checks

1. **Experience and return.** Output: Trace rewards and discounted returns by hand in a short game. Check: Explain why two reward definitions select different moves.
2. **Tabular prediction and control.** Output: Build a playable gridworld with a value display. Check: Compare the learned values with a solvable case.
3. **Explore and generalize.** Output: Compare exploration choices and a small feature-based learner. Check: Use fixed seeds and distinguish learning from measurement noise.
4. **Evaluate policies under change.** Output: Expose a reward exploit and test performance on a modified level. Check: Measure recovery and one failure separately.

## Assessed deliverable

A playable project plus derivations and a seeded leaderboard of policies with baselines and known limitations. Keep each proposed chapter paired with an original working game. Begin independently; log any AI assistance and independently verify its claims and outputs.

## Drafting gate

Resolve source title collisions and compare with the complete Order 14 Game RL plan. The default is to reuse that plan, not launch this near-duplicate; advance only if evidence supports a substantially different non-game evaluation scope. Use originals only; textbook access does not transfer third-party adaptation rights.
