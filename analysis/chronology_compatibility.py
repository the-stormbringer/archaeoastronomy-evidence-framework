from pathlib import Path
import csv,json
B=Path(__file__).resolve().parent;O=B/'analysis/identity-chronology-2026-10-24';r=list(csv.DictReader((B/'source_reconciliation-2026-10-22/published_claims.csv').open()));out=[]
for x in r:
 if x['source']!='Malville et al. 2007' or not x['date_range_as_printed']:continue
 older,younger=map(int,x['date_range_as_printed'].split('–'))
 for end in [4200,4100]:
  length=max(0,min(older,4600)-max(younger,end));gap=max(0,end-older,younger-4600)
  out.append(dict(group=x['alignment'],target=x['target_as_printed'],published_target_date_BC=x['date_range_as_printed'],context_window_BC=f'4600–{end}',intersection_duration_years=length,minimum_gap_years=gap,status='overlap' if length>0 else 'touching' if gap==0 else 'no overlap',interpretation='Conditional interval arithmetic only; context window is a source hypothesis, not a hard row-construction bound; no likelihood or probability assigned.'))
with (O/'chronology_compatibility.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
assert len(out)==14
assert all(x['status']=='no overlap' for x in out if x['group']=='A1' or (x['group']=='B2' and x['target']=='Sirius'))
assert all(x['status']=='overlap' for x in out if x['group']=='B1')
print(json.dumps(out,indent=2))
