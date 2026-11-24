from pathlib import Path
import os,csv
os.environ.setdefault('MPLCONFIGDIR','/tmp/nabta-mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;O=B/'analysis/geometry-comparison-2026-10-23'
r=list(csv.DictReader((O/'rounding_scenarios.csv').open()))
names={'WM2001_original':'2001 original table','BR2005_repeated_WM2001':'2005 repeated 2001','BR2005_QB2002':'2002 satellite','BR2005_GPS2003':'2003 GPS'}
fig,axes=plt.subplots(3,2,figsize=(12,10),layout='constrained')
for ax,group in zip(axes.flat,['A3','A2','A1','B2','B1','C1']):
 for i,(src,name) in enumerate(names.items()):
  x=next(x for x in r if x['source']==src and x['group']==group);partial=x['complete']!='True';color='#bd6d13' if partial else '#245b82'
  ax.plot([float(x['sampled_min_deg']),float(x['sampled_max_deg'])],[i,i],color=color,linewidth=2,linestyle='--' if partial else '-')
  ax.scatter(float(x['nominal_deg']),i,color=color,s=30,marker='x' if partial else 'o')
 ax.set_yticks(range(4),names.values());ax.invert_yaxis();ax.set_title(group);ax.set_xlabel('Azimuth east of north (degrees)');ax.grid(axis='x',alpha=.2);ax.set_ylim(3.5,-.5)
fig.suptitle('Published-coordinate reconstruction: conditional rounding scenarios',fontsize=15)
fig.supxlabel('Segments are sampled envelopes under nearest rounding, NOT confidence intervals.\nAssumed WGS84; shared origin; table membership. Orange dashed = missing GPS members.\nRepeated versions are dependent evidence; C identity and ancient positions remain unresolved.',fontsize=10)
fig.savefig(O/'rounding_scenarios.png',dpi=160);fig.savefig(O/'rounding_scenarios.svg');print(O/'rounding_scenarios.png')
