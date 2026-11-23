# AI+1: An Auditable Workflow for Drafting AI-Ready Textbook Chapters

*Working manuscript for author review. The chapter workflow and comparative evaluation are proposed. No effectiveness or student learning results are reported.*

## Abstract

A textbook chapter can explain a subject accurately without preparing students to work with AI in that subject. Adding a generic prompt does little to close the gap. We propose a chapter authoring workflow that takes an instructor's brief and permitted sources and produces a first draft, a claim ledger, a disciplinary exercise, an independent check, and an AI Readiness evidence report. The design adapts PaperOrchestra's staged drafting, source synthesis, optional figure work, and refinement to teaching. It retains AI+1's human authorship and approval gates. We specify how to compare the workflow with a single-pass draft and the existing AI+1 workflow, holding the underlying model and source access fixed. A local mechanical test is reported separately; it does not establish that the proposed workflow produces better chapters or that students learn more.

## 1. What makes a useful first draft?

The unit of work is one chapter for a specified audience, not a book generated end to end. Consider a chapter on graph traversal. A good draft should explain the graph model and its assumptions, give a small example a student can work by hand, and distinguish reachability from a shortest-path claim. If the chapter asks a student to delegate a trace to AI, it should also say which reasoning the student still owns and how to check the answer against the graph. The student should then be able to solve or defend a new case without the tool.

We ask whether an evidence-linked, staged workflow improves **readiness for faculty review** over a single-pass draft or existing AI+1 alone. A useful gain would be more complete, usable evidence for the proposed teaching activities without more unsupported claims, worse content, or disproportionate review time. A fluent but inaccurate chapter, a technically correct chapter with a token AI exercise, and a report that marks a missing syllabus as a pass are all failures.

## 2. What we take from PaperOrchestra

