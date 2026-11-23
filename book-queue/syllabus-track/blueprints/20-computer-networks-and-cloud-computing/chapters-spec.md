# Chapter specifications

**Private Blueprint only. Draft route: `ready-for-draft-review`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. How a Request Reaches a Service

- **Observable capability:** Trace a request through addressing, DNS and transport.
- **Teaching blocks:** names; IP; ports; HTTP
- **Original worked example to write:** A browser reaches a mock community weather API.
- **Assessable practice:** Annotate a trace and identify where one failed request stops.

## 2. Build and Explain Network Boundaries

- **Observable capability:** Create reachability and deny-by-default expectations.
- **Teaching blocks:** address ranges; routes; network segmentation; least privilege
- **Original worked example to write:** Public and internal demo services need different routes.
- **Assessable practice:** Draw and test allowed and blocked flows in a toy setup.

## 3. Choose Compute and Persistence

- **Observable capability:** Match workload behavior to resource and storage choices.
- **Teaching blocks:** virtualization; containers; managed service abstractions; persistence
- **Original worked example to write:** A community notice board stores uploads across restarts.
- **Assessable practice:** Rank options for a sample workload and demonstrate a restart.

## 4. Availability Has Tradeoffs

- **Observable capability:** Predict what breaks under a simulated resource failure.
- **Teaching blocks:** load distribution; failure domains; backups; cost drivers
- **Original worked example to write:** Two read-only replicas serve a transit schedule.
- **Assessable practice:** Take one mock node out and prove which requests still succeed.

## 5. Deployment Decision Record

- **Observable capability:** Defend deployment topology using measured evidence.
- **Teaching blocks:** observability; capacity assumptions; trace evidence; operations handoff
- **Original worked example to write:** A club calendar moves from a single demo server to a split architecture.
- **Assessable practice:** Submit a topology diagram, smoke-test log and cost assumptions.
