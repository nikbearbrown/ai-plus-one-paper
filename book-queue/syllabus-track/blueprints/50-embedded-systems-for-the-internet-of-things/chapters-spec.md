# Chapter specifications

**Private Blueprint only. Draft route: `ready-for-draft-review`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. What state is the device in?

- **Observable capability:** Express hardware-independent behavior with states and events
- **Teaching blocks:** sampling loop; sensors and outputs; state transitions; initial conditions
- **Original worked example to write:** A simulated reading-room lamp changes status after a local button input and a timer.
- **Assessable practice:** Draw a deterministic transition table and trace held and bouncing inputs in a supplied fixture.

## 2. Choose a sampling budget

- **Observable capability:** Calculate whether timing and storage satisfy a simple requirement
- **Teaching blocks:** ticks; buffer memory; sampling frequency; deadline
- **Original worked example to write:** An invented humidity logger stores fixed-size samples before upload.
- **Assessable practice:** Compute how long the buffer lasts and select an interval under two constraints.

## 3. When timing changes behavior

- **Observable capability:** Explain how scheduling or delayed input changes the result
- **Teaching blocks:** polling; queued events; scheduling delay; bounded work
- **Original worked example to write:** A toy controller delays one reading while processing a burst of inputs.
- **Assessable practice:** Trace two candidate loops and identify the one that meets a response bound.

## 4. Read a hardware boundary in a trace

- **Observable capability:** Choose a buffered interface and explain the transfer and concurrency assumptions
- **Teaching blocks:** serial vs shared-bus concepts; memory boundaries; interrupts; queue contention
- **Original worked example to write:** Two simulated peripheral readings share a queue whose service interval is longer than one burst.
- **Assessable practice:** Interpret supplied traces and select a buffering approach that preserves the coverage requirement.

## 5. Design a boring failure

- **Observable capability:** Specify a safe fallback and prove it in a simulation trace
- **Teaching blocks:** watchdog concept; stale readings; fallback state; recovery
- **Original worked example to write:** A simulated room indicator receives contradictory or stale sensor input.
- **Assessable practice:** Produce a test matrix that demonstrates safe defaults and shows what is not proven about real hardware.
