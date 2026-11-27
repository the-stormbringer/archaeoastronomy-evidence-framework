# Repository architecture and maintainer review — 27 November 2026

Repository: `archaeoastronomy-evidence-framework`. Scope: candidate reusable workflow, developed through the Nabta case. It does not yet provide a general library or completed framework validation.

| Layer | Location | Ownership and change rules |
|---|---|---|
| Framework design | `framework/` | Reusable principles and future interface; no claim of empirical generality |
| Case navigation/intake | `cases/nabta/`, `cases/_template/` | Case-specific next-work location and prospective intake outline |
| Frozen Nabta analysis | `analysis/`, `data/source/`, `data/reference/`, `data/pipeline.json` | Preserve source/reference hashes; controlled corrections only |
| Execution/governance | `scripts/`, `tests/` | Tested runner and acceptance checks; some policies are Nabta-specific |
| Scientific authority | `docs/PROJECT_PLAN.md`, `PROJECT_STATE.json`, protocols and work queue | Canonical scientific state; navigation/roadmaps cannot silently advance it |
| Literature | `docs/sources/` and `docs/evidence/` | Chicago references, access catalogue, cited digest, provenance and reviewed notes |
| Reporting | `docs/manuscript/`, `docs/validation/`, `docs/audits/` | Provisional paper; versioned acceptance and failure evidence |
| Historical support | `support/` | Exact legacy diagnostics; not part of the supported numerical runner |
| Local-only material | ignored `legacy/`, `agent_artifacts/`, `runs/` | Source PDFs, worker scratch and exploratory outputs; never implicit clone dependencies |

## Review findings and disposition

- **Data and code handoff:** input/reference/context CSVs, inventory, ten-script runner and tests are public. Earlier omitted diagnostic/plotting code is in `support/`, with portability limits stated.
- **Scientific context:** plans, acceptance rules, competing interpretations, sources and Chicago references are public. A consolidated cited evidence digest is now provided; it distinguishes published observations from our calculations.
- **Generality:** the previous project title was case-specific. Framework and case indexes now separate intent from validated capability. Existing scientific paths remain unchanged because their hashes and provenance are evidence, not disposable organization.
- **Outstanding execution issue:** hosted numerical comparison fails in nine of thirteen tables despite passing repository checks and 34 tests. Durable actual outputs and logs exist. Investigating this is the first engineering task; no relaxed tolerance or substituted reference is accepted here.
- **Outstanding implementation work:** new E1–E4 engines/records are not implemented by the old benchmark runner; support plotting/extraction scripts are not portable entry points. Treat these as explicit tasks, not completed capabilities.
- **External access:** fresh primary-page adjudication still requires the publications. DOI/catalogue links and hashes are public, research PDFs are not. No original unrounded survey dataset is supplied.
- **Governance:** automated checks validate structure/integrity, not evidence adequacy. Case-specific dependency policies must be amended before new cases are accepted.
- **Rights/authorship:** public availability is authorized, but no outbound reuse licence or final authorship is assigned. Work directed by the owner can continue; a broader contribution/reuse policy remains an owner decision before open collaboration or publication packaging.

A newcomer should start with [HANDOFF.md](HANDOFF.md), then [ROADMAP.md](ROADMAP.md), then the relevant work package. This structural review does not close any scientific gate, fix numerical portability, or make the manuscript submission-ready.
