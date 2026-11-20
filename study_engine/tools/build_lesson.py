#!/usr/bin/env python3
"""
Turn a lesson markdown file into ONE self-contained HTML page (all images embedded as base64),
so a lesson with diagrams + handwritten pages can be opened anywhere (browser / phone, offline).

Usage (repo root):  python3 study_engine/tools/build_lesson.py study/DLD/lessons/L01/L01_lesson.md
Output: same folder, same name, .html
Needs: pip install markdown
"""
import sys, os, re, base64, mimetypes
import markdown

CSS = """
body{margin:0;background:#fbf8ee;font-family:system-ui,Segoe UI,Roboto,sans-serif;color:#1d1d1d;line-height:1.6}
main{max-width:900px;margin:0 auto;padding:18px 18px 60px}
h1{color:#16266e;border-bottom:4px solid #b2191e;padding-bottom:6px}
h2{color:#b2191e;margin-top:38px;border-left:6px solid #16266e;padding-left:10px}
h3{color:#16266e}
img{max-width:100%;display:block;margin:14px auto;border-radius:10px;box-shadow:0 2px 10px #0002;background:#fff}
table{border-collapse:collapse;margin:12px 0;width:100%;background:#fff}
th,td{border:1px solid #c9cfe6;padding:7px 10px;text-align:left}th{background:#dfe7fb;color:#16266e}
blockquote{margin:14px 0;padding:10px 16px;background:#fff6c9;border-left:6px solid #e0b100;border-radius:6px}
code{background:#eef1fb;padding:1px 5px;border-radius:4px}
details{background:#eef1fb;border-radius:8px;padding:10px 14px;margin:10px 0}summary{cursor:pointer;font-weight:600;color:#16266e}
.cap{text-align:center;color:#667;font-size:14px;margin-top:-6px}
"""


def inline_images(html, base):
    def rep(m):
        src = m.group(2)
        if src.startswith(("http", "data:")):
            return m.group(0)
        p = os.path.normpath(os.path.join(base, src))
        if not os.path.exists(p):
            print("  ! missing image", p)
            return m.group(0)
        mime = mimetypes.guess_type(p)[0] or "image/png"
        data = base64.b64encode(open(p, "rb").read()).decode()
        return f'{m.group(1)}data:{mime};base64,{data}{m.group(3)}'
    return re.sub(r'(<img[^>]*src=")([^"]+)(")', rep, html)


def main():
    src = sys.argv[1]
    base = os.path.dirname(os.path.abspath(src))
    text = open(src, encoding="utf-8").read()
    title = (re.search(r"^# (.+)$", text, re.M) or [None, "Lesson"])[1]
    body = markdown.markdown(text, extensions=["tables", "fenced_code", "md_in_html"])
    body = inline_images(body, base)
    out = os.path.splitext(src)[0] + ".html"
    open(out, "w", encoding="utf-8").write(
        f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" '
        f'content="width=device-width,initial-scale=1"><title>{title}</title><style>{CSS}</style></head>'
        f"<body><main>{body}</main></body></html>")
    print(f"wrote {out} ({os.path.getsize(out)//1024} KB)")


if __name__ == "__main__":
    main()
