# Archaeoastronomy Evidence Framework — design status

This is a framework **under development**, not an independently validated general method or an installable general-purpose package. Nabta Playa is the first development case. The aim is a repeatable way to determine which archaeoastronomical conclusions survive explicit source, identity, geometry and dating assumptions, and what evidence would change them.

## Candidate workflow

1. Identify source editions, access/read depth and exact observation units.
2. Transcribe observations without silently correcting conflicting sources; retain lineage and dependent copies.
3. Represent feature identity and membership alternatives, including missing data.
4. Define the estimand: a radial bearing, constrained axis, free axis or other quantity. Keep its archaeological meaning explicit.
5. Test recording assumptions, shared-reference effects and observation influence using bounded, declared scenarios.
6. Distinguish reproducibility, mathematical validity, archaeological reconstruction and astronomical interpretation.
7. Decide whether evidence supports a substantive contribution, a narrower result, or a documented limit.
8. Test any claimed generality on a separately selected case with a prospective protocol.

These steps are design commitments, not proof of accuracy, effectiveness or novelty. Neither generic uncertainty analysis nor combining astronomy software is claimed as new.

## Code and schema boundaries

- `analysis/` and `data/source/` currently implement **Nabta-specific** frozen analyses. They are retained at their established paths for hash stability and regression testing. Do not present them as generic framework modules.
- `scripts/` provides a runner and repository governance. It contains case-specific assumptions and dependency checks; reuse requires inspection, not simple copying.
- `docs/work_packages/OUTPUT_SCHEMAS.json` specifies current claim/experiment records. It is a starting point for cross-case design, not a validated universal ontology.
- New experiments should live under `cases/nabta/experiments/<experiment-id>/`, consume versioned inputs, and write only into a fresh ignored run directory. Each needs a declared input/output contract, units, branch conventions, numerical checks and review receipt.
- Extract common code into a future package only after at least two independently implemented cases expose a stable shared interface. Keep site-specific adapters, source identities and archaeological assumptions separate.

## What a future shared interface must carry

A case ID and revision; source/version/page and read depth; source-observation identifiers distinct from physical-feature hypotheses; coordinate and north conventions; origin/reference linkage; membership alternatives; units and missingness; uncertainty model and limits; chosen estimand; eligibility/exclusions; run environment and input hashes; results including failure/inconclusive states; and review/disposition.

Do not force a later site's evidence into Nabta's A/B/C labels, decimal rounding model, shared-origin geometry, quarry chronology or target list. A framework succeeds only if these are explicit case choices, not hidden defaults.

See [architecture](../docs/ARCHITECTURE.md), [Nabta case index](../cases/nabta/README.md), [new-case template](../cases/_template/README.md) and [phased roadmap](../docs/ROADMAP.md).
