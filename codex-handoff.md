# Codex handoff: consolidate textbooks into AI One editions

Start with Corporate Finance. Then keep working through one comparable course-book family at a time. The deliverable is one maintained **Subject AI One** edition per course scope, not a pile of clones and not another parallel copy of the same book. Use a lowercase kebab-case repo slug ending in `-ai-one`.

## Get the inputs

Use the signed-in GitHub account. Do not print credentials. Clone into separate workspaces; never fetch over local author edits.

| Repository | Treatment |
| --- | --- |
| [AI+1 CLI](https://github.com/nikbearbrown/ai1-cli) | Download the updated skill and record the exact revision. Follow its pre-review and existing human release gates. |
| [AI Readiness](https://github.com/nikbearbrown/ai-readiness) | Download the audit tool; record the commit actually used. |
| [MBA Corporate Finance](https://github.com/nikbearbrown/mba-corporate-finance) | Main Corporate Finance source candidate: public book with 15 chapters and supplements. At inventory time main began at `a7973887`. |
| [Corporate Finance with AI](https://github.com/nikbearbrown/corporate-finance-with-ai) | Private working edition with the same 15 numbered chapter filenames but different chapter bodies; read with authorized access only. At inventory time main began at `4d36ba0a`. Compare the actual content. Reconcile attribution and reuse rights before copying or releasing anything. |
| [Corporate Finance with Excel, Python and LLMs](https://github.com/nikbearbrown/Corporate-Finance-with-Excel-Python-and-LLMs) | Inspect as a possible lab companion, not a duplicate to retire. TOC differs and the current draft has only one substantial chapter plus exercises and a cheat sheet. At inventory time main began at `5dcd6841`. |
| [AI for Education](https://github.com/nikbearbrown/ai-for-education) | Use its book and course indexes to discover candidates, not as proof of duplication or reuse rights. |

Re-check recorded heads and visibility. Pin all actual inputs by full commit. If you lack access to a possible source, report that honestly, do not fabricate its contribution, and keep any retirement decision pending.

## Run a single family

1. **Identify the teaching scope.** Compare learning outcomes, audience, TOCs, chapter bodies, assignments, code/figures, and license and authorship notices. Select one canonical scope and a source to build on. Keep truly distinct courses, supplementary labs, and editions separate. For Corporate Finance, do not fold in introductory finance, Principles of Finance, or Computational Finance because their titles share words.
2. **Make the blueprint.** Map prerequisites, learning outcomes, coverage and sequence. Record the unique material in each edition and choose what to keep, adapt, omit or send to a companion. Where book gates require a human decision, mark it pending rather than signing it yourself.
3. **Build the chapter drafts.** Reuse permissioned rough chapters, lectures, slides, examples and exercises instead of rewriting automatically. Keep provenance at the chapter or section, including source repo, full commit, file/section, permissions, and what changed. Resolve dependencies, do not import secrets, student records, private manuscript text or third-party media into a release merely because a repo provided access.
4. **Check, audit, revise.** Fact-check claims, calculations, citations and worked examples; run AI Readiness; then revise using both reports and recheck changed claims and activities. For finance examples use synthetic or licensed data, document assumptions and recompute worked answers.
5. **Make figures and previews.** Use CAJAL to plan teaching visuals; validate accuracy, captions, accessibility, and rights separately from design/layout. Use the default design or an authorized replacement profile. Produce requested Markdown, EPUB, LaTeX, standalone HTML and IMSCC review proofs where supported. Do not claim Canvas import from a manifest or run a live import.
6. **Hand off to the expert.** Put the editable source, supporting evidence, figures, preview links, and unresolved issues in the new review repo, starting with `corporate-finance-ai-one`. The title is **Corporate Finance AI One**. Keep the initial repo private until rights and human review support the intended release. MCP is a handoff channel only if the service is actually configured and verified; otherwise hand off the same packet in the repo. The final pass belongs to the human expert.

## Keep the queue moving without breaking old links

Maintain one queue with a row per comparable family: sources and pins, scope, stage, replacement repo, checks, owner decision, and blockers. Use one working family at a time until the first pass is stable. Then start the next blueprint while prior families wait for expert review. Do not start a paid API loop, continuous worker or additional service without a stated budget and user approval.

Suggested next families for **verification** before selection:

- **Principles of Finance:** compare `nikbearbrown/mba-finance` and `nikbearbrown/principles-finance-with-llms`. Keep separate from Corporate Finance.
- **Computational Finance:** compare `nikbearbrown/mba-computational-finance` and `nikbearbrown/computational-finance-with-ai` (private). Keep the separately scoped `nikbearbrown/computational-finance` out until its scope is confirmed.

- **Introductory Statistics:** compare `nikbearbrown/math-statistics` and `nikbearbrown/introductory-statistics-bundle-with-llms`; confirm the matching chapter names are the same course scope.
- **Contemporary Mathematics:** compare `nikbearbrown/math-contemporary-mathematics` and `nikbearbrown/contemporary-mathematics-with-llms`.
- **Algorithms:** compare `nikbearbrown/algorithms-vol1` against `nikbearbrown/algorithms-vol1-with-llms`, and Vol. 2 against `nikbearbrown/algorithms-vol2-with-llms`. Decide separately whether Vols. 1 and 2 are distinct course scopes. Keep the INFO 6205 course material separate unless confirmed otherwise.

## Making confirmed old repos private is the last step

Do not change source repo visibility during discovery, drafting, or waiting for sign-off. First verify the approved replacement is reachable to its intended users, identify affected GitHub Pages/custom domains/forks/collaborators and inbound syllabus, catalog and website links, record exact old repo names and current visibility, migrate affected links and preserve Git history. Show Nik one exact retirement list and obtain any required confirmations before making **only those confirmed superseded book repositories** private. Never change visibility on unrelated courses, platform/tool repos, clients, companions, organization/shared repos or unresolved editions. Do not delete, rename, force-push or mirror private history into new public repos. Verify the replacement URL and final visibility, report the actual actions, and continue with the next family independently.
