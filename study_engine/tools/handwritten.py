#!/usr/bin/env python3
"""
Handwritten-notes renderer (Mentor tool).

Turns a simple marked-up text file into realistic "notebook page" PNG images
with handwriting fonts, ruled lines, a red margin, coloured ink, boxed
formulas and embedded diagrams.  Content is typed by the mentor (so it is
100 % accurate) – only the *look* is handwritten.

Usage:
    python3 study_engine/tools/handwritten.py notes.hw  out_dir/prefix

Markup (one instruction per line):
    # Heading              big red underlined heading
    ## Sub heading         blue bold underlined
    - bullet text          bullet point            (use "  - " for sub bullet)
    1. text                numbered point (any number)
    ! important text       red star line
    > formula / def        yellow-highlighted box
    TIP: text              green ink
    MEM: text              purple ink (mnemonic)
    ```                    start/stop code block (monospace)
    ![600](path.png)       embed image, width in px (max 1000)
    ---                    new page
    (blank line)           skip half a line
Inline:  **word**  -> red bold,   __word__ -> underlined blue bold
"""
import sys, os, re, random
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
W, H = 1240, 1754                 # A4 @150 dpi
LINE = 46                          # ruled line spacing
TOP = 150                          # first ruled line
MARGIN_X = 120                     # red margin line
LEFT = MARGIN_X + 22
RIGHT = W - 70
PAPER = (252, 249, 238)
RULE = (170, 200, 230)
MARGIN = (225, 120, 120)
INK = {"blue": (22, 38, 110), "red": (180, 25, 30), "green": (20, 110, 50),
       "purple": (100, 30, 140), "black": (30, 30, 30), "gray": (60, 60, 60)}

def _font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)

try:
    import matplotlib
    _DJ = os.path.join(os.path.dirname(matplotlib.__file__), "mpl-data", "fonts", "ttf")
    SYM = ImageFont.truetype(os.path.join(_DJ, "DejaVuSans.ttf"), 26)
    SYM_B = ImageFont.truetype(os.path.join(_DJ, "DejaVuSans-Bold.ttf"), 34)
    MONO = ImageFont.truetype(os.path.join(_DJ, "DejaVuSansMono.ttf"), 22)
except Exception:                   # pragma: no cover
    SYM = SYM_B = MONO = ImageFont.load_default()

F_BODY = _font("kalam-400.ttf", 31)
F_BOLD = _font("kalam-700.ttf", 31)
F_H1 = _font("kalam-700.ttf", 44)
F_H2 = _font("kalam-700.ttf", 36)

from fontTools.ttLib import TTFont
_CMAP = set(TTFont(os.path.join(FONTS, "kalam-400.ttf")).getBestCmap().keys())


def chunks(text, font, symfont):
    """split text into runs of (substring, font) using symbol fallback"""
    runs, cur, curf = [], "", None
    for ch in text:
        f = font if (ord(ch) in _CMAP or ch == " ") else symfont
        if f is not curf and cur:
            runs.append((cur, curf)); cur = ""
        cur += ch; curf = f
    if cur:
        runs.append((cur, curf))
    return runs


def text_w(text, font, symfont):
    return sum(f.getlength(s) for s, f in chunks(text, font, symfont))


