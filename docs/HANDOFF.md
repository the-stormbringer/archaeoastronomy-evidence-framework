# Continuation handoff — 24 November 2026

This is the public working repository for the owner's Nabta project. It contains the curated numerical inputs, fixed outputs, scientific code, evidence notes, provisional manuscript, plans and acceptance rules. It is sufficient to continue software work and conditional analysis. It is **not self-contained for fresh primary-source verification**: third-party publications and original field records are not in the clone. Do not claim otherwise.

## Start and authority

1. Read [research charter](RESEARCH_CHARTER.md), [current plan](PROJECT_PLAN.md), [state](PROJECT_STATE.json), [acceptance criteria](ACCEPTANCE_CRITERIA.md) and [work queue](work_packages/WORK_QUEUE.json).
2. Read the [deep audit](audits/2026-11-23-DEEP_AUDIT.md), [dispositions](audits/2026-11-23-DISPOSITIONS.json), [claim evidence map](CLAIM_EVIDENCE_MAP.json) and [identity premise](IDENTITY_PREMISE.json). Earlier assessments and the working manuscript are provisional and can be superseded by these records.
3. Follow [contribution instructions](../CONTRIBUTING.md). The project owner retains direction; the acting lead reviews worker evidence and scientific acceptance. A previous worker's confidence, passing tests or polished draft is not acceptance.
4. Install the pinned environment and run the commands in [reproduction instructions](REPRODUCIBILITY.md). Preserve failures. The current hosted numerical run is **not passing**; see below.

## Immediate work, in order

- Engineering: investigate the hosted/local numerical differences recorded in [hosted validation](validation/hosted-2026-11-24/README.md). Reproduce the environment and trace differences before proposing any tolerance amendment. Do not replace historical outputs or widen thresholds to make CI green.
- Science: W0 planning is complete; [W1](work_packages/W1_EVIDENCE_AUDIT.md) is ready, not complete. Audit memberships, ordering assumptions/selection history, A-X/A-4 identity and A-5/A-6 control, chronology/claim scope and prior work. Software diagnostics can proceed in parallel with source acquisition.
- Then run E1–E4 only under [W2](work_packages/W2_EXPERIMENTS.md) and the [protocol](protocols/EXPERIMENT_PROTOCOL.md), with prerequisites and typed receipts. E5/E6 and astronomy are conditional branches. Manuscript rebuilding and external scrutiny follow the contribution decision; independent framework validation is a later study.

## Data and context map

| Need | Public location | Qualification |
|---|---|---|
| Transcribed coordinates, memberships, published claims | `data/source/` | 100 source-coordinate rows, 47 membership rows, 19 claim rows; repeated sources are dependent |
| Fixed outputs and execution contract | `data/reference/`, `data/pipeline.json` | 13 reference tables and 10 preserved scripts; immutable unless a reviewed correction is accepted |
| Analysis CSV headers, row counts and hashes | [inventory](../data/INVENTORY.json), [dictionary](../data/DICTIONARY.md) | Includes curated contextual tables and historical diagnostic tables |
| Source identity and procurement locators | [source guide](sources/README.md), [catalogue](sources/CATALOGUE.json) | Bibliographic metadata, hashes and local holdings; no full-text redistribution |
| Chronology, source decisions, identity crosswalks, drawing-space candidates | `docs/evidence/` | See claim evidence map; page coordinates are not survey coordinates |
| Figures and provisional paper | `docs/manuscript/` | Existing snapshots, not a final publication |
| Original figure/extraction/diagnostic code omitted from initial packaging | [historical support](../support/README.md) | Source preserved with hashes; historic paths/dependencies, outside supported runner |
| Current validation failure | `docs/validation/hosted-2026-11-24/` | Durable receipts from public CI, not just expiring artifacts |

## Decisions that must survive a handoff

- The goal is a substantive, defensible contribution, not merely a reproducible computation. Novelty and publishability remain open.
- Assume the Sahara 5:7–16 article cannot be procured. Retain its discovery-history gap; do not stop all radial-row work for it. See [dependency assessment](evidence/source_reconciliation-2026-10-22/SAHARA_DEPENDENCY.md).
- The owner has no additional unpublished survey records, field notes or existing researcher contact. Do not repeatedly request them. Missing identity/reduction evidence limits physical reconstruction.
- Nature 1998, the SEAC proceedings containing Iwaniszewski's reassessment, Haynie 2014 and the 2025 monograph were obtained locally. Old acquisition-gap lists are superseded for these sources. Iwaniszewski's 2009 conference contribution appeared in 2021 proceedings; it concerns the separate calendar-circle module.
- Do not silently resolve A-X/A-4 or C-6/C-8 identities; do not invent A-10 coordinates. Keep table and narrative memberships separate. Preserve printed azimuth discrepancies and date conventions.
- Archaeological context dates, proposed quarry windows and target-fit dates are different evidence. Coordinate rounding is not a survey-accuracy model; numerical enclosure is not a confidence interval or evidence of intention.
- New agents need not inherit a local Hermes session. If the owner enables delegation, use bounded tasks and independently inspect outputs. Never copy keys, worker transcripts or unrelated personal files into the repo.

## What must be supplied separately

For disputed source passages, obtain the corresponding publications through the catalogue's DOI/publisher/repository locators or ask the owner for lawful access to their research copy. Exact file hashes identify the copies used; a different edition requires page reconciliation. The earliest archaeology sourcebook, Brophy–Rosen tables and the 2025 catalogue/maps are especially important for W1. Acquiring a PDF does not establish survey identities or resolve the historical reduction procedure.

The ignored legacy archive contains inherited notebooks, terrain/astronomy assets and outputs with earlier reliability concerns. These are not prerequisites for the approved current pipeline. Any future reuse must begin with an explicit provenance and validation task, not importing them as accepted results. No private full-text or archive handoff is implied by public availability. The [local-archive policy](LOCAL_ARCHIVE.md) and [rights statement](../RIGHTS.md) apply.

No scientific gate was advanced by this handoff or GitHub publication. The owner authorized public repository publication; authorship, a reuse licence, journal submission and external correspondence still require their own decisions where applicable.

## Literature and references

See the [literature dependency matrix](sources/LITERATURE_DEPENDENCIES.md), [Chicago author–date bibliography](sources/BIBLIOGRAPHY_CHICAGO.md) and [citation guide](sources/CITATION_GUIDE.md). Catalogue entries map to stable reference keys; citation metadata does not upgrade source read depth.

## Framework organization — November 27, 2026

The public repository is now `archaeoastronomy-evidence-framework`. Nabta remains its first development case; the physical local folder name is unchanged. Read the [architecture review](ARCHITECTURE.md), [phased roadmap](ROADMAP.md), [framework design](../framework/README.md) and [cited literature evidence](sources/LITERATURE_EVIDENCE.md). Existing scientific paths and hashes are preserved. No general-purpose package or validated cross-case capability is implied by the name.
