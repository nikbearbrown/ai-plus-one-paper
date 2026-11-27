# AI+1: Silent Critique review and revision record

Scope: original manuscript, chapter protocol, synthetic BFS fixture, ARC pilot receipt, exports and source inventory at base revision `1604b5e`. Follow-up checks target [the revised manuscript](ai-plus-one-draft.md). No execution of ARC, export, hosted model, or experiments; the figure is a schematic whose source was inspected, not a visually verified GitHub render.

## VERDICT

**Major revision before submission.** The repository describes a grounded chapter workflow and has an existing small mechanical smoke test. It does not yet establish whether the workflow improves reviewable teaching evidence versus a comparable baseline. Draft improvements below strengthen the research protocol; they cannot close empirical gaps.

## STRUCTURAL DIAGNOSIS

Original §§1–5 supply the intended question but interleave existing governance, proposed stage changes, and the reported single example. The revised abstract and §§2–4 signpost the three states separately, and §5 states why the study does not measure student learning.

## METHODOLOGICAL REALITY

Original §4 permits arms to differ in gate handling and human input despite describing equivalent sources. Revised §3 names an explicit common checkpoint, records the assumption behind it, documents matched human input, and distinguishes a controlled test from a naturalistic comparison when the baseline would otherwise be altered. Packet formats can reveal the arm, so the revised text limits blind review to normalized content and evaluates report usability separately. Still needed: a frozen version of the baseline and a workable low-leakage review procedure.

## STATISTICAL INTEGRITY

Original §4 alternates between reviewable readiness evidence and multiple accuracy measures; it gives no decision threshold. Revised §3 defines objective eligibility before generation, distinguishes errors per assigned brief from errors per checked claim, recognizes asymmetric omissions, and states a joint primary decision. No tolerance, minimum useful gain, outcome variance or study size is available. Figure 1 is illustrative: no axes, observations or inferred effect sizes. Comparative plots are deferred.

## RESULTS & DISCUSSION

The BFS fixture discloses its solution next to the purported independent attempt. Pilot R2 shows CHECK anyway. Revised §4 gives this discrepancy as a documented example of why an automatic screen and faculty judgment differ, rather than evidence of diagnostic accuracy or a finding on comparative workflows. The reported module/page counts are traced to the receipt, not independently reproduced.

## WRITING AS DESIGN

The revised opening uses one concrete task before introducing readiness. It keeps “reviewable,” “approved,” “delivered” and “learned” as four different claims. It explicitly distinguishes the bundled treatment from attribution to any one stage.

## ETHICAL SCREENING

No learner records are needed for the design. Keep restricted source content and instructor solutions out of public artifacts; measure conditions across permitted source and tool access, and record actual limits on reuse. Any later learner study needs a separate design and appropriate institutional review. Author identity, funding and conflicts should be supplied by the authors, not inferred.

## RANKED IMPROVEMENTS

1. **[MAJOR, partially repaired]** Cross-arm checkpoint and input equality → operationalize and dry-run the checkpoint in §3 from the same versioned brief → protects the incremental comparison. Acceptance check: another author can identify the same freeze step, output field set and human prompts for every arm.
2. **[MAJOR, needs pilot]** Outcome thresholds in §3 → calibrate the materiality and coverage rubric and set a useful gain and tolerable error increase before scoring confirmatory data → turns the design into a falsifiable comparison. Acceptance check: publish anchored rubric examples, outcome windows and a frozen analysis plan.
3. **[MAJOR, needs research]** Scope of novelty in §§1 and 5 → read primary studies from relevant instructional-design and AI authoring literatures, including negative findings → bounds what is genuinely new. Acceptance check: claims distinguish architecture precedent, independent verification and evidence on teaching.
4. **[MINOR, drafted]** Missing central schematic → Figure 1 shows the actor boundary and caption explicitly marks it proposed → makes the split between draft production and approval legible. Acceptance check: inspect the GitHub render and a plain-text or print fallback before submission.

## WHAT WORKS

The constructed lesson and mechanical audit have a precise artifact trail, and the original clearly refuses to equate tool output with student outcomes. Section 4 now makes that restraint part of the paper's main argument.
