# Hosted reproduction failure — 24 November 2026

Public GitHub Actions run: https://github.com/the-stormbringer/nabta/actions/runs/45407872761
Tested commit: `0d8b1ebb528a6e845ed0382cbd7d9781157523ae`.

A clean hosted dependency installation, repository checks and all 34 tests passed. All ten numerical scripts ran, and thirteen tables were compared. Four were byte-identical; nine failed the existing comparison contract. Reported differences were numeric, with largest reported absolute difference about 3.52e-10 in the same-cell screen. Values have different units across tables; this maximum is not a single angular error estimate. The root cause has not been established.

The exact [validation receipt](VALIDATION.json), [provenance](PROVENANCE.json), [pipeline contract](PIPELINE.json) and [table summary](SUMMARY.json) are retained here so the failure evidence survives the Actions artifact's seven-day retention. Paths in receipts describe the original runner and are historical metadata, not dependencies of a clone. All thirteen generated comparison tables and ten script logs are retained under `generated/` and `logs/` beside these receipts, so differences can be inspected without rerunning or relying on expiring artifacts. They are failed-run evidence, not replacement reference tables.

This is a new cross-host reproducibility issue. It does not invalidate every mathematical claim by itself, nor is it a passing numerical validation. Do not broaden tolerances or overwrite the reference tables based on apparent smallness alone. Compare Python, mathematical libraries, binary builds and numerical paths; inspect decision boundaries and document justified changes before any acceptance. Existing scientific scripts, references and tolerance rules were not changed during publication or handoff.
