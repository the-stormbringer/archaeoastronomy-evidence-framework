# W2 Robustness and influence experiments

Status: pending the relevant W1 source premises. Owner and method decisions: main agent. Governing specification: [EXPERIMENT_PROTOCOL.md](../protocols/EXPERIMENT_PROTOCOL.md). The existing reproduction runner checks the October pipeline; it does not implement these experiments.

## Execution skeleton

| Experiment | Preconditions | Implementation deliverable | Acceptance |
|---|---|---|---|
| E1 Recording and membership | Source-matched identities and complete/partial status established | Separate scenario enumerator, interval/grid result table and all exclusions | Shared origin; explicit documentary versus counterfactual scenarios; interval containing zero labelled inconclusive; no silent membership repair |
| E2 Point and origin influence | Same source identity/membership contract | Leave-one-observation-out results and shared-origin perturbation diagnostics | Removal is a diagnostic only; one origin per contrast; partial or one-point results correctly labelled |
| E3 Estimand and importance | E1/E2 available; existing estimator definitions reviewed | All 15 table-group pairs with completeness and relevance; matched estimator comparison | Cross-sector controls not promoted to discoveries; distinguish radial means, constrained and unoriented free axes |
| E4 Identity challenge | W1-03/04 source review | A-X/A-4 challenge and A-5/A-6 control disposition | Conditional conflict, corrected premise or unresolved identity explicitly distinguished; no claim of ancient movement from a label conflict |

## Implementation requirements

Create new experiment code separately from the preserved analysis scripts, with its own protocol version and input hashes. Before full runs, use small known-geometry checks and an independently implemented numerical comparison. Reuse existing results where their domains actually match; do not call finite-grid extrema continuous bounds or combine duplicate coordinates as independent observations.

Run outputs initially belong under ignored runs/ or agent_artifacts. Include all attempted cases, failed cases and exclusions. No output table may omit an incomplete group without a recorded reason. Keep scientific acceptance separate from process exit status.

Only after main-agent review should accepted experiment code/results enter the curated repository and the pipeline contract change. Preserve the original reference snapshot as a named historical benchmark. Do not update expected results simply to make the old runner pass.

## Completion decision

For each experiment state what changed about the supported inference. A null, negative or unresolved result is acceptable. If a required premise is inaccessible, record the bounded result permitted by the remaining evidence and continue unaffected work. E1–E4 are not complete until their acceptance records exist.
