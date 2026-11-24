# Codex handoff: consolidate textbooks into AI Plus One editions

Start with Corporate Finance. Then keep working through one comparable course-book family at a time. The deliverable is one maintained **Subject (AI Plus One)** edition per course scope, not a pile of clones and not another parallel copy of the same book. Use the lowercase kebab-case repo slug in the queue (these end in `-ai-one`). Keep the course number in source references, not the book title. Keep “AI” where it is part of the subject name, as in **Validating AI (AI Plus One)**.

## Select the format first

Use the [catalog](book-queue/) to distinguish the three formats. This workflow runs only the [course and textbook queue](book-queue/queue.tsv) and eligible syllabus blueprints. Do not run the [other-format inventory](book-queue/other-formats.tsv), its legacy family keys, or a `workshop-reference` blueprint through full-course production. Popular books are general-audience author projects, without AI Plus One branding. Workshops are short practical sessions or series, sometimes self-study and often noncredit; scope them around a task, a worked example, and a takeaway, not a semester. Work on those formats only under their own editorial brief.

**Validating AI** is the course. **Computational Skepticism** is a separate [popular-book plan](book-queue/computational-skepticism.md) that may share source ideas without replacing or retiring the course.

## Get the inputs

Use the signed-in GitHub account. Do not print credentials. Clone into separate workspaces; never fetch over local author edits.

