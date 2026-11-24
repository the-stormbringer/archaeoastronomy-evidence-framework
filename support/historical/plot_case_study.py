from pathlib import Path
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;O=B/'analysis/case-study-2026-10-24';F=O/'figures';F.mkdir(exist_ok=True)
r=list(csv.DictReader((O/'continuous_spherical_contrasts.csv').open()));sources=[('WM2001_original','2001 table'),('BR2005_QB2002','2002 satellite'),('BR2005_GPS2003','2003 GPS')]
fig,axes=plt.subplots(1,2,figsize=(10,4.6),sharey=True)
for ax,contrast,title in zip(axes,['A2 minus A3','A1 minus A2'],['A2 − A3','A1 − A2']):
 for y,(s,label) in enumerate(sources):
  x=next(x for x in r if x['source']==s and x['contrast']==contrast and x['origin_axis_subdivisions']=='16');lo=float(x['lower_enclosure_deg']);hi=float(x['upper_enclosure_deg']);ax.plot([lo,hi],[y,y],lw=5,color='#216e83',solid_capstyle='butt');ax.text(lo,y+.15,f'{lo:.3f}°',fontsize=9,ha='left')
 ax.axvline(0,color='#555555',ls='--',lw=1);ax.set_title(title);ax.set_xlabel('Difference between radial means (degrees)');ax.set_yticks(range(3),[x[1] for x in sources]);ax.set_xlim(-.2,4.3);ax.set_ylim(2.5,-.5);ax.grid(axis='x',alpha=.2)
fig.suptitle('Northern ordering under continuous coordinate-rounding scenarios',fontsize=13)
fig.text(.05,.035,'Numerical enclosures, not confidence intervals. Spherical model; published table memberships; shared origin.\nRepeated 2001 values omitted from display. Bounds do not reconstruct ancient stone positions.',fontsize=9)
fig.subplots_adjust(left=.14,right=.98,bottom=.24,top=.80,wspace=.13)
for ext in ['png','svg']:fig.savefig(F/f'continuous_ordering.{ext}',dpi=180)
plt.close(fig)
r=list(csv.DictReader((B/'source_reconciliation-2026-10-22/published_claims.csv').open()));r=[x for x in r if x['source']=='Malville et al. 2007' and x['date_range_as_printed']]
fig,ax=plt.subplots(figsize=(10,5.7));ax.axvspan(4600,4200,color='#c8dce2',label='Proposed context: 4600–4200 BC');ax.axvspan(4200,4100,facecolor='#edf3f5',hatch='///',edgecolor='#93aab2',label='Alternative younger endpoint: 4100 BC')
for y,x in enumerate(r):
 old,young=map(int,x['date_range_as_printed'].split('–'));ax.plot([old,young],[y,y],color='#293b59',lw=5,solid_capstyle='butt')
ax.set_yticks(range(len(r)),[x['alignment']+' / '+x['target_as_printed'] for x in r]);ax.set_xlim(4750,3300);ax.set_ylim(len(r)-.5,-.6);ax.set_xlabel('Published target-fit date (BC; source convention retained)');ax.set_title('Published target dates against two contextual quarry windows');ax.grid(axis='x',alpha=.2);ax.legend(loc='upper center',bbox_to_anchor=(.5,-.18),frameon=False,fontsize=9,ncol=1)
fig.text(.02,.02,'Context windows are hypotheses, not direct row-construction dates. Bars reproduce source claims; no new star fits or probabilities.',fontsize=9)
fig.subplots_adjust(left=.22,right=.98,bottom=.31,top=.88)
for ext in ['png','svg']:fig.savefig(F/f'chronology_context.{ext}',dpi=180)
plt.close(fig)
print('Generated two figures in PNG and SVG.')