class Page:
    def __init__(self, title):
        self.img = Image.new("RGB", (W, H), PAPER)
        self.d = ImageDraw.Draw(self.img)
        rnd = random.Random(7)
        for y in range(TOP, H - 40, LINE):
            self.d.line([(0, y), (W, y)], fill=RULE, width=1)
        self.d.line([(MARGIN_X, 0), (MARGIN_X, H)], fill=MARGIN, width=2)
        self.d.line([(MARGIN_X + 5, 0), (MARGIN_X + 5, H)], fill=MARGIN, width=1)
        # punched holes
        for y in (300, H // 2, H - 300):
            self.d.ellipse([28, y - 16, 60, y + 16], fill=(230, 226, 214))
        if title:
            self.d.text((LEFT, 60), title, font=_font("caveat-700.ttf", 34), fill=INK["gray"])
        self.y = TOP          # baseline we write on next
        self.rnd = rnd

    def room(self, n_lines=1):
        return self.y + LINE * n_lines < H - 60


class Renderer:
    def __init__(self, title, out_prefix):
        self.title, self.out = title, out_prefix
        self.pages = []
        self.new_page()
        self.rnd = random.Random(42)

    def new_page(self):
        self.p = Page(f"{self.title}   — p{len(self.pages)+1}")
        self.pages.append(self.p)

    def ensure(self, n=1):
        if not self.p.room(n):
            self.new_page()

    # -- low level draw of a run list on baseline
    def draw_runs(self, x, words, color_default):
        d = self.p.d
        base = self.p.y - 8
        for word, style in words:
            font = F_BOLD if style in ("b", "u") else F_BODY
            col = INK["red"] if style == "b" else INK["blue"] if style == "u" else color_default
            jitter = self.rnd.uniform(-1.5, 1.5)
            x0 = x
            for s, f in chunks(word, font, SYM):
                asc = f.getmetrics()[0]
                d.text((x, base - asc + jitter), s, font=f, fill=col)
                x += f.getlength(s)
            if style == "u":
                d.line([(x0, base + 6), (x, base + 5)], fill=col, width=2)
            x += F_BODY.getlength(" ")
        return x

    def parse_inline(self, text):
        out = []
        for part in re.split(r"(\*\*.+?\*\*|__.+?__)", text):
            if not part:
                continue
            if part.startswith("**"):
                st, part = "b", part[2:-2]
            elif part.startswith("__"):
                st, part = "u", part[2:-2]
            else:
                st = "n"
            for w in part.split(" "):
                if w:
                    out.append((w, st))
        return out

    def wrap(self, words, width):
        lines, cur, cw = [], [], 0
        sp = F_BODY.getlength(" ")
        for w, st in words:
            ww = text_w(w, F_BOLD if st != "n" else F_BODY, SYM)
            if cur and cw + ww > width:
                lines.append(cur); cur, cw = [], 0
            cur.append((w, st)); cw += ww + sp
        if cur:
            lines.append(cur)
        return lines or [[]]

    def para(self, text, indent=0, color="blue", prefix=None):
        words = self.parse_inline(text)
        x0 = LEFT + indent
        lines = self.wrap(words, RIGHT - x0 - 40)
        for i, ln in enumerate(lines):
            self.ensure()
            self.p.y += LINE
            if i == 0 and prefix:
                pc = INK["red"] if prefix == "★" else INK[color]
                f = SYM if prefix in ("•", "◦", "★") else F_BOLD
                self.p.d.text((x0 - 30, self.p.y - 8 - f.getmetrics()[0] + (2 if f is SYM else 0)), prefix, font=f, fill=pc)
            self.draw_runs(x0, ln, INK[color])

    def heading(self, text, level):
        self.ensure(2)
        self.p.y += LINE if self.p.y > TOP else 0
        self.p.y += LINE
        f, col = (F_H1, INK["red"]) if level == 1 else (F_H2, INK["blue"])
        sf = SYM_B
        x = LEFT
        for s, ff in chunks(text, f, sf):
            self.p.d.text((x, self.p.y - 6 - ff.getmetrics()[0]), s, font=ff, fill=col)
            x += ff.getlength(s)
        # wavy underline
        pts = [(LEFT + i, self.p.y + 4 + (2 if (i // 12) % 2 else 0)) for i in range(0, int(x - LEFT), 6)]
        if len(pts) > 1:
            self.p.d.line(pts, fill=col, width=3 if level == 1 else 2)

    def box(self, text):
        words = self.parse_inline(text)
        lines = self.wrap(words, RIGHT - LEFT - 80)
        self.ensure(len(lines) + 1)
        top = self.p.y + 8
        bottom = top + 18 + len(lines) * LINE
        ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        od = ImageDraw.Draw(ov)
        od.rectangle([LEFT + 6, top, RIGHT - 20, bottom], fill=(255, 240, 80, 110))
        self.p.img.paste(Image.alpha_composite(self.p.img.convert("RGBA"), ov).convert("RGB"))
        self.p.d = ImageDraw.Draw(self.p.img)
        for o in (0, 3):            # sketchy double border
            self.p.d.rectangle([LEFT + 6 - o, top - o, RIGHT - 20 + o, bottom + o], outline=INK["black"], width=1)
        for i, ln in enumerate(lines):
            self.p.y = top + 44 + i * LINE      # draw_runs writes at y-8
            self.draw_runs(LEFT + 30, ln, INK["black"])
        self.p.y = TOP + ((bottom - TOP) // LINE + 1) * LINE

    def code(self, lines):
        h = len(lines) * 30 + 20
        if self.p.y + h + LINE > H - 60:
            self.new_page()
        top = self.p.y + 18
        self.p.d.rectangle([LEFT + 6, top, RIGHT - 20, top + h], fill=(240, 240, 235), outline=INK["gray"])
        y = top + 10
        for ln in lines:
            self.p.d.text((LEFT + 20, y), ln, font=MONO, fill=INK["black"])
            y += 30
        # snap to next rule
        self.p.y = TOP + ((top + h - TOP) // LINE + 1) * LINE - LINE + 10

    def image(self, path, width):
        im = Image.open(path).convert("RGB")
        width = min(width, RIGHT - LEFT - 20)
        im = im.resize((width, int(im.height * width / im.width)))
        if self.p.y + im.height + 40 > H - 60:
            self.new_page()
        top = self.p.y + 20
        self.p.img.paste(im, (LEFT + (RIGHT - LEFT - width) // 2, top))
        self.p.d.rectangle([LEFT + (RIGHT - LEFT - width) // 2 - 2, top - 2,
                            LEFT + (RIGHT - LEFT + width) // 2 + 2, top + im.height + 2], outline=INK["gray"])
        self.p.y = TOP + ((top + im.height - TOP) // LINE + 1) * LINE

    def render(self, src_lines, base_dir):
        in_code, code_buf = False, []
        for raw in src_lines:
            line = raw.rstrip("\n")
            if line.strip() == "```":
                if in_code:
                    self.code(code_buf); code_buf = []
                in_code = not in_code
                continue
            if in_code:
                code_buf.append(line); continue
            s = line.strip()
            if not s:
                self.p.y += LINE // 2
                self.p.y = TOP + ((self.p.y - TOP + LINE - 1) // LINE) * LINE if self.p.y > TOP else self.p.y
                continue
            if s == "---":
                self.new_page(); continue
            m = re.match(r"!\[(\d+)\]\((.+)\)", s)
            if m:
                self.image(os.path.join(base_dir, m.group(2)), int(m.group(1))); continue
            if s.startswith("## "):
                self.heading(s[3:], 2)
            elif s.startswith("# "):
                self.heading(s[2:], 1)
            elif s.startswith("> "):
                self.box(s[2:])
            elif s.startswith("! "):
                self.para(s[2:], indent=30, color="red", prefix="★")
            elif s.startswith("TIP:"):
                self.para("Tip: " + s[4:].strip(), indent=0, color="green")
            elif s.startswith("MEM:"):
                self.para("Trick: " + s[4:].strip(), indent=0, color="purple")
            elif re.match(r"\d+[.)] ", s):
                n, rest = s.split(" ", 1)
                self.para(rest, indent=40, prefix=n)
            elif line.startswith("  - ") or line.startswith("    - "):
                self.para(s[2:], indent=80, prefix="◦")
            elif s.startswith("- "):
                self.para(s[2:], indent=40, prefix="•")
            else:
                self.para(s)
        paths = []
        os.makedirs(os.path.dirname(self.out) or ".", exist_ok=True)
        for i, pg in enumerate(self.pages, 1):
            fp = f"{self.out}_p{i}.png"
            pg.img.save(fp, optimize=True)
            paths.append(fp)
        return paths


def main():
    src, out = sys.argv[1], sys.argv[2]
    lines = open(src, encoding="utf-8").readlines()
    title = os.path.splitext(os.path.basename(src))[0].replace("_", " ")
    if lines and lines[0].startswith("TITLE:"):
        title = lines.pop(0)[6:].strip()
    for p in Renderer(title, out).render(lines, os.path.dirname(os.path.abspath(src))):
        print(p)


if __name__ == "__main__":
    main()
