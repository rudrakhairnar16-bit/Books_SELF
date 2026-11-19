#!/usr/bin/env python3
"""Extract text of every non-book PDF in SEM*/ to study_engine/extracted/ (skips scans).
Run from repo root:  python3 study_engine/tools/extract.py"""
import pymupdf, os, glob, re
BOOKS={'SEM3/DS/BOOK.pdf','SEM3/Python_Programing/Reference Book.pdf','SEM3/DLD/Morris Mano Digital Design 3rd Edition Reference Book.pdf','SEM3/DLD/Digital-Electronics_AK reference book 1.pdf'}
out='study_engine/extracted'
for p in sorted(glob.glob('SEM*/**/*.pdf', recursive=True)):
    if p in BOOKS or re.search(r'book', os.path.basename(p), re.I): continue   # Rule R2: no books
    d=pymupdf.open(p)
    txt=[]
    for i,pg in enumerate(d):
        txt.append(f"\n===== PAGE {i+1} =====\n"+pg.get_text())
    t=''.join(txt)
    if len(t.replace('=','').strip())/d.page_count<150: continue
    rel=(p.split('/',1)[1] if p.startswith('SEM3/') else p)[:-4].replace('!','')
    fp=os.path.join(out,re.sub(r'[^\w/.-]+','_',rel)+'.txt')
    os.makedirs(os.path.dirname(fp),exist_ok=True)
    open(fp,'w').write(f"SOURCE: {p}\n"+t)
