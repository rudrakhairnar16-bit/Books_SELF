#!/usr/bin/env python3
"""Lesson 1 visuals: analog vs digital, switch analogy for AND/OR."""
import os, tempfile, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import schemdraw, schemdraw.elements as elm
from PIL import Image
OUT = os.path.dirname(os.path.abspath(__file__)); TMP = tempfile.mkdtemp()

# 1. analog vs digital
fig, ax = plt.subplots(1, 2, figsize=(12, 3.6))
t = np.linspace(0, 4 * np.pi, 600)
ax[0].plot(t, 2.5 + 2 * np.sin(t) + 0.4 * np.sin(3.3 * t), color="#16266e", lw=2.5)
ax[0].set_title("ANALOG – any value, continuous", fontsize=14, color="#16266e", fontweight="bold")
bits = [0, 1, 1, 0, 1, 0, 0, 1]
x = np.repeat(np.arange(len(bits) + 1), 2)[1:-1]; y = np.repeat(bits, 2) * 5
ax[1].plot(x, y, color="#b2191e", lw=2.5)
for i, b in enumerate(bits):
    ax[1].text(i + 0.5, b * 5 + 0.35, str(b), ha="center", fontsize=14, fontweight="bold")
ax[1].set_title("DIGITAL – only 0 (0 V) or 1 (5 V)", fontsize=14, color="#b2191e", fontweight="bold")
for a in ax:
    a.set_ylim(-0.5, 6.2); a.set_xticks([]); a.set_ylabel("Voltage"); a.set_xlabel("time →")
    a.spines[["top", "right"]].set_visible(False)
ax[1].set_yticks([0, 5]); ax[1].set_yticklabels(["0 V (LOW)", "5 V (HIGH)"])
ax[0].set_yticks([])
plt.tight_layout(); plt.savefig(os.path.join(OUT, "analog_vs_digital.png"), dpi=120); plt.close()

# 2. switch analogy
def circuit(series, fp):
    with schemdraw.Drawing(show=False) as d:
        d.config(fontsize=15, lw=2)
        bat = d.add(elm.BatteryCell().up().label("5 V", "left"))
        d.add(elm.Line().right(0.8))
        if series:
            d.add(elm.Switch().right().label("A", "top"))
            d.add(elm.Switch().right().label("B", "top"))
        else:
            d.push(); d.add(elm.Line().up(1.5)); d.add(elm.Switch().right().label("A", "top")); d.add(elm.Line().down(1.5)); d.pop()
            d.add(elm.Switch().right().label("B", "bottom"))
        d.add(elm.Line().right(1.2))
        d.add(elm.Lamp().down().label("Y\n(bulb)", "right", ofst=0.3))
        d.add(elm.Line().left().tox(bat.start))
        d.save(fp, dpi=130)
    return Image.open(fp)
imgs = {ser: circuit(ser, os.path.join(TMP, f"c{ser}.png")) for ser in (True, False)}
fig, ax = plt.subplots(1, 2, figsize=(12, 4.4))
for a, ser, title, note in [(ax[0], True, "AND = switches in SERIES", "Bulb glows only if A AND B are both closed (1·1 = 1)"),
                            (ax[1], False, "OR = switches in PARALLEL", "Bulb glows if A OR B (or both) is closed")]:
    a.imshow(imgs[ser]); a.set_axis_off()
    a.set_title(title, fontsize=15, fontweight="bold", color="#16266e")
    a.text(0.5, -0.08, note, ha="center", transform=a.transAxes, fontsize=12, color="#b2191e")
fig.tight_layout(); fig.savefig(os.path.join(OUT, "switch_analogy.png"), dpi=110); plt.close()
print("ok")

# 3. master truth table in handwriting font
from matplotlib import font_manager as fm
FD = os.path.join(OUT, "..", "..", "..", "..", "study_engine", "tools", "fonts")
fp = fm.FontProperties(fname=os.path.join(FD, "kalam-400.ttf"), size=21)
fb = fm.FontProperties(fname=os.path.join(FD, "kalam-700.ttf"), size=21)
cols = ["A", "B", "AND", "OR", "NAND", "NOR", "XOR", "XNOR"]
fns = [lambda a, b: a & b, lambda a, b: a | b, lambda a, b: 1 - (a & b), lambda a, b: 1 - (a | b),
       lambda a, b: a ^ b, lambda a, b: 1 - (a ^ b)]
rows = [[a, b] + [f(a, b) for f in fns] for a in (0, 1) for b in (0, 1)]
fig, ax = plt.subplots(figsize=(10, 3.3)); fig.patch.set_alpha(0); ax.set_axis_off()
t = ax.table(cellText=rows, colLabels=cols, cellLoc="center", bbox=[0, 0, 1, 1])
for (r, c), cell in t.get_celld().items():
    cell.set_edgecolor("#16266e"); cell.set_linewidth(1.4)
    txt = cell.get_text(); txt.set_fontproperties(fb if r == 0 or c < 2 else fp)
    if r == 0: cell.set_facecolor("#dfe7fb"); txt.set_color("#b2191e")
    elif c < 2: cell.set_facecolor("#f3f3f3"); txt.set_color("#16266e")
    else:
        cell.set_facecolor("#fff4b0" if txt.get_text() == "1" else "#fffdf5"); txt.set_color("#16266e")
fig.savefig(os.path.join(OUT, "master_truth_table.png"), dpi=110, transparent=True, bbox_inches="tight"); plt.close(fig)
print("table ok")
