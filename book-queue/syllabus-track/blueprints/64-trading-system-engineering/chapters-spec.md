# Chapter specifications

**Private Blueprint only. Draft route: `compare-scope`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Model order state

- **Observable capability:** Trace a toy order through distinct states
- **Teaching blocks:** events; timestamps; fills; cancellation
- **Original worked example to write:** A fictional order partially fills then cancels
- **Assessable practice:** Build a transition table and invariant

## 2. Represent instrument and risk limits

- **Observable capability:** Compare input and constraints for two fictional instrument types
- **Teaching blocks:** instrument payoff; scenario; standardized representation; compliance boundary
- **Original worked example to write:** A mock contract tracks an event threshold
- **Assessable practice:** Compute hand-defined scenario outcomes and list invalid assumptions

## 3. Replay a market fixture

- **Observable capability:** Separate synthetic inputs from simulator behavior
- **Teaching blocks:** event ordering; deterministic ticks; latency; assumptions
- **Original worked example to write:** Two quotes arrive out of order
- **Assessable practice:** Predict and check two replay variants

## 4. Account for execution assumptions

- **Observable capability:** Explain a backtest error without optimizing a strategy
- **Teaching blocks:** spread; fees; look-ahead; slippage assumptions
- **Original worked example to write:** Two identical signals with different toy fill rules
- **Assessable practice:** Compute and qualify the return difference

## 5. Demonstrate controls

- **Observable capability:** Specify a simulation stop rule and audit trail
- **Teaching blocks:** limits; rejection; monitoring; recovery
- **Original worked example to write:** A duplicate simulated message
- **Assessable practice:** Show which guard acts and why
