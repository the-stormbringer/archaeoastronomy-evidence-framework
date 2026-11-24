"""Read-only diagnostic of inherited data, not a replacement research analysis.
Writes only alongside this file. Does not import or execute inherited code.
"""
from pathlib import Path
import csv,json,itertools,sys
import numpy as np
from pyproj import Transformer,Geod,Proj
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]/'legacy/MC'
geod=Geod(ellps='WGS84')
utm=Transformer.from_crs(4326,32636,always_xy=True)
script_members={'A3':['A-1','A-2','A-3'],'A2':['A-0','A-4','A-X'],'A1':['A-5','A-6','A-7','A-8','A-9'],'B2':['B-1','B-4','B-5','B-6'],'B1':['B-2','B-3','B-7'],'C1':['C-1','C-2','C-3','C-4','C-5','C-6']}
source_members={**script_members,'B2':['B-1','B-2','B-3','B-4'],'B1':['B-5','B-6','B-7']}
data={}
for ds,file in [('legacy','BR_leg.geojson'),('quickbird','BR_QB.geojson'),('gps2003','BR_field.geojson')]:
 features=json.loads((ROOT/'handoff/code/data'/file).read_text())['features']
 data[ds]={f['properties']['Megalith']:np.array(f['geometry']['coordinates']) for f in features if f['geometry']}

def axial_delta(a,b):return (a-b+90)%180-90

def en_from_origin(coords,origin):
 coords=np.asarray(coords)
 az,_,d=geod.inv(np.full(coords.shape[:-1],origin[0]),np.full(coords.shape[:-1],origin[1]),coords[...,0],coords[...,1])
 return np.stack((d*np.sin(np.deg2rad(az)),d*np.cos(np.deg2rad(az))),axis=-1),az

def axes(xy,center=True):
 z=xy-xy.mean(axis=-2,keepdims=True) if center else xy
 xx=(z[...,0]**2).sum(axis=-1); yy=(z[...,1]**2).sum(axis=-1); xyv=(z[...,0]*z[...,1]).sum(axis=-1)
 # dominant eigenvector, angle east of north
 a=(90-np.rad2deg(0.5*np.arctan2(2*xyv,xx-yy)))%180
 lmax=((xx+yy)+np.sqrt((xx-yy)**2+4*xyv**2))/2
 lmin=np.maximum(0,((xx+yy)-np.sqrt((xx-yy)**2+4*xyv**2))/2)
 return a,np.sqrt(lmin/z.shape[-2]),lmax

