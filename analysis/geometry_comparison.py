"""Conditional published-coordinate comparison; no probabilistic accuracy claims."""
from pathlib import Path
import csv, math, json, hashlib
from pyproj import Geod
BASE=Path(__file__).resolve().parent
INPUT=BASE/'source_reconciliation-2026-10-22/source_coordinate_observations.csv'
OUT=BASE/'analysis/geometry-comparison-2026-10-23'
def mean_angle(values):
    return math.degrees(math.atan2(sum(math.sin(math.radians(v)) for v in values),sum(math.cos(math.radians(v)) for v in values)))%360

def main():
    rows=list(csv.DictReader(INPUT.open()))
    models={'sphere':Geod(a=6371008.8,b=6371008.8),'WGS84_assumed':Geod(ellps='WGS84')}
    result=[]
    for source in sorted({r['source_id'] for r in rows}):
        data=[r for r in rows if r['source_id']==source]
        origin=next(r for r in data if r['alignment_as_table']=='Complex Structure A')
        lon,lat=float(origin['longitude_printed']),float(origin['latitude_printed'])
        for model,g in models.items():
            # Independent cardinal-direction check on the equator.
            assert abs(g.inv(0,0,1,0)[0]-90)<1e-10
            assert abs(g.inv(0,0,0,1)[0])<1e-10
            for group in ['A3','A2','A1','B2','B1','C1']:
                members=[r for r in data if r['alignment_as_table']==group]
                valid=[r for r in members if r['longitude_printed'] and r['latitude_printed']]
                values=[g.inv(lon,lat,float(r['longitude_printed']),float(r['latitude_printed']))[0]%360 for r in valid]
                result.append(dict(source=source,group=group,model=model,n_available=len(valid),n_listed=len(members),missing=';'.join(r['label'] for r in members if r not in valid),arithmetic_mean_deg=sum(values)/len(values),circular_mean_deg=mean_angle(values),status='conditional complete table' if len(valid)==len(members) else 'partial membership; not a full-row estimate'))
    expected={'A3':26.83,'A2':28.60,'A1':31.24,'B2':115.81,'B1':118.97,'C1':129.71}
    for r in result:
        if r['source']=='BR2005_repeated_WM2001' and r['model']=='sphere':
            assert abs(r['arithmetic_mean_deg']-expected[r['group']])<.005
    assert abs(mean_angle([359,1]))<1e-10 or abs(mean_angle([359,1])-360)<1e-10
    OUT.mkdir(parents=True,exist_ok=True)
    with (OUT/'comparisons.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=result[0]);w.writeheader();w.writerows(result)
    spans=[]
    for group in expected:
        r=[x for x in result if x['group']==group and x['model']=='WGS84_assumed' and x['n_available']==x['n_listed']]
        vals=[x['arithmetic_mean_deg'] for x in r]
        spans.append(dict(group=group,n_complete_source_versions=len(r),min_deg=min(vals),max_deg=max(vals),span_deg=max(vals)-min(vals)))
    (OUT/'validation.json').write_text(json.dumps(dict(input_sha256=hashlib.sha256(INPUT.read_bytes()).hexdigest(),checks=['cardinal bearings','circular wrap','six published rounded means'],rows=len(result),complete_source_spans=spans,caveat='Source scenarios are dependent, not replicate samples. C membership differs. No confidence intervals or survey accuracy inferred.'),indent=2)+'\n')
    print(json.dumps(spans,indent=2))
if __name__=='__main__':main()
