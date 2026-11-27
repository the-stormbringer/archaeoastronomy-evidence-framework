# Archaeoastronomy Evidence Framework

A framework under development for source-critical, reproducible archaeoastronomical research. **Nabta Playa is the first development case**: what the numerical record supports, what depends on archaeological identification, and what remains unresolved. Generality requires an independent follow-up case.

Start with the [framework design](framework/README.md), [Nabta case index](cases/nabta/README.md), [repository architecture](docs/ARCHITECTURE.md), [phased roadmap](docs/ROADMAP.md) and [cited literature evidence](docs/sources/LITERATURE_EVIDENCE.md).

**Current research stage:** scientific design and evidence validation. W0 planning is complete; W1 evidence and competing-explanation review is next. E1–E4 experiments are specified but have not run. The working manuscript is provisional. A general framework requires an independent follow-up study.

## Start here

- [Literature dependencies](docs/sources/LITERATURE_DEPENDENCIES.md), [Chicago bibliography](docs/sources/BIBLIOGRAPHY_CHICAGO.md) and [citation conventions](docs/sources/CITATION_GUIDE.md).
- **New maintainer:** read the [continuation handoff](docs/HANDOFF.md), [data dictionary](data/DICTIONARY.md) and [source catalogue](docs/sources/README.md).
- **Known issue:** [hosted numerical reproduction fails](docs/validation/hosted-2026-11-24/README.md) despite passing repository checks and 34 tests; investigation remains open.

- [Deep audit and dispositions](docs/audits/2026-11-23-DEEP_AUDIT.md), [strict acceptance criteria](docs/ACCEPTANCE_CRITERIA.md) and [claim evidence map](docs/CLAIM_EVIDENCE_MAP.json).
- [Action plan](docs/PROJECT_PLAN.md), [current state](docs/PROJECT_STATE.json) and [research charter](docs/RESEARCH_CHARTER.md).
- [Assumptions](docs/protocols/ASSUMPTIONS.md), [experiment protocol](docs/protocols/EXPERIMENT_PROTOCOL.md) and [next work packages](docs/work_packages/README.md).
- [Working manuscript](docs/manuscript/MANUSCRIPT_WORKING_DRAFT.md) and [prior-work comparison](docs/manuscript/PRIOR_WORK_COMPARISON.md).
- [Reproduction instructions](docs/REPRODUCIBILITY.md), [data provenance](data/README.md) and [contribution workflow](CONTRIBUTING.md).

## Run the existing analysis

Use Python 3.13 in a virtual environment:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/check_repository.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/reproduce.py
```

The runner uses the ten existing scientific scripts, three source ledgers and thirteen fixed reference tables. It writes into a fresh ignored `runs/` directory and never overwrites the source data or historical outputs. The numerical comparison permits only the documented floating-point tolerance in two TLS-related fields; all other fields must match exactly. Reproduction does not establish ancient positions, astronomical intention or publication readiness.

## Repository layout

| Directory | Contents |
|---|---|
| `framework/`, `cases/` | Candidate shared design, Nabta navigation and prospective case template |
| `docs/` | Canonical plan/state, protocols, work packages, provisional manuscript and curated evidence notes |
| `analysis/` | Existing scientific scripts, preserved byte-for-byte from the checked pipeline |
| `data/source/` | Three transcribed input ledgers |
| `data/reference/` | Thirteen fixed historical output tables |
| `scripts/`, `tests/` | Portable runner, integrity checks and failure-mode tests |
| `runs/` | Generated local results, ignored by Git |
| `agent_artifacts/`, `legacy/` | Preserved local archive, source PDFs and worker material, ignored by Git |

A clone contains everything needed for numerical reproduction. Primary publication PDFs, survey records and historical worker transcripts are not included; see [local archive](docs/LOCAL_ARCHIVE.md). New accepted research belongs in the curated directories; worker scratch material stays in agent_artifacts.

## Research limits and rights

Published coordinate versions are dependent evidence. Membership and point identities remain partly unresolved; quarry chronology does not directly date individual rows. Mathematical bounds are conditional scenarios, not confidence intervals. The current paper and framework claims remain under review.

This public working-research repository includes the curated analysis, evidence ledgers, provisional manuscript, plans and review protocols. Public availability does not establish scientific acceptance or paper submission. Author attribution and an outbound licence have not been finalized; see [RIGHTS.md](RIGHTS.md).