| Repository | Treatment |
| --- | --- |
| [AI+1 CLI](https://github.com/nikbearbrown/ai1-cli) | Download the updated skill and record the exact revision. Follow its pre-review and existing human release gates. |
| [AI Readiness](https://github.com/nikbearbrown/ai-readiness) | Download the audit tool; record the commit actually used. |
| [MBA Corporate Finance](https://github.com/nikbearbrown/mba-corporate-finance) | Main Corporate Finance source candidate: public book with 15 chapters and supplements. At inventory time main began at `a7973887`. |
| [Corporate Finance with AI](https://github.com/nikbearbrown/corporate-finance-with-ai) | Private working edition with the same 15 numbered chapter filenames but different chapter bodies; read with authorized access only. At inventory time main began at `4d36ba0a`. Compare the actual content. Reconcile attribution and reuse rights before copying or releasing anything. |
| [Corporate Finance with Excel, Python and LLMs](https://github.com/nikbearbrown/Corporate-Finance-with-Excel-Python-and-LLMs) | Treat as a source lead for the consolidated [Computational Finance](book-queue/computational-finance.md) labs; consult for Corporate Finance-specific examples where appropriate. The TOC differs and the draft has one substantive chapter plus extras. Do not infer retirement or reuse rights. At inventory time main began at `5dcd6841`. |
| [AI for Education](https://github.com/nikbearbrown/ai-for-education) | Use its book and course indexes to discover candidates, not as proof of duplication or reuse rights. |

Start with the Blueprint link in the catalog row. The [editorial blueprint set](book-queue/editorial-blueprints/) fills planning gaps; the syllabus plans and [local Blueprint inventory](book-queue/local-blueprints/) point to more developed work. Reuse existing full plans rather than scaffolding again. For a compact plan, compare the actual sources, confirm outcomes and assessment, then expand the plan where needed before drafting. Transfer only authorized source material.

Re-check recorded heads and visibility. Pin all actual inputs by full commit. If you lack access to a possible source, report that honestly, do not fabricate its contribution, and keep any retirement decision pending.

## Run a single family

1. **Identify the teaching scope.** Compare learning outcomes, audience, TOCs, chapter bodies, assignments, code/figures, and license and authorship notices. Select one canonical scope and a source to build on. Keep truly distinct courses, supplementary labs, and editions separate. For Corporate Finance, do not fold in introductory finance, Principles of Finance, or Computational Finance because their titles share words.
2. **Make the blueprint.** Map prerequisites, learning outcomes, coverage and sequence. Record the unique material in each edition and choose what to keep, adapt, omit or send to a companion. Where book gates require a human decision, mark it pending rather than signing it yourself.
3. **Build the chapter drafts.** Reuse permissioned rough chapters, lectures, slides, examples and exercises instead of rewriting automatically. Keep provenance at the chapter or section, including source repo, full commit, file/section, permissions, and what changed. Resolve dependencies, do not import secrets, student records, private manuscript text or third-party media into a release merely because a repo provided access.
4. **Check, audit, revise.** Fact-check claims, calculations, citations and worked examples; run AI Readiness; then revise using both reports and recheck changed claims and activities. For finance examples use synthetic or licensed data, document assumptions and recompute worked answers.
5. **Make figures and previews.** Use CAJAL to plan teaching visuals; validate accuracy, captions, accessibility, and rights separately from design/layout. Use the default design or an authorized replacement profile. Produce requested Markdown, EPUB, LaTeX, standalone HTML and IMSCC review proofs where supported. Do not claim Canvas import from a manifest or run a live import.
6. **Hand off to the expert.** Put the editable source, supporting evidence, figures, preview links, and unresolved issues in the new review repo, starting with `corporate-finance-ai-one`. The title is **Corporate Finance (AI Plus One)**. The AI Plus One repository is the public replacement. Prepare review materials in a private workspace. Create or publish the new repo as **public**, with only the approved, rights-cleared edition and public-safe evidence. Never publish the private review packet or private source history. MCP is a handoff channel only if the service is actually configured and verified; otherwise hand off the same packet in the repo. The final pass belongs to the human expert.

## Standardize the book README

Use the [book README standard](book-queue/readme-standard.md) for every book repository. Check the reader-facing table of contents against the actual chapter files before linking a new draft from the catalog.

## Keep the queue moving without breaking old links

Maintain one queue with a row per comparable family: sources and pins, scope, stage, replacement repo, checks, owner decision, and blockers. Use one working family at a time until the first pass is stable. Then start the next blueprint while prior families wait for expert review. Do not start a paid API loop, continuous worker or additional service without a stated budget and user approval.

Use the [course and textbook TSV](book-queue/queue.tsv) as the production order. Corporate Finance is first, followed by the named generic course-to-book priorities and the rest of the mapped families. Treat `ready` as ready for Blueprint review and source pinning, `compare` as edition/scope analysis first, and `hold` as planning only. A Blueprint does not change the route or sign the author gate. If one row is awaiting a decision, record it and go on to the next actionable row. The [source triage](book-queue/source-triage.tsv) preserves unplaced candidates, aliases and backups without turning each into a new book.

## Syllabus-only subjects from Fall 2026 and Spring 2027

Use the [84 completed syllabus Blueprints](book-queue/syllabus-track/blueprints/) as the next candidate pool after the course queue. Skip any plan labeled `workshop-reference` in full-course production. Start from the existing-book mapping, compare routes, and source holds there rather than rerunning every Blueprint. Use the [syllabus track](book-queue/syllabus-track/) for provenance and the original inventory. Map each group to an existing manuscript or course first. If only a usable syllabus is available, create an original scope brief, run Blueprint `/scaffold silent`, then write the first draft in a private workspace and run the normal fact-check, AI Readiness, revision, figures and proof sequence. Silent mode skips conversational intake, not human release approval. Do not create one book per CRN, republish syllabi or claim drafting from a title alone. Log holds and keep going with the next eligible group.

## Publish AI Plus One, then make the superseded source books private

Do not change source repo visibility during discovery, drafting, or waiting for sign-off. First verify the approved replacement is reachable to its intended users, identify affected GitHub Pages/custom domains/forks/collaborators and inbound syllabus, catalog and website links, record exact old repo names and current visibility, migrate affected links and preserve Git history. For each confirmed superseded source book used to create the replacement, **public → private; private → stays private**. For Corporate Finance, the intended repository is public `nikbearbrown/corporate-finance-ai-one`; its confirmed public predecessor `nikbearbrown/mba-corporate-finance` goes private after cutover, and `nikbearbrown/corporate-finance-with-ai` stays private. The Excel/Python/LLMs draft is a possible companion, not a predecessor to retire. Verify the new edition as a signed-out reader. Record the exact retirement list and obtain any required tool approval; pause if an unexpected Pages, fork, or collaborator impact remains unresolved. Never change visibility on unrelated courses, platform/tool repos, clients, companions, organization/shared repos or unresolved editions. Do not delete, rename, force-push or mirror private history into new public repos. Verify the replacement URL and final visibility, report the actual actions, and continue with the next family independently.