def write(name,rows):
 with (OUT/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

results=[];bootstrap=[];quant=[]
for ds,positions in data.items():
 for spec,members in [('script_membership',script_members),('table_membership',source_members)]:
  for align,ids in members.items():
   kept=[i for i in ids if i in positions];coords=np.array([positions[i] for i in kept]);origin=positions['A'];n=len(coords)
   en,bearings=en_from_origin(coords,origin)
   a,rms,_=axes(en);anch,arms,_=axes(en,False);plus,_,_=axes(np.vstack(([0,0],en)))
   mean=np.rad2deg(np.angle(np.mean(np.exp(1j*np.deg2rad(bearings)))))%360
   x,y=utm.transform(coords[:,0],coords[:,1]);xy=np.stack((x,y),axis=-1);grid,_,_=axes(xy)
   loo=max(abs(axial_delta(axes(np.delete(en,i,axis=0))[0],a)) for i in range(n)) if n>2 else float('nan')
   span=max(np.linalg.norm(en[i]-en[j]) for i in range(n) for j in range(n))
   results.append(dict(dataset=ds,membership=spec,alignment=align,n=n,stones=';'.join(kept),axis_true_deg=float(a),axis_grid_deg=float(grid),radial_axis_true_deg=float(anch),mean_bearing_true_deg=float(mean),pca_including_origin_axis_deg=float(plus),perp_rms_m=float(rms),radial_perp_rms_m=float(arms),axial_loo_max_deg=float(loo),row_max_span_m=float(span),min_origin_dist_m=float(np.linalg.norm(en,axis=1).min())))
   if spec=='script_membership':
    # Exact empirical bootstrap distribution; exclude all-identical/zero-variance draws.
    inds=np.array(list(itertools.product(range(n),repeat=n)));samples=en[inds];ba,_,lm=axes(samples)
    valid=lm>1e-10; unique=np.array([len(set(i)) for i in inds]);concentration=abs(np.exp(2j*np.deg2rad(ba[valid])).mean());sd=np.rad2deg(np.sqrt(-2*np.log(concentration)))/2
    bootstrap.append(dict(dataset=ds,alignment=align,n=n,total_resamples=len(inds),zero_variance_count=int((~valid).sum()),zero_variance_pct=float(100*(~valid).mean()),only_two_distinct_pct=float(100*(unique==2).mean()),axial_std_valid_deg=float(sd),axial_loo_max_deg=float(loo)))
   else:
    # Illustrative independent rounding-cell perturbations, not survey confidence intervals.
    rng=np.random.default_rng(20261019)
    draws=10000
    pt=coords+rng.uniform(-.00005,.00005,(draws,n,2));po=origin+rng.uniform(-.00005,.00005,(draws,2))
    az,_,dist=geod.inv(np.repeat(po[:,0,None],n,1),np.repeat(po[:,1,None],n,1),pt[:,:,0],pt[:,:,1]);pe=np.stack((dist*np.sin(np.deg2rad(az)),dist*np.cos(np.deg2rad(az))),axis=-1)
    qa,_,_=axes(pe);qar,_,_=axes(pe,False);qm=np.rad2deg(np.angle(np.mean(np.exp(1j*np.deg2rad(az)),axis=1)))%360
    vals={}
    for name,v,base in [('free_axis',qa,a),('radial_axis',qar,anch),('mean_bearing',qm,mean)]:
     low,high=np.quantile(axial_delta(v,base),[.025,.975]);vals[name+'_delta_q025_deg']=float(low);vals[name+'_delta_q975_deg']=float(high)
    quant.append(dict(dataset=ds,alignment=align,n=n,draws=draws,**vals))
write('estimand_membership_diagnostics.csv',results);write('bootstrap_diagnostics.csv',bootstrap);write('rounding_sensitivity.csv',quant)
# Explicitly separate two source discrepancy scenarios from production data.
scenarios=[]
for label in ['as_inherited','BR2005_A7_as_printed']:
 p={k:v.copy() for k,v in data['gps2003'].items()}
 if label!='as_inherited':p['A-7']=np.array([30.7289,22.5131])
 en,b=en_from_origin([p[i] for i in source_members['A1']],p['A']);a,r,_=axes(en);ra,rr,_=axes(en,False)
 scenarios.append(dict(dataset='gps2003',scenario=label,alignment='A1',axis_true_deg=float(a),mean_bearing_true_deg=float(np.rad2deg(np.angle(np.exp(1j*np.deg2rad(b)).mean()))),radial_axis_true_deg=float(ra),rms_m=float(r)))
with (ROOT/'P1T1/nabta_alignment_table.csv').open() as f:table=list(csv.DictReader(x for x in f if x.strip()))
for label in ['BR2005_WM_as_inherited','WM2001_Table16_1_as_printed']:
 p={k:v.copy() for k,v in data['legacy'].items()}
 if label!='BR2005_WM_as_inherited':
  for row in table:
   key=row['Megalith'];key='A' if key=='Complex Structure A' else ('C-6' if key=='C-8' else key)
   p[key]=np.array([float(row['Longitude']),float(row['Latitude'])])
 en,b=en_from_origin([p[i] for i in source_members['C1']],p['A']);a,r,_=axes(en);ra,rr,_=axes(en,False)
 scenarios.append(dict(dataset='legacy',scenario=label,alignment='C1',axis_true_deg=float(a),mean_bearing_true_deg=float(np.rad2deg(np.angle(np.exp(1j*np.deg2rad(b)).mean()))),radial_axis_true_deg=float(ra),rms_m=float(r)))
write('source_discrepancy_scenarios.csv',scenarios)
# Cross-survey translations: observed differences include rounding and common offsets.
offsets=[]
for first,second in [('legacy','quickbird'),('quickbird','gps2003')]:
 common=sorted(set(data[first])&set(data[second]));p=np.array([data[first][i] for i in common]);q=np.array([data[second][i] for i in common]);az,_,d=geod.inv(p[:,0],p[:,1],q[:,0],q[:,1]);dx=d*np.sin(np.deg2rad(az));dy=d*np.cos(np.deg2rad(az));
 offsets.append(dict(first=first,second=second,n=len(common),mean_east_m=float(dx.mean()),mean_north_m=float(dy.mean()),sd_east_m=float(dx.std()),sd_north_m=float(dy.std())))
write('survey_offset_diagnostics.csv',offsets)
lon,lat=data['legacy']['A'];cell_e=geod.inv(lon,lat,lon+.0001,lat)[2];cell_n=geod.inv(lon,lat,lon,lat+.0001)[2]
metadata={'python':sys.version,'numpy':np.__version__,'coordinate_cell_east_m':cell_e,'coordinate_cell_north_m':cell_n,'rounding_half_diagonal_m':float(np.hypot(cell_e,cell_n)/2),'grid_convergence_at_A_deg':Proj('EPSG:32636').get_factors(lon,lat).meridian_convergence,'notes':['All numbers are audit diagnostics, not validated archaeological estimates.','Rounding draws assume independent uniform quantization cells, including an origin shared across row stones. This is not a survey-error model.','Exact empirical bootstrap excludes only zero-variance samples; low unique counts are tabulated, not validated as confidence intervals.','Table16.1 C-8 is provisionally keyed C-6 solely for a coordinate-version comparison; no identity adjudication.']}
(OUT/'diagnostics_metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
print(json.dumps(metadata,indent=2))
print('Wrote five diagnostic CSV files.')
