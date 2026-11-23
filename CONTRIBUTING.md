# Research contribution workflow

Read docs/PROJECT_PLAN.md, docs/PROJECT_STATE.json and the relevant protocol before changing research. W1 is next; do not mark a scientific stage complete because a repository check passes.

1. Choose a work package and record source inputs, expected output and acceptance criteria.
2. Keep raw sources and existing reference tables immutable. Preserve failed and inconclusive results.
3. Place exploratory runs and delegate packets under ignored runs/ or agent_artifacts/. Review factual worker output against primary evidence before promoting it.
4. Keep documentary alternatives, computation assumptions and archaeological claims distinct. Never impute a missing stone coordinate or silently pool source versions.
5. For code changes, run repository checks, failure-mode tests and the full numerical reproduction in a fresh output directory. Inspect differences before intentionally updating a reference snapshot.
6. Update the plan/state and affected claims after accepted scientific work. Record protocol changes before running new experiments.

The main agent owns scientific planning, method choice, interpretation and acceptance. Hermes leaf workers handle bounded extraction, inventory and arithmetic only, with the authorized provider/model/effort. Their self-reports are not evidence of completion. All worker scratch artifacts stay under agent_artifacts.

Changes to reference data, authorship, licences, publication, external correspondence and submission require their own substantive justification or user decision as applicable. No remote or publication destination is inferred from a local repository request.

Follow [acceptance criteria](docs/ACCEPTANCE_CRITERIA.md). New structured research records belong in docs/records; completed work needs a hash-bound acceptance receipt and closed required dependencies. The validator checks structure and file integrity; the named reviewer must still judge evidence relevance and scientific adequacy.
