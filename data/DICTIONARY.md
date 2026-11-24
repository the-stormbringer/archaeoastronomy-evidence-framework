# Data dictionary and dependency rules

[INVENTORY.json](INVENTORY.json) enumerates all 42 public CSV files with exact headers, row counts and SHA-256. Fields in auxiliary tables retain their original names and source notes; this inventory is not an inference that all numeric columns use the same units.

## Three pipeline inputs

| File | Rows | Observation unit |
|---|---:|---|
| `source/source_coordinate_observations.csv` | 100 | One printed coordinate representative in one source version, including origins and missing coordinates |
| `source/membership_scenarios.csv` | 47 | One label's assignment in a table or narrative alternative |
| `source/published_claims.csv` | 19 | One published alignment/target claim, possibly without a numerical date |

Coordinate fields: `source_id` distinguishes versions; `source_page` preserves printed locator; `label` preserves feature name; `latitude_printed` and `longitude_printed` retain decimal-degree strings and their decimal resolution; `alignment_as_table` records table grouping; `datum`, `status`, `change_from_legacy` retain evidence qualifications. Missing values are unknown/unreported, never zero. Do not infer a verified datum from apparent geographic plausibility.

`WM2001_original` is the 2001 Table 16.1 transcription. `BR2005_repeated_WM2001` repeats that source in 2005; `BR2005_QB2002` and `BR2005_GPS2003` are the satellite/GPS columns in the 2005 source. These are dependent documentary versions, not four independent sets of monuments. Repeated feature names do not prove physical point identity across sources.

Membership fields: `scenario` is `WM2001_table` or `WM2001_narrative`; `alignment` is the group; `label` is its named member; `origin` is the named origin; `status` preserves that neither alternative is automatically preferred. Source-specific memberships must not be silently pooled.

Claim fields: `source`, `printed_page`, `alignment` locate the claim; `azimuth_degrees` is the published direction; `target_as_printed` retains the target name; `date_range_as_printed` and `date_unit_as_printed` preserve source conventions; `date_evidence_type`, `verification`, `status` qualify the evidence. A target-fit BC range is not an independently dated construction interval. A blank date is not a zero or infinite interval. Do not silently translate historical BC into astronomical year numbering.

## Other public data

`reference/` holds thirteen fixed derived CSVs. Their allowed comparisons are defined in `pipeline.json`; they are not ancient ground truth. `docs/evidence/` contains chronology transcriptions, documentary identity candidates, quarry records and map-path observations. Map fields ending `_pdf_pt` are drawing-space points, not latitude/longitude or measured stone centres. A drawn path need not be one stone. `support/historical/` contains older diagnostic tables, explicitly outside the accepted runner.

Use the [claim evidence map](../docs/CLAIM_EVIDENCE_MAP.json) and adjacent evidence notes for interpretation. Conditional bounds and rounding scenarios are not confidence intervals. Preserve all original headers, units, source labels and missingness when deriving new tables. Log any corrected transcription with its source page and affected claims before updating the pipeline hashes.

`docs/validation/hosted-2026-11-24/generated/` retains thirteen hosted-run outputs that failed the existing comparison contract in nine tables. These are diagnostic evidence, not new accepted reference data.
