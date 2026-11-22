> Historical evidence record. Dates and acquisition statements below describe the original review; use [current project state](../../PROJECT_STATE.json) for current status.

# Reconciliation decisions and source gate

22 October 2026. Companion to the initial README. This update supersedes the initial note that quarry numerical measurements had not yet been recovered. Scientific interpretation remains provisional.

## Completed with held sources

- Visually checked every coordinate cell in WM2001 Table 16.1 and BR2005 Table 1 against the inherited CSVs. Produced 100 source-observation records across four separately identified table representations, including two explicitly missing GPS coordinate pairs. These represent 25 table entries per representation, not 100 physical features.
- Corrected the two GPS2003 A-7 fields in the new derivative only. Retained the source's C coordinate differences and C-8/C-6 labels without replacing either publication.
- Preserved 47 membership entries for two competing sourcebook descriptions. A3 and B groups agree between narrative and table; A1 and A2 do not. A-10 lacks a tabulated coordinate. The narrative A1 alternative cannot be reconstructed completely from the held coordinate tables. A-W and other unselected stones remain evidence that the published selected rows are not an exhaustive spatial population.
- Produced 24 conditional mean radial-bearing calculations, with WGS84 explicitly an assumption and missing stones reported. These are diagnostic calculations, not accepted original orientations or formal uncertainty estimates. They do not resolve original standing positions or the correct point within Complex A.
- Reproduced all six values in the BR2005 Table 2 “From Wendorf and Malville 2001” column using spherical initial bearings and an arithmetic mean, to the table's 0.01-degree precision. This numerical match establishes a sufficient computational recipe, not proof of the authors' exact implementation. Earlier WGS84-versus-table differences should not be characterized as errors without acknowledging this model difference.
- Recovered three laboratory-labelled contextual determinations plus an alternate reporting of DRI-3358, and seven figure-labelled determinations in Malville2015 Fig.89.9 (five quarry, two Ring Hill). There are 11 observation records, not 11 independent samples. No date is assigned directly to an individual A/B/C row.

## Chronology findings

The laboratory identifier DRI-3358 links the Structure E discussion to the master table. Table 3.1 p.54 reports 4800 ±85 radiocarbon years; chapter 17 p.517 reports 4800 ±80. Both were visually checked. The table's sigma column is explicit; the figure-labelled quarry ±40 values are transcribed without independently confirming the laboratory convention. No averaging of inconsistent errors is justified.

On p.520 the archaeological discussion explicitly conditions a circa-4800 BC date for Structure A on its role as the hub of the stellar alignments. That date is therefore not independent confirmation of those same astronomical associations. The relative stratigraphic argument that A/B precede E is a distinct claim and should not be discarded merely because the absolute-date argument contains astronomical input.

Fig.89.9 p.1087 in Malville2015 gives quarry labels 3–7 and measurements 5600±40, 5530±40, 5460±40, 5450±40 and 5470±40 BP. Its caption associates these with the quarry, but provides no laboratory IDs or detailed context. The paired Ring Hill labels 2 and 2/BIS must not be assumed independent samples or averaged; their relationship is not established here. Recalibration of contextual activity is possible once measurement conventions are checked, but would still not date individual rows. Reading approximate endpoints from a calibration plot is not a replacement for reproducing the calibration.

## Decisions that can be made now

1. Use radial directions from a documented Complex A origin to assess the historical radial claims. Keep free row axes as a separate geometric question.
2. Treat WM2001 original and BR2005 repeated-WM values as separate documentary observations, not independent surveys. Treat QB2002 and GPS2003 as related measurements of the same remains.
3. Retain A1/A2 narrative/table scenarios. Do not invent A-10 coordinates or silently relocate A-X/A-5.
4. Preserve C as a disputed feature. No astronomical claim about it can erase the physical-placement concern.
5. Keep chronological context, calibration and stellar-fit dates in separate fields. Do not pool them into a single construction prior.
6. Do not run an unrestricted sky search or generate p-values from the incomplete selected-feature population.
7. Treat the reproduced BR column as a computational validation check. Full reproduction of its final combined-survey column is unresolved; a common translation cancels from origin-to-stone vectors when applied consistently, so arbitrarily shifting individual points to force agreement is unacceptable.

