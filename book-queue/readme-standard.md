# Book README standard

A rough draft is not done until its README helps a first-time reader start. Apply this checklist to every assigned book; do not copy generic prose between books.

## Inspect first

Pin the branch you inspect. List the whole tracked tree, not just expected folders. Read the manuscript, chapter headings, blueprint, detailed outline, teaching materials, assessments, assets, and exports that actually exist. Reconcile numbering against the intended reading copy. Compare competing versions using navigation, content, status and source evidence. Flag unresolved duplicates; do not delete, relocate, rename or silently select them.

## Root README

Use the book’s normal title case and these six headings in order:

1. **About the book.** A book-specific paragraph with subject, intended reader, concrete outcome, prerequisites when known, and edition status: blueprint, partial manuscript, rough draft, or reviewed edition.
2. **Start reading.** Direct links to the first written chapter, the complete guide and any usable web/download edition. If no chapter is written, say so and link the blueprint.
3. **Chapter guide.** List every chapter in intended order, grouped in parts. Use the manuscript title without a duplicate number, add one sentence on what it teaches, and link written files directly. Mark outline-only chapters **planned** without fictitious paths. Keep appendices, front matter and alternate material distinct. Put a long guide in `chapters/README.md` and link it prominently.
4. **How to teach or study it.** Explain the sequence, what learners do, and how they demonstrate learning. Link the actual blueprint, outline, syllabus or guide where present. Label a proposed plan as proposed.
5. **What’s in this repo.** Use `Resource | Link | Coverage | Status`, reporting verified counts or ranges for chapters, slides, exercises, quizzes and assessments, answer keys, figures, videos, code, datasets and exports. Distinguish overview decks from chapter decks, plans from finished videos, and web source from a verified live site. Say **not found** when absent; use **planned** only with a plan.
6. **Credits, license, and corrections.** Name only confirmed contributors or maintainers. Link the actual rights notice or license, or state none was found. Give a concrete correction route.

## Layout and verification

Use lowercase kebab-case for new repo names, folders and content files; keep `README.md` and `LICENSE` conventional. Every content folder needs a short README with a real starting point; do not create empty placeholders. Do not rename existing repos or move manuscripts to fit this convention.

Verify every relative link and anchor, reading order, and table count against the target tree. Test a usable edition before calling it live. Check the root as a new reader: within 30 seconds, can you tell what the book is, where to start, and what teaching material exists? Preserve changes to manuscripts, assets and visibility outside this docs scope. Report updated repos and unresolved manuscript or resource questions.
