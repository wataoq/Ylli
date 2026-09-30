import subprocess,os,re,sys,json,pymupdf as fitz
css=open('fonts/archivo.css').read()+open('fonts/notojp.css').read()
def render(n,w,h,scale=1,out=None):
    s=open(f'canvas/project/{n}.dc.html').read().replace('<script src="./support.js"></script>','')
    s=re.sub(r'<link href="https://fonts[^>]*>','<style>'+css+'</style>',s)
    os.makedirs('p3/shot',exist_ok=True); open(f'p3/shot/{n}.html','w').write(s)
    tmp=os.path.abspath(f'p3/shot/_{n}.png')
    subprocess.run(['/opt/pw-browsers/chromium','--headless','--no-sandbox','--disable-gpu','--allow-file-access-from-files','--hide-scrollbars',f'--force-device-scale-factor={scale}',f'--window-size={w},{h+200}','--virtual-time-budget=6000',f'--screenshot={tmp}','file://'+os.path.abspath(f'p3/shot/{n}.html')],capture_output=True,timeout=180)
    pm=fitz.Pixmap(tmp); d=fitz.open(); pg=d.new_page(width=pm.width,height=pm.height); pg.insert_image(pg.rect,pixmap=pm)
    pix=pg.get_pixmap(clip=fitz.Rect(0,0,w*scale,h*scale),dpi=72); os.remove(tmp)
    out=out or f'p3/shot/{n}.png'; pix.save(out); return out
def pdf(items,path,quality=90):
    doc=fitz.open()
    for png,w,h in items:
        pg=doc.new_page(width=w,height=h)
        pm=fitz.Pixmap(png)
        pg.insert_image(pg.rect,stream=pm.tobytes('jpeg',jpg_quality=quality))
    doc.save(path,deflate=True,garbage=3); return path
