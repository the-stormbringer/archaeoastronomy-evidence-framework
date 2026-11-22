from pathlib import Path
import csv,math,json
import numpy as np
from pyproj import Geod
B=Path(__file__).resolve().parent;O=B/'analysis/geometry-comparison-2026-10-23';g=Geod(ellps='WGS84')
r=list(csv.DictReader((B/'source_reconciliation-2026-10-22/source_coordinate_observations.csv').open()))
out=[]
for src in sorted({x['source_id'] for x in r}):
 data=[x for x in r if x['source_id']==src];o=next(x for x in data if x['alignment_as_table']=='Complex Structure A');lon,lat=float(o['longitude_printed']),float(o['latitude_printed'])
 for group in ['A3','A2','A1','B2','B1','C1']:
  rr=[x for x in data if x['alignment_as_table']==group];ps=[x for x in rr if x['latitude_printed']];vectors=[];angles=[]
  for x in ps:
   a,_,d=g.inv(lon,lat,float(x['longitude_printed']),float(x['latitude_printed']));ar=math.radians(a);vectors.append([d*math.sin(ar),d*math.cos(ar)]);angles.append(a%360)
  v=np.array(vectors);eig,axes=np.linalg.eigh(v.T@v);axis=axes[:,-1]
  if np.dot(axis,v.mean(axis=0))<0:axis=-axis
  direction=math.degrees(math.atan2(axis[0],axis[1]))%360
  circular=math.degrees(math.atan2(sum(math.sin(math.radians(a)) for a in angles),sum(math.cos(math.radians(a)) for a in angles)))%360
  arithmetic=sum(angles)/len(angles)
  out.append(dict(source=src,group=group,complete=len(ps)==len(rr),arithmetic_radial_mean_deg=arithmetic,circular_radial_mean_deg=circular,origin_constrained_TLS_deg=direction,TLS_minus_arithmetic_deg=direction-arithmetic,circular_minus_arithmetic_deg=circular-arithmetic))
with (O/'estimand_comparison.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=out[0]);w.writeheader();w.writerows(out)
# A synthetic exactly radial group must recover its known direction regardless of distances.
a=math.radians(31);v=np.array([[d*math.sin(a),d*math.cos(a)] for d in [10,100,700]]);_,axes=np.linalg.eigh(v.T@v);z=axes[:,-1]
if np.dot(z,v.mean(axis=0))<0:z=-z
assert abs(math.degrees(math.atan2(z[0],z[1]))-31)<1e-10
summary={'largest_complete_TLS_minus_mean_deg':max(abs(x['TLS_minus_arithmetic_deg']) for x in out if x['complete']),'largest_complete_circular_minus_arithmetic_deg':max(abs(x['circular_minus_arithmetic_deg']) for x in out if x['complete']),'synthetic_radial_check':'passed','interpretation':'TLS minimizes squared perpendicular displacement in origin-centred geodesic polar coordinates; it weights long sightlines more strongly and is an alternative estimand, not a correction.'}
(O/'estimand_validation.json').write_text(json.dumps(summary,indent=2)+'\n');print(summary)
