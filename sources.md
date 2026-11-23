# Skill and source inventory

## Architecture and precedents

| Source | Reuse | Boundary |
| --- | --- | --- |
| [PaperOrchestra paper](https://arxiv.org/html/2604.05018v1) and [implementation](https://github.com/google-research/paper-orchestra/tree/d9bae997e793a015ed38bb1605be9eb58c00284f) | Structured outline, separate source and figure work, section drafting, refinement and matched evaluation. | Scientific paper generation is a different task. No upstream CLI, API, output text, benchmark results or autorater scores were used for this paper. |
| [AI+1 constitution](https://github.com/nikbearbrown/ai1-cli/blob/main/AI1.md) and [Conductor](https://github.com/nikbearbrown/ai1-cli/blob/main/CONDUCTOR.md) | Preserve generation fallback, artifact passports, the human-only rewrite and current phase gates. | This document changes neither the skill nor the sync manifest. |
| [AI Readiness](https://github.com/nikbearbrown/ai-readiness/tree/2c0c51ef090230aacaf0d45e0b2a141c39e125b6) | Existing audit, suggest, decide, build subskills and ARC checks. | Course-level signs and institutional approvals cannot be inferred from a chapter or a keyword scan. |

## Bear Brown skills to reuse

The focused Hetzner check found a metadata index but no Bear Brown matches or relevant installed skill text in the locations checked. The sources below were verified in the public [Bear Brown Tools collection](https://github.com/nikbearbrown/bear-brown-tools); no claim is made that they were installed or executed on Hetzner.

| Authoring task | Skill |
| --- | --- |
| Shape the textbook and chapter | [Textbook Architecture](https://github.com/nikbearbrown/bear-brown-tools/tree/main/skills/textbook-architecture) uses backward design, sequence and chapter maps. |
| Convert notes and evidence into prose | [Source to Chapter](https://github.com/nikbearbrown/bear-brown-tools/tree/main/skills/source-to-chapter) and [Engineering Textbook Author](https://github.com/nikbearbrown/bear-brown-tools/tree/main/skills/engineering-textbook-author) give chapter structure, worked phenomena and failure analysis. |
| Make bounded exercises | [Socratic Prompt Coach](https://github.com/nikbearbrown/bear-brown-tools/tree/main/skills/socratic-prompt-coach) and [LLM Exercise Design](https://github.com/nikbearbrown/bear-brown-tools/tree/main/skills/llm-exercise-design) scrutinize how much reasoning the tool does. |
| Map course artifacts and policy | [Course Artifacts](https://github.com/nikbearbrown/bear-brown-tools/tree/main/skills/course-artifacts), [Instructional Design Engine](https://github.com/nikbearbrown/bear-brown-tools/tree/main/skills/instructional-design-engine), and [Syllabus Architect](https://github.com/nikbearbrown/bear-brown-tools/tree/main/skills/syllabus-architect). |
| Design and review figures | [Science Figure Intelligence](https://github.com/nikbearbrown/bear-brown-tools/tree/main/skills/science-figure-intelligence); AI+1’s existing in-repo design and accuracy rules govern final figures. A generated figure is not measured data. |
| Review process evidence and the manuscript | [Frictional](https://github.com/nikbearbrown/frictional) keeps process clues distinct from actual learning; [Critique](https://github.com/nikbearbrown/critique) checks the manuscript, methods, and claims. Neither replaces human judgment. |
