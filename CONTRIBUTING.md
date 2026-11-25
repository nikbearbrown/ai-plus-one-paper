# Help write the AI+1 paper

*AI+1: An Auditable Workflow for Drafting AI-Ready Textbook Chapters* describes a way to draft a textbook chapter with AI so that each step leaves evidence a reviewer can check. The draft is in [manuscript.md](manuscript.md).

**Where it stands:** this is an author-review draft. It proposes an evaluation and does not report comparative results. One pilot chapter has been built ([pilot.md](pilot.md)). The evaluation's statistical power, rubric anchors and cost limits still need a pilot.

**If you have an hour:** read one section of the [manuscript](manuscript.md) and [open an issue](https://github.com/nikbearbrown/ai-plus-one-paper/issues/new) with one claim you would keep, change or qualify.

## Pick a way to help

| Contribution | Where to start | What to send |
|---|---|---|
| **Review a section** | [manuscript.md](manuscript.md) | A missing argument, an alternative explanation, or a claim the pilot does not support. |
| **Critique the proposed evaluation** | Section 4 of the manuscript | Is the comparison fair? Propose rubric anchors, a sample size with its reasoning, or a cheaper design that answers the same question. |
| **Try the protocol on a chapter** | [workflow.md](workflow.md) | Draft one chapter by following the steps. Report where a step was unclear, what evidence it produced, and how long it took. Use a subject you can judge. |
| **Review the pilot** | [pilot.md](pilot.md) and [pilot-chapter.md](pilot-chapter.md) | What the pilot does and does not establish, and any error in the chapter that the automatic check missed. |
| **Verify the inventory** | [sources.md](sources.md) | Pick an item marked as needing verification. Confirm or correct it with a link. |
| **Add related work** | Section 2 and the references | A primary source on AI-assisted writing workflows or textbook quality, with the claim it supports or contradicts. |

## What makes a review useful

- **Start from a specific sentence, step or table.** Show your evidence and say what you would change.
- **Don't report results the paper doesn't have.** The manuscript makes no comparative claim yet. Keep proposals and findings apart.
- **The catalog is not the paper.** The `book-queue/` folder lists books and courses for production. Changes there are not contributions to the paper.
- **Pull before you edit.** More than one coding agent works in this repo.
- **The tool lives elsewhere.** Bugs and features for the implementation go to the [AI+1 CLI](https://github.com/nikbearbrown/ai1-cli).

## How to submit

For a discussion, [open an issue](https://github.com/nikbearbrown/ai-plus-one-paper/issues/new) with the file or section, your evidence, and a proposed next step. For an edit, fork, branch, and open a focused pull request. Say what you changed and how you checked it. If you use an AI-generated answer, verify its citations and claims before submitting it.

If you want to collaborate beyond a single contribution, open an issue describing what you'd like to take on, and read [Credit and what we expect from authors](#credit-and-what-we-expect-from-authors) first.

## Credit and what we expect from authors

The author list isn't decided yet. We follow [Yale's guidance on authorship](https://provost.yale.edu/policies/academic-integrity/guidance-authorship-scholarly-or-scientific-publications). Under it, an author has done **all four** of these:

1. **Contributed to a component of the work:** its conception, design, conduct, analysis, or interpretation of at least part of the results.
2. **Helped write the paper:** drafted part of it, or revised it for substance, not just copy edits.
3. **Approved the final version** before submission.
4. **Agreed to be accountable** for the work, including helping answer questions about its accuracy or integrity.

Some contributions are valuable but don't by themselves make someone an author: a single issue, a copy edit, or one verified inventory item. Everyone who contributes that way is thanked by name in the acknowledgments, unless they ask not to be. To be an author, take on a component, such as running the protocol on a set of chapters and reporting the evidence, building the evaluation rubric, or carrying out the blinded review, and then do the writing, approval and accountability steps too. An AI model can't be an author, since it can't approve the paper or answer for it.

If you want to be an author, we expect you to:

- **Read the whole paper,** not just your section. You're putting your name on all of it.
- **Think about it, then give feedback.** Does the method answer the question? Are the comparisons fair? Do the numbers in the text match the tables, figures and data?
- **Suggest changes when they matter.** Don't make a suggestion just to have made one. If you find nothing to change, say so; that's a useful answer. A real problem, raised clearly with a proposed fix, is the most valuable thing you can give.
- **Disclose AI assistance.** AI tools are fine for code and drafting, but say where you used them. You stay accountable for everything you contribute.
- **Keep a record of what you did:** what, when, and where it lives (issue, pull request, commit, figure). The paper's contribution statement is drawn from it and lists each author's [CRediT roles](https://credit.niso.org/).
- **Sign off only when you can stand behind it.** Before submission, every author confirms in writing that they have read the full paper, agree with it, and accept accountability for it. If something is wrong or unclear, say so before approval, not after publication.

Raise authorship early, and we'll revisit it as roles change. Author order follows contribution. If you think your work merits authorship and it isn't reflected, say so before the final draft. Sending an issue or pull request does not by itself settle authorship.

## Licence

No licence has been chosen for this repo yet. Until one is, ask before reusing its text or data elsewhere.
