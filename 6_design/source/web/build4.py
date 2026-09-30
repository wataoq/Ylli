import re
t=open('web/template4.html').read()
seq='(function(){\n'+open('web/seq.js').read()+'\n})();'
t=t.replace('__SEQ__',seq).replace('__PHYS__',open('web/phys.js').read()).replace('__PLATES__',open('web/plates.js').read()).replace('__DATA__',open('web/data.json').read())
open('web/ylli_site.html','w').write(t)
css=open('fonts/notojp.css').read()
body=re.sub(r'<link rel="stylesheet" href="https://fonts[^>]*>','<style>'+css+'</style>',t)
head='<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
open('web/test.html','w').write(head+'</head><body>'+body+'</body></html>')
open('web/test2.html','w').write(head+'<style>.seq{display:none}</style></head><body>'+body+'</body></html>')
print(len(t)//1024,'KB')
