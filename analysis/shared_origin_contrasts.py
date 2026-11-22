"""Pairwise angular contrasts under a single shared origin and nearest-rounding scenarios."""
from pathlib import Path
from itertools import product
import csv,json
from pyproj import Geod
B=Path(__file__).resolve().parent;O=B/'analysis/geometry-comparison-2026-10-23';g=Geod(ellps='WGS84')
r=list(csv.DictReader((B/'source_reconciliation-2026-10-22/source_coordinate_observations.csv').open()));offsets=[-.00005,-.000025,0,.000025,.00005];out=[]
def coord(x):return float(x['longitude_printed']),float(x['latitude_printed'])
def angles(o,ps):return [g.inv(*o,*p)[0]%360 for p in ps]
for source in sorted({x['source_id'] for x in r}):
 data=[x for x in r if x['source_id']==source];o=coord(next(x for x in data if x['alignment_as_table']=='Complex Structure A'))
 groups={a:[x for x in data if x['alignment_as_table']==a] for a in ['A3','A2','A1','B2','B1']}
 for a,b in [('A2','A3'),('A1','A2'),('A1','A3'),('B1','B2')]:
  complete=all(x['latitude_printed'] and x['longitude_printed'] for x in groups[a]+groups[b])
  ps={k:[coord(x) for x in groups[k] if x['latitude_printed'] and x['longitude_printed']] for k in [a,b]}
  nom=sum(angles(o,ps[a]))/len(ps[a])-sum(angles(o,ps[b]))/len(ps[b]);lows=[];highs=[]
  for dx,dy in product(offsets,repeat=2):
   oo=(o[0]+dx,o[1]+dy);bounds={}
   for k in [a,b]:
    mn=[];mx=[]
    for p in ps[k]:
     v=angles(oo,[(p[0]+x,p[1]+y) for x,y in product(offsets,repeat=2)]);mn.append(min(v));mx.append(max(v))
    bounds[k]=(sum(mn)/len(mn),sum(mx)/len(mx))
   lows.append(bounds[a][0]-bounds[b][1]);highs.append(bounds[a][1]-bounds[b][0])
  out.append(dict(source=source,contrast=a+' minus '+b,complete=complete,nominal_deg=nom,sampled_min_deg=min(lows),sampled_max_deg=max(highs),ordering_preserved_on_grid=min(lows)>0,scope='shared origin within contrast; finite rounding grid; table membership only'))
with (O/'shared_origin_contrasts.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=out[0]);w.writeheader();w.writerows(out)
assert all(x['sampled_min_deg']<=x['nominal_deg']<=x['sampled_max_deg'] for x in out)
print(json.dumps(out,indent=2))
