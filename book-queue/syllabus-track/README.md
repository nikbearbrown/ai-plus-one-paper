# Syllabus-led AI Plus One books

This track extends the ordered book queue without turning each section into a book. It covers the public Fall 2026 and Spring 2027 [Newton](http://newton.northeastern.edu/spring2027/) SEIS indexes and the separate set of already found public Fall syllabi from other Northeastern colleges. It is not a census of all courses or all available syllabi at Northeastern. The private [SEIS archive](https://github.com/nikbearbrown/seis-syllabi) holds source files and source-level provenance. Access to this planning repo does not itself grant access to that archive.

- [Newton sections](newton-sections.tsv): offered labels and CRNs as indexed, plus any known corrections; a posted link is not proof of a usable syllabus. Keep multiple sections and terms as provenance.
- [Newton subjects](newton-subjects.tsv): one row per course code and named special topic, with a proposed reader-facing title or a reference to the existing book queue. Identical proposed titles across rows are one comparison group, not multiple new books.
- [Other Fall leads](other-fall-leads.tsv): separate public-course pages and external sources from the earlier search; historical samples, presence-only catalog rows and unlabeled third-party copies do not become draft inputs.
- [Completed private Blueprint handoff](blueprints/): 84 consolidated plans for the drafting session, including exact existing-book targets and source holds. Use this as the current route map.
- [Syllabus queue](syllabus-queue.tsv): grouped subjects in a numbered handoff. Run the numbered course-and-textbook queue first; proceed with eligible syllabus-led groups as time allows. Do not turn a workshop reference into a full course. Keep rows on hold when actual outline evidence is absent. Do not claim that a proposed title is a completed book.

## Evidence counts

The Newton index has 122 Fall section rows (121 unique URLs) and 106 Spring section rows (106 unique URLs). The section table also includes one Fall syllabus verified in the earlier archive but absent from the current Newton links. The broader Fall source set adds 18 leads from outside the Newton collection, including hold-only entries. These are coverage counts, not counts of usable or rights-cleared documents.

## First syllabus-led books to check

Start from these groups when the earlier queue is moving. The evidence column identifies starting sources, not permission to publish.

| Order | Book | Starting evidence and decision |
| --- | --- | --- |
| 1 | Knowledge Graphs and Generative AI (AI Plus One) | Fall DAMG 6310, CRN 21970, from the earlier verified archive. Use the course-information body over the inconsistent heading. Graph modeling, query and grounded retrieval, not general graph search. A seven-chapter private pilot was drafted; reuse it if available rather than starting a duplicate. |
| 2 | Data Engineering for AI (AI Plus One) | Fall DAMG 6300, 21965; compare the additional INFO 7375 sections. One combined scope if evidence supports it. |
| 3 | High-Performance Machine Learning (AI Plus One) | Fall CSYE 7105, 16364; compare Spring 35348 and general high-performance computing before creating a second book. |
| 4 | Generative Modeling (AI Plus One) | CSYE 7380, multiple terms. Verify a common modeling scope across usable sections. Compare the specialized advanced language-model and neural-network candidates. |
| 5 | LLMOps (AI Plus One) | CSYE 7374 named Infrastructure and DevOps with LLMs. Verify the Spring syllabus or inspect the authoritative Fall link; no reuse of meeting-access material. |
| 6 | Designing Scalable and Reliable Software Services (AI Plus One) | INFO 7375 named System Design in the Age of AI. Compare 22278 and 42128. Assess architectural tradeoffs as the core, distinct from agent tool use and experience design. |

For all other candidates, follow the additional run order in the TSV and skip any row that is not actionable. The mapping uses the earliest term and course code as stable tie-breakers. `existing-queue` means feed the existing manuscript, `compare-scope` means check overlap first, and `verify-syllabus-first` means investigate a possible new scope, not that the section has already been validated. `hold` routes do not start drafting. Preserve unsuccessful leads for future checks.

## What the other Codex session should do

1. Start at the [Blueprint handoff](blueprints/) and reuse the completed plan for the subject. Resolve the best matching authorized syllabus in the archive; verify term, course or named topic, section when available, file digest, audience, prerequisite tier and what the document actually teaches. Check multiple sections for real scope differences. Note disagreements and use the verified book or course first if one exists; compare any neighboring rows before starting a new book.
2. If only a syllabus exists, use its factual subject boundaries, prerequisites, topic progression and assessment *types* as a private scope brief. Write an original `book.md` and provisional `outline.md`; separate explicitly supported facts from reasonable proposals. Do not copy the instructor's prose, exercises, grading rules, local logistics, live links or assessments, and do not imply university endorsement. Public availability is not a republication license. Use independent authoritative sources for content and independently designed, synthetic examples.
3. If a plan requires revision, pin the [AI Plus One skill](https://github.com/nikbearbrown/ai1-cli). Follow [Blueprint's `/scaffold silent` procedure](https://github.com/nikbearbrown/ai1-cli/blob/main/conductor/00-blueprint/blueprint-library.md) in the private workspace. Write vision, architecture, chapter specs, risks, and updated outline; mark unsupported decisions `[NEEDS HUMAN INPUT]`, not an invented syllabus outcome or market claim. Silent means no interim intake or conversational gates; it doesn't mean that an author approved the Blueprint.
4. For a syllabus-led group with adequate evidence, write an original book-length first draft with chapter-level objectives, explanations, checked worked examples, exercises and sources. Fact-check, run AI Readiness, revise, then make and check figures and export review proofs under the normal [handoff](../../codex-handoff.md). Track what actually ran. When source or safety limits matter, label a partial draft or hold the affected topic and take the next eligible group. In particular, use defensive or educational framing on security topics, not exploit-development exercises.
5. Leave every new draft private until the author reviews it. No silent signoff, publication, external handoff, Canvas import, access grant, or changes to old repository visibility. The final author edit and existing public replacement policy are unchanged.

New display titles use **Subject (AI Plus One)** without a course code. The course section, term and source URL belong in provenance only.
