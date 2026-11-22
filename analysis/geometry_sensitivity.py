"""Deterministic sensitivity scenarios, not confidence bounds or inferred survey errors."""
from pathlib import Path
import csv,json,math,hashlib
from itertools import product
from pyproj import Geod
B=Path(__file__).resolve().parent
D=B/'source_reconciliation-2026-10-22'
O=B/'analysis/geometry-comparison-2026-10-23'
g=Geod(ellps='WGS84')
def coord(r):return float(r['longitude_printed']),float(r['latitude_printed'])
def bearing(o,p):return g.inv(*o,*p)[0]%360
def mean(o,ps):return sum(bearing(o,p) for p in ps)/len(ps)
def write(name,rs):
 with (O/name).open('w') as f:
  w=csv.DictWriter(f,fieldnames=rs[0]);w.writeheader();w.writerows(rs)
def main():
 rows=list(csv.DictReader((D/'source_coordinate_observations.csv').open()))
 members=list(csv.DictReader((D/'membership_scenarios.csv').open()))
 wm={r['label']:r for r in rows if r['source_id']=='WM2001_original'}
 membership=[]
 for scenario in sorted({r['scenario'] for r in members}):
  for group in ['A3','A2','A1','B2','B1','C1']:
   labels=[r['label'] for r in members if r['scenario']==scenario and r['alignment']==group]
   missing=[s for s in labels if s not in wm]
   ps=[coord(wm[s]) for s in labels if s in wm]
   membership.append(dict(scenario=scenario,group=group,available=len(ps),listed=len(labels),missing=';'.join(missing),mean_deg=mean(coord(wm['Complex Structure A']),ps),status='partial; do not interpret as full row' if missing else 'complete coordinate membership'))
 write('membership_comparison.csv',membership)
 rounding=[];origins=[]
 for source in sorted({r['source_id'] for r in rows}):
  data=[r for r in rows if r['source_id']==source]
  origin=next(r for r in data if r['alignment_as_table']=='Complex Structure A');o=coord(origin)
  # Printed values are four decimal places. Half-unit scenarios assume nearest rounding.
  assert all(len(r[k].split('.')[-1])==4 for r in data for k in ['latitude_printed','longitude_printed'] if r[k])
  for group in ['A3','A2','A1','B2','B1','C1']:
   rr=[r for r in data if r['alignment_as_table']==group]
   ps=[coord(r) for r in rr if r['latitude_printed'] and r['longitude_printed']]
   nominal=mean(o,ps);lo=[];hi=[]
   for dx,dy in product([-0.00005,0,.00005],repeat=2):
    oo=(o[0]+dx,o[1]+dy);mins=[];maxs=[]
    for p in ps:
     v=[bearing(oo,(p[0]+x,p[1]+y)) for x,y in product([-.00005,0,.00005],repeat=2)]
     mins.append(min(v));maxs.append(max(v))
    lo.append(sum(mins)/len(ps));hi.append(sum(maxs)/len(ps))
   rounding.append(dict(source=source,group=group,complete=len(ps)==len(rr),nominal_deg=nominal,sampled_min_deg=min(lo),sampled_max_deg=max(hi),sampled_width_deg=max(hi)-min(lo)))
   for radius in [1,5,10,25]:
    v=[]
    for az in range(0,360,5):
     x,y,_=g.fwd(*o,az,radius);v.append(mean((x,y),ps))
    origins.append(dict(source=source,group=group,complete=len(ps)==len(rr),radius_m=radius,sampled_min_deg=min(v),sampled_max_deg=max(v),max_abs_shift_deg=max(abs(x-nominal) for x in v)))
 # Shared-origin dependence: one origin location per group scenario; never independently shifted per stone.
 write('rounding_scenarios.csv',rounding);write('origin_scenarios.csv',origins)
 assert len(membership)==12 and len(rounding)==24 and len(origins)==96
 assert all(r['sampled_min_deg']<=r['nominal_deg']<=r['sampled_max_deg'] for r in rounding)
 # Inverse/forward consistency at an oblique real-site location.
 a,d=37.2,850
 x,y,_=g.fwd(30.7256,22.508,a,d)
 az,_,distance=g.inv(30.7256,22.508,x,y)
 assert abs(az-a)<1e-7 and abs(distance-d)<1e-6
 (O/'sensitivity_validation.json').write_text(json.dumps(dict(checks=['12 membership scenarios','24 coordinate-rounding scenarios','96 origin-radius scenarios','nominal enclosed in sampled rounding envelope','oblique geodesic forward/inverse'],inputs={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [D/'source_coordinate_observations.csv',D/'membership_scenarios.csv']},limitations=['WGS84 assumed','nearest-rounding model assumed, not verified','finite grid extrema are sampled envelopes, not certified bounds','origin radii are hypothetical sensitivity parameters, not measured error','incomplete rows explicitly retained as partial','arithmetic mean used to match historical computation; no bearings wrap through north in these rows']),indent=2)+'\n')
 print(json.dumps({'membership':membership,'rounding_widths':[round(r['sampled_width_deg'],3) for r in rounding if r['complete']],'origin_10m_max_shift':[round(r['max_abs_shift_deg'],3) for r in origins if r['complete'] and r['radius_m']==10]},indent=2))
if __name__=='__main__':main()
