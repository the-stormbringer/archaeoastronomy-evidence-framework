# Outstanding research work packages

These packages turn the current plan into reviewable next actions. They are specifications, not executed experiments or accepted findings. W1 is ready; W2 depends on the relevant W1 premises. The canonical research statuses remain in [PROJECT_STATE.json](../PROJECT_STATE.json).

1. [W1 evidence and alternatives](W1_EVIDENCE_AUDIT.md): page-level claim lineage, alternative explanations and selection history.
2. [W2 experiments](W2_EXPERIMENTS.md): bounded E1–E4 execution and acceptance.
3. [W3 and W4 decisions](W3_W4_DECISIONS.md): decide useful extensions and whether the contribution warrants a paper.

[WORK_QUEUE.json](WORK_QUEUE.json) records the initial task skeletons. [OUTPUT_SCHEMAS.json](OUTPUT_SCHEMAS.json) defines reviewable outputs for future workers. Keep instantiated packets and raw results under agent_artifacts; promote only reviewed outputs. An empty or planned record is never counted as completed evidence.

Stage dependencies govern acceptance: W2 cannot be accepted before W1 closes. Limited W2 preparation may overlap W1, as allowed by the plan. The task queue records local prerequisites for that preparation, not permission to bypass the stage gate. Experiment statuses live in this queue; the source assumption matrix remains in docs/protocols/ASSUMPTIONS.md.

New records must pass the dispatched schema through scripts/check_repository.py; store them in docs/records. See [acceptance criteria](../ACCEPTANCE_CRITERIA.md). E5/E6 are explicit conditional decisions in the queue. Completing one experiment after its relevant W1 prerequisites is distinct from closing the entire W2 stage.
