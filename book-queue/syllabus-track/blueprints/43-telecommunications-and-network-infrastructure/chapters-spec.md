# Chapter specifications

**Private Blueprint only. Draft route: `ready-for-draft-review`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Layers, clocks and service budgets

- **Observable capability:** Trace the same service requirement through a stack.
- **Teaching blocks:** Optical/radio/IP layers; timing; latency; availability.
- **Original worked example to write:** Allocate a synthetic library video service's end-to-end delay budget.
- **Assessable practice:** Identify the likely limiting layer and justify changes without double-counting delay.

## 2. Signal and link margins

- **Observable capability:** Compute headroom from losses, noise and receiver constraints.
- **Teaching blocks:** dBm and dB; path/optical loss; OFDM intuition; fade margin.
- **Original worked example to write:** Compare a short fiber run against a licensed-link classroom model using fictional distances.
- **Assessable practice:** Check two link alternatives and report sensitivities to loss uncertainty.

## 3. From local links to packet services

- **Observable capability:** Select a transport architecture given traffic demand and constraints.
- **Teaching blocks:** Packet aggregation; capacity; queueing; quality of service.
- **Original worked example to write:** Design a fictional regional classroom service with live and asynchronous traffic.
- **Assessable practice:** Validate peak use and show which traffic exceeds the latency budget first.

## 4. Protect availability and troubleshoot safely

- **Observable capability:** Design realistic fallback and test it in a benign tabletop.
- **Teaching blocks:** Protection switching; shared dependencies; alarms; service recovery.
- **Original worked example to write:** Compare two diverse paths against two paths sharing one power supply.
- **Assessable practice:** Write a failure matrix and demonstrate isolation and recovery without modeling disruptive attack behavior.
