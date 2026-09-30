import subprocess,os,re,sys,pymupdf as fitz
css=open('fonts/archivo.css').read()+open('fonts/notojp.css').read()
def pdf1(n,w,h):
    s=open(f'canvas/project/{n}.dc.html').read().replace('<script src="./support.js"></script>','')
    s=re.sub(r'<link href="https://fonts[^>]*>','<style>'+css+f'@page{{size:{w}px {h}px;margin:0}}html,body{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}</style>',s)
    os.makedirs('p3/pdf',exist_ok=True); open(f'p3/pdf/{n}.html','w').write(s)
    out=os.path.abspath(f'p3/pdf/{n}.pdf')
    subprocess.run(['/opt/pw-browsers/chromium','--headless','--no-sandbox','--disable-gpu','--allow-file-access-from-files','--virtual-time-budget=8000','--no-pdf-header-footer',f'--print-to-pdf={out}','file://'+os.path.abspath(f'p3/pdf/{n}.html')],capture_output=True,timeout=180)
    return out
def merge(parts,path):
    doc=fitz.open()
    for p in parts:
        d=fitz.open(p); doc.insert_pdf(d,from_page=0,to_page=0)
    doc.save(path,garbage=3,deflate=True); return path
if __name__=='__main__':
    n,w,h=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]); p=pdf1(n,w,h); d=fitz.open(p); print(d.page_count,d[0].rect,os.path.getsize(p))
    d[0].get_pixmap(dpi=40).save(f'p3/pdf/{n}.png')
