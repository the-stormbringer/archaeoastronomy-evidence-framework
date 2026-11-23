# Nabta repository instructions

- Start with docs/PROJECT_STATE.json and docs/PROJECT_PLAN.md. The current research next step is W1; E1–E4 are pending. Repository work does not advance research gates.
- Preserve legacy/ and historical agent_artifacts inputs. Store all worker packets, scratch notes and logs under agent_artifacts/. Only reviewed research outputs belong in docs/, analysis/ and data/.
- Run scientific scripts through scripts/reproduce.py, which stages their historical layout in an ignored run directory. Running analysis/*.py directly would write into the source tree.
- Never modify data/source or data/reference to make a test pass. Preserve source labels, missing values, dependence and rounding assumptions.
- Keep mathematical verification, archaeological interpretation and scientific contribution distinct. No claim of original stone positions, construction dates or intention follows from numerical repetition.
- Use medium-effort Hermes children for bounded mechanical tasks when useful under the user's established authorization. The main agent retains design, interpretation and acceptance. Inspect real artifacts and tool records; never accept worker self-report as truth. Do not resume old ultra Codex agents.
- No external messaging, publication or pushing to a remote without authorization. Do not inspect credentials or introduce provider fallbacks.
- Checks: python scripts/check_repository.py; python -m unittest discover -s tests -v; python scripts/reproduce.py. Record exact outcomes and limitations.

- Read docs/ACCEPTANCE_CRITERIA.md and the latest docs/audits review before accepting changes. Validate new records under docs/records. Complete stages/tasks require evidence receipts; changes to required dependencies need an explicit plan and validator amendment. Do not infer scientific acceptance from a well-formed receipt.
