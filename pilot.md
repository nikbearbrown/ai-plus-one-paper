# Local pilot: synthetic breadth-first search lesson

This smoke test uses [pilot-chapter.md](pilot-chapter.md), a deliberately small, constructed chapter with no student, institutional, or employer data. It exercised the audit handoff, not the entire AI+1 pipeline. No answers were shared with learners and no production gate was signed.

At AI Readiness commit `2c0c51ef090230aacaf0d45e0b2a141c39e125b6`, ARC opened a scratch folder containing one copy of the fixture. The folder was structured as a single chapter subfolder. The commands, run from the ARC repository with a clean scratch directory, were:

```bash
./arc open "$specimen" "$work" --title 'Synthetic BFS chapter' --standards northeastern-edge
./arc check "$work"
```

ARC found one module and one page, with no assignments, quizzes, or rubrics. The qualitative review below checked the actual teaching text separately.

| Question | Automatic signal | Qualitative check |
| --- | --- | --- |
| R1 · Rules and disclosure | NOT SUPPLIED | A prompt asks for disclosure. An actual syllabus policy and instructor disclosure were not supplied. |
| R2 · First attempt | CHECK | The student is asked for a prediction, but the answer appears in the next sentence. Separate the attempt from the reveal. |
| R3 · Disciplinary AI work | MISSING | An optional comparison proposes a bounded AI task; it does not require students to run a tool, and access is unverified. |
| R4 · Independent verification | MISSING | The text explicitly asks for a suspicion and a hand trace. Actual learner verification and assessment of it remain untested. |
| R5 · Graded process | NOT SUPPLIED | A note about revisions is requested. There is no graded assignment, process rubric, or evidence of learner work. |
| R6 · Independent assessment | MISSING | A no-AI self-check is present, but it is ungraded and has no delivery, rubric, or outcome evidence. |

The optional Northeastern Edge scan reported E1–E5 as NOT SUPPLIED, CHECK, MISSING, MISSING, NOT SUPPLIED. The reviewer did not find an explicit AI learning objective, even though the E2 screen reported CHECK. That difference shows why a keyword signal cannot stand in for reviewing the chapter. Neither scan was a certification.

A revision would withhold the worked answer until the attempt, add an explicit objective, and present a new graph for unaided transfer. R1, required access, and grading would be decisions for the course team rather than facts asserted by the writer. No model generation study, package build, LMS import, or learner evaluation was run for this specimen.
