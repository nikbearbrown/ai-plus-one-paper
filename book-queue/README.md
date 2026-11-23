# AI Plus One textbook production queue

Build one standalone **Subject (AI Plus One)** book per genuine course scope. Use a subject title that tells a reader what the book teaches. Put university course identifiers in source references, not the title. For example, the INFO 7375 materials feed **Prompt Engineering and Generative AI (AI Plus One)** or **Validating AI (AI Plus One)**, and INFO 6205 feeds **Algorithms (AI Plus One)**. Keep “AI” when it belongs to the subject, as in **Conducting AI (AI Plus One)**. Use the target slug in the queue for GitHub, not the display title.

## Browse all titles

- [All 138 book candidates from existing materials](#138-book-candidates-from-existing-materials)
- [All 84 Fall 2026 and Spring 2027 syllabus blueprints](#84-fall-2026-and-spring-2027-syllabus-blueprints)

The two lists overlap. Ten syllabus blueprints explicitly feed a book in the first list; other scopes marked for comparison may also overlap. Do not add the two counts to get a unique-book total. These are plans, not finished manuscripts.

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

## 138 book candidates from existing materials

In working order: **37 ready to scope, 57 to compare, and 44 on hold**. The [working TSV](queue.tsv) gives the primary and related sources and the decision needed for every title. Where a syllabus blueprint already exists, it is linked below.

| Order | Book | Track | Stage | Syllabus blueprint |
| ---: | --- | --- | --- | --- |
| 1 | Corporate Finance (AI Plus One) | Priority | Compare sources |  |
| 2 | Prompt Engineering and Generative AI (AI Plus One) | Priority | Ready to scope | [Open plan](syllabus-track/blueprints/14-prompt-engineering-and-generative-ai/) |
| 3 | Validating AI (AI Plus One) | Priority | Compare sources | [Open plan](syllabus-track/blueprints/13-validating-ai/) |
| 4 | Algorithms (AI Plus One) | Priority | Compare sources | [Open plan](syllabus-track/blueprints/07-algorithms/) |
| 5 | Principles of Finance (AI Plus One) | Business | Ready to scope |  |
| 6 | Introductory Statistics (AI Plus One) | Business | Ready to scope |  |
| 7 | Application Engineering and Development (AI Plus One) | Computing | Compare sources | [Open plan](syllabus-track/blueprints/09-application-engineering-and-development/) |
| 8 | Building Virtual Environments (AI Plus One) | Computing | Ready to scope | [Open plan](syllabus-track/blueprints/08-building-virtual-environments/) |
| 9 | Computational Finance (AI Plus One) | Business | Ready to scope |  |
| 10 | Contemporary Mathematics (AI Plus One) | Business | Ready to scope |  |
| 11 | Conducting AI (AI Plus One) | Computing | Compare sources |  |
| 12 | Design Engineering (AI Plus One) | Priority | On hold | [Open plan](syllabus-track/blueprints/69-design-engineering/) |
| 13 | Game AI (AI Plus One) | Priority | Compare sources |  |
| 14 | Game Reinforcement Learning (AI Plus One) | Priority | On hold |  |
| 15 | Principles of Accounting (AI Plus One) | Business | Ready to scope |  |
| 16 | Principles of Management (AI Plus One) | Business | Ready to scope |  |
| 17 | Principles of Marketing (AI Plus One) | Business | Ready to scope |  |
| 18 | Introduction to Intellectual Property (AI Plus One) | Business | Ready to scope |  |
| 19 | MBA Math (AI Plus One) | Business | Ready to scope |  |
| 20 | Prealgebra (AI Plus One) | Business | Ready to scope |  |
| 21 | College Algebra (AI Plus One) | Business | Ready to scope |  |
| 22 | Calculus (AI Plus One) | Business | Ready to scope |  |
| 23 | Mathematics for Physics Volume 2 (AI Plus One) | Business | Ready to scope |  |
| 24 | Python Programming (AI Plus One) | Computing | Ready to scope |  |
| 25 | Causal Modeling for Business Decisions (AI Plus One) | Computing | Ready to scope |  |
| 26 | Figma Design with AI (AI Plus One) | Computing | Ready to scope |  |
| 27 | AI for Teachers (AI Plus One) | Education | Ready to scope |  |
| 28 | AI for Students (AI Plus One) | Education | Ready to scope |  |
| 29 | Trust the Teacher (AI Plus One) | Education | Ready to scope |  |
| 30 | NotebookLM (AI Plus One) | Education | Ready to scope |  |
| 31 | NotebookLM for Education (AI Plus One) | Education | Ready to scope |  |
| 32 | Claude for Education (AI Plus One) | Education | Ready to scope |  |
| 33 | Claude Code for Teachers (AI Plus One) | Education | Ready to scope |  |
| 34 | Claude Code for Students (AI Plus One) | Education | Ready to scope |  |
| 35 | Codex for Students (AI Plus One) | Education | Ready to scope |  |
| 36 | GitHub Copilot CLI for Students (AI Plus One) | Education | Ready to scope |  |
| 37 | AI for Slides (AI Plus One) | Education | Ready to scope |  |
| 38 | AI for Infographics (AI Plus One) | Education | Ready to scope |  |
| 39 | Research Writing (AI Plus One) | Education | Ready to scope |  |
| 40 | Quantum Mechanics, Volume 1: Foundations (AI Plus One) | Science | Ready to scope |  |
| 41 | Quantum Mechanics, Volume 2: Formalism and the Three-Dimensional Atom (AI Plus One) | Science | Ready to scope |  |
| 42 | Quantum Mechanics, Volume 3: Approximation Methods and Real Systems (AI Plus One) | Science | Ready to scope |  |
| 43 | Quantum Mechanics, Volume 4: Information, Measurement, and Open Systems (AI Plus One) | Science | Ready to scope |  |
| 44 | Quantum Mechanics, Volume 5: Math for Quantum Physics (AI Plus One) | Science | Ready to scope |  |
| 45 | Quantum Mechanics: A Companion Guide (AI Plus One) | Science | Ready to scope |  |
| 46 | Business Ethics (AI Plus One) | Business | Compare sources |  |
| 47 | Business Case Analysis (AI Plus One) | Business | Compare sources |  |
| 48 | Verified Finance with Agents (AI Plus One) | Business | Compare sources |  |
| 49 | Investing in Quantum (AI Plus One) | Business | Compare sources |  |
| 50 | Branding and Marketing (AI Plus One) | Business | Compare sources |  |
| 51 | Social Media Marketing (AI Plus One) | Business | Compare sources |  |
| 52 | Social Media Marketing Platforms (AI Plus One) | Business | Compare sources |  |
| 53 | Healthcare Marketing (AI Plus One) | Business | Compare sources |  |
| 54 | Causal Inference in Pharmaceutical Marketing (AI Plus One) | Business | Compare sources |  |
| 55 | Bayesian Probability (AI Plus One) | Business | Compare sources |  |
| 56 | Mathematics for Physics Volume 1 (AI Plus One) | Business | Compare sources |  |
| 57 | Design of Agentic Systems (AI Plus One) | Computing | Compare sources | [Open plan](syllabus-track/blueprints/58-design-of-agentic-systems/) |
| 58 | Agentic Search and Graphs (AI Plus One) | Computing | Compare sources |  |
| 59 | AI-Assisted Software Engineering (AI Plus One) | Computing | Compare sources |  |
| 60 | Coding Agents and Local Project Workflows (AI Plus One) | Computing | Compare sources |  |
| 61 | AI Systems Validation (AI Plus One) | Computing | Compare sources |  |
| 62 | Intelligence (AI Plus One) | Computing | Compare sources |  |
| 63 | Reinforcement Learning (AI Plus One) | Computing | Compare sources |  |
| 64 | Generative AI for Game Development (AI Plus One) | Computing | Compare sources |  |
| 65 | Agentic Filmmaking (AI Plus One) | Computing | Compare sources |  |
| 66 | Creative Engineering (AI Plus One) | Computing | Compare sources |  |
| 67 | Branding and AI (AI Plus One) | Computing | Compare sources | [Open plan](syllabus-track/blueprints/12-branding-and-ai/) |
| 68 | Creative Direction (AI Plus One) | Computing | Compare sources |  |
| 69 | Data Visualization and Infographics (AI Plus One) | Computing | Compare sources | [Open plan](syllabus-track/blueprints/11-data-visualization-and-infographics/) |
| 70 | Slide Design and Authoring (AI Plus One) | Computing | Compare sources |  |
| 71 | Interactive Visualization with D3 (AI Plus One) | Computing | Compare sources |  |
| 72 | Data Science Engineering (AI Plus One) | Computing | Compare sources | [Open plan](syllabus-track/blueprints/10-data-science-engineering/) |
| 73 | Research Methods in AI (AI Plus One) | Computing | Compare sources |  |
| 74 | Programmable Logic Controller Design (AI Plus One) | Computing | Compare sources |  |
| 75 | AI for Course Design (AI Plus One) | Education | Compare sources |  |
| 76 | Learning Experience Design (AI Plus One) | Education | Compare sources |  |
| 77 | When to Use AI in Learning AI (AI Plus One) | Education | Compare sources |  |
| 78 | AI for Writing (AI Plus One) | Education | Compare sources |  |
| 79 | Research Computing (AI Plus One) | Education | Compare sources |  |
| 80 | Validating AI Output (AI Plus One) | Education | Compare sources |  |
| 81 | Irreducibly Human (AI Plus One) | Education | Compare sources |  |
| 82 | Statistics with AI (AI Plus One) | Education | Compare sources |  |
| 83 | Managerial Economics (AI Plus One) | Education | Compare sources |  |
| 84 | Intellectual Property (AI Plus One) | Education | Compare sources |  |
| 85 | University Physics (AI Plus One) | Science | Compare sources |  |
| 86 | Classical Mechanics (AI Plus One) | Science | Compare sources |  |
| 87 | Electromagnetism (AI Plus One) | Science | Compare sources |  |
| 88 | Modern Physics (AI Plus One) | Science | Compare sources |  |
| 89 | Optics (AI Plus One) | Science | Compare sources |  |
| 90 | Thermodynamics (AI Plus One) | Science | Compare sources |  |
| 91 | Astronomy (AI Plus One) | Science | Compare sources |  |
| 92 | Quantum Mechanics: Interactive Simulations (AI Plus One) | Science | Compare sources |  |
| 93 | Evolution of Intelligence (AI Plus One) | Science | Compare sources |  |
| 94 | Diversity of Life (AI Plus One) | Science | Compare sources |  |
| 95 | Anatomy and Physiology (AI Plus One) | Science | Compare sources |  |
| 96 | Programmable Logic Controllers and Industrial Automation (AI Plus One) | Science | Compare sources |  |
| 97 | Principles of Economics (AI Plus One) | Business | On hold |  |
| 98 | Business Law (AI Plus One) | Business | On hold |  |
| 99 | Introduction to Finance (AI Plus One) | Business | On hold |  |
| 100 | Corporate Finance with Excel and Python (AI Plus One) | Business | On hold |  |
| 101 | Computational Finance with Python (AI Plus One) | Business | On hold |  |
| 102 | Computational Marketing (AI Plus One) | Business | On hold |  |
| 103 | Economics of Happiness (AI Plus One) | Business | On hold |  |
| 104 | Economics (AI Plus One) | Business | On hold |  |
| 105 | Computational Finance Methods (AI Plus One) | Business | On hold |  |
| 106 | Algebra (AI Plus One) | Business | On hold |  |
| 107 | Animation with Blender (AI Plus One) | Computing | On hold |  |
| 108 | Interactive Storytelling (AI Plus One) | Computing | On hold |  |
| 109 | AI in Everyday Life (AI Plus One) | Computing | On hold |  |
| 110 | College Success (AI Plus One) | Education | On hold |  |
| 111 | The Learning Engineer (AI Plus One) | Education | On hold |  |
| 112 | Codex for Teachers (AI Plus One) | Education | On hold |  |
| 113 | GitHub Copilot CLI for Teachers (AI Plus One) | Education | On hold |  |
| 114 | Figma for Educational AI (AI Plus One) | Education | On hold |  |
| 115 | Work and AI (AI Plus One) | Education | On hold |  |
| 116 | Causal Inference (AI Plus One) | Education | On hold |  |
| 117 | World History (AI Plus One) | Education | On hold |  |
| 118 | United States History (AI Plus One) | Education | On hold |  |
| 119 | American Government (AI Plus One) | Education | On hold |  |
| 120 | Psychology (AI Plus One) | Education | On hold |  |
| 121 | Music, Imitation, and AI (AI Plus One) | Education | On hold |  |
| 122 | College Physics: Mechanics and Waves (AI Plus One) | Science | On hold |  |
| 123 | Quantum Computing (AI Plus One) | Science | On hold |  |
| 124 | Biology (AI Plus One) | Science | On hold |  |
| 125 | Cell Biology (AI Plus One) | Science | On hold |  |
| 126 | Genetics and Evolution (AI Plus One) | Science | On hold |  |
| 127 | Animal Physiology (AI Plus One) | Science | On hold |  |
| 128 | Microbiology (AI Plus One) | Science | On hold |  |
| 129 | Cancer Biology (AI Plus One) | Science | On hold |  |
| 130 | Computational Cancer Biology (AI Plus One) | Science | On hold |  |
| 131 | Cancer Biology and Therapeutics (AI Plus One) | Science | On hold |  |
| 132 | Cancer Medicine (AI Plus One) | Science | On hold |  |
| 133 | Cancer Nanomedicine (AI Plus One) | Science | On hold |  |
| 134 | Cancer Research (AI Plus One) | Science | On hold |  |
| 135 | Imaging in Cancer and Nanomedicine (AI Plus One) | Science | On hold |  |
| 136 | Cancer: Foundations to Therapy (AI Plus One) | Science | On hold |  |
| 137 | Electron Microscopy (AI Plus One) | Science | On hold |  |
| 138 | Organic Chemistry (AI Plus One) | Science | On hold |  |

## 84 Fall 2026 and Spring 2027 syllabus blueprints

Click any title to read its blueprint, including the chapter outline and source notes. A candidate for a private draft still needs source and rights checks; a hold is not permission to draft. See [scope and consolidation notes](syllabus-track/blueprints/merge-log.md). Gaps in the blueprint IDs are from merged plans.

| ID | Book and blueprint | Drafting route | Planned chapters |
| ---: | --- | --- | ---: |
| 1 | [Knowledge Graphs and Generative AI (AI Plus One)](syllabus-track/blueprints/01-knowledge-graphs-and-generative-ai/) | Reuse the private pilot | 7 |
| 2 | [Data Engineering for AI (AI Plus One)](syllabus-track/blueprints/02-data-engineering-for-ai/) | Compare with related books | 6 |
| 3 | [High-Performance Machine Learning (AI Plus One)](syllabus-track/blueprints/03-high-performance-machine-learning/) | Candidate for a private draft | 6 |
| 4 | [Generative Modeling (AI Plus One)](syllabus-track/blueprints/04-generative-modeling/) | Candidate for a private draft | 6 |
| 5 | [LLMOps (AI Plus One)](syllabus-track/blueprints/05-llmops/) | On hold pending source or scope | 4 |
| 6 | [Systems Design (AI Plus One)](syllabus-track/blueprints/06-systems-design/) | Candidate for a private draft | 5 |
| 7 | [Algorithms (AI Plus One)](syllabus-track/blueprints/07-algorithms/) | Use the existing book plan | 6 |
| 8 | [Building Virtual Environments (AI Plus One)](syllabus-track/blueprints/08-building-virtual-environments/) | Use the existing book plan | 5 |
| 9 | [Application Engineering and Development (AI Plus One)](syllabus-track/blueprints/09-application-engineering-and-development/) | Use the existing book plan | 5 |
| 10 | [Data Science Engineering (AI Plus One)](syllabus-track/blueprints/10-data-science-engineering/) | Use the existing book plan | 6 |
| 11 | [Data Visualization and Infographics (AI Plus One)](syllabus-track/blueprints/11-data-visualization-and-infographics/) | Use the existing book plan | 5 |
| 12 | [Branding and AI (AI Plus One)](syllabus-track/blueprints/12-branding-and-ai/) | Use the existing book plan | 5 |
| 13 | [Validating AI (AI Plus One)](syllabus-track/blueprints/13-validating-ai/) | Use the existing book plan | 5 |
| 14 | [Prompt Engineering and Generative AI (AI Plus One)](syllabus-track/blueprints/14-prompt-engineering-and-generative-ai/) | Use the existing book plan | 5 |
| 15 | [Discrete Structures (AI Plus One)](syllabus-track/blueprints/15-discrete-structures/) | Candidate for a private draft | 5 |
| 16 | [Distributed Systems (AI Plus One)](syllabus-track/blueprints/16-distributed-systems/) | Candidate for a private draft | 5 |
| 17 | [Foundations of Artificial Intelligence (AI Plus One)](syllabus-track/blueprints/17-foundations-of-artificial-intelligence/) | Candidate for a private draft | 5 |
| 18 | [Computer Systems (AI Plus One)](syllabus-track/blueprints/18-computer-systems/) | Candidate for a private draft | 5 |
| 19 | [Object-Oriented Design and Design Patterns (AI Plus One)](syllabus-track/blueprints/19-object-oriented-design-and-design-patterns/) | Candidate for a private draft | 9 |
| 20 | [Computer Networks and Cloud Computing (AI Plus One)](syllabus-track/blueprints/20-computer-networks-and-cloud-computing/) | Candidate for a private draft | 5 |
| 22 | [Big Data Engineering with Scala (AI Plus One)](syllabus-track/blueprints/22-big-data-engineering-with-scala/) | Candidate for a private draft | 5 |
| 23 | [DevOps (AI Plus One)](syllabus-track/blueprints/23-devops/) | On hold pending source or scope | 4 |
| 24 | [Software Testing (AI Plus One)](syllabus-track/blueprints/24-software-testing/) | On hold pending source or scope | 4 |
| 25 | [Database Design and Data Management (AI Plus One)](syllabus-track/blueprints/25-database-design-and-data-management/) | Candidate for a private draft | 5 |
| 26 | [Big Data Systems and Analytics (AI Plus One)](syllabus-track/blueprints/26-big-data-systems-and-analytics/) | On hold pending source or scope | 4 |
| 27 | [Data Architecture for Business Intelligence (AI Plus One)](syllabus-track/blueprints/27-data-architecture-for-business-intelligence/) | Candidate for a private draft | 5 |
| 28 | [Neural Modeling (AI Plus One)](syllabus-track/blueprints/28-neural-modeling/) | Candidate for a private draft | 5 |
| 29 | [Business Analysis and Information Engineering (AI Plus One)](syllabus-track/blueprints/29-business-analysis-and-information-engineering/) | Candidate for a private draft | 5 |
| 30 | [Software Quality Engineering (AI Plus One)](syllabus-track/blueprints/30-software-quality-engineering/) | Candidate for a private draft | 5 |
| 31 | [Mobile App Development with Swift (AI Plus One)](syllabus-track/blueprints/31-mobile-app-development-with-swift/) | On hold pending source or scope | 4 |
| 32 | [Operational Risk Engineering (AI Plus One)](syllabus-track/blueprints/32-operational-risk-engineering/) | Candidate for a private draft | 4 |
| 33 | [Business Process Engineering (AI Plus One)](syllabus-track/blueprints/33-business-process-engineering/) | Candidate for a private draft | 4 |
| 34 | [Industry Project Practicum (AI Plus One)](syllabus-track/blueprints/34-industry-project-practicum/) | Candidate for a private draft | 4 |
| 35 | [Cybersecurity Governance, Risk, and Compliance (AI Plus One)](syllabus-track/blueprints/35-cybersecurity-governance-risk-and-compliance/) | Candidate for a private draft | 4 |
| 36 | [Neural Networks (AI Plus One)](syllabus-track/blueprints/36-neural-networks/) | On hold pending source or scope | 5 |
| 37 | [Neurosymbolic AI (AI Plus One)](syllabus-track/blueprints/37-neurosymbolic-ai/) | Candidate for a private draft | 4 |
| 38 | [Semantic Intelligence in Language Models (AI Plus One)](syllabus-track/blueprints/38-semantic-intelligence-in-language-models/) | Candidate for a private draft | 4 |
| 39 | [Number Theory (AI Plus One)](syllabus-track/blueprints/39-number-theory/) | Candidate for a private draft | 9 |
| 41 | [Elliptic Curves and Modular Forms (AI Plus One)](syllabus-track/blueprints/41-elliptic-curves-and-modular-forms/) | Candidate for a private draft | 5 |
| 42 | [Computational Network Science (AI Plus One)](syllabus-track/blueprints/42-computational-network-science/) | Candidate for a private draft | 5 |
| 43 | [Telecommunications and Network Infrastructure (AI Plus One)](syllabus-track/blueprints/43-telecommunications-and-network-infrastructure/) | Candidate for a private draft | 4 |
| 44 | [Internet Protocols and Architecture (AI Plus One)](syllabus-track/blueprints/44-internet-protocols-and-architecture/) | On hold pending source or scope | 5 |
| 45 | [Linux for Network Engineers (AI Plus One)](syllabus-track/blueprints/45-linux-for-network-engineers/) | Candidate for a private draft | 5 |
| 46 | [Network Security (AI Plus One)](syllabus-track/blueprints/46-network-security/) | On hold pending source or scope | 5 |
| 47 | [Infrastructure Automation (AI Plus One)](syllabus-track/blueprints/47-infrastructure-automation/) | On hold pending source or scope | 5 |
| 48 | [Machine Learning for the Internet of Things (AI Plus One)](syllabus-track/blueprints/48-machine-learning-for-the-internet-of-things/) | On hold pending source or scope | 5 |
| 49 | [Connected Devices (AI Plus One)](syllabus-track/blueprints/49-connected-devices/) | Candidate for a private draft | 5 |
| 50 | [Embedded Systems for the Internet of Things (AI Plus One)](syllabus-track/blueprints/50-embedded-systems-for-the-internet-of-things/) | Candidate for a private draft | 5 |
| 51 | [5G Networks and Services (AI Plus One)](syllabus-track/blueprints/51-5g-networks-and-services/) | On hold pending source or scope | 5 |
| 52 | [Cryptography (AI Plus One)](syllabus-track/blueprints/52-cryptography/) | Candidate for a private draft | 5 |
| 53 | [Managing Information Systems Development (AI Plus One)](syllabus-track/blueprints/53-managing-information-systems-development/) | Candidate for a private draft | 5 |
| 54 | [Introduction to Program Design and Implementation (AI Plus One)](syllabus-track/blueprints/54-introduction-to-program-design-and-implementation/) | Compare with related books | 4 |
| 55 | [Web Development (AI Plus One)](syllabus-track/blueprints/55-web-development/) | Compare with related books | 5 |
| 56 | [Foundations of Trustworthy AI (AI Plus One)](syllabus-track/blueprints/56-foundations-of-trustworthy-ai/) | Compare with related books | 5 |
| 57 | [User Experience Design and Testing (AI Plus One)](syllabus-track/blueprints/57-user-experience-design-and-testing/) | Compare with related books | 5 |
| 58 | [Design of Agentic Systems (AI Plus One)](syllabus-track/blueprints/58-design-of-agentic-systems/) | Use the existing book plan | 5 |
| 59 | [Data Science Engineering with Python (AI Plus One)](syllabus-track/blueprints/59-data-science-engineering-with-python/) | Compare with related books | 5 |
| 60 | [Designing and Prototyping Optical Systems (AI Plus One)](syllabus-track/blueprints/60-designing-and-prototyping-optical-systems/) | Compare with related books | 5 |
| 61 | [Research Methods in Design and Media (AI Plus One)](syllabus-track/blueprints/61-research-methods-in-design-and-media/) | Compare with related books | 5 |
| 62 | [Web Design and User Experience Engineering (AI Plus One)](syllabus-track/blueprints/62-web-design-and-user-experience-engineering/) | Compare with related books | 5 |
| 63 | [Advanced Language Models (AI Plus One)](syllabus-track/blueprints/63-advanced-language-models/) | Compare with related books | 5 |
| 64 | [Trading System Engineering (AI Plus One)](syllabus-track/blueprints/64-trading-system-engineering/) | Compare with related books | 5 |
| 65 | [Enterprise AI Architecture (AI Plus One)](syllabus-track/blueprints/65-enterprise-ai-architecture/) | Compare with related books | 5 |
| 66 | [Building AI Applications (AI Plus One)](syllabus-track/blueprints/66-building-ai-applications/) | Compare with related books | 5 |
| 67 | [User Experience Design for AI (AI Plus One)](syllabus-track/blueprints/67-user-experience-design-for-ai/) | Compare with related books | 5 |
| 68 | [Application Modeling and Design (AI Plus One)](syllabus-track/blueprints/68-application-modeling-and-design/) | Compare with related books | 5 |
| 69 | [Design Engineering (AI Plus One)](syllabus-track/blueprints/69-design-engineering/) | Use the existing book plan | 5 |
| 70 | [Data and Context Engineering for Agentic AI (AI Plus One)](syllabus-track/blueprints/70-data-and-context-engineering-for-agentic-ai/) | Compare with related books | 5 |
| 71 | [AI Agent Infrastructure (AI Plus One)](syllabus-track/blueprints/71-ai-agent-infrastructure/) | On hold pending source or scope | 4 |
| 72 | [Self-Improving AI (AI Plus One)](syllabus-track/blueprints/72-self-improving-ai/) | On hold pending source or scope | 4 |
| 73 | [Machine Learning for Medical Devices (AI Plus One)](syllabus-track/blueprints/73-machine-learning-for-medical-devices/) | On hold pending source or scope | 4 |
| 74 | [High-Performance Computing for AI (AI Plus One)](syllabus-track/blueprints/74-high-performance-computing-for-ai/) | On hold pending source or scope | 4 |
| 75 | [Natural Language Engineering (AI Plus One)](syllabus-track/blueprints/75-natural-language-engineering/) | On hold pending source or scope | 4 |
| 76 | [Data Architecture and Governance (AI Plus One)](syllabus-track/blueprints/76-data-architecture-and-governance/) | On hold pending source or scope | 4 |
| 77 | [Compilers (AI Plus One)](syllabus-track/blueprints/77-compilers/) | Candidate for a private draft | 5 |
| 78 | [Deep Learning (AI Plus One)](syllabus-track/blueprints/78-deep-learning/) | Compare with related books | 5 |
| 79 | [Fintech and Financial Innovation (AI Plus One)](syllabus-track/blueprints/79-fintech-and-financial-innovation/) | On hold pending source or scope | 4 |
| 80 | [Global Perspectives on Discrimination and Health (AI Plus One)](syllabus-track/blueprints/80-global-perspectives-on-discrimination-and-health/) | On hold pending source or scope | 4 |
| 81 | [Enterprise Software Design (AI Plus One)](syllabus-track/blueprints/81-enterprise-software-design/) | On hold pending source or scope | 4 |
| 82 | [Operating Systems (AI Plus One)](syllabus-track/blueprints/82-operating-systems/) | On hold pending source or scope | 4 |
| 83 | [Software Engineering (AI Plus One)](syllabus-track/blueprints/83-software-engineering/) | On hold pending source or scope | 4 |
| 84 | [Accounting and Budgeting for Engineers (AI Plus One)](syllabus-track/blueprints/84-accounting-and-budgeting-for-engineers/) | On hold pending source or scope | 4 |
| 85 | [Technical Communication for Engineers (AI Plus One)](syllabus-track/blueprints/85-technical-communication-for-engineers/) | On hold pending source or scope | 4 |
| 86 | [Medical Device Software Engineering (AI Plus One)](syllabus-track/blueprints/86-medical-device-software-engineering/) | On hold pending source or scope | 4 |
