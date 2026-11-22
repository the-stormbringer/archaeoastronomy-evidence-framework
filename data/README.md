# Data provenance and reference policy

source/ holds the three original transcribed ledgers: source_coordinate_observations.csv, membership_scenarios.csv and published_claims.csv. Source identifiers, printed page references, missing coordinates and unresolved identities are retained. They are not independent observations of 100 monuments.

reference/ contains the thirteen output tables from the existing October 2026 numerical pipeline. These are repeatability benchmarks, not ground truth about ancient Nabta. pipeline.json records their hashes, execution order and the two columns permitted a 1e-10-degree floating-point difference. All other values and structure require exact agreement. This tolerance originated in the inspected October rerun, not an empirical measurement-error model.

Input ledgers and historical output tables are byte-preserved during repository setup. [Promotion manifest](../docs/PROMOTION_MANIFEST.json) records source and destination hashes. No new transcription or scientific acceptance occurred during packaging. Full-text research copies remain in the ignored local archive; consult source labels and the curated evidence notes for provenance.

To intentionally revise a ledger or reference: document the source correction and affected claim, preserve the old Git revision, inspect all resulting differences, then explicitly update the relevant hashes in pipeline.json. Never refresh hashes automatically during a normal check or run.