[Song et al. (2026)](https://arxiv.org/html/2604.05018v1) describe an outline that guides literature review and optional plot generation, followed by section writing and iterative refinement. They evaluate scientific manuscript generation with matched baselines, side-by-side comparisons, and ablations. We reuse the separation of responsibilities, the intermediate artifacts, and the evaluation pattern. PaperWritingBench reconstructs source packs from published research papers, so its outcomes do not measure chapter pedagogy or classroom learning. We do not reuse its effect sizes, evaluator scores, or submission-ready premise. No upstream model API or generated literature is required by this draft.

In the [existing AI+1 constitution](https://github.com/nikbearbrown/ai1-cli/blob/main/AI1.md), the human owns the blueprint, rewrite, and gates. The [Conductor](https://github.com/nikbearbrown/ai1-cli/blob/main/CONDUCTOR.md) already separates blueprint, research, draft, human rewrite, fact check, images, and image review. The proposed extension adds a pre-review draft lane: early fact-checking, AI Readiness, an evidence-driven revision, figures and draft exports precede the final expert edit. These are first-draft checks, not replacements for the current tool’s release gates. This paper does not change the existing skill.

## 3. System design

| Stage | Input and operation | Evidence passed forward |
| --- | --- | --- |
| Blueprint | Specify audience, prerequisites, learning outcomes, scope, access constraints, and what students must do without AI. Reuse approved material before generating new content. | Author-approved chapter contract and stable scope identifiers. |
| Research | Use authorized sources, distinguish a supporting passage from a citation string, and log disputes and permission restrictions. Identify likely visual needs at the outline stage; prepare and validate review figures after the two audits and revision. | Versioned source packet, claim ledger, example and visual briefs. |
| Draft | Incorporate relevant rough drafts, lecture notes, slides, examples and exercises from the approved packet before filling gaps: explain, work an example, let the student try, delegate a bounded task, verify, then transfer. Separate examples, student material, and instructor-only answer keys. | Reviewable Markdown, claim anchors, example inputs and expected checks, assessment and rubric proposal. |
| Fact-check | Check the draft’s claims, citations, worked calculations and examples against independent evidence. | Claim-level results and unresolved issues. |
| Readiness review | Run pinned AI Readiness/ARC on a scratch copy. Interpret automatic signals against actual teaching evidence and mark what is missing or owned by the instructor. | Automatic check, qualitative R1–R6 matrix, proposed changes, and unresolved decisions. |
| Revision | Use both reports to revise and recheck changed claims and activities. | Revised rough draft with known issues. |
| Figures and visualizations | Use [CAJAL](https://github.com/nikbearbrown/ai1-cli/blob/main/chapters/88-appendix-cajal.md) to identify where a figure teaches a concept; reuse or make it, then check accuracy, rendering, accessibility, and rights. Use the default design or an instructor-supplied profile. | Figure briefs and assets, separate layout and substance checks, plus captions and alt text. |
| Draft proofs and handoff | Export requested drafts and pass the editable chapter, figures, sources, and review notes to the expert through the proposed MCP. | [Format-specific preview and verification record](exports-and-design.md). |
| Final human pass | The expert reads, checks and edits the complete draft. Rebuild proofs from the new revision. | Human decisions and remaining exceptions, not an agent signature or automatic release. |

The workflow treats drafting as proposing a structure, and review as accepting responsibility for it. Verified artifacts are reused. A disputed fact, unlicensed item, unsafe example, unresolved conflict marker, or a source that cannot be pinned is a reason to hold the affected work rather than fill the gap with invented material. Chapter approval does not authorize asset release, student exposure, or LMS import.

### Consolidating multiple editions

The workflow takes a book family as input when several repositories contain material for the same course. Build the pedagogical blueprint first; then compare existing manuscripts, slides and exercises against it. For each retained section, record which edition and revision it came from, what was reused or adapted, and what the next editor should verify. Do not merge prerequisites, semester scope, or audience merely because two titles share words. A course repository, a lab companion, a dedicated programming edition, and a backup need different treatment. The intended result is one authoritative chapter set per comparable course scope, without treating unused material as permission to delete source history.

A suggested evaluation stratum uses overlapping, permissioned source packets. Measure the coverage of distinct source concepts, unsupported merges, duplicate coverage, and provenance completeness. These are separate from learner outcome measures. Corporate Finance is a proposed first family, not a completed consolidation.

### Built-in readiness review

The [AI Readiness framework](https://github.com/nikbearbrown/ai-readiness/blob/2c0c51ef090230aacaf0d45e0b2a141c39e125b6/docs/framework.md) asks six questions. The chapter packet identifies an evidence location, what it actually demonstrates, what is missing, and who decides for each:

1. **R1, rules and disclosure:** identify the proposed policy and disclosure mechanism. The instructor supplies the actual policy and their own disclosure.
2. **R2, independent first attempt:** put the unaided prediction or worked attempt before prompt exposure where the skill matters.
3. **R3, meaningful AI use:** ask learners to run a bounded discipline-specific task. A supplied AI-like answer can teach auditing but does not demonstrate tool access or engagement.
4. **R4, judgment and verification:** ask learners what looks wrong before checking it against a source, a calculation, test cases, or observed data independent of the model.
5. **R5, graded process:** request a Frictional record covering the attempt, revisions, AI contributions and unresolved uncertainty, with a proposed rubric. Grading claims require evidence from the course.
6. **R6, independent assessment:** include a new case, explanation, or planted-flaw task the learner can complete without AI.

A standalone chapter can contain strong R2 or R4 design evidence while its R1 policy, tool access and R5 grading implementation remain unknown. ARC’s automatic result is a screening record, not a faculty verdict. Packaging success is separate from course approval and from student learning.

## 4. Proposed evaluation

Build a set of permissioned chapter briefs from more than one subject and difficulty level. Each brief has a learner profile, objectives, frozen source packet, and independently authored verification cases. Include sparse and detailed briefs; track open questions rather than give the systems implicit access to missing answers. Keep near-duplicates, shared source packets, and model-exposed reference answers out of held-out tasks. Use synthetic or permissioned examples, not actual student submissions.

Give every arm the same chapter and exercise deliverables, and the same evidence-report fields. Compare three predeclared arms: **A**, a single-pass model draft from the same packet; **B**, the current AI+1 drafting path with its normal gates; and **C**, the same path with explicit evidence handoffs and the built-in readiness review. Give each arm the same allowed inputs and underlying model. Fix a resource budget for the primary comparison and report actual tokens, storage, wall time, and human review time; document where equal budgets are impractical. Preserve unsuccessful drafts and abstentions in the denominator. No arm gets extra human content without measuring it.

The incremental primary contrast is C versus B; C versus A compares the complete workflow with a single pass. Freeze first drafts before substantive human rewrite, with any prior gates and faculty input documented and matched across arms. Normalize chapter and exercise formatting for blinded content review and randomize order within each brief. Evaluate the evidence report's usability separately and acknowledge that its format may reveal the arm. Use independent subject and instructional reviewers; double-score a shared subset and report agreement before discussion. Separately measure faculty time and changes to reach reviewability. Reviewers should examine a chapter and its student-facing exercise, not reward a condition for merely shipping a lengthy audit. Analyze at the brief level, with paired comparisons and uncertainty that respect repeated reviews of a brief. Final sample size and a practically meaningful difference should be set after feasibility estimates and before a confirmatory run.

Primary measures are material factual errors and completion of reviewable, instructionally aligned readiness evidence. Report citation entailment and coverage separately; do not count unknown course-level evidence as a pass. Secondary measures include goal-to-exercise fit, example correctness, whether independent verification catches a known mistake, unaided assessment suitability, accessibility, rights readiness, and time needed for correction. Before the confirmatory run, define a meaningful improvement in readiness evidence and a noninferiority margin or ceiling for material errors; require both. Prespecify the contrast hierarchy and objective-coverage floor. Report errors per draft and per assessed claim along with missing objectives and failed drafts, so brevity or abstention cannot masquerade as correctness. Report outcomes separately rather than combining them into one score. Compare a removal of the readiness stage as a secondary ablation only if costs and assessment support it.

## 5. What the first demonstration establishes

The [local pilot receipt](pilot.md) concerns what the existing ARC tool can extract from a constructed chapter. It is a check of the audit handoff, not an evaluation of model-generated pedagogy or a Canvas deployment. The staged workflow, comparative study, and later learner study remain separate. Report four distinct states: evidence present in a draft, faculty approval, classroom implementation, and measured learning. An unaided task establishes a design feature; only an observed student response can assess whether the learner succeeded. Any learner study would require institutional review as applicable, permission, and an independent outcome measure.

## References

- Yiwen Song, Yale Song, Tomas Pfister and Jinsung Yoon. 2026. [PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://arxiv.org/abs/2604.05018). arXiv preprint.
- Nik Bear Brown. [AI+1 constitution](https://github.com/nikbearbrown/ai1-cli/blob/main/AI1.md) and [Conductor](https://github.com/nikbearbrown/ai1-cli/blob/main/CONDUCTOR.md).
- Nik Bear Brown. [AI Readiness framework](https://github.com/nikbearbrown/ai-readiness/blob/2c0c51ef090230aacaf0d45e0b2a141c39e125b6/docs/framework.md).
