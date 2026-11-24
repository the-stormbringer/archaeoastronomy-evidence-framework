from pathlib import Path
import csv,json,math
from itertools import product
from pyproj import Geod
B=Path(__file__).resolve().parent;D=B/'source_reconciliation-2026-10-22';O=B/'analysis/geometry-comparison-2026-10-23'
rows=list(csv.DictReader((D/'source_coordinate_observations.csv').open()))
sphere=Geod(a=6371008.8,b=6371008.8);ellipsoid=Geod(ellps='WGS84')
def pt(r):return float(r['longitude_printed']),float(r['latitude_printed'])
def bearing(g,a,b):return g.inv(*a,*b)[0]%360
errors=[];refinement=[]
for source in sorted({r['source_id'] for r in rows}):
 data=[r for r in rows if r['source_id']==source];o=pt(next(r for r in data if r['alignment_as_table']=='Complex Structure A'))
 for r in data:
  if r['alignment_as_table']=='Complex Structure A' or not r['latitude_printed']:continue
  p=pt(r);l1,f1,l2,f2=map(math.radians,(*o,*p));dl=l2-l1
  a=math.degrees(math.atan2(math.sin(dl)*math.cos(f2),math.cos(f1)*math.sin(f2)-math.sin(f1)*math.cos(f2)*math.cos(dl)))%360
  errors.append(abs(a-bearing(sphere,o,p)))
 for group in ['A3','A2','A1','B2','B1','C1']:
  ps=[pt(r) for r in data if r['alignment_as_table']==group and r['latitude_printed']]
  bounds=[]
  for n in [3,5]:
   offsets=[-.00005+i*.0001/(n-1) for i in range(n)];lows=[];highs=[]
   for dx,dy in product(offsets,repeat=2):
    oo=(o[0]+dx,o[1]+dy);a=[];b=[]
    for p in ps:
     v=[bearing(ellipsoid,oo,(p[0]+x,p[1]+y)) for x,y in product(offsets,repeat=2)]
     a.append(min(v));b.append(max(v))
    lows.append(sum(a)/len(a));highs.append(sum(b)/len(b))
   bounds.append((min(lows),max(highs)))
  refinement.append(max(abs(a-b) for a,b in zip(*bounds)))
assert max(errors)<1e-7
assert max(refinement)<1e-8
out={'independent_spherical_formula_max_difference_deg':max(errors),'rounding_grid_3_to_5_max_endpoint_change_deg':max(refinement),'note':'Finite-grid convergence check only; not proof of global extrema or a survey error model.'}
(O/'independent_validation.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
