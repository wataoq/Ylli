import subprocess,os,re,sys,pymupdf as fitz
css=open('fonts/archivo.css').read()
names=sys.argv[1:]
os.makedirs('out/story2',exist_ok=True)
for i,n in enumerate(names):
    s=open(f'canvas/project/{n}.dc.html').read().replace('<script src="./support.js"></script>','')
    s=re.sub(r'<link href="https://fonts[^>]*>','<style>'+css+'</style>',s)
    open(f'p3/shot/{n}.html','w').write(s)
    subprocess.run(['/opt/pw-browsers/chromium','--headless','--no-sandbox','--disable-gpu','--allow-file-access-from-files','--hide-scrollbars','--force-device-scale-factor=1','--window-size=1080,2120','--virtual-time-budget=3000',f'--screenshot={os.path.abspath("out/tmp.png")}','file://'+os.path.abspath(f'p3/shot/{n}.html')],capture_output=True,timeout=120)
    pm=fitz.Pixmap('out/tmp.png'); d=fitz.open(); pg=d.new_page(width=pm.width,height=pm.height); pg.insert_image(pg.rect,pixmap=pm)
    pg.get_pixmap(clip=fitz.Rect(0,0,1080,1920),dpi=72).save(f'out/story2/{n}.png')
os.remove('out/tmp.png')
out=fitz.open(); pg=out.new_page(width=len(names)*540,height=960)
for i,n in enumerate(names): pg.insert_image(fitz.Rect(i*540,0,i*540+540,960),filename=f'out/story2/{n}.png')
pg.get_pixmap(dpi=40).save('p3/shot/story2.png')
