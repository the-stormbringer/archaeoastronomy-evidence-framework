"""Conditional identity checks; no georeferencing or ancient-position inference."""
from pathlib import Path
import csv,json,math
from pyproj import Geod
B=Path(__file__).resolve().parent;O=B/'analysis/identity-chronology-2026-10-24';O.mkdir(exist_ok=True)
r=list(csv.DictReader((B/'source_reconciliation-2026-10-22/source_coordinate_observations.csv').open()));g=Geod(ellps='WGS84');out=[]
for s in dict.fromkeys(x['source_id'] for x in r):
 d={x['label']:x for x in r if x['source_id']==s}
 for a,b in [('A-4','A-X'),('A-5','A-6')]:
  x,y=d[a],d[b];la,lo,lb,lp=map(float,[x['latitude_printed'],x['longitude_printed'],y['latitude_printed'],y['longitude_printed']]);dist=g.inv(lo,la,lp,lb)[2]
  # Minimum meridional gap between latitude rounding intervals; a conservative
  # local-distance screening bound under WGS84 and nearest rounding to 0.0001 deg.
  low,high=sorted([la,lb]);gap=max(0,g.inv(0,low+.00005,0,high-.00005)[2]) if high-low>.0001 else 0
  out.append(dict(source=s,pair=f'{a}/{b}',same_cell_2025='r20' if a=='A-4' else 'x20',published_point_separation_m=dist,meridional_gap_after_rounding_m=gap,maximum_square_side_tested_m=50,maximum_square_diagonal_m=50*math.sqrt(2),incompatible_under_test=gap>50*math.sqrt(2),scope='Same labelled features, same physical positions, square side <=50m, nearest coordinate rounding, WGS84 assumed. Not proof which source is wrong.'))
with (O/'same_cell_screen.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
# Cross-publication date-label arithmetic; do not convert or recalibrate radiocarbon ages.
claims=list(csv.DictReader((B/'source_reconciliation-2026-10-22/published_claims.csv').open()));dates=[]
for old in claims:
 if old['source']!='Malville et al. 2007' or not old['date_range_as_printed']:continue
 for new in claims:
  if new['source']!='Malville 2015' or new['alignment']!=old['alignment']:continue
  target=old['target_as_printed'];same=target==new['target_as_printed'] or (target=='α Centauri' and new['target_as_printed']=='α Cen')
  if not same:continue
  a=[int(x.replace(',','')) for x in old['date_range_as_printed'].split('–')];b=[int(x.replace(',','')) for x in new['date_range_as_printed'].split('–')]
  dates.append(dict(group=old['alignment'],target=target,BC_2007=old['date_range_as_printed'],BP_2015=new['date_range_as_printed'],older_endpoint_offset=b[0]-a[0],younger_endpoint_offset=b[1]-a[1],status='Source-labelled ranges retained; 2000-year arithmetic offset observed, BP epoch not silently assumed'))
with (O/'date_label_comparison.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(dates[0]));w.writeheader();w.writerows(dates)
assert len(out)==8 and len(dates)==5
assert all(x['incompatible_under_test'] for x in out if x['pair']=='A-4/A-X')
assert all(x['older_endpoint_offset']==x['younger_endpoint_offset']==2000 for x in dates)
(O/'validation.json').write_text(json.dumps({'pair_records':len(out),'matched_date_ranges':len(dates),'all_five_date_ranges_offset_2000':True,'AX_A4_incompatible_in_all_four_table_versions_under_stated_test':True,'independence_warning':'Repeated WM values are not a fourth independent survey.'},indent=2)+'\n')
print(json.dumps(out,indent=2));print(json.dumps(dates,indent=2))
