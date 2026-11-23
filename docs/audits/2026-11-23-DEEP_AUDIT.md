# Deep audit and reconciled state — 23 November 2026

The repository is a useful working baseline, not a submission-ready paper. Concrete acceptance and provenance weaknesses were corrected, and several initial statements were narrowed after critique. No new mathematical counterexample to the frozen northern-ordering calculation was established in this bounded review. That does not validate its archaeological premises or prove publishability.

## Scope and independence

Baseline `0dd3561` was frozen before review. The main pass examined all ten scientific scripts, runner/checks/tests, plan/state/assumptions/experiment protocol, working manuscript, prior-work comparison and selected evidence records. One primary page was visually rechecked; see [read-depth record](2026-11-23-SOURCE_CHECK.md). This was not a fresh transcription of every coordinate, complete rereading of the library or exhaustive new literature search.

A Codex child at medium effort and one Hermes child on DeepSeek Flash/medium each critiqued F01–F16 in order against the same frozen snapshot. Rate limits and payload approval delayed Hermes, so execution was not simultaneous. Codex was instructed not to read Hermes outputs; Hermes tool-call inspection shows initial findings, frozen files and isolated probes, not Codex outputs or candidate files. They share evidence and may share blind spots; neither is an independent archaeological specialist.

The main agent read both critiques, checked concrete failure mechanisms and adjudicated every point. Both declined to verify the inaccessible PDF observation. Hermes stayed within ten tool calls. No confidence score or agreement count was treated as proof. Scientific authority and final acceptance remained with the main agent.

## Ordered dispositions

The [full ledger](2026-11-23-DISPOSITIONS.json) preserves initial claims, both objections and evidence locators alongside the decisions.

| Point | Codex / Hermes | Main-agent disposition |
|---|---|---|
| F01 Scientific readiness | upheld / upheld | Both confirm existing readiness disclosures, not a new defect. A preserved computational baseline is usable; W1, experiments, novelty, specialist review and external reproduction remain open. |
| F02 Fixed historical pipeline | qualified / qualified | The pipeline contains outcome-dependent assertions, but not every script asserts a positive result. Some outputs are written before assertions and ordinary script failures are logged. Preserve historical regression scope; new experiments must retain negative and inconclusive outcomes. |
| F03 State acceptance weakness | upheld / upheld | Both independently reproduced absent status/task validation. New checks validate W/S/task graphs, required dependency edges, statuses, closure receipts and evidence hashes. W0 has a retrospective planning-only receipt. Checks do not judge evidence relevance. |
| F04 Schema root | upheld / upheld | A definitions-only schema is legitimate as a library. The defect was no enforced consumer. Added typed root dispatch, jsonschema dependency, recursive record validation and negative tests. |
| F05 Schema content | qualified / qualified | Separate the record kinds: claim records already required evidence text; experiment records lacked reviewer/evidence and allowed empty hashes. Accepted records now need review, evidence, real hashed inputs and a hash-bound output. Honest uncomputable/qualified outcomes and nullable pages remain possible. |
| F06 Pipeline contract limits | qualified / upheld | Duplicating execution evades old checks only with coherent hash membership edits. Infinite tolerance permits finite differences only in named fields; nonfinite deltas were already rejected. New checks reject duplicate/unsafe entries and changed tolerance/staging policy. This is not protection against coordinated rewriting of all policy and references. |
| F07 Run provenance | upheld / upheld | Provenance was split, not absent. New receipts save contract bytes/hash, staged input and runner hashes, dependency versions, generated-output hashes, timestamps and optional revision/dirty status. Contract changes during execution are detected. Exported trees honestly have no Git revision. |
| F08 Historical claim locators | upheld / upheld | Historical names remain unchanged. C06 has a generated CSV and an unstaged note locator; C09/C10 cite unstaged notes. A validated locator map resolves every frozen reference to curated evidence. Existence is not relevance or fresh primary reading. |
| F09 Interval interpretation | qualified / upheld | Retain the conditional code-level enclosure reading, with interval-library trust and no formal or archaeological certification. Reject Hermes guaranteed excess-width claim: shared variables alone do not prove strict over-enclosure; for x in [0,1], x - (-x) yields the exact [0,2] even without symbolic elimination. Keep may over-enclose. Correct the endpoint-storage description separately. |
| F10 Identity evidence | unverifiable / unverifiable | Both reviewers lacked the PDF and could not independently confirm the main-agent render. The source-check note records its exact scope. Square text was visually checked; scale, feature identity, older representatives and historical positions remain separate premises. E4 is not complete. |
| F11 Contribution and selection | upheld / upheld | Existing plans already constrain novelty and exploratory selection. All-15-pair eligibility is a transparency requirement, not 15 archaeological discoveries. No fresh exhaustive literature search or publishability finding is claimed. |
| F12 Secondary claims | upheld / upheld | Existing caveats are sound. Convex combinations concern displayed final values and two reconstructed row means, not all reductions or unrounded observations. Quarry overlap is contextual arithmetic. Scientific consequence remains a W1/W4 decision. |
| F13 Reproduction scope | qualified / qualified | Scope exclusions were already disclosed. Main agent witnessed prior/current runs; reviewers inspected historical summaries, not that historical execution. Same-host repetition, static figures, incomplete source verification, unexecuted remote CI and external review remain distinct. |
| F14 Stage/task consistency | qualified / qualified | Existing prose already allows local preparation and acceptance after relevant premises. Checks now enforce required dependency edges and stage children. Individual experiments need local W1 prerequisites; whole W2 needs W1 and E1–E4 closed. E5/E6 may close by reasoned omission without claiming execution. |
| F15 Source coverage | upheld / upheld | 100 rows and unique source-label keys were independently counted; that does not verify coordinates, page claims, repeated positions or free-text statuses. Historical labels are preserved; claim-level source review remains necessary. |
| F16 Audit decision rule | upheld / qualified | This is a procedure, not a defect. Both ordered critiques now exist and every point is adjudicated here. Agreement is not proof. Tested controls can close while scientific gates remain open. |

