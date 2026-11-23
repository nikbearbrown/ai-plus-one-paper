# AI Plus One textbook production queue

Build one standalone **Subject (AI Plus One)** book per genuine course scope. Use a subject title that tells a reader what the book teaches. Put university course identifiers in source references, not the title. For example, the INFO 7375 materials feed **Prompt Engineering and Generative AI (AI Plus One)** or **Validating AI (AI Plus One)**, and INFO 6205 feeds **Algorithms (AI Plus One)**. Keep “AI” when it belongs to the subject, as in **Conducting AI (AI Plus One)**. Use the target slug in the queue for GitHub, not the display title.

## What to run

- [Queue](queue.tsv): working order, title, target repository slug, sources to clone or access, and the decision that might stop a family.
- [Source triage](source-triage.tsv): the remaining inventory candidates and exclusions, so overlapping books, separate course materials and uncertain sources are not lost.
- [Codex handoff](../codex-handoff.md): workflow, output and release rules.
- [Syllabus-led extension](syllabus-track/): Fall 2026 and Spring 2027 course evidence, scope mapping and a silent Blueprint route where no manuscript exists.

The production queue is a plan, not a record of books already generated. Work from the top. Move to the next row when a family is waiting for access, rights, a scope decision or the expert's edit; return to the held row once it clears. Do not wait for a book's final approval to inspect the next family. A single row covers one coherent course, not one repository. A related source may help the writer but is not automatically eligible to retire.

## Interpret each row

| State | Action |
| --- | --- |
| Ready | Start the source inventory and blueprint. This is permission to scope work, not rights clearance or permission to publish. |
| Compare | Inspect overlapping editions or course scope first. Use the most complete rights-cleared manuscript as a base. Do not guess or create a rival book if the scope is unresolved. |
| Hold | Plan only until access, manuscript maturity, author rights, or domain review is resolved. Continue with other rows. |

GitHub source names are recorded as owner/repository where known. An unqualified source means the personal `nikbearbrown` account. A `local:` reference means that the initial inventory located a Mac manuscript rather than a verified cloneable upstream; obtain an authorized copy on the other machine before using it. Check current access and pin the actual revisions. Never merge the course's grades, answer keys, student work, credentials or private history into the new repository.

Each approved replacement is public. Only confirmed superseded public **source book** repositories go private, after the new edition is reachable and affected links have been migrated. Private sources stay private. A course site, toolkit, lab companion or app is not retired merely because it contributed material. No deletion. No automatic publication of rough drafts.

## First run

The queue has **138 planned book families**: 37 ready for blueprint work, 57 to compare before drafting, and 44 on hold. The triage table accounts for the 580 supplied GitHub entries plus the spreadsheet error placeholder. Additional known source leads may appear in a queue row. Counts do not represent rights-clearance, books already built, or unique finished manuscripts.

| Order | Book | Start with | Stage |
| --- | --- | --- | --- |
| 1 | **Corporate Finance (AI Plus One)** | `nikbearbrown/mba-corporate-finance`, `nikbearbrown/corporate-finance-with-ai` | compare |
| 2 | **Prompt Engineering and Generative AI (AI Plus One)** | `nikbearbrown/prompt-engineering`, `nikbearbrown/info-7375-prompt-engineering-for-generative-ai` | ready |
| 3 | **Validating AI (AI Plus One)** | `nikbearbrown/computational-skepticism-for-ai` | compare |
| 4 | **Algorithms (AI Plus One)** | `nikbearbrown/Coursera_INFO_6205_Algorithms`, `nikbearbrown/info-6205-algorithms` | compare |
| 5 | **Principles of Finance (AI Plus One)** | `nikbearbrown/mba-finance` | ready |
| 6 | **Introductory Statistics (AI Plus One)** | `nikbearbrown/math-statistics` | ready |
| 7 | **Application Engineering and Development (AI Plus One)** | `nikbearbrown/info-5100-application-engineering-and-development` | compare |
| 8 | **Building Virtual Environments (AI Plus One)** | `nikbearbrown/csye-7270-building-virtual-environments` | ready |
| 9 | **Computational Finance (AI Plus One)** | `nikbearbrown/mba-computational-finance` | ready |
| 10 | **Contemporary Mathematics (AI Plus One)** | `nikbearbrown/math-contemporary-mathematics` | ready |
| 11 | **Conducting AI (AI Plus One)** | `nikbearbrown/info-7375-conducting-ai` | compare |
| 12 | **Design Engineering (AI Plus One)** | `local:design-engineering` | hold |
