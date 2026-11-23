# Chapter specifications

**Private Blueprint only. Draft route: `ready-for-draft-review`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Who owns this service file?

- **Observable capability:** Explain whether a service account can read its intended file
- **Teaching blocks:** filesystem ownership; modes; identities and groups; least privilege
- **Original worked example to write:** A fixture file inside a teaching folder is readable to the maintainer but not the service identity.
- **Assessable practice:** Explain the mismatch and recommend a narrowly scoped ownership or permission review, not blanket permission changes.

## 2. The process behind the service

- **Observable capability:** Tie process state and service records to a claim
- **Teaching blocks:** process relationships; services; exit states; timestamps
- **Original worked example to write:** A fake weather display shows a dead service and a stale status file.
- **Assessable practice:** Build a three-event timeline and mark which conclusion the timestamp does not support.

## 3. A host’s view of the network

- **Observable capability:** Diagnose an interface, route, or naming mismatch from fixed outputs
- **Teaching blocks:** interface state; address and route entries; local bindings; resolver observations
- **Original worked example to write:** A fictional catalog service is healthy locally while clients see nothing.
- **Assessable practice:** Use fixture evidence to distinguish three candidate failure locations and justify one next read-only check.

## 4. Reduce the logs without losing evidence

- **Observable capability:** Explain and verify a bounded local text-processing pipeline
- **Teaching blocks:** filters; stable fields; missing values; reproducible counts
- **Original worked example to write:** A static fixture contains five synthetic service events with duplicate entries and one absent timestamp.
- **Assessable practice:** Specify a read-only extraction, predict the event count by hand, and reconcile one mismatch against the original log.

## 5. Write a safe operator handoff

- **Observable capability:** Communicate diagnosis without assuming permission to act
- **Teaching blocks:** read-only boundary; log redaction; confidence; reversible next steps
- **Original worked example to write:** A rotating lab support group inherits competing explanations of a server outage.
- **Assessable practice:** Produce a handoff whose peer can reproduce the evidence trail without elevated permissions.
