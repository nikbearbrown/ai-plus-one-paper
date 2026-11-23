# Chapter specifications

**Private Blueprint only. Draft route: `hold-source`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Swift values and native app structure

- **Observable capability:** Model an app's data and trace an event to its handler.
- **Teaching blocks:** Swift types; optionals; value and reference semantics; project organization.
- **Original worked example to write:** Model shuttle route and departure records with missing-times handling.
- **Assessable practice:** Implement records and a parser that rejects malformed intervals visibly.

## 2. Views, navigation and accessibility

- **Observable capability:** Create a native UI that exposes an understandable path through a task.
- **Teaching blocks:** Native layout; navigation stack; focus and accessibility labels; orientation.
- **Original worked example to write:** Build a route list and a detail screen with a VoiceOver-readable stop summary.
- **Assessable practice:** Demonstrate the task on two simulator sizes and write an accessibility receipt.

## 3. State, persistence and lifecycle

- **Observable capability:** Keep user choices coherent after navigation, suspension and relaunch.
- **Teaching blocks:** State ownership; validation; persistence boundary; lifecycle callbacks.
- **Original worked example to write:** Preserve saved route preferences after app restart without duplicating entries.
- **Assessable practice:** Use a reproducible test to demonstrate restored data and a safe empty-state reset.

## 4. Asynchronous data and release evidence

- **Observable capability:** Show actionable loading, failure and retry behavior in a tested native build.
- **Teaching blocks:** Asynchronous requests; cancellation; fixtures; simulator end-to-end checks.
- **Original worked example to write:** Model an outdated shuttle timetable and recover when an offline fixture returns.
- **Assessable practice:** Prove navigation away cancels work and that a second attempt retains valid cached data.