## Remaining source-dependent decisions

| Item requested from user | Necessary decision it supports | Boundary if unavailable |
|---|---|---|
| Malville et al. 1998, Nature, DOI 10.1038/33131 | Directly establish the initial five-line definitions, reported azimuths, the due-east feature, observation assumptions and qualifications. BR2005's account is available but is not a substitute for checking the original. | Limit any historical comparison to sources actually examined; do not present a comprehensive adjudication of the initial Nature claim. |
| Wendorf, Close and Schild 1992–93, Sahara 5:7–16 | Verify earliest mapping/feature descriptions and the relation of the initially recognized group to subsequent subdivisions. | Leave early feature history unresolved; later coordinate scenarios remain usable, but early-to-late identity continuity cannot be claimed as verified. |
| Iwaniszewski SEAC2009 reassessment manuscript/slides, if recoverable | Determine the arguments and evidence in that specific E-92-9 critique. | This concerns the calendar-circle module; it does not block the radial-row study. Exclude that module or acknowledge the inaccessible presentation without attributing unverified arguments. |
| Wendorf and Schild 1998, DOI 10.1006/jaar.1998.0319 | Check the intermediate archaeological synthesis and its chronology statements. | Held excavation chapters support much of the context. This is secondary priority to the first two for the current history check. |

These papers may document or clarify the issues; none is guaranteed to contain unrounded coordinates, an A-10 position, or quarry laboratory reports. Failure to find those in the papers would create a separate archive/author-data request or require a deliberately limited evidence-resolution paper.

## Additional evidence now specifically identified

- Original laboratory reports or a detailed publication for quarry labels Nabta Playa 3–7, including wood/material identification, context and sample-to-quarrying association.
- Confirmation of the DRI-3358 uncertainty (80 versus 85), ideally from laboratory metadata. A sensitivity check can preserve both until then.
- Field-label crosswalk for A-4/A-5/A-X/A-10 and C-6/C-8; unrounded survey coordinates and the actual observation-point definition if preserved.
- Original reduction details for BR2005 final combined-survey directions and the later 2007/2008/2015 azimuths. A numerical resemblance to one coordinate dataset is not sufficient to infer that provenance.

## Paper design prepared up to the source gate

Primary question: how do source choice, feature definition and available spatial precision affect what published Nabta radial-alignment claims can establish?

Primary unit: one archaeological row hypothesis, identified by source and physical membership; repeated coordinate versions are paired observations, never independent monuments.

Main comparisons: published direction versus reproduced direction; source-table versus narrative membership where calculable; spherical versus ellipsoidal conventions; rounded-coordinate and origin-definition scenarios. Flag incomplete scenarios rather than excluding missing points silently. Quantify sensitivity separately from sampling uncertainty.

Validation: source transcriptions checked against pages; exact reproduction of a published calculation where possible; synthetic geodesic direction checks; dependence-preserving perturbations if a defensible measurement model is available. Calibration of a statistical test and independent validation of a general framework are later work, not accomplished by these checks.

Novelty gate: demonstrate an archaeological consequence beyond the discrepancy already identified by BR2005 and the probabilistic orientation methods already developed by Silva. A preliminary benchmark should compare handling of source lineage, physical identity alternatives, shared-origin uncertainty and unresolved outcomes; absence of a feature from a cursory reading does not establish novelty.

Manuscript claims permitted now: documented differences between printed records, reproducibility of the specified BR2005 column, and explicit dependency of some chronological arguments on astronomy. Claims not yet permitted: intended target identification, independent construction dates for rows, calibrated statistical significance, a validated transferable framework, or a complete history of the initial alignment claims.

## Stop boundary

The available-source reconciliation and bounded computational preparation above are complete for this pass. Finalizing the original-claim history and freezing the case-study hypothesis set now requires checking the Nature and Sahara sources the user is obtaining. Additional modelling could be performed conditionally, but would not remove that documentary dependency and is deferred rather than treated as accepted research. The entire project is not intrinsically impossible without those papers: if unavailable, explicitly narrow its historical scope before proceeding.

