# Gemini Notebook for Education

*AI Plus One · Revised opening and edition brief · Private draft for author review*

## Start with one lesson, not one tool

Suppose you are teaching students how to tell whether two sources really disagree. You have a short reading and a class handout. Put those two materials in a Gemini Notebook, ask for one apparent disagreement, and open the cited passages before you use the answer. If the reading describes an average and the handout describes one exceptional case, the sources may be answering different questions. Make that judgment part of the lesson: ask learners to explain the distinction in their own words and point to the evidence.

Gemini Notebook is the standalone research and study tool formerly called NotebookLM. It can help turn a selected collection of materials into something students can query, review, and test themselves against. Source grounding gives you a way to inspect an answer; it does not make the answer correct. Check whether the source imported intact, whether the cited passage supports the claim, and whether the output quietly skipped context that changes the meaning. [Google’s product help](https://support.google.com/gemininotebook/answer/16164461)

### What changed

- **Same notebook, new name.** Google began the rebrand in July 2026 and said old shared notebook and user links would redirect. If you are updating a lesson, show both names once, then use Gemini Notebook. Check that a student with the intended school account can still open the link. [Workspace rebrand announcement](https://workspaceupdates.googleblog.com/2026/07/notebooklm-now-gemini-notebook.html)
- **Notebooks across Google surfaces.** Google documents sync between the standalone tool and the Gemini app. In managed Workspace, the app route depends on both services being enabled. Google subsequently announced an August rollout to AI Mode in Search with market and language limits. The core lesson works in the standalone tool; Search is an optional route, not a dependency. [Workspace rollout](https://workspaceupdates.googleblog.com/2026/09/notebooks-in-gemini-dedicated-workspace-for-focused-organized-work-now-for-schools-and-organizations.html) · [Search rollout](https://blog.google/products-and-platforms/products/search/back-to-school-study-tools/)
- **Code-assisted analysis.** Google announced a cloud computer for code execution inside notebooks, starting with Google AI Ultra and qualifying Workspace business add-ons, followed by a planned web rollout to Pro. Do not assume a school license includes it. Use an optional, synthetic data lab, and use a spreadsheet for the same learning objective if code execution is unavailable. Check the actual institution account before specifying any UI steps or feature entitlement. [Google’s code announcement](https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/#explore-under-the-hood-upgrades) · [School-account feature matrix](https://support.google.com/gemininotebook/answer/16337734)

### Optional lab: verify a result before teaching from it

Give learners a synthetic table from two fictional sections. Section A has 3 correct answers out of 5 attempts; Section B has 2 out of 10. Ask for each rate and the pooled rate. If the school account offers code execution, ask the notebook to show the calculation or code when available. Otherwise use a spreadsheet. Verify the numerators and denominators independently: A is 60%, B is 20%, and the pooled rate is 5/15 or about 33.3%. Averaging the two rates gives 40%, which is not the pooled rate because the sections have different numbers of attempts. Ask students to explain why. This example uses no student records and supports the same assessment without a premium feature.

## How to revise the 14-chapter educator guide

Work from the [educator manuscript](https://github.com/nikbearbrown/notebook-lm-for-education-a-practitioners-guide/tree/908c3f881a9a4b3f9ce54dca50f4eb2546971b22). Keep the [general practitioner guide](https://github.com/nikbearbrown/notebooklm-a-practitioners-guide) a distinct reference. Do not duplicate its product tour or retitle either original repository.

| Source chapters | Revision |
| --- | --- |
| 1–3: Boundaries, first notebook, output choices | Use the new opening. Rewrite absolute statements about source boundaries to identify the surface, selected sources and tools. Have the reader check an import, inspect a citation and identify an unsupported answer before generating learning materials. |
| 4–5: K–12 teaching and learning | Use age-appropriate, teacher-cleared materials. Keep the assignment about explaining and checking evidence, with a no-account or no-feature alternative that meets the same learning goal. |
| 6: Classroom integration | Verify teacher sharing and student access separately in a managed test class. Do not teach Gems instructions as Gemini Notebook instructions. Use [Google’s current student guide](https://support.google.com/edu/classroom/answer/16538778) for the access path. |
| 7–8: Assessment and integrity | Ask learners to show evidence, explain a correction, and disclose tool use. Do not assume platform logs can establish authorship or understanding. |
| 9–10: Higher education | Use a source-comparison exercise and an unaided retrieval check. Add the optional synthetic-data lab above, with independent reproduction. |
| 11–13: Privacy, tool choice, and administrator decisions | Separate service, license, admin enablement, account, age, region, and UI. Treat Gemini app, standalone Notebook, Classroom, and Search as different surfaces. Do not use identifiable grades, submissions, accommodations, credentials, or other protected records in labs. Check source rights and local policy before school use. |
| 14: Capability and evidence | Distinguish documented features, verified local behavior and evidence of educational impact. Do not imply that a generated study guide improves learning without a measured outcome. |

Before a release, verify procedures on the relevant teacher and student accounts with approved sample material; recheck the feature matrix and accessibility; refresh screenshots, front matter, cover, export metadata, and catalog labels together; retain the old name as a discovery term. Follow the [AI Plus One handoff](../codex-handoff.md) for rights, author review, verification, and export. No authenticated classroom or code-execution checks were run for this draft.
