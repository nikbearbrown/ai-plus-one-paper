# Chapter specifications

**Private Blueprint only. Draft route: `hold-source`. Evidence: `no-usable-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Define a model-service contract

- **Observable capability:** Make failure states observable and bounded.
- **Teaching blocks:** request types; response schema; deadline; fallback
- **Original worked example to write:** Fit a fictional office glossary assistant behind a fake model endpoint.
- **Assessable practice:** Annotate behavior for malformed output, refusal and too-late response.

## 2. Control retries and resource spend

- **Observable capability:** Select a deterministic retry/fallback policy under load.
- **Teaching blocks:** timeouts; request IDs; backpressure; fallback
- **Original worked example to write:** Inject duplicate requests and a simulated provider stall.
- **Assessable practice:** Show that a retry storm cannot exceed budget; prove it from redacted request IDs.

## 3. Measure before promoting

- **Observable capability:** Compare pinned versions on a held-out case bank.
- **Teaching blocks:** semantic fixtures; regression; slices; versioning
- **Original worked example to write:** Evaluate two fictional model-provider versions on short support cases.
- **Assessable practice:** Reject a faster variant that silently fails schema checks and explain the gate.

## 4. Roll back and write a clear incident note

- **Observable capability:** Recover from a simulated regression with verifiable state.
- **Teaching blocks:** canary; feature flag; smoke checks; follow-up
- **Original worked example to write:** Observe a fake release worsen the timed-out request share.
- **Assessable practice:** Demonstrate rollback, provide logs and state what wasn't proven.
