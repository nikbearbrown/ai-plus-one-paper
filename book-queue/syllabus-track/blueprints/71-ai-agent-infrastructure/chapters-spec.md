# Chapter specifications

**Private Blueprint only. Draft route: `hold-source`. Evidence: `no-usable-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Trace a unit of work

- **Observable capability:** Separate run, task and attempt identities
- **Teaching blocks:** queue; context; retry; ownership
- **Original worked example to write:** A duplicate synthetic document request
- **Assessable practice:** Draw the states and identify intentional retries

## 2. Build repeatable recovery

- **Observable capability:** Prevent an accidental repeated side effect in simulation
- **Teaching blocks:** idempotence; timeout; queue; no-op
- **Original worked example to write:** A mock receipt duplicated after restart
- **Assessable practice:** Set a test for only one recorded completion

## 3. Observe and stop

- **Observable capability:** Specify latency, quality and escalation thresholds
- **Teaching blocks:** observability; synthetic flags; budget; state
- **Original worked example to write:** A classifier returns an unsupported label repeatedly
- **Assessable practice:** Write a proposed stopping condition and audit trail

## 4. Review the deployment boundary

- **Observable capability:** Evaluate access, data and workload assumptions
- **Teaching blocks:** access restriction; isolation; manual control; comparison
- **Original worked example to write:** A read-only synthetic catalog lookup
- **Assessable practice:** Draft a safe tabletop deployment at mock scale
