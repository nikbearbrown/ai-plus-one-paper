# Chapter specifications

**Private Blueprint only. Draft route: `hold-source`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Define a mobile task and device constraints

- **Observable capability:** Describe a single task and its success, empty, error and offline outcomes.
- **Teaching blocks:** Small-screen constraints, orientation, touch, accessibility and intermittent connectivity.
- **Original worked example to write:** A rider needs the next shuttle departure while walking between campus buildings.
- **Assessable practice:** Specify the task when the timetable is fresh, missing or stale.

## 2. Prototype and hand off in Figma

- **Observable capability:** Make a testable prototype and convert it to an implementation brief.
- **Teaching blocks:** Reusable components and variants, adaptive layout, navigation, state annotations and accessibility intent.
- **Original worked example to write:** Prototype route search, stop details and a stale timetable indicator.
- **Assessable practice:** Walk the happy path and a failure path; hand off states, labels, expected navigation and acceptance checks. Treat prototype accessibility notes as requirements to test in the actual app.

## 3. Implement the flow in a chosen stack

- **Observable capability:** Implement the Figma flow using the same acceptance checks in one stack.
- **Teaching blocks:** Screen composition, platform navigation, events and state ownership; Swift/iOS, Kotlin/Android or a cross-platform path as optional implementation choices.
- **Original worked example to write:** Translate route-list and route-detail components into views and map state consistently across them.
- **Assessable practice:** Direct an agent to build one bounded interaction. Review its changes and demonstrate the same user task on two screen sizes. Do not require parallel implementations.

## 4. Manage state, data, and interruptions

- **Observable capability:** Preserve user choices and show truthful loading, cached and error states.
- **Teaching blocks:** Persistence boundary, asynchronous requests, cancellation, lifecycle, fixtures and offline policy.
- **Original worked example to write:** Preserve saved routes after relaunch, and show cached departures as stale during an outage.
- **Assessable practice:** Test restart, navigation away during a request and retry against synthetic fixtures.

## 5. Verify accessibility, offline behavior, and release readiness

- **Observable capability:** Demonstrate that the runnable build meets the intent documented in Figma.
- **Teaching blocks:** Simulator/device checks, text scaling, accessible names, screen-reader order, regression evidence and release limits.
- **Original worked example to write:** Verify route selection and the offline alert on two different device configurations.
- **Assessable practice:** Submit the Figma prototype, implementation, and a reproducible evidence checklist. Distinguish local build evidence from platform certification or store release.
