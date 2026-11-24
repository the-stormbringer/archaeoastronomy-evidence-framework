from pathlib import Path
import csv,json,math,hashlib
from pyproj import Geod
base=Path('/tmp/nabta-reconciliation');root=Path('/home/stormbringer/Research_Projects/nabta');old=root/'legacy/MC/P1T1'
def read(p):return list(csv.DictReader(p.read_text().strip().splitlines()))
def write(name,rows):
 with (base/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
wm=read(old/'nabta_alignment_table.csv');br=read(old/'brophy_rosen_coords.csv');obs=[]
for r in wm:
 obs.append(dict(source_id='WM2001_original',source_page='498 Table 16.1',label=r['Megalith'],latitude_printed=f"{float(r['Latitude']):.4f}",longitude_printed=f"{float(r['Longitude']):.4f}",alignment_as_table=r['Alignment'],datum='not established in checked passage',status='visually checked published coordinates; physical identity not fully adjudicated',change_from_legacy='none'))
membership={r['Megalith']:r['Alignment'] for r in wm};membership.update({'A':'Complex Structure A','C-6':'C1'})
for ds,suffix in [('BR2005_repeated_WM2001','WM_2001'),('BR2005_QB2002','QB_2002'),('BR2005_GPS2003','GPS_2003')]:
 for r in br:
  lat,lon=r['lat_'+suffix],r['long_'+suffix];change='none'
  if r['Megalith']=='A-7' and suffix=='GPS_2003':lat,lon='22.5131','30.7289';change='Corrected legacy 22.5130/30.7288 to visually checked Table 1 values; legacy preserved'
  obs.append(dict(source_id=ds,source_page=('16' if r['Megalith'].startswith('A') else '17')+' Table 1',label=r['Megalith'],latitude_printed=lat,longitude_printed=lon,alignment_as_table=membership[r['Megalith']],datum='not established in checked passage',status='visually checked published coordinates; physical identity not fully adjudicated' if lat else 'missing in published table; no imputation',change_from_legacy=change))
write('source_coordinate_observations.csv',obs)
assert len(obs)==100
assert sum(not x['latitude_printed'] for x in obs)==2
# Explicit source membership alternatives. Never turn unresolved names into a single canonical identity.
mem=[]
table={'A3':['A-1','A-2','A-3'],'A2':['A-0','A-4','A-X'],'A1':['A-5','A-6','A-7','A-8','A-9'],'B2':['B-1','B-2','B-3','B-4'],'B1':['B-5','B-6','B-7'],'C1':['C-1','C-2','C-3','C-4','C-5','C-8']}
narr={'A3':['A-1','A-2','A-3'],'A2':['A-4','A-5'],'A1':['A-6','A-7','A-8','A-9','A-10'],'B2':['B-1','B-2','B-3','B-4'],'B1':['B-5','B-6','B-7'],'C1':['C-1','C-2','C-3','C-4','C-5','C-6']}
for scen,m in [('WM2001_table',table),('WM2001_narrative',narr)]:
 for a,labels in m.items():
  for label in labels:mem.append(dict(scenario=scen,alignment=a,label=label,origin='Complex Structure A',status='source-defined alternative; not adjudicated'))
write('membership_scenarios.csv',mem)
chron=[]
def date(key,age,sigma,material,context,source,association,note):chron.append(dict(sample_label=key,radiocarbon_age_BP=age,reported_sigma=sigma,material=material,context=context,source=source,association_to_alignment=association,notes=note))
date('DRI-3358',4800,85,'Charcoal','E-96-1; Megalith E; pit under structure','WM2001 Table 3.1 p.54','Different complex structure; no direct row date','Table sigma conflicts with chapter 17 p.517 value 80; p.38 also reports 85. Preserve both; calibration not run.')
date('DRI-3358',4800,80,'Charcoal','Structure E Pit 1; hearth on upper step','WM2001 chapter 17 p.517','Different complex structure; no direct row date','Same sample as table entry, not an independent determination.')
date('CAMS-17287',6000,60,'Charcoal','E-92-9; calendar circle; Hearth 9','WM2001 Table 3.1 p.54','Nearby/contextual; not a row construction date','Do not infer association strength from proximity alone.')
date('CAMS-17289',6470,270,'Wood','E-94-1; northern tumulus; burial pit','WM2001 Table 3.1 p.54','Different monument; not a row construction date','Table says wood; chapter 16 gives contextual discussion. No recalibration yet.')
for label,age,sigma in [('Nabta Playa 2',4450,60),('Nabta Playa 2/BIS',4820,40),('Nabta Playa 3',5600,40),('Nabta Playa 4',5530,40),('Nabta Playa 5',5460,40),('Nabta Playa 6',5450,40),('Nabta Playa 7',5470,40)]:
 date(label,age,sigma,'Not specified in figure; text describes quarry charcoal for 3–7','Ring Hill' if label.endswith(('2','BIS')) else 'Quarry','Malville2015 Fig.89.9 p.1087','Contextual activity; connection to individual rows unproven','Visually transcribed figure labels; not laboratory IDs. Graphic calibrated distributions not digitized; curve/version and detailed context unresolved.')
write('chronology_evidence.csv',chron)
# Conditional geometry diagnostic: source tables remain distinct; ellipsoid is a stated computational assumption.
geod=Geod(ellps='WGS84');results=[]
for ds in sorted({x['source_id'] for x in obs}):
 positions={x['label']:(float(x['longitude_printed']),float(x['latitude_printed'])) for x in obs if x['source_id']==ds and x['latitude_printed']}
 origin=positions['Complex Structure A' if ds=='WM2001_original' else 'A']
 for a,labels in table.items():
  labels=list(labels)
  if ds!='WM2001_original' and a=='C1':labels[-1]='C-6'
  used=[x for x in labels if x in positions];missing=[x for x in labels if x not in positions];az=[]
  for x in used:az.append(geod.inv(*origin,*positions[x])[0]%360)
  mean=math.degrees(math.atan2(sum(math.sin(math.radians(t)) for t in az),sum(math.cos(math.radians(t)) for t in az)))%360
  results.append(dict(source_id=ds,alignment=a,members=';'.join(used),missing_members=';'.join(missing),mean_radial_bearing_deg=mean,min_bearing_deg=min(az),max_bearing_deg=max(az),status='conditional diagnostic; WGS84 assumed; source table membership; no survey accuracy claim'))
write('conditional_radial_geometry.csv',results)
# Verify cardinal geodesic convention used by this diagnostic.
assert abs(geod.inv(30,22,30,23)[0])<1e-9
assert abs(geod.inv(30,0,31,0)[0]-90)<1e-9
write('source_input_hashes.csv',[{'file':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [old/'nabta_alignment_table.csv',old/'brophy_rosen_coords.csv']])
print(json.dumps({'coordinate_observations':len(obs),'missing_pairs':2,'chronology_records':len(chron),'radial_diagnostics':len(results),'membership_records':len(mem),'checks':'passed'},indent=2))