## Additional findings

- **Codex-N01 — documentation_corrected:** The frozen interval comment promises full endpoint strings but serializes padded float summaries. Documentation corrected; historical code/results preserved. This is not a demonstrated enclosure failure.
- **Hermes-NF01 — merged_with_F06_F07:** The contract is outside its own hash map. Requiring a file to contain its own full-content hash is not a useful fix. Save/hash the contract separately, check it after execution, and enforce the fixed tolerance/staging policy. This overlaps F06/F07; any-comparison wording was too broad.
- **Hermes-NF02 — guard_added:** Square labels are hardcoded rather than read from the crosswalk. IDENTITY_PREMISE.json and identity_premise_errors now flag crosswalk/script drift and differing square assignments. Historical outputs remain unchanged; E4 still needs source/identity review.
- **Hermes-NF03 — default_failure_rejected_local_presence_checked:** Archive absence is intentional in a portable clone and already disclosed. Default checks must not require ignored files. All seven live local_archive_artifacts paths exist, verified by main agent; presence does not establish content/source validity.
- **Codex-CR01..04 — fixed_and_independently_rechecked:** Deleted dependencies, unbound accepted input/output paths, inherited optimization and skipped nested records were found in candidate review, corrected, and independently re-probed by Codex. Added a documentary-drift regression for NF02.

## Strict acceptance and remaining work

[Acceptance criteria](../ACCEPTANCE_CRITERIA.md) now govern typed records, required dependencies, evidence-bound closure, portable claim locators and documentary-premise consistency. Automation checks structure and integrity; a reviewer still must judge relevance, source read depth, method validity and scientific consequence. A well-formed receipt is not self-authenticating science.

The ten historical scripts, three ledgers and thirteen reference tables remain byte-identical. The draft is preserved with an audit-status notice. Historical notes are not relabelled as fresh verification. New receipts bind contract, staged inputs, code and outputs. Tests include inherited optimization and documentary drift. Full numerical runs remain same-host; no remote CI, fresh second-host installation, end-to-end source/figure reproduction or specialist acceptance is implied. Final counts and run scope are in [the validation record](../REPOSITORY_VALIDATION.json).

W1 remains next: verify source/narrative memberships, ordering assumptions and selection history; complete the identity challenge and compatible control; review reduction/chronology consequence; document direct predecessor overlap. E1–E4 then deliver bounded outcomes under their prerequisites. W3 decides E5/E6, including reasoned omission. W4 chooses a full case study, narrower note, further-evidence route or no submission before manuscript reconstruction. External scrutiny, external reproduction, author/venue/rights decisions and independent framework testing remain open.

Audit completion means both critique streams have dispositions and accepted control changes pass checks. It does not complete W1, establish a framework or declare the paper publishable.
