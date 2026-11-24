from pathlib import Path
import csv,math,json
from pyproj import Geod
b=Path('/tmp/nabta-reconciliation');r=list(csv.DictReader((b/'source_coordinate_observations.csv').open()));out=[]
g=Geod(a=6371008.8,b=6371008.8)
p={x['label']:(float(x['longitude_printed']),float(x['latitude_printed'])) for x in r if x['source_id']=='BR2005_repeated_WM2001'}
for a,expected in [('A3',26.83),('A2',28.60),('A1',31.24),('B2',115.81),('B1',118.97),('C1',129.71)]:
 vals=[g.inv(*p['A'],*p[x['label']])[0]%360 for x in r if x['source_id']=='BR2005_repeated_WM2001' and x['alignment_as_table']==a]
 result=sum(vals)/len(vals);assert abs(result-expected)<.005
 out.append(dict(alignment=a,published_BR2005_recalculated_WM_deg=expected,spherical_arithmetic_mean_deg=result,residual_deg=result-expected,check='matches published 0.01 degree rounding'))
with (b/'BR2005_WM_column_reproduction.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=out[0].keys());w.writeheader();w.writerows(out)
print('PASS: all six published recalculated WM2001 values reproduced within 0.005 degrees')
