from pathlib import Path
import csv,json,hashlib
out=Path('/tmp/nabta-reconciliation');rows=[]
def add(src,page,alignment,az,target,date='',unit=''):
 rows.append(dict(source=src,printed_page=page,alignment=alignment,azimuth_degrees=az,target_as_printed=target,date_range_as_printed=date,date_unit_as_printed=unit,date_evidence_type='astronomical association, not independent construction dating' if date else 'no numerical date in this table',verification='visually checked printed table',status='source claim; not independently validated'))
for a,az,t,d in [('A3',26.3,'Arcturus','4530–4320'),('A2',28.1,'Arcturus','4220–4020'),('A1',30.6,'Arcturus','3810–3630'),('B2',116.6,'Alnilam','4340–4150'),('B2',116.6,'Sirius','3700–3430'),('B2',116.6,'Winter Solstice',''),('B1',120.1,'Sirius','4640–4400'),('B1',120.1,'α Centauri','4500–4260')]:add('Malville et al. 2007',5,a,az,t,d,'BC' if d else '')
for a,az,t in [('A3',26.3,'Arcturus'),('A2',28.3,'Arcturus'),('A1',30.6,'Arcturus'),('B2',116.6,'Alinlam Winter solstice'),('B1',120.1,'Sirius α Centauri')]:add('Malville et al. 2008',139,a,az,t)
for a,az,t,d in [('A3',26.3,'Arcturus','6,530–6,320'),('A2',28.1,'Arcturus','6,220–6,020'),('A1',30.6,'Arcturus','5,810–5,630'),('B2',116.6,'Belt of Orion','6,300–6,100'),('B1',120.1,'Sirius','6,640–6,400'),('B1',120.1,'α Cen','6,500–6,260')]:add('Malville 2015',1086,a,az,t,d,'BP')
with (out/'published_claims.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
# Verify inherited 2015 CSV against independently transcribed printed values.
p=Path('/home/stormbringer/Research_Projects/nabta/legacy/MC/P1T1/malville_2015_alignments.csv')
old=list(csv.DictReader(p.read_text().strip().splitlines()))
expected=[('A3','26.3','Arcturus','6530-6320',''),('A2','28.1','Arcturus','6220-6020',''),('A1','30.6','Arcturus','5810-5630',''),('B2','116.6','Belt of Orion','6300-6100',''),('B1','120.1','Sirius; α Centauri','6640-6400','6500-6260')]
for r,e in zip(old,expected):assert tuple(r[k] for k in ['Alignment','Azimuth_deg','Targets','Date_range_BP_1','Date_range_BP_2'])==e
assert len(old)==len(expected)
(out/'legacy_2015_check.json').write_text(json.dumps({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'checked_rows':5,'result':'All alignment, azimuth, target and date fields match printed 2015 p.1086; alpha Centauri abbreviation expanded correctly. This verifies transcription only.'},indent=2))
(out/'README.md').write_text('''# First source-reconciliation milestone — 22 October 2026

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
''')
print('19 claim entries; all 5 inherited 2015 rows checked successfully')
