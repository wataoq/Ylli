import re,sys,subprocess,os
css=open('fonts/archivo.css').read()
for arg in sys.argv[1:]:
    n,w,h=arg.split(':')
    s=open(f'canvas/project/{n}.dc.html').read()
    s=s.replace('<script src="./support.js"></script>','')
    s=re.sub(r'<link href="https://fonts[^>]*>','<style>'+css+'</style>',s)
    open(f'p3/shot/{n}.html','w').write(s)
    subprocess.run(['/opt/pw-browsers/chromium','--headless','--no-sandbox','--disable-gpu','--allow-file-access-from-files','--hide-scrollbars',f'--window-size={w},{int(h)+200}','--virtual-time-budget=3000',f'--screenshot={os.path.abspath("p3/shot/"+n+".png")}','file://'+os.path.abspath(f'p3/shot/{n}.html')],capture_output=True,timeout=90)
    import pymupdf as fitz
    pm=fitz.Pixmap(f'p3/shot/{n}.png'); d=fitz.open(); pg=d.new_page(width=pm.width,height=pm.height); pg.insert_image(pg.rect,pixmap=pm)
    pg.get_pixmap(clip=fitz.Rect(0,0,int(w),int(h)),dpi=72).save(f'p3/shot/{n}.png'); print(n,'ok')
