> Historical evidence record. Dates and acquisition statements below describe the original review; use [current project state](../../PROJECT_STATE.json) for current status.

# First source-reconciliation milestone — 22 October 2026

Scope: visually checked alignment tables in the 2007 article (printed p.5), 2008 chapter (p.139), and 2015 handbook chapter (p.1086). This is a bounded first ledger, not completed source adjudication or accepted analysis data. No legacy data or research code were changed.

## Verified findings

- `published_claims.csv` records 19 source-claim entries, preserving original labels, units and target groupings. Repeated claims across publications are not independent observations.
- The five inherited 2015 CSV rows accurately transcribe all tabulated azimuths, targets and date ranges; see `legacy_2015_check.json`. Their scientific validity is a separate question.
- A2 is 28.1 degrees in 2007 and 2015 but 28.3 in 2008. This is visible in the original tables, not an OCR artifact. It remains an unresolved publication discrepancy; neither a correction nor a new measurement is established.
- B2 changes presentation: 2007 lists Alnilam, Sirius and winter solstice; 2008 lists Alnilam (printed “Alinlam”) and winter solstice; 2015 lists Belt of Orion. Omission from a later summary is not evidence of formal withdrawal. These cannot silently become one invariant target hypothesis.
- The 2007 table gives BC ranges while 2015 gives BP. For A3, A2, A1 and both B1 targets, corresponding numerical endpoints differ by exactly 2,000. This does not establish a valid BP conversion: conventional BP uses 1950, and the source convention must be traced before normalization. B2 also changes numerical ranges and target specificity, so a uniform conversion cannot reconcile the full table.
- Tabulated stellar date ranges describe astronomical associations. They are not independent archaeological construction dates and must not be reused as such to validate the proposed stellar association.

## Chronological and geometric context: extraction pending full verification

The 2007 printed p.4 (visually checked) associates five quarry radiocarbon dates with 4500–4200 BC and mentions a 3600 BC date for Complex Structure E; the authors infer a broader megalith period of roughly 4500–3600 BC. These are context-based associations. Laboratory IDs, measured ages, calibration details and the association to individual rows are not provided in this passage and must be traced to the underlying records.

The 2008 pp.136–138 text states that the five rows radiate from Complex Structure A, combines two GPS sets and satellite measurements, assumes a level horizon and includes ±0.6 degrees uncertainty. The 2007 p.5 visually checked text additionally says refraction and extinction were included and describes uncertainty from fragmentation and irregular stele positions. Neither the wording nor ±0.6 alone establishes a Gaussian standard deviation or a confidence interval. Do not assign a distribution without justification.

The 2007 p.5 visually checked text declines to interpret C because stones on dunes may not preserve an original alignment. The 2008 p.138 extracted text similarly questions stones on erosional silt hillocks. This supports treating C as a contested-feature scenario, not an unquestioned sixth astronomical alignment. It does not prove the row never existed.

The 2015 p.1085 extracted text reports quarry dates of 6,600–6,200 BP. The table on visually checked p.1086 supplies astronomical ranges and discusses stored blocks and A1 as an exception. Calibration/unit provenance and the link between quarrying, storage and placement require separate adjudication; no calendar conversion has been adopted here.

## Evidence locations

- 2007 PDF: `../analysis/assessment-2026-10-19/literature/source-inspection/malville_2007.pdf`, PDF pages 3–4, printed pp.4–5. Existing checked renders remain in that directory.
- 2008 PDF: `../source_library-2026-10-22/papers/malville2008.pdf`, PDF page 9, printed p.139. Checked render: `m2008-09.png`.
- 2015 PDF: `../source_library-2026-10-22/papers/malville2015.pdf`, PDF page 8, printed p.1086. Checked render: `m2015-08.png`.

## Next reconciliation gates

1. Crosswalk these alignment names to physical stones and the sourcebook/Brophy–Rosen coordinate tables. Resolve narrative/table identity conflicts explicitly; do not infer membership from similar labels alone.
2. Trace the quarry and Complex E dates to sample-level records. Preserve raw radiocarbon dates, calibrated ranges, astronomical dates and author summaries separately.
3. Determine the origin and construction of each published azimuth and whether the A2 discrepancy has a documented explanation.
4. Incorporate the missing early papers and any reassessment when supplied. Record what they change rather than postponing all work.
5. Only after those checks, freeze defensible geometry/date scenarios and decide which astronomical comparisons are warranted.

## Extended available-source pass

See [DECISIONS.md](DECISIONS.md) for the subsequent coordinate verification, recovered quarry measurements, chronology dependencies, successful spherical-bearing reproduction and exact source-dependent decisions. This supersedes the earlier pending numerical-quarry-data status. New CSVs preserve documentary alternatives; conditional numerical outputs are not accepted astronomical conclusions.
