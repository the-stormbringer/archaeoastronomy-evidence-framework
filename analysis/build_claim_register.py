from pathlib import Path
import csv,json
B=Path(__file__).resolve().parent;G=B/'analysis/geometry-comparison-2026-10-23';I=B/'analysis/identity-chronology-2026-10-24';O=B/'analysis/case-study-2026-10-24';O.mkdir(exist_ok=True)
def rows(p):return list(csv.DictReader(p.open()))
def rel(p):return str(p.relative_to(B))
claims=[]
def add(id,status,claim,evidence,limit,next_test):claims.append(dict(id=id,status=status,claim=claim,evidence=evidence,limit=limit,next_test=next_test))
x=json.loads((G/'validation.json').read_text());assert x['rows']==48
add('C01','reproduced','All six BR2005 recalculated-WM mean directions reproduced within 0.005 degrees.',rel(G/'validation.json'),'Specific historical column and spherical arithmetic-mean reduction only; not original survey accuracy.','Preserve benchmark and input hash in release.')
r=rows(G/'membership_comparison.csv');a=next(x for x in r if x['scenario']=='WM2001_narrative' and x['group']=='A2');b=next(x for x in r if x['scenario']=='WM2001_table' and x['group']=='A2');delta=float(a['mean_deg'])-float(b['mean_deg'])
add('C02','conditional',f'A2 narrative versus table membership changes the computed direction by {delta:.6f} degrees.',rel(G/'membership_comparison.csv'),'Both membership alternatives are documentary scenarios; neither is certified ancient alignment membership.','Keep separate; do not average with arbitrary weights.')
r=rows(G/'combination_family_check.csv');complete=[x for x in r if x['both_rows_complete']=='True'];assert len(complete)==8 and all(float(x['outside_convex_range_deg'])>0 for x in complete)
add('C03','conditional','Four complete groups fail the tested convex combination of printed QB/GPS row means under both Earth models.',rel(G/'combination_family_check.csv'),'Excludes only this reduction family; unrounded positions, different weights and other reductions remain possible.','No stronger claim without actual reduction details.')
x=json.loads((G/'estimand_validation.json').read_text())
add('C04','conditional',f"Largest complete-group circular/arithmetic difference is {x['largest_complete_circular_minus_arithmetic_deg']:.6f} degrees; origin-constrained TLS/mean difference is {x['largest_complete_TLS_minus_mean_deg']:.6f} degrees.",rel(G/'estimand_validation.json'),'TLS and radial bearing means estimate different quantities.','Explain estimand choice before comparing results.')
r=rows(G/'shared_origin_contrasts.csv');a=[x for x in r if x['complete']=='True' and x['contrast']=='A2 minus A3'];z=[x for x in r if x['complete']=='True' and x['contrast']=='A1 minus A2']
assert all(float(x['sampled_min_deg'])>0 for x in a+z)
add('C05','finite-grid finding',f"A3 < A2 < A1 holds on the tested shared-origin grids; smallest sampled adjacent gaps are {min(float(x['sampled_min_deg']) for x in a):.6f} and {min(float(x['sampled_min_deg']) for x in z):.6f} degrees.",rel(G/'shared_origin_contrasts.csv'),'Not certified over continuous coordinate intervals, other memberships or original ancient positions.','Continuous-domain validation required before stronger robustness wording.')
r=rows(I/'same_cell_screen.csv');a=[x for x in r if x['pair']=='A-4/A-X'];assert all(x['incompatible_under_test']=='True' for x in a)
add('C06','conditional incompatibility','A-X/A-4 same-square interpretation fails the permissive <=50 m square and nearest-rounding scenario in all four table versions.',rel(I/'same_cell_screen.csv')+'; '+rel(I/'FINDINGS.md'),'Does not identify which record is wrong; repeated WM values are dependent.','Keep identity unresolved unless new public evidence appears.')
r=rows(I/'date_label_comparison.csv');assert len(r)==5
add('C07','documentary arithmetic','Five matched 2007 BC / 2015 BP date ranges differ by exactly 2000 at both endpoints.',rel(I/'date_label_comparison.csv'),'Not a correction, new calibration or established explanation of author convention.','Retain original conventions; do not silently pool.')
r=rows(I/'chronology_compatibility.csv');assert len(r)==14
add('C08','conditional chronology','A1/Arcturus and later B2/Sirius have no overlap with either contextual quarry window; both B1 candidates overlap both windows.',rel(I/'chronology_compatibility.csv'),'Quarry window is a source hypothesis, not a hard construction bound; overlap durations are not probabilities.','Do not reject or select targets solely from this screen.')
add('C09','unresolved','Published map shapes and fragment descriptions do not establish a pointwise match to the older B coordinate IDs.','source_reconciliation-2026-10-22/monograph2025/map_audit/README.md','Absence of established mapping in reviewed evidence is not proof no such record exists.','No nearest-neighbour identity assignment or invented point definition.')
add('C10','not established','A unique ancient target, original row-construction date, intentionality and general framework validity remain unestablished.','analysis/geometry-comparison-2026-10-23/EVIDENCE_GATE.md','These are limits of the present analysis, not universal impossibility claims.','Require independent archaeological association, physical reconstruction and validated astronomical/inferential models.')
r=rows(O/'continuous_spherical_contrasts.csv');r=[x for x in r if x['origin_axis_subdivisions']=='16'];assert len(r)==12 and all(x['strictly_positive']=='True' for x in r)
a=min(float(x['lower_enclosure_deg']) for x in r if x['contrast']=='A2 minus A3');b=min(float(x['lower_enclosure_deg']) for x in r if x['contrast']=='A1 minus A2')
add('C11','continuous numerical enclosure',f'Spherical arithmetic-mean A3 < A2 < A1 holds over the specified continuous rounding boxes; outward lower enclosures are at least {a:.6f} and {b:.6f} degrees for adjacent contrasts.',rel(O/'continuous_spherical_contrasts.csv')+'; '+rel(O/'continuous_validation.json')+'; '+rel(O/'independent_interval_validation.json'),'Conditional on table memberships, spherical model and independent stone rounding boxes with a shared origin. Not a formal proof-assistant certificate or a WGS84/ancient-position result.','Retain precise interval method and independent validation in release; do not replace the distinct WGS84 finite-grid record.')
with (O/'claim_register.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(claims[0]));w.writeheader();w.writerows(claims)
text='# Claim-to-evidence register\n\nGenerated from saved analysis outputs; this is an internal scientific audit, not a submission-ready manuscript.\n\n'
for c in claims:text+=f"## {c['id']} — {c['status']}\n\n{c['claim']}\n\nEvidence: `{c['evidence']}`\n\nLimit: {c['limit']}\n\nNext: {c['next_test']}\n\n"
(O/'CLAIMS.md').write_text(text);print(f'Generated {len(claims)} linked claims.')
