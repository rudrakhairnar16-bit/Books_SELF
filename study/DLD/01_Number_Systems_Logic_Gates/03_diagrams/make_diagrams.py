#!/usr/bin/env python3
"""Diagrams for DLD Unit 1. Run: python3 make_diagrams.py  (from this folder or anywhere)"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import schemdraw
import schemdraw.logic as logic
import schemdraw.elements as elm

OUT = os.path.dirname(os.path.abspath(__file__))
schemdraw.config(fontsize=13)


# ---------------------------------------------------------------- helpers
import tempfile
from PIL import Image
TMP = tempfile.mkdtemp()


def schem_png(build, name):
    """build(d) adds elements to a schemdraw Drawing; returns PIL image"""
    fp = os.path.join(TMP, name + ".png")
    with schemdraw.Drawing(show=False) as d:
        d.config(fontsize=16, lw=2)
        build(d)
        d.save(fp, dpi=140)
    return Image.open(fp)


def show(ax, img):
    ax.imshow(img); ax.set_axis_off()


# ---------------------------------------------------------------- 1. all gates
GATES = [
    ("AND", logic.And, "Y = A·B", "IC 7408", lambda a, b: a & b, 2),
    ("OR", logic.Or, "Y = A + B", "IC 7432", lambda a, b: a | b, 2),
    ("NOT", logic.Not, "Y = A'", "IC 7404", lambda a, b: 1 - a, 1),
    ("NAND", logic.Nand, "Y = (A·B)'", "IC 7400", lambda a, b: 1 - (a & b), 2),
    ("NOR", logic.Nor, "Y = (A + B)'", "IC 7402", lambda a, b: 1 - (a | b), 2),
    ("XOR", logic.Xor, "Y = A ⊕ B = A'B + AB'", "IC 7486", lambda a, b: a ^ b, 2),
    ("XNOR", logic.Xnor, "Y = (A ⊕ B)' = AB + A'B'", "IC 74266", lambda a, b: 1 - (a ^ b), 2),
]


def gate_symbol(G, n):
    def b(d):
        g = G().right()
        d += g
        if n == 1:
            d += logic.Line().at(g.in1).left(1.0).label("A", "left")
        else:
            d += logic.Line().at(g.in1).left(0.7).label("A", "left")
            d += logic.Line().at(g.in2).left(0.7).label("B", "left")
        d += logic.Line().at(g.out).right(0.7).label("Y", "right")
    return b


def all_gates():
    fig, axes = plt.subplots(2, 4, figsize=(16, 8.6))
    for ax, (name, G, expr, ic, fn, n) in zip(axes.flat, GATES):
        ax.set_axis_off()
        ax.set_title(f"{name} gate", fontsize=15, fontweight="bold", color="#16266e")
        sub = ax.inset_axes([0.15, 0.55, 0.7, 0.42]); show(sub, schem_png(gate_symbol(G, n), name))
        ax.text(0.5, 0.45, expr, ha="center", fontsize=12, transform=ax.transAxes)
        ax.text(0.5, 0.38, ic, ha="center", fontsize=10.5, color="#b2191e", transform=ax.transAxes)
        if n == 1:
            rows = [[a, fn(a, 0)] for a in (0, 1)]; cols = ["A", "Y"]
        else:
            rows = [[a, b, fn(a, b)] for a in (0, 1) for b in (0, 1)]; cols = ["A", "B", "Y"]
        t = ax.table(cellText=rows, colLabels=cols, bbox=[0.25, 0.0, 0.5, 0.34], cellLoc="center")
        t.set_fontsize(11)
        for (r, c), cell in t.get_celld().items():
            if r == 0:
                cell.set_facecolor("#dfe7fb")
            if c == len(cols) - 1 and r > 0:
                cell.set_facecolor("#fff4b0")
    ax = axes.flat[7]; ax.set_axis_off()
    ax.text(0.02, 0.95, "Remember", fontsize=15, fontweight="bold", color="#b2191e", va="top")
    tips = ["AND  → 1 only if ALL inputs 1", "OR   → 1 if ANY input 1", "NOT  → inverts",
            "NAND → 0 only if ALL inputs 1", "NOR  → 1 only if ALL inputs 0", "XOR  → 1 if inputs DIFFERENT",
            "XNOR → 1 if inputs SAME", "", "Basic gates: AND, OR, NOT", "Universal gates: NAND, NOR",
            "Bubble (o) at output = inversion"]
    for i, t in enumerate(tips):
        ax.text(0.02, 0.84 - i * 0.075, t, fontsize=11.5, family="monospace", va="top")
    fig.suptitle("DLD Unit 1 — Logic gates: symbol, expression, IC number, truth table", fontsize=17, fontweight="bold")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "logic_gates_all.png"), dpi=120)
    plt.close(fig)


# ---------------------------------------------------------------- 2. universal gates
def tied(d, G, at=None, label=None):
    """gate with both inputs tied together (acts as NOT); returns gate"""
    g = G().right() if at is None else G().right().anchor("in1").at(at)
    d += g
    d += logic.Line().at(g.in1).left(0.4); t = d.here
    d += logic.Line().at(g.in2).left(0.4); b = d.here
    d += logic.Line().at(t).to(b)
    mid = (t[0], (t[1] + b[1]) / 2)
    d += logic.Dot().at(mid)
    return g, mid


def universal(kind):
    G = logic.Nand if kind == "NAND" else logic.Nor
    gate_out = "AB" if kind == "NAND" else "A+B"
    other = "A+B" if kind == "NAND" else "AB"

    def b_not(d):
        g, mid = tied(d, G)
        d += logic.Line().at(mid).left(0.8).label("A", "left")
        d += logic.Line().at(g.out).right(0.7).label("A'", "right")

    def b_direct(d):           # G followed by G-as-NOT  -> AND (NAND) / OR (NOR)
        g1 = G(); d += g1
        d += logic.Line().at(g1.in1).left(0.7).label("A", "left")
        d += logic.Line().at(g1.in2).left(0.7).label("B", "left")
        d += logic.Line().at(g1.out).right(0.4); p = d.here
        g2 = G().right().anchor("in1").at((p[0] + 0.8, p[1] + (g1.in1[1] - g1.in2[1]) / 2)); d += g2
        d += logic.Line().at(g2.in1).left(0.4); t = d.here
        d += logic.Line().at(g2.in2).left(0.4); bt = d.here
        d += logic.Line().at(t).to(bt)
        d += logic.Line().at(p).to((t[0], p[1])); d += logic.Dot().at((t[0], p[1]))
        d += logic.Line().at(g2.out).right(0.7).label(gate_out, "right")

    def b_inverted(d):         # invert inputs, then G -> OR (NAND) / AND (NOR)
        ga, ma = tied(d, G, at=(0, 2.2)); d += logic.Line().at(ma).left(0.7).label("A", "left")
        gb, mb = tied(d, G, at=(0, -0.6)); d += logic.Line().at(mb).left(0.7).label("B", "left")
        g3 = G().right().anchor("in1").at((ga.out[0] + 1.6, (ga.out[1] + gb.out[1]) / 2 + 0.5)); d += g3
        xm = ga.out[0] + 0.8
        d += logic.Line().at(ga.out).to((xm, ga.out[1])); d += logic.Line().to((xm, g3.in1[1])); d += logic.Line().to(g3.in1)
        d += logic.Line().at(gb.out).to((xm, gb.out[1])); d += logic.Line().to((xm, g3.in2[1])); d += logic.Line().to(g3.in2)
        d += logic.Line().at(g3.out).right(0.7).label(other, "right")

    fig, axes = plt.subplots(1, 3, figsize=(16, 4.8), gridspec_kw={"width_ratios": [1, 1.3, 1.3]})
    imgs = [schem_png(b_not, kind + "not"), schem_png(b_direct, kind + "dir"), schem_png(b_inverted, kind + "inv")]
    if kind == "NAND":
        titles = ["NOT = one NAND (inputs tied)", "AND = NAND + NAND-inverter", "OR = invert inputs, then NAND"]
        res = ["(A·A)' = A'", "((AB)')' = AB", "(A'·B')' = A + B  (De Morgan)"]
    else:
        titles = ["NOT = one NOR (inputs tied)", "OR = NOR + NOR-inverter", "AND = invert inputs, then NOR"]
        res = ["(A+A)' = A'", "((A+B)')' = A + B", "(A'+B')' = AB  (De Morgan)"]
    for ax, img, t, r in zip(axes, imgs, titles, res):
        show(ax, img); ax.set_title(t, fontsize=13.5, fontweight="bold", color="#16266e")
        ax.text(0.5, -0.12, r, ha="center", fontsize=13, transform=ax.transAxes, color="#b2191e")
    fig.suptitle(f"{kind} is a UNIVERSAL gate — any circuit can be built from {kind} alone"
                 f"   (gates needed: NOT 1, AND {2 if kind=='NAND' else 3}, OR {3 if kind=='NAND' else 2})", fontsize=14.5, fontweight="bold")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, f"universal_{kind.lower()}.png"), dpi=120, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- 3. conversion map
def conversion_map():
    fig, ax = plt.subplots(figsize=(11, 8)); ax.set_axis_off(); ax.set_xlim(0, 10); ax.set_ylim(0, 8)
    pos = {"DECIMAL\n(base 10)": (5, 7), "BINARY\n(base 2)": (5, 3.6), "OCTAL\n(base 8)": (1.5, 1), "HEX\n(base 16)": (8.5, 1)}
    for k, (x, y) in pos.items():
        ax.add_patch(FancyBboxPatch((x - 1.1, y - 0.5), 2.2, 1.0, boxstyle="round,pad=0.1", fc="#dfe7fb", ec="#16266e", lw=2))
        ax.text(x, y, k, ha="center", va="center", fontsize=14, fontweight="bold")

    def arrow(a, b, text, off=(0, 0), color="#16266e", rad=0.15):
        (x1, y1), (x2, y2) = pos[a], pos[b]
        ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), connectionstyle=f"arc3,rad={rad}", arrowstyle="-|>",
                                     mutation_scale=22, lw=2, color=color, shrinkA=38, shrinkB=38))
        ax.text((x1 + x2) / 2 + off[0], (y1 + y2) / 2 + off[1], text, ha="center", va="center", fontsize=10.5,
                bbox=dict(fc="white", ec="none", alpha=0.9), color=color)
    D, B, O, H = list(pos)
    arrow(D, B, "Integer: ÷2, remainders\nREAD UPWARD\nFraction: ×2, carries\nREAD DOWNWARD", (-1.25, 0), "#b2191e")
    arrow(B, D, "Σ digit × 2ⁿ\n(…,8,4,2,1 . ½,¼,…)", (1.3, 0))
    arrow(B, O, "Group 3 bits from\nthe point → 1 octal digit", (-1.2, 0.6))
    arrow(O, B, "Each octal digit\n→ 3 bits", (0.3, -0.7))
    arrow(B, H, "Group 4 bits from\nthe point → 1 hex digit", (1.2, 0.6))
    arrow(H, B, "Each hex digit\n→ 4 bits", (-0.3, -0.7))
    arrow(D, O, "÷8 / ×8", (-2.3, 1.1), "#1d7a3a", rad=0.35)
    arrow(D, H, "÷16 / ×16", (2.3, 1.1), "#1d7a3a", rad=-0.35)
    arrow(O, H, "Octal ↔ Hex: go via BINARY", (0, -0.95), "#6a1b9a", rad=0.25)
    ax.set_title("Number-system conversion map (Unit 1)", fontsize=16, fontweight="bold")
    fig.savefig(os.path.join(OUT, "conversion_map.png"), dpi=120, bbox_inches="tight"); plt.close(fig)


# ---------------------------------------------------------------- 4. digital system block
def digital_system():
    fig, ax = plt.subplots(figsize=(11, 3.4)); ax.set_axis_off(); ax.set_xlim(0, 11); ax.set_ylim(0, 3.4)
    ax.add_patch(FancyBboxPatch((3.5, 0.9), 4, 1.6, boxstyle="round,pad=0.1", fc="#dfe7fb", ec="#16266e", lw=2))
    ax.text(5.5, 1.7, "Discrete Information\nProcessing System", ha="center", va="center", fontsize=13, fontweight="bold")
    ax.annotate("", xy=(3.4, 1.7), xytext=(0.6, 1.7), arrowprops=dict(arrowstyle="-|>", lw=2.5))
    ax.text(1.9, 2.0, "Discrete inputs", ha="center", fontsize=12)
    ax.annotate("", xy=(10.4, 1.7), xytext=(7.6, 1.7), arrowprops=dict(arrowstyle="-|>", lw=2.5))
    ax.text(9.0, 2.0, "Discrete outputs", ha="center", fontsize=12)
    ax.annotate("", xy=(5.5, 2.65), xytext=(5.5, 3.3), arrowprops=dict(arrowstyle="<|-|>", lw=2, color="#b2191e"))
    ax.text(6.9, 3.0, "System state (memory)", fontsize=11.5, color="#b2191e")
    ax.text(5.5, 0.25, "No state → COMBINATIONAL  |  State updated at clock → SYNCHRONOUS sequential  |  any time → ASYNCHRONOUS",
            ha="center", fontsize=10.5)
    fig.savefig(os.path.join(OUT, "digital_system_block.png"), dpi=120, bbox_inches="tight"); plt.close(fig)


if __name__ == "__main__":
    all_gates(); universal("NAND"); universal("NOR"); conversion_map(); digital_system()
    print("done:", sorted(f for f in os.listdir(OUT) if f.endswith(".png")))
