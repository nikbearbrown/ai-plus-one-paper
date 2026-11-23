# Chapter specifications

**Private Blueprint only. Draft route: `existing-book`. Evidence: `matched-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. Turn a user need into a domain model

- **Observable capability:** Define entities and rules before choosing screens.
- **Teaching blocks:** actors; use cases; object identity; constraints
- **Original worked example to write:** Model a fictional repair-room loan assignment and late return.
- **Assessable practice:** Add an exception to the workflow without duplicating domain state.

## 2. Draw boundaries the code can enforce

- **Observable capability:** Separate services, data persistence and presentation.
- **Teaching blocks:** interfaces; dependency direction; state ownership; unit tests
- **Original worked example to write:** Implement checkout rules without rendering any user interface.
- **Assessable practice:** Replace storage with an in-memory fake while passing the same tests.

## 3. Validate the whole transaction

- **Observable capability:** Check input, domain rules and recovery on failure.
- **Teaching blocks:** validation; transaction atomicity; rollback; messaging
- **Original worked example to write:** Create two simultaneous requests for one loan slot with an injected storage failure.
- **Assessable practice:** Test invocations preserve consistency and state the expected user response.

## 4. Design a workflow out of components

- **Observable capability:** Connect user actions to domain events and readable feedback.
- **Teaching blocks:** flow diagram; list/detail mapping; empty states; accessibility
- **Original worked example to write:** Design a booking cancel path with no entry on first open.
- **Assessable practice:** Run a scripted event sequence and give evidence of feedback in three states.

## 5. Change the application without guesswork

- **Observable capability:** Use structured regression evidence to decide a refactor.
- **Teaching blocks:** test seams; fixtures; code review; reproducible run
- **Original worked example to write:** Add equipment kit checkout to an existing single-item app.
- **Assessable practice:** Submit a before/after behavior comparison, failing test and verified fix.
