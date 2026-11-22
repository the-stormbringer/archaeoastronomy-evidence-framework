from pathlib import Path
import csv,json,random
from pyproj import Geod
B=Path(__file__).resolve().parent;O=B/'analysis/case-study-2026-10-24'
R=list(csv.DictReader((B/'source_reconciliation-2026-10-22/source_coordinate_observations.csv').open()));V=[x for x in csv.DictReader((O/'continuous_spherical_contrasts.csv').open()) if x['origin_axis_subdivisions']=='16'];g=Geod(a=6371008.8,b=6371008.8);rng=random.Random(20261024);n=0
for source in sorted({x['source_id'] for x in R}):
 data=[x for x in R if x['source_id']==source];origin=next(x for x in data if x['alignment_as_table']=='Complex Structure A');groups={k:[x for x in data if x['alignment_as_table']==k] for k in ['A3','A2','A1']};limits={x['contrast']:(float(x['lower_enclosure_deg']),float(x['upper_enclosure_deg'])) for x in V if x['source']==source}
 def point(p):return (float(p['longitude_printed'])+rng.uniform(-.00005,.00005),float(p['latitude_printed'])+rng.uniform(-.00005,.00005))
 for i in range(2000):
  org=point(origin);means={k:sum(g.inv(*org,*point(p))[0] for p in ps)/len(ps) for k,ps in groups.items()}
  for a,b in [('A2','A3'),('A1','A2'),('A1','A3')]:
   lo,hi=limits[f'{a} minus {b}'];assert lo<=means[a]-means[b]<=hi;n+=1
(O/'independent_interval_validation.json').write_text(json.dumps(dict(seed=20261024,draws_per_source=2000,contrasts_checked=n,independent_calculation='pyproj spherical inverse geodesic; independently drawn interiors and shared origin',all_inside_interval_enclosures=True,limit='Sampling is a cross-check of implementation, not the basis of the continuous enclosure claim.'),indent=2)+'\n');print(n,'independent sampled contrasts inside enclosures')
