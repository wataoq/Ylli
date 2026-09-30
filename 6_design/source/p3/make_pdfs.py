import json,sys,os
sys.path.insert(0,'p3')
from printpdf import pdf1, merge
cj=json.load(open('canvas/project/canvas.json'))
bx=[o for o in cj['order'] if cj['boards'].get(o,{}).get('page')=='v7']
bx=[b.replace('.dc.html','') for b in bx]
os.makedirs('out/pdf',exist_ok=True)
parts=[pdf1(b,1920,1080) for b in bx]
merge(parts,'out/pdf/260930_ylli_bxguidelines_F.pdf'); print('guidelines',len(parts))
posters=['PZ01Shift','PZ02Apart','PZ03Close','PZ04Form','PZ05Unresolved','PZ01cShift0','PZ01bShift']
merge([pdf1(p,1000,1414) for p in posters],'out/pdf/260930_ylli_poster_launch_F.pdf'); print('posters')
stories=['ST_sig_k','ST_sig_w','ST_shift0','ST_shift']+[f'XSTORY0{i}' for i in range(1,7)]
merge([pdf1(p,1080,1920) for p in stories],'out/pdf/260930_ylli_sns_story_F.pdf'); print('stories')
