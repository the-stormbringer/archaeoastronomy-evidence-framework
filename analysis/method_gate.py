"""Evaluate a specified combination family and a geometric celestial-coordinate transform."""
from pathlib import Path
import csv,json,math
B=Path(__file__).resolve().parent;O=B/'analysis/geometry-comparison-2026-10-23'
def read(n):return list(csv.DictReader((O/n).open()))
def write(n,r):
 with (O/n).open('w') as f:
  w=csv.DictWriter(f,fieldnames=r[0]);w.writeheader();w.writerows(r)
r=read('comparisons.csv');expected={'A3':25.86,'A2':27.68,'A1':30.00,'B2':117.49,'B1':121.11,'C1':130.10};out=[]
for model in ['sphere','WGS84_assumed']:
 for group,published in expected.items():
  q=[x for x in r if x['source'] in ['BR2005_GPS2003','BR2005_QB2002'] and x['group']==group and x['model']==model]
  vals=[float(x['arithmetic_mean_deg']) for x in q];lo,hi=min(vals),max(vals)
  out.append(dict(group=group,model=model,published_final_deg=published,input_min_deg=lo,input_max_deg=hi,outside_convex_range_deg=max(lo-published,published-hi,0),both_rows_complete=all(x['n_available']==x['n_listed'] for x in q),scope='nonnegative weighted average of two printed-coordinate row means only'))
write('combination_family_check.csv',out)
def dec(a,h,lat):
 a,h,lat=map(math.radians,[a,h,lat]);return math.degrees(math.asin(math.sin(lat)*math.sin(h)+math.cos(lat)*math.cos(h)*math.cos(a)))
assert abs(dec(90,0,22.508))<1e-12
assert abs(dec(0,0,22.508)-(90-22.508))<1e-10
assert abs(dec(180,0,22.508)+(90-22.508))<1e-10
coords=list(csv.DictReader((B/'source_reconciliation-2026-10-22/source_coordinate_observations.csv').open()))
lats={x['source_id']:float(x['latitude_printed']) for x in coords if x['alignment_as_table']=='Complex Structure A'}
rr=read('rounding_scenarios.csv');dd=[]
for x in rr:
 for h in [0,1,2]:
  a,b=float(x['sampled_min_deg']),float(x['sampled_max_deg']);lat=lats[x['source']]
  v=[dec(a,h,lat),dec(b,h,lat)]
  dd.append(dict(source=x['source'],group=x['group'],complete=x['complete'],geometric_altitude_deg=h,declination_min_deg=min(v),declination_max_deg=max(v),declination_width_deg=max(v)-min(v),scope='fixed altitude scenario; no refraction, extinction, target date or intentionality inferred'))
write('declination_scenarios.csv',dd)
(O/'method_gate_validation.json').write_text(json.dumps({'combination_rows':len(out),'declination_rows':len(dd),'transform_checks':['east at zero altitude gives zero declination','north/south cardinal values'],'combined_method_not_reproduced':True},indent=2)+'\n')
print(json.dumps(out,indent=2))
