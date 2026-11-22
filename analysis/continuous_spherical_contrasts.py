"""Interval enclosure of spherical radial contrasts, conditional on printed table membership."""
from pathlib import Path
from decimal import Decimal
import csv,json,math,hashlib
import mpmath
from mpmath import iv
from pyproj import Geod
B=Path(__file__).resolve().parent;O=B/'analysis/case-study-2026-10-24';O.mkdir(exist_ok=True)
P=B/'source_reconciliation-2026-10-22/source_coordinate_observations.csv'
R=list(csv.DictReader(P.open()));iv.dps=35
half=Decimal('.00005');rad=iv.pi/180
def box(s):
 a=Decimal(s);return iv.mpf([str(a-half),str(a+half)])
def bearing(olat,olon,lat,lon):
 a,b,c,d=[x*rad for x in [olat,olon,lat,lon]]
 dl=d-b;y=iv.sin(dl)*iv.cos(c);x=iv.cos(a)*iv.sin(c)-iv.sin(a)*iv.cos(c)*iv.cos(dl)
 assert x.a>0 and y.a>0 # northern/eastern chart, no wrapping or singularity
 return iv.atan2(y,x)/rad
def pieces(s,n):
 a=Decimal(s)-half;h=2*half/Decimal(n)
 return [iv.mpf([str(a+i*h),str(a+(i+1)*h)]) for i in range(n)]
results=[];max_residual=0;g=Geod(a=6371008.8,b=6371008.8)
for source in sorted({x['source_id'] for x in R}):
 data=[x for x in R if x['source_id']==source];org=next(x for x in data if x['alignment_as_table']=='Complex Structure A');groups={k:[x for x in data if x['alignment_as_table']==k] for k in ['A3','A2','A1']}
 for ps in groups.values():
  for p in ps:
   vals=[org['latitude_printed'],org['longitude_printed'],p['latitude_printed'],p['longitude_printed']];v=bearing(*[iv.mpf(z) for z in vals]);ref=g.inv(float(vals[1]),float(vals[0]),float(vals[3]),float(vals[2]))[0];max_residual=max(max_residual,abs(ref-float(v.mid)))
 for n in [1,4,16]:
  bounds={('A2','A3'):[],('A1','A2'):[],('A1','A3'):[]}
  for a in pieces(org['latitude_printed'],n):
   for b in pieces(org['longitude_printed'],n):
    means={k:sum((bearing(a,b,box(p['latitude_printed']),box(p['longitude_printed'])) for p in ps),iv.mpf(0))/len(ps) for k,ps in groups.items()}
    for pair in bounds:bounds[pair].append(means[pair[0]]-means[pair[1]])
  for pair,vs in bounds.items():
   # Preserve full interval endpoint strings; floats below are outward-padded summaries.
   low=min(v.a for v in vs);high=max(v.b for v in vs)
   lo=math.nextafter(float(low),-math.inf);hi=math.nextafter(float(high),math.inf)
   results.append(dict(source=source,contrast=f'{pair[0]} minus {pair[1]}',origin_axis_subdivisions=n,origin_boxes=n*n,lower_enclosure_deg=lo,upper_enclosure_deg=hi,strictly_positive=bool(low>0),scope='Spherical arithmetic mean; table membership; continuous nearest-rounding coordinate boxes; shared origin; no physical displacement model'))
assert max_residual<1e-8
assert all(x['strictly_positive'] for x in results if x['origin_axis_subdivisions']==16)
with (O/'continuous_spherical_contrasts.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(results[0]));w.writeheader();w.writerows(results)
# Each refinement partitions the same domain. Bounds must tighten, up to tiny rounding.
for source in sorted({x['source'] for x in results}):
 for contrast in sorted({x['contrast'] for x in results}):
  rs=[x for x in results if x['source']==source and x['contrast']==contrast]
  assert all(y['lower_enclosure_deg']>=x['lower_enclosure_deg']-1e-10 and y['upper_enclosure_deg']<=x['upper_enclosure_deg']+1e-10 for x,y in zip(rs,rs[1:]))
meta=dict(input_sha256=hashlib.sha256(P.read_bytes()).hexdigest(),mpmath_version=mpmath.__version__,interval_decimal_precision=35,point_formula_vs_pyproj_sphere_max_difference_deg=max_residual,all_refined_northern_contrasts_positive=True,domain='Every stone and shared origin within independent +/-0.00005-degree latitude/longitude intervals; original printed table memberships.',caveats=['Interval-library numerical enclosure, not a formal proof-assistant certificate.','No probability distribution assigned.','Spherical model only; does not certify earlier WGS84 grid results.','No identity correction or ancient-position inference.','Repeated WM coordinate version is not independent evidence.'])
(O/'continuous_validation.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta,indent=2));print(json.dumps([x for x in results if x['origin_axis_subdivisions']==16],indent=2))
