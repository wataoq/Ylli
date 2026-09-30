import sys; sys.path.insert(0,'.')
import json
exec(open('bx/partA.py').read()); exec(open('bx/partB.py').read()); exec(open('bx/partC.py').read())
from bx.common import BOARDS as BB
cj=json.load(open('canvas/project/canvas.json'))
for k in [k for k in cj['boards'] if k.startswith('P') and k[1:3].isdigit()]: del cj['boards'][k]
cj['order']=[o for o in cj['order'] if not (o.startswith('P') and o[1:3].isdigit())]
cj['notes'].pop('q1',None)
cj['pages']=[p for p in cj['pages'] if p['id']!='v6']
for p in cj['pages']:
    if p['id']=='v5': p['name']='v5 HODOKE v0.2 ＋ 改良検討（P0〜P4）'
rows={'A':0,'B':0,'C':0}; ystart={'A':0,'B':2700,'C':7900}
cnt={'A':0,'B':0,'C':0}
order=[]
for fn,title,part in BB:
    i=cnt[part]; cnt[part]+=1
    cj['boards'][fn]={'h':1080,'page':'v7','title':title,'w':1920,'x':(i%6)*2000,'y':ystart[part]+(i//6)*1200}
    order.append(fn)
cj['order']=order+[o for o in cj['order'] if o not in order]
cj['notes']['g1']={'kind':'title1','maxW':11920,'page':'v7','text':'Part A — Brand Strategy（Cover / Contents 含む）','w':240,'x':0,'y':-300}
cj['notes']['g2']={'kind':'title1','maxW':11920,'page':'v7','text':'Part B — BX Design Elements（ロゴ：45°の平筆）','w':240,'x':0,'y':2400}
cj['notes']['g3']={'kind':'title1','maxW':11920,'page':'v7','text':'Part C — BX Design Application（15 接点）','w':240,'x':0,'y':7600}
if not any(p['id']=='v7' for p in cj['pages']): cj['pages'].insert(0,{'id':'v7','name':'v7 BX Guidelines 1.0 — 平筆のロゴ'})
cj['launch']={'page':'v7','view':'canvas'}
json.dump(cj,open('canvas/project/canvas.json','w'),ensure_ascii=False,indent=1)
print(len(BB), cnt)
print(json.dumps([fn for fn,_,_ in BB]))
