"""Extract drawing-space observations, never survey coordinates or monument IDs."""
from pathlib import Path
import bisect,csv,hashlib,json
import fitz
BASE=Path(__file__).resolve().parent
PDF=BASE/'source_library-2026-10-22/papers/user sourced/The Megaliths of Nabta Playa_I.pdf'
OUT=BASE/'source_reconciliation-2026-10-22/monograph2025/map_audit'
OUT.mkdir(exist_ok=True)
doc=fitz.open(PDF); p=doc[29]; drawings=p.get_drawings()
def cluster(values):
 groups=[]
 for x in sorted(values):
  if not groups or x-groups[-1][-1]>.01:groups.append([x])
  else:groups[-1].append(x)
 return [sum(g)/len(g) for g in groups]
grid=[d for d in drawings if d['color'] and abs(d['color'][0]-.736919224)<1e-6]
xs=cluster([x for d in grid for x in (d['rect'].x0,d['rect'].x1)])
ys=cluster([y for d in grid for y in (d['rect'].y0,d['rect'].y1)])
assert len(xs)==25 and len(ys)==35
cells={'m18':'B2',**{f'n{n}':'B2' for n in range(19,23)},**{f'o{n}':'B1' for n in range(23,28)}}
records=[]
for k,d in enumerate(drawings):
 fill=d['fill']
 if not fill or abs(fill[0]-.930418849)>1e-6:continue
 r=d['rect'];x=(r.x0+r.x1)/2;y=(r.y0+r.y1)/2
 if not (xs[0]<x<xs[-1] and ys[0]<y<ys[-1]):continue
 row=chr(97+bisect.bisect_right(xs,x)-1); col=35-bisect.bisect_right(ys,y);cell=f'{row}{col}'
 if cell not in cells:continue
 records.append(dict(drawing_index=k,sector='C',cell=cell,chapter7_group=cells[cell],x_pdf_pt=x,y_pdf_pt=y,x0=r.x0,y0=r.y0,x1=r.x1,y1=r.y1,point_definition='bounding-box centre of red filled drawing path; not a surveyed stone point',printed_page=28,pdf_page=30))
with (OUT/'sector_C_candidate_paths.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(records[0]));w.writeheader();w.writerows(records)
# Read-only rendering with overlays in an in-memory document; source PDF unchanged.
for cell in cells:
 row=ord(cell[0])-97;col=int(cell[1:]);j=34-col
 p.draw_rect(fitz.Rect(xs[row],ys[j],xs[row+1],ys[j+1]),color=(0,0,.8),width=.45)
 p.insert_text((xs[row]+.5,ys[j]+4),cell,fontsize=3,color=(0,0,.8))
for r in records:p.draw_circle((r['x_pdf_pt'],r['y_pdf_pt']),1.1,color=(0,0,.8),width=.3)
p.get_pixmap(matrix=fitz.Matrix(3,3)).save(OUT/'sector_C_review.png')
counts={cell:sum(r['cell']==cell for r in records) for cell in cells}
meta=dict(pdf_sha256=hashlib.sha256(PDF.read_bytes()).hexdigest(),printed_page=28,pdf_page=30,grid_x_pdf_pt=xs,grid_y_pdf_pt=ys,candidate_path_count=len(records),counts_by_cell=counts,selection='Red filled paths whose bounding-box centres fall in chapter 7 B1/B2 cells. Paths are not necessarily distinct stones.',orientation='Unregistered page coordinates: x increases a to x, y increases 34 to 1. True-north and survey registration unresolved.',excluded_uses=['ancient placement','survey accuracy estimate','automatic old-table stone identity','true azimuth'])
(OUT/'validation.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps({'candidate_paths':len(records),'counts':counts},indent=2))
