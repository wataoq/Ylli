import re,subprocess,sys,os,hashlib
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
url=sys.argv[1]; out=sys.argv[2]
css=subprocess.run(['curl','-sS','-m','60','-A',UA,url],capture_output=True,text=True).stdout
def dl(m):
    u=m.group(1); fn='fonts/'+hashlib.md5(u.encode()).hexdigest()[:12]+'.woff2'
    if not os.path.exists(fn): subprocess.run(['curl','-sS','-m','60','-o',fn,u])
    return f'url(file://{os.path.abspath(fn)})'
css=re.sub(r'url\((https://[^)]+)\)',dl,css)
open(out,'w').write(css); print(len(css), css.count('@font-face'))
