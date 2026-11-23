# Reproducing the existing numerical analysis

Use Python 3.13 and requirements.txt. The pipeline contract in data/pipeline.json locks ten scripts, three input ledgers and thirteen reference tables by SHA-256. Run `python scripts/check_repository.py`, then `python -m unittest discover -s tests -v`, then `python scripts/reproduce.py`. An optional `--output /absolute/new/directory` selects a new external run location; existing directories are refused.

The wrapper stages the scientific scripts and inputs in their original relative layout under the new run directory. It executes them in the declared order with the current interpreter, records logs and dependency versions, compares every declared output, and verifies that locked repository files remain unchanged. The scientific scripts themselves are byte-preserved; running them directly from analysis/ is unsupported because their historical paths assume staging.

Twelve tables matched byte-for-byte in the October isolated environment; the remaining table differed in ten TLS-related cells by at most about 2.84e-14 degrees. Only origin_constrained_TLS_deg and TLS_minus_arithmetic_deg in the named estimand table allow up to 1e-10 degrees of absolute difference. This documented, post-inspection tolerance does not apply to other columns, identities, row counts or files. A missing output fails the run. The reference snapshot is never rewritten automatically.

The wrapper produces VALIDATION.json and per-script logs in ignored runs/. Exact byte equality may depend on the platform; inspect any failure rather than expanding tolerance automatically. Python optimization (-O) is refused because historical scripts include assertion checks.

Scope: existing numerical outputs only. PDF transcription, map extraction, source identity, ancient point reconstruction, stellar calculations, manuscript figure rendering and the new E1–E4 experiments are outside this runner. The manuscript figures are existing snapshots. A successful run is computational repeatability, not scientific or external specialist acceptance.

The CI workflow runs these same checks if this repository is later hosted on GitHub. No remote is configured or publication performed by creating the workflow. Local results are recorded in REPOSITORY_VALIDATION.json after repository acceptance.

Use a UTF-8 environment for the preserved scripts (for example, set `PYTHONUTF8=1`). Their original file I/O uses the interpreter default encoding. The validated configuration is Python 3.13 with the pinned requirements; other Python versions have not been validated here.

## Audit controls and new run receipts

The root record schema now dispatches claim and experiment types; repository checks validate all JSON records recursively under docs/records, required stage/task dependencies, acceptance receipts and the claim-evidence locator map. Fixed tolerance and staging policies cannot be broadened by editing only the pipeline contract. These controls catch the audited failure modes; they do not establish scientific correctness or defend against coordinated rewriting of every policy and reference.

New runs save PIPELINE.json, PROVENANCE.json and VALIDATION.json. Receipts include staged/script/input hashes, runner hashes, generated-output hashes, dependency versions, timestamps and an optional Git revision plus dirty state. A dirty/exported tree remains identifiable by content hashes; no Git revision is fabricated. Child processes explicitly preserve assertions and use UTF-8 even if the launching shell sets PYTHONOPTIMIZE. The installed configuration was tested on the same host; this audit did not perform a clean installation on a second host or run remote CI.

The historical interval script's comment about retaining full endpoint strings overstates its serialized output: it saves outward-padded float summaries. The frozen script is retained unchanged. A future interval implementation should preserve full endpoint representations when needed for auditing; this documentation correction does not demonstrate an invalid enclosure.
