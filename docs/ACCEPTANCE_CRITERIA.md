# Acceptance criteria after the deep audit

These rules distinguish a checkable record from a justified scientific conclusion. Passing the automated checks is necessary for accepting repository changes, and never sufficient for accepting an archaeological interpretation.

## Repository changes

1. Preserve the frozen ten scientific scripts, three input ledgers and thirteen reference tables byte-for-byte. Changes belong in a separately versioned experiment, not a silent historical rewrite.
2. Review each audit finding against evidence. Record both reviewer dispositions and the main-agent decision, including disagreements and unverified assertions. Reviewer agreement is not a vote establishing truth.
3. Run integrity, state, record and locator checks plus targeted failure-mode tests. After runner changes, complete the numerical pipeline in a new directory and compare all thirteen tables under the fixed tolerance policy.
4. Bind each new run to its contract, staged inputs, runner hashes, dependency versions and optional Git revision/dirty state. A clean-clone run on this machine remains same-host evidence. CI is unexecuted until a real run is recorded.
5. Keep worker packets and raw transcripts under agent_artifacts. Keep source PDFs and legacy material out of Git; do not infer redistribution rights from local possession.

## Research records and stage closure

New claim-audit and experiment-result records belong in docs/records and must pass the dispatched schema. Accepted records require an attributed reviewer and inspectable evidence. Qualified, inconclusive, counterexample and uncomputable outcomes may be accepted when their scope and evidence justify them; a positive finding is not required.

Each complete objective, stage, work item or publication gate requires an acceptance_record pointing to a JSON receipt. The receipt identifies the item, decision, reviewer, date, scope, rationale, limitations, explicitly met criteria, and nonempty evidence paths with SHA-256 hashes. The checks detect missing or stale evidence; a reviewer must still determine relevance, read depth and whether the criteria were honestly met. The retrospective W0 receipt certifies planning artifacts only.

Work dependencies govern closure rather than prohibiting all preparation. An individual E1–E4 experiment can be accepted after its listed W1 prerequisites close. Whole W2 cannot close until W1 and all E1–E4 items close. W1 requires all six W1 work items. W3 requires reasoned E5 and E6 decisions. A conditional E5/E6 branch may close as omitted_with_reason; it must not be reported as an executed experiment. A receipt cannot bypass an open dependency. W6 and external publication gates P2/P3 additionally require inspectable external attestations, not another model review.

## Scientific thresholds that remain open

- **Evidence:** each proposed headline claim has the source/version/page or explicit access limit, physical observation unit, transcription lineage, assumptions, contrary evidence, strongest competing account and main-agent disposition. A source PDF's presence or a historical note does not count as fresh verification.
- **Numerics:** new implementations pass known-geometry checks and a separate numerical comparison. Report all eligibility rules, exclusions and failed/inconclusive cases. For continuous claims, specify domains, angular branches, dependence and the interval-library trust assumption; a finite grid or sampling check cannot certify continuous coverage.
- **Interpretation:** table-derived bearings are not reconstructed prehistoric positions. Identity conflicts require documented correspondences; a compatible control is a limited diagnostic, not validation of the whole method. Quarry-window intersections are not construction dates or target probabilities.
- **Contribution:** document exploratory selection, all eligible contrasts and direct prior-work overlap. Demonstrate what inference changes. A full paper, narrower note, further-evidence route or no submission are all admissible W4 outcomes.
- **Publication:** no framework claim from the development case alone; no specialist acceptance from automated reviews; no external reproduction from same-host reruns. Authorship, venue, rights and authorization remain separate release conditions.

The current paper draft and October claim register are preserved historical working artifacts. The deep audit does not complete W1 or E1–E4, and does not certify the draft for publication.

The C06 square assignments are hardcoded in the frozen historical calculation. IDENTITY_PREMISE.json and the documentary-drift check bind that scenario to the reviewed crosswalk; correcting the crosswalk flags the claim for review rather than silently leaving it valid or rewriting historical output. A new E4 result must use explicitly reviewed premises.
