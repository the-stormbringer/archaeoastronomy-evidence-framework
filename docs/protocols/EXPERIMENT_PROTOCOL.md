# Discriminating tests — execution protocol v1

25 October 2026. No new experiment in this document has been executed. Preserve the existing pipeline and outputs. Implement new tests in a separate subdirectory here after confirming input hashes. Record software versions, source/label membership, assumptions, all attempted scenarios, failures and exclusions. Amend this protocol before expanding a test; explain the reason and preserve the previous version. Known prior results mean this is prospective development work on familiar data, not a blinded confirmatory study.

## E1 — Recording convention and membership sensitivity (required)

Question: does the published-table ordering survive defensible combinations, and where does the claim stop?

Inputs: frozen coordinate and membership ledgers. For each matched table version, compute nominal means and within-sector contrasts. Primary scenario: existing nearest-rounding ±0.00005° boxes. Counterfactual scenarios: positive-coordinate truncation [x,x+0.0001°], and ±0.0001° boxes. Treat each convention consistently within a source scenario; do not independently choose favourable conventions per point. Run complete original-WM narrative alternatives separately. Missing complete-row contrasts are explicitly uncomputable.

Retain a shared origin. On northern geometry, use the established spherical interval method with validity checks and origin subdivisions 1,4,16; if needed, extend once to 32 per axis with a documented numerical reason. A failure to prove positivity after this remains inconclusive. Do not refine indefinitely to obtain a desired verdict. Southern/cross-sector computations must use correct angular branches; if no validated continuous extension is implemented, report nominal/finite-grid scope explicitly.

Outcomes: positive certified numerical enclosure under the declared model; nonpositive upper enclosure where order is reversed throughout; inconclusive enclosure; or uncomputable. A sampled counterexample demonstrates a violation within the scenario but not an extremum. Interval containment of zero alone is not a counterexample. Compare numerical margins with nominal group separation. No confidence levels or scenario probabilities.

Decision: retain a precisely scoped result, narrow it, or remove a general robustness claim. Do not retroactively change membership to rescue ordering.

## E2 — Individual-point and origin influence (required)

Question: is the conclusion carried by particular representatives or the common origin?

For each complete table row, remove one labelled observation at a time and record remaining sample count, radial-mean change and affected contrasts. A one-point remainder may be reported as a point-bearing diagnostic but not a fitted axis. No point is removed from the accepted source dataset. Keep original-WM narrative analysis separate.

For shared origin perturbations, reuse radii 0,1,5,10,25 m and directions every 5° as a finite grid. Use one perturbed origin simultaneously for all rows in a contrast. Run matched spherical/WGS84 nominal and perturbation calculations; do not call the grid continuous coverage. Keep origin displacement separate from E1 initially. Rank influence descriptively, without an arbitrary pass/fail significance threshold.

Decision: identify fragile claims and the observation or definition that matters. High influence is not evidence that a point is wrong.

## E3 — Estimator and claim-importance comparison (required review; bounded computation)

Use existing radial arithmetic/circular/TLS results first. Compare only matched coordinates/memberships. Specify whether a method estimates an observer-to-markers direction, a constrained axis, or a free row axis. New free-axis calculation is warranted only if its archaeological interpretation is defensible; do not introduce it solely to increase the method count. Do not fit a free axis to a single point or report a signed directional difference for an unoriented 180° axis without normalization.

Produce an eligibility/result table for all 15 table-group pairs, flagging missing rows and sector relevance. Within-sector outcomes deserve substantive interpretation; large cross-sector separation is a control, not a discovery. Record whether retained ordering conveys more than nominal group labels. Test whether an actual published inference changes when source/identity alternatives are respected.

Decision: distinguish a substantive result from a reproducibility benchmark or illustration. If the ordering adds little archaeological information, move it to a supporting role rather than promote it as the paper's main novelty.

## E4 — Physical-identity challenge (required source work)

Recheck A-X/A-4 against printed descriptions, mapped square assignment, catalogue entries, scale and the older labels. Check available alternative correspondences without adopting them. Use at least one comparison pair with an apparently compatible square assignment (the existing A-5/A-6 control) to test that the incompatibility test does not declare every pair contradictory. Record identities independently of geometric proximity. Verify the <=50 m square premise and the interpretation of the mapped location.

Decision: confirmed conditional documentary conflict, corrected transcription/interpretation, or unresolved premise. If corrected, revise dependent manuscript claims and preserve the correction trail. Do not assume conflict establishes ancient displacement.

## E5 — Synthetic validation (conditional; design decision after E1–E4)

Run only if we intend to claim the diagnostic procedure has capability beyond this one transcription. The written design must first specify the synthetic geometry, row membership, observation formation, recording convention, corruption locations, random seeds/deterministic cases, metrics and fair comparators. Do not tune it after observing favourable results.

Minimum informative cases: known undisturbed geometry under the stated rounding model; an origin shared across observations; displaced representative points outside that model; and an incorrect label assignment. Include positive and negative ordering examples. Evaluate whether true contrasts are enclosed when assumptions hold, whether the method properly returns inconclusive results, and whether hidden violations can yield misleading apparent stability. Equal information must be supplied to comparisons. Deliberate hidden violations demonstrate limitations, not calibrated false-positive rates for ancient Nabta.

A separate locked E5 specification is required before execution. This conditional plan is not yet that specification. If E1–E4 already answer the paper's question and simulation adds no discriminating evidence, document the decision to omit it.

## E6 — Astronomy/chronology expansion (branch gate only)

Open only if there is an identifiable geometric quantity, an explicit fixed published hypothesis, justified horizon/visibility conventions and a noncircular chronological question that available evidence can address. Otherwise explain why documentary compatibility is the maximum warranted result. Do not require a stellar solution to justify the case study. General framework validation belongs to an independent second case.

## Acceptance and reproducibility

Use deterministic synthetic checks of any new geometry implementation, named published benchmarks and a separate numerical cross-check. Preserve historical results; compare new outputs with them rather than overwrite them. Same-host implementation checks are not external acceptance. Record every excluded or failed case. A test is complete when its question receives a bounded answer and its evidence is inspectable, not when its desired conclusion is obtained.
