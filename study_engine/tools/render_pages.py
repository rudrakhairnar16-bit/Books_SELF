#!/usr/bin/env python3
"""Render PDF pages to PNG so scanned / handwritten material can be read visually.

Usage (from repo root):
    python3 study_engine/tools/render_pages.py "SEM3/MATHS3/Unit-4_Basic Statistics.pdf"          # all pages
    python3 study_engine/tools/render_pages.py "SEM3/DLD/Unit 2_Handwritten.pdf" 3-6 --zoom 1.6     # page range
Output: study_engine/_scan_pages/<file-stem>/p<N>.png   (git-ignored, re-creatable)
"""
import sys, os, re, argparse
import pymupdf

ap = argparse.ArgumentParser()
ap.add_argument("pdf"); ap.add_argument("pages", nargs="?", default="all")
ap.add_argument("--zoom", type=float, default=1.4)
a = ap.parse_args()
doc = pymupdf.open(a.pdf)
if a.pages == "all":
    pages = range(1, doc.page_count + 1)
else:
    s, _, e = a.pages.partition("-"); pages = range(int(s), int(e or s) + 1)
stem = re.sub(r"[^\w.-]+", "_", os.path.splitext(os.path.basename(a.pdf))[0])
out = os.path.join("study_engine", "_scan_pages", stem); os.makedirs(out, exist_ok=True)
for n in pages:
    pix = doc[n - 1].get_pixmap(matrix=pymupdf.Matrix(a.zoom, a.zoom))
    fp = os.path.join(out, f"p{n}.png"); pix.save(fp); print(fp)