## Source arrival update — 22 October 2026

The user has now supplied the correct Nature 1998 article and Wendorf–Schild 1998 synthesis. Their acquisition dependencies are closed; direct claim reconciliation is newly unblocked and remains to be done. Sahara 5:7–16 remains missing: neither supplied candidate is that article. See the source-library intake check.

## SEAC proceedings received

The user supplied the SEAC 2021 publication of the 2009 conference, edited by Michael A. Rappenglück and Mossalam Shaltout, ISBN 978-3-00-069946-7. This supersedes the prospective editor attribution in the handbook. Iwaniszewski reassessment: printed pp.10–13, PDF pp.19–22. Malville climate-change paper: printed pp.3–9, PDF pp.12–18. Both acquisition gaps are closed; substantive review remains pending. No chapter DOI verified. Sahara 5:7–16 remains missing.

## Revised Sahara dependency — 23 October 2026

[Targeted dependency audit](SAHARA_DEPENDENCY.md) identifies no indispensable numeric input known to exist only in the missing article. The earlier blanket stop boundary is superseded: later-source reconciliation and analysis can proceed, while original discovery-history claims remain qualified.

## Proceeding after missing-source decision — 23 October 2026

User accepted recording the Sahara limitation and proceeding. The [supplied-source reconciliation](SUPPLIED_SOURCE_RECONCILIATION.md) now records Nature's separate five-direction claim set, the printed origin hemisphere issue, and the recovered Iwaniszewski chapter's calendar-circle alternatives. The radial-row case study can proceed conditionally with the held tables. Calendar-circle hypotheses remain a separate optional module. No unverified identity crosswalk, construction date, or intended celestial target is adopted.

## Operational state and geometry milestone — 23 October 2026

User instructed us to assume Sahara cannot be procured and continue. PROJECT_STATE.json and PROJECT_PLAN.md in agent_artifacts now track goals, dependencies, deliverables and completion criteria. No current task depends on obtaining Sahara.

The portable geometry_comparison.py produced 48 source/group/model comparisons. Cardinal direction, circular wrap and all six BR2005 recalculated-WM rounded-mean checks passed. Complete table versions give conditional mean-direction spreads of approximately 0.66° A3, 0.74° A2, 1.05° A1, 0.26° B2, 1.99° B1 and 0.28° C1 under assumed WGS84. These are source-scenario spreads, not confidence intervals. Missing GPS members exclude its B2/C1 estimates from complete-table spreads; C label continuity remains unresolved. Membership alternatives, coordinate-resolution and observation-point sensitivity remain unfinished. The case study is not yet ready for astronomical inference.


## 24 October — physical identity and chronology decisions

- Preserve A-X/A-4 as an unresolved cross-publication identity conflict. Do not relocate A-X, correct a grid square or pool surveys without source evidence. See identity-chronology-2026-10-24/FINDINGS.md under analysis.
- Keep vector drawing paths, text fragment inventories and representative coordinate points as different observational units.
- Preserve original BC/BP labels; five matched ranges differ arithmetically by exactly 2000 years. Do not silently standardize their epoch or treat them as independent dating results.
- Treat the 2025 proposed quarry window as contextual and conditional, not a hard construction bound for each row. Both B1 target chronologies overlap it; younger A1/B2 claims are in conditional tension, not conclusively rejected.
- Exact ancient-bearing reconstruction awaits point identities/definitions; no unsupported original-position estimates or new target search are authorized by these diagnostics. This is an evidential limit, not a requirement for permission to continue documentary work.


## 24 October — user response and documentary continuation

The user confirmed no additional field records or researcher contact. The source question is closed as unavailable; do not repeat it. Ancient-position reconstruction remains evidence-limited, while the documentary case study continues. See analysis/case-study-2026-10-24/SPECIFICATION.md and CLAIMS.md. A new interval analysis encloses the northern ordering over continuous rounding boxes under the spherical model; this does not upgrade the separate WGS84 grid result or establish ancient positions. S4 is now in progress; novelty remains open.
