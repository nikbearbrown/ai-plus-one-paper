# Fall 2026 and Spring 2027 syllabus Blueprints

**84 private Blueprints**, consolidating 86 input scope rows. These are plans, not manuscripts. The [canonical AI Plus One Blueprint](https://github.com/nikbearbrown/ai1-cli/blob/e01147c0fee59516ebfc8410d29e98aa52560f3b/conductor/00-blueprint/blueprint-library.md#scaffold--cowork-native-planning-file-synthesis) silent-mode format produces vision, learning architecture, chapter specifications and risks, plus a brief, outline and source register per title. Every plan separates observed evidence from proposed teaching, examples and assessments.

- [Machine-readable handoff](index.tsv) and [prior syllabus queue](../syllabus-queue.tsv).
- [Consolidation decisions](merge-log.md).
- Counts by evidence: 59 matched-source, 16 no-usable-source, 9 tentative-source.
- Counts by route: 1 reuse-private-pilot, 17 compare-scope, 31 ready-for-draft-review, 25 hold-source, 10 existing-book.
- Input assignments use the physical row number of the prior TSV (excluding header), not the first numeric column. The [prior ordered book queue](../../queue.tsv) remains unchanged.

## How the drafting session should use this packet

1. Reuse the Knowledge Graphs pilot and attach `existing-book` plans to the corresponding existing manuscripts. Read the actual manuscript and source rights before adapting.
2. In the original syllabus order, take `ready-for-draft-review` plans as private drafting candidates after checking the actual source, rights and open decisions. For `compare-scope`, decide whether to assimilate or use a separate book based on comparable learner outcomes, prerequisite level and assessed artifact, not titles. Use the top-level [Codex handoff](../../../codex-handoff.md).
3. Do not draft from `hold-source` entries. They have candidate architecture and original exercises but no sufficient source match, or an explicit scope conflict. Unavailable and unassigned index entries are not silently treated as new courses.
4. No public release, institutional attribution as author, administrative or grading content, signatures, or manuscript approvals are implied. Do not copy or publicly attach source syllabi.

`matched-source` means at least one selected usable archive/index-matched or a public term-specific syllabus or outline, not every document confirmed or a complete manual section audit. `tentative-source` means only weaker topic evidence. `no-usable-source` means no suitable body was used. Some matched sources retain conflicts noted in their own register.

| ID | Blueprint | Route | Evidence | Existing book queue row |
| ---: | --- | --- | --- | ---: |
| 1 | [Knowledge Graphs and Generative AI (AI Plus One)](01-knowledge-graphs-and-generative-ai/) | `reuse-private-pilot` | matched-source |  |
| 2 | [Data Engineering for AI (AI Plus One)](02-data-engineering-for-ai/) | `compare-scope` | matched-source |  |
| 3 | [High-Performance Machine Learning (AI Plus One)](03-high-performance-machine-learning/) | `ready-for-draft-review` | matched-source |  |
| 4 | [Generative Modeling (AI Plus One)](04-generative-modeling/) | `ready-for-draft-review` | matched-source |  |
| 5 | [LLMOps (AI Plus One)](05-llmops/) | `hold-source` | no-usable-source |  |
| 6 | [Designing Scalable and Reliable Software Services (AI Plus One)](06-systems-design/) | `ready-for-draft-review` | matched-source |  |
| 7 | [Algorithms (AI Plus One)](07-algorithms/) | `existing-book` | matched-source | 4 |
| 8 | [Building Virtual Environments (AI Plus One)](08-building-virtual-environments/) | `existing-book` | tentative-source | 8 |
| 9 | [Application Engineering and Development (AI Plus One)](09-application-engineering-and-development/) | `existing-book` | matched-source | 7 |
| 10 | [Data Science Engineering (AI Plus One)](10-data-science-engineering/) | `existing-book` | matched-source | 72 |
| 11 | [Data Visualization and Infographics (AI Plus One)](11-data-visualization-and-infographics/) | `existing-book` | matched-source | 69 |
| 12 | [Branding and AI (AI Plus One)](12-branding-and-ai/) | `existing-book` | matched-source | 67 |
| 13 | [Validating AI (AI Plus One)](13-validating-ai/) | `existing-book` | matched-source | 3 |
| 14 | [Prompt Engineering and Generative AI (AI Plus One)](14-prompt-engineering-and-generative-ai/) | `existing-book` | matched-source | 2 |
| 15 | [Discrete Structures (AI Plus One)](15-discrete-structures/) | `ready-for-draft-review` | matched-source |  |
| 16 | [Distributed Systems (AI Plus One)](16-distributed-systems/) | `ready-for-draft-review` | matched-source |  |
| 17 | [Foundations of Artificial Intelligence (AI Plus One)](17-foundations-of-artificial-intelligence/) | `ready-for-draft-review` | matched-source |  |
| 18 | [Computer Systems (AI Plus One)](18-computer-systems/) | `ready-for-draft-review` | matched-source |  |
| 19 | [Object-Oriented Design and Design Patterns (AI Plus One)](19-object-oriented-design-and-design-patterns/) | `ready-for-draft-review` | matched-source |  |
| 20 | [Computer Networks and Cloud Computing (AI Plus One)](20-computer-networks-and-cloud-computing/) | `ready-for-draft-review` | matched-source |  |
| 22 | [Big Data Engineering with Scala (AI Plus One)](22-big-data-engineering-with-scala/) | `ready-for-draft-review` | matched-source |  |
| 23 | [DevOps (AI Plus One)](23-devops/) | `hold-source` | tentative-source |  |
| 24 | [Software Testing (AI Plus One)](24-software-testing/) | `hold-source` | no-usable-source |  |
| 25 | [Database Design and Data Management (AI Plus One)](25-database-design-and-data-management/) | `ready-for-draft-review` | matched-source |  |
| 26 | [Big Data Systems and Analytics (AI Plus One)](26-big-data-systems-and-analytics/) | `hold-source` | tentative-source |  |
| 27 | [Data Architecture for Business Intelligence (AI Plus One)](27-data-architecture-for-business-intelligence/) | `ready-for-draft-review` | matched-source |  |
| 28 | [Neural Modeling (AI Plus One)](28-neural-modeling/) | `ready-for-draft-review` | matched-source |  |
| 29 | [Business Analysis and Information Engineering (AI Plus One)](29-business-analysis-and-information-engineering/) | `ready-for-draft-review` | matched-source |  |
| 30 | [Software Quality Engineering (AI Plus One)](30-software-quality-engineering/) | `ready-for-draft-review` | matched-source |  |
| 31 | [Mobile App Development with Swift (AI Plus One)](31-mobile-app-development-with-swift/) | `hold-source` | matched-source |  |
| 32 | [Operational Risk Engineering (AI Plus One)](32-operational-risk-engineering/) | `ready-for-draft-review` | matched-source |  |
| 33 | [Business Process Engineering (AI Plus One)](33-business-process-engineering/) | `ready-for-draft-review` | matched-source |  |
| 34 | [Industry Project Practicum (AI Plus One)](34-industry-project-practicum/) | `ready-for-draft-review` | matched-source |  |
| 35 | [Cybersecurity Governance, Risk, and Compliance (AI Plus One)](35-cybersecurity-governance-risk-and-compliance/) | `ready-for-draft-review` | matched-source |  |
| 36 | [Neural Networks (AI Plus One)](36-neural-networks/) | `hold-source` | tentative-source |  |
| 37 | [Neurosymbolic AI (AI Plus One)](37-neurosymbolic-ai/) | `ready-for-draft-review` | matched-source |  |
| 38 | [Semantic Intelligence in Language Models (AI Plus One)](38-semantic-intelligence-in-language-models/) | `ready-for-draft-review` | matched-source |  |
| 39 | [Number Theory (AI Plus One)](39-number-theory/) | `ready-for-draft-review` | matched-source |  |
| 41 | [Elliptic Curves and Modular Forms (AI Plus One)](41-elliptic-curves-and-modular-forms/) | `ready-for-draft-review` | matched-source |  |
| 42 | [Computational Network Science (AI Plus One)](42-computational-network-science/) | `ready-for-draft-review` | matched-source |  |
| 43 | [Telecommunications and Network Infrastructure (AI Plus One)](43-telecommunications-and-network-infrastructure/) | `ready-for-draft-review` | matched-source |  |
| 44 | [Internet Protocols and Architecture (AI Plus One)](44-internet-protocols-and-architecture/) | `hold-source` | tentative-source |  |
| 45 | [Linux for Network Engineers (AI Plus One)](45-linux-for-network-engineers/) | `ready-for-draft-review` | matched-source |  |
| 46 | [Network Security (AI Plus One)](46-network-security/) | `hold-source` | tentative-source |  |
| 47 | [Infrastructure Automation (AI Plus One)](47-infrastructure-automation/) | `hold-source` | tentative-source |  |
| 48 | [Machine Learning for the Internet of Things (AI Plus One)](48-machine-learning-for-the-internet-of-things/) | `hold-source` | tentative-source |  |
| 49 | [Connected Devices (AI Plus One)](49-connected-devices/) | `ready-for-draft-review` | matched-source |  |
| 50 | [Embedded Systems for the Internet of Things (AI Plus One)](50-embedded-systems-for-the-internet-of-things/) | `ready-for-draft-review` | matched-source |  |
| 51 | [5G Networks and Services (AI Plus One)](51-5g-networks-and-services/) | `hold-source` | tentative-source |  |
| 52 | [Cryptography (AI Plus One)](52-cryptography/) | `ready-for-draft-review` | matched-source |  |
| 53 | [Managing Information Systems Development (AI Plus One)](53-managing-information-systems-development/) | `ready-for-draft-review` | matched-source |  |
| 54 | [Introduction to Program Design and Implementation (AI Plus One)](54-introduction-to-program-design-and-implementation/) | `compare-scope` | matched-source |  |
| 55 | [Web Development (AI Plus One)](55-web-development/) | `compare-scope` | matched-source |  |
| 56 | [Foundations of Trustworthy AI (AI Plus One)](56-foundations-of-trustworthy-ai/) | `compare-scope` | matched-source |  |
| 57 | [User Experience Design and Testing (AI Plus One)](57-user-experience-design-and-testing/) | `compare-scope` | matched-source |  |
| 58 | [Design of Agentic Systems (AI Plus One)](58-design-of-agentic-systems/) | `existing-book` | matched-source | 57 |
| 59 | [Data Science Engineering with Python (AI Plus One)](59-data-science-engineering-with-python/) | `compare-scope` | matched-source |  |
| 60 | [Designing and Prototyping Optical Systems (AI Plus One)](60-designing-and-prototyping-optical-systems/) | `compare-scope` | matched-source |  |
| 61 | [Research Methods in Design and Media (AI Plus One)](61-research-methods-in-design-and-media/) | `compare-scope` | matched-source |  |
| 62 | [Web Design and User Experience Engineering (AI Plus One)](62-web-design-and-user-experience-engineering/) | `compare-scope` | matched-source |  |
| 63 | [Advanced Language Models (AI Plus One)](63-advanced-language-models/) | `compare-scope` | matched-source |  |
| 64 | [Trading System Engineering (AI Plus One)](64-trading-system-engineering/) | `compare-scope` | matched-source |  |
| 65 | [Enterprise AI Architecture (AI Plus One)](65-enterprise-ai-architecture/) | `compare-scope` | matched-source |  |
| 66 | [Building AI Applications (AI Plus One)](66-building-ai-applications/) | `compare-scope` | matched-source |  |
| 67 | [User Experience Design for AI (AI Plus One)](67-user-experience-design-for-ai/) | `compare-scope` | matched-source |  |
| 68 | [Application Modeling and Design (AI Plus One)](68-application-modeling-and-design/) | `compare-scope` | matched-source |  |
| 69 | [Design Engineering (AI Plus One)](69-design-engineering/) | `existing-book` | matched-source | 12 |
| 70 | [Data and Context Engineering for Agentic AI (AI Plus One)](70-data-and-context-engineering-for-agentic-ai/) | `compare-scope` | matched-source |  |
| 71 | [AI Agent Infrastructure (AI Plus One)](71-ai-agent-infrastructure/) | `hold-source` | no-usable-source |  |
| 72 | [Self-Improving AI (AI Plus One)](72-self-improving-ai/) | `hold-source` | no-usable-source |  |
| 73 | [Machine Learning for Medical Devices (AI Plus One)](73-machine-learning-for-medical-devices/) | `hold-source` | no-usable-source |  |
| 74 | [High-Performance Computing for AI (AI Plus One)](74-high-performance-computing-for-ai/) | `hold-source` | no-usable-source |  |
| 75 | [Natural Language Engineering (AI Plus One)](75-natural-language-engineering/) | `hold-source` | no-usable-source |  |
| 76 | [Data Architecture and Governance (AI Plus One)](76-data-architecture-and-governance/) | `hold-source` | no-usable-source |  |
| 77 | [Compilers (AI Plus One)](77-compilers/) | `ready-for-draft-review` | matched-source |  |
| 78 | [Deep Learning (AI Plus One)](78-deep-learning/) | `compare-scope` | matched-source |  |
| 79 | [Fintech and Financial Innovation (AI Plus One)](79-fintech-and-financial-innovation/) | `hold-source` | no-usable-source |  |
| 80 | [Global Perspectives on Discrimination and Health (AI Plus One)](80-global-perspectives-on-discrimination-and-health/) | `hold-source` | no-usable-source |  |
| 81 | [Enterprise Software Design (AI Plus One)](81-enterprise-software-design/) | `hold-source` | no-usable-source |  |
| 82 | [Operating Systems (AI Plus One)](82-operating-systems/) | `hold-source` | no-usable-source |  |
| 83 | [Software Engineering (AI Plus One)](83-software-engineering/) | `hold-source` | no-usable-source |  |
| 84 | [Accounting and Budgeting for Engineers (AI Plus One)](84-accounting-and-budgeting-for-engineers/) | `hold-source` | no-usable-source |  |
| 85 | [Technical Communication for Engineers (AI Plus One)](85-technical-communication-for-engineers/) | `hold-source` | no-usable-source |  |
| 86 | [Medical Device Software Engineering (AI Plus One)](86-medical-device-software-engineering/) | `hold-source` | no-usable-source |  |
