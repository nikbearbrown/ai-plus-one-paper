# Chapter specifications

**Private Blueprint only. Draft route: `compare-scope`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Specify what a feed promises

- **Observable capability:** Define and test schema, freshness and lineage contracts.
- **Teaching blocks:** typed records; event vs arrival time; privileges; quarantine
- **Original worked example to write:** Trace fictional bike-dock events from a JSON feed to a daily table.
- **Assessable practice:** Write invariants and an acceptance table for missing IDs and delayed arrivals.

## 2. Ingest without double counting

- **Observable capability:** Implement replay-safe ingestion with graceful data failure.
- **Teaching blocks:** dedup keys; batching; idempotence; failure queue
- **Original worked example to write:** Send two copies of an invalid meter reading plus one correction.
- **Assessable practice:** Design repeated-load assertions and show why row count stays stable.

## 3. Transform as of a decision time

- **Observable capability:** Join features using only information available at evaluation time.
- **Teaching blocks:** timestamps; as-of join; leakage; backfill
- **Original worked example to write:** Predict park occupancy using readings corrected after prediction.
- **Assessable practice:** Hand-compute held-out join pairs and test that a future update cannot change past features.

## 4. Version data and transformations

- **Observable capability:** Reconstruct a dataset from source and processing identities.
- **Teaching blocks:** digests; schemas; versions; replay trace
- **Original worked example to write:** Backfill a toy weather station feature using corrected units.
- **Assessable practice:** Rebuild two snapshots and attribute each result difference to one change.

## 5. Prepare evidence for retrieval

- **Observable capability:** Refresh a queryable collection without losing source permissions or document identity.
- **Teaching blocks:** chunk/document keys; metadata; freshness; versioned index
- **Original worked example to write:** Index synthetic library handbook pages with one withdrawn policy.
- **Assessable practice:** Show that stale or withdrawn records leave no unsupported answer in a fixture replay.

## 6. Release a data product responsibly

- **Observable capability:** Decide to accept or quarantine a feed from measured guarantees.
- **Teaching blocks:** freshness SLA; drift signals; incident response; retention
- **Original worked example to write:** Detect late sensor batches and compare raw vs quarantined output.
- **Assessable practice:** Write a reproducible release packet and defend a recovery criterion.
