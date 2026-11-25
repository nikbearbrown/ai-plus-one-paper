# AI+1: An Auditable Workflow for Drafting AI-Ready Textbook Chapters

[Read the draft](manuscript.md) · [Help with the paper](CONTRIBUTING.md) · [Chapter-drafting protocol](workflow.md)

**We're inviting collaborators.** Review one claim, check a source, or take on one of the tasks listed below. You don't need to review the whole paper to help. To join, follow [Getting started](CONTRIBUTING.md#getting-started) in the contributor guide.

An author-review draft about the existing AI+1 approach and a proposed extension for drafting and auditing an AI-ready chapter.

## Abstract

A textbook chapter can explain a subject accurately without preparing students to work with AI in that subject. Adding a generic prompt does little to close the gap. We propose a chapter authoring workflow that takes an instructor's brief and permitted sources and produces a first draft, a claim ledger, a disciplinary exercise, an independent check, and an AI Readiness evidence report. The design adapts PaperOrchestra's staged drafting, source synthesis, optional figure work, and refinement to teaching. It retains AI+1's human authorship and approval gates. We specify how to compare the workflow with a single-pass draft and the existing AI+1 workflow, holding the underlying model and source access fixed. A local mechanical test is reported separately; it does not establish that the proposed workflow produces better chapters or that students learn more.

## Where the draft is

The draft is [manuscript.md](manuscript.md). It is an author-review draft and reports no comparative results.

## What needs to be done

- Pilot the proposed evaluation to set its statistical power, rubric anchors and cost limits.
- Run the comparison the manuscript specifies. It has not been run.
- Try the chapter-drafting protocol on more chapters and report what evidence it produces.
- Verify the items in the inventory that are still unconfirmed.

## How to contribute

Start with [Getting started](CONTRIBUTING.md#getting-started) in the [contributor guide](CONTRIBUTING.md): read the draft or plan, pick one thing to do, and email Nik to be added as a collaborator. The guide lists each kind of contribution with where to start and what to send, the rules for this repo, how to submit, and how credit and authorship work.

- **A quick contribution:** open an issue about one claim, source or decision. You don't need to review the whole paper.
- **To become an author:** take on a component of the work, help write the paper, approve the final version and agree to be accountable for it. The guide explains each step.

## What is here

- [Manuscript](manuscript.md): research question, architecture, and proposed evaluation.
- [Chapter-drafting protocol](workflow.md): the proposed authoring steps and the required AI Readiness evidence.
- [Skill and evidence inventory](sources.md): what we can reuse and what still needs verification.
- [Draft exports and design profiles](exports-and-design.md): what builds today, draft-proof checks, and default versus custom styling.
- [Codex handoff for the other machine](codex-handoff.md): repo inputs, queue rules, draft production, and safe retirement of duplicate editions.
- [Books, courses, and workshops](book-queue/): the catalog by format and topic, with links to current materials.
- [Local pilot receipt](pilot.md): one constructed chapter and what ARC's automatic check can and cannot establish.

**Critique pass:** standardized the shared outputs, separated blinded chapter review from the audit-document review, and made the evidence-gain and error-floor criteria explicit. Power, rubric anchors, and feasible cost limits still need a pilot.

The implementation is maintained in [AI+1 CLI](https://github.com/nikbearbrown/ai1-cli). Nothing in this paper repo signs an AI+1 gate. The manuscript is not a report of comparative results.
