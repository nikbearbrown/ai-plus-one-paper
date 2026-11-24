# Chapter specifications

The examples and exercises are proposed original work. They do not reproduce the reference examples, source plots, figures, projects or chapter sequence.

## 1. Choose what to generate
**Capability:** State what belongs in a model call, what belongs in deterministic code, and what stays authored.
**Blocks:** play the authored slice; list mechanics and invariants; distinguish authored, rule-based and learned generation; compare offline and runtime constraints.
**Worked example:** Rotate ferry arrivals by scripted schedule; generate only draft signage; forbid the model from changing fuel and arrival state.
**Exercises:** Trace an authored playthrough. Classify four lighthouse tasks. Defend a no-generation implementation for one task and state a test.

## 2. Set boundaries before creating assets
**Capability:** Turn a creative brief into an acceptance checklist with a provenance record.
**Blocks:** audience and art direction; allowed inputs and rights; rejection criteria; human approval and record retention.
**Worked example:** Two original beacon signs are scored for readability at game scale and whether the source is recorded; reject the prettier sign if attribution is unknown.
**Exercises:** Write a one-paragraph brief. Complete an origin/permission ledger for supplied synthetic assets. Explain when to reject rather than clean up a candidate.

## 3. Keep branching dialogue inside the game state
**Capability:** Verify that generated dialogue cannot bypass authored transitions.
**Blocks:** route graph and prerequisites; request/response schema; immutable game state; authored fail-safe line and consequence tests.
**Worked example:** A ferryman asks to borrow fuel; generated wording may vary, but a dialogue line cannot unlock a fuel transfer.
**Exercises:** Trace two branch choices. Reject a line contradicting inventory. Design a negative test that proves presentation does not write to game state.

## 4. Turn generated art into usable assets
**Capability:** Admit an asset only after checking it in context rather than grading a preview.
**Blocks:** asset brief and engine contract; visual silhouette and scale; safe original materials and attribution; import, alternates, and acceptance record.
**Worked example:** Compare original hazard decals from a small candidate set at intended screen size and with a low-contrast lighting fixture; retain an authored alternate.
**Exercises:** Specify dimensions and format. Document why a candidate fails at intended size. Validate a corrected import against a collision-neutral display scene.

## 5. Check a generated world before a player enters
**Capability:** Separate proposal generation from deterministic validation.
**Blocks:** tagged tiles and constraints; seeds and reproducibility; reachability and rejection; content diversity versus valid play.
**Worked example:** A proposed map has an isolated battery and a reachable alternate. Run the same graph check on both; no assumption that visually adjacent tiles connect.
**Exercises:** Mark walkable routes by hand. Write a test fixture with an unreachable goal. Describe a comparison under fixed seeds and report rejection rates without calling them player ratings.

## 6. Put a time limit on runtime generation
**Capability:** Keep a playable scene responsive when a text service is slow, invalid or missing.
**Blocks:** local request boundary; response validation; timeout and offline fallback; latency and cost measurements by environment.
**Worked example:** After the service misses the scene's illustrative deadline, authored dock dialogue loads without losing the chosen branch.
**Exercises:** Trace the three response paths. Inject a late response in a local stub and verify it cannot overwrite the fallback. Record measured latency and the limits of one local run.

## 7. Test the generated variant against a baseline
**Capability:** Compare two variants using the same acceptance cases.
**Blocks:** matched playthroughs; blocked-path and continuity checks; defect tagging; evaluation versus claims about players.
**Worked example:** Replay two authored and two candidate ferry scenes under the same state, compare contradiction counts, and distinguish tests from user research.
**Exercises:** Produce a test matrix. Find a planted continuity problem. Correct a claim equating fewer detected defects with higher enjoyment.

## 8. Ship a playable slice and an evidence trail
**Capability:** Hand off an original, playable prototype that can be audited and replayed offline.
**Blocks:** assembly and run instructions; provenance and accessibility evidence; deterministic fixtures; review decision and rollback.
**Worked example:** A reviewer runs the slice offline, confirms a blocked unsupported candidate, and reconstructs the rationale from small receipts.
**Exercises:** Make an offline reproduction route. Have a peer reproduce one rejected candidate without a model. Present a release/hold recommendation tied to acceptance criteria.
