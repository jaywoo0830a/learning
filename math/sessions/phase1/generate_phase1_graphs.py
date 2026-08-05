#!/usr/bin/env python3
"""Generate graphs for phase1 sessions 01-06 (English, phase2-style)."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle, Circle, FancyBboxPatch, Polygon
import os

plt.rcParams.update({
    'figure.dpi': 200, 'font.size': 11, 'font.family': 'sans-serif',
    'axes.titlesize': 12, 'axes.labelsize': 11,
    'legend.fontsize': 9, 'xtick.labelsize': 8, 'ytick.labelsize': 8,
    'axes.grid': False, 'figure.facecolor': 'white', 'axes.facecolor': 'white',
})
BASE = os.path.join(os.path.dirname(__file__), 'graphs')
os.makedirs(BASE, exist_ok=True)

BLUE = '#1a73e8'
RED = '#d93025'
GREEN = '#188038'
AMBER = '#f9ab00'
GRAY = '#999999'

def save(fig, name):
    fig.savefig(os.path.join(BASE, name), bbox_inches='tight')
    plt.close(fig)

# ───────────────────────── Session 01 ─────────────────────────

def s01_connectives():
    """Four mini truth tables: AND, OR, IF-THEN, IFF."""
    fig, axes = plt.subplots(1, 4, figsize=(13, 4.2))
    data = {
        r'AND  $A\wedge B$':   [[('T','T','T'),('T','F','F'),('F','T','F'),('F','F','F')]],
        r'OR  $A\vee B$':     [[('T','T','T'),('T','F','T'),('F','T','T'),('F','F','F')]],
        r'IF-THEN  $A\to B$': [[('T','T','T'),('T','F','F'),('F','T','T'),('F','F','T')]],
        r'IFF  $A\leftrightarrow B$': [[('T','T','T'),('T','F','F'),('F','T','F'),('F','F','T')]],
    }
    for ax, (title, rows) in zip(axes, data.items()):
        ax.axis('off')
        ax.set_title(title, fontweight='bold', fontsize=11)
        rows = rows[0]
        # header row (above the data rows)
        for col, htxt in [(0, 'A'), (1, 'B'), (2, 'out')]:
            ax.add_patch(Rectangle((col, 4.0), 1, 0.6, fc='#f1f3f4', ec='#bbb', lw=0.8))
            ax.text(col+0.5, 4.3, htxt, ha='center', va='center', fontsize=11, fontweight='bold')
        # data rows
        for i, (a, b, r) in enumerate(rows):
            y = 3 - i
            ax.add_patch(Rectangle((0, y), 1, 1, fc='white', ec='#bbb', lw=0.8))
            ax.add_patch(Rectangle((1, y), 1, 1, fc='white', ec='#bbb', lw=0.8))
            ax.add_patch(Rectangle((2, y), 1, 1,
                         fc='#e6f4ea' if r == 'T' else '#fce8e6', ec='#bbb', lw=0.8))
            ax.text(0.5, y+0.5, a, ha='center', va='center', fontsize=11)
            ax.text(1.5, y+0.5, b, ha='center', va='center', fontsize=11)
            ax.text(2.5, y+0.5, r, ha='center', va='center', fontsize=11, fontweight='bold')
        ax.set_xlim(-0.1, 3.1); ax.set_ylim(-0.2, 4.8)
    fig.suptitle('The four connectors — one false row pattern each', fontweight='bold', fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.92])
    save(fig, '01a-connectives.png')

def s01_demorgan():
    """Two Venn diagrams shaded identically: not(A and B) = not A or not B."""
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.6))
    for ax in axes:
        ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis('off')
        # universe
        ax.add_patch(Rectangle((0.8, 0.8), 8.4, 4.4, fc='white', ec='#bbb', lw=1.2))
        ax.text(8.9, 5.1, 'universe', ha='right', fontsize=9, color='#888')
    # left: shade everything except A∩B
    ax = axes[0]
    ax.add_patch(Rectangle((0.8, 0.8), 8.4, 4.4, fc='#fce8e6', ec='#bbb', lw=1.2))
    ax.add_patch(Circle((4.2, 3.0), 1.9, fc='white', ec=BLUE, lw=2))
    ax.add_patch(Circle((5.8, 3.0), 1.9, fc='white', ec=GREEN, lw=2))
    ax.text(4.2, 3.0, 'A', ha='center', va='center', fontsize=13, color=BLUE, fontweight='bold')
    ax.text(5.8, 3.0, 'B', ha='center', va='center', fontsize=13, color=GREEN, fontweight='bold')
    ax.set_title(r'$\neg(A \wedge B)$' '\n' 'red = true region', fontweight='bold', fontsize=12)
    # right: shade ¬A region ∪ ¬B region
    ax = axes[1]
    ax.add_patch(Rectangle((0.8, 0.8), 8.4, 4.4, fc='#fce8e6', ec='#bbb', lw=1.2))
    ax.add_patch(Circle((4.2, 3.0), 1.9, fc='white', ec=BLUE, lw=2))
    ax.add_patch(Circle((5.8, 3.0), 1.9, fc='white', ec=GREEN, lw=2))
    ax.text(4.2, 3.0, 'A', ha='center', va='center', fontsize=13, color=BLUE, fontweight='bold')
    ax.text(5.8, 3.0, 'B', ha='center', va='center', fontsize=13, color=GREEN, fontweight='bold')
    ax.set_title(r'$\neg A \vee \neg B$' '\n' 'red = true region (same!)', fontweight='bold', fontsize=12)
    fig.suptitle(r'De Morgan: $\neg(A \wedge B) \equiv \neg A \vee \neg B$ — identical true regions',
                 fontweight='bold', fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.9])
    save(fig, '01b-demorgan.png')

def s01_tautology():
    """Tautology A or not A — the whole universe is covered."""
    fig, ax = plt.subplots(figsize=(7, 4.6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis('off')
    ax.add_patch(Rectangle((0.8, 0.8), 8.4, 4.4, fc='#e6f4ea', ec='#bbb', lw=1.2))
    ax.add_patch(Circle((4.2, 3.0), 1.9, fc='#a8d5ff', ec=BLUE, lw=2))
    ax.text(4.2, 3.0, r'$A$', ha='center', va='center', fontsize=16, color='#0b57d0', fontweight='bold')
    ax.text(7.3, 4.6, r'$\neg A$', ha='center', va='center', fontsize=14, color=GREEN, fontweight='bold')
    ax.annotate('', xy=(5.6, 4.0), xytext=(5.2, 3.8),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=0))
    ax.text(5.0, 1.4, r'$A \vee \neg A$ covers everything — always true',
            fontsize=11, color=GREEN, fontweight='bold')
    ax.set_title(r'$A \vee \neg A$ — a tautology', fontweight='bold', fontsize=13)
    fig.tight_layout()
    save(fig, '01c-tautology.png')

# ───────────────────────── Session 02 ─────────────────────────

def s02_all_some():
    """Left: All satisfy P. Right: Some satisfy P."""
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.6))
    for ax, mode in zip(axes, ['all', 'some']):
        ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis('off')
        ax.add_patch(Rectangle((0.7, 0.7), 8.6, 4.6, fc='white', ec='#bbb', lw=1.2))
        ax.add_patch(Rectangle((3.2, 0.7), 6.1, 4.6, fc='#e6f4ea', ec=GREEN, lw=1.6, ls='--'))
        ax.text(3.5, 5.0, r'$P(x)$ region', fontsize=10, color=GREEN)
        if mode == 'all':
            inside = [(4.0, 3.4), (5.0, 2.6), (6.0, 3.6), (7.0, 2.2), (8.0, 3.0),
                      (4.8, 1.6), (6.6, 1.4), (8.6, 4.2)]
            for x, y in inside:
                ax.add_patch(Circle((x, y), 0.22, fc=GREEN, ec='white', lw=1))
            ax.set_title('"All objects satisfy $P$"\n→ every dot inside the region',
                         fontweight='bold', fontsize=11)
        else:
            inside = [(4.0, 3.4), (7.0, 2.2), (5.2, 1.5)]
            outside = [(1.7, 3.4), (1.7, 2.4), (1.7, 1.4)]
            for x, y in inside:
                ax.add_patch(Circle((x, y), 0.22, fc=GREEN, ec='white', lw=1))
            for x, y in outside:
                ax.add_patch(Circle((x, y), 0.22, fc=RED, ec='white', lw=1))
            ax.text(4.0, 4.0, 'witness!', fontsize=9, color=GREEN, ha='center')
            ax.set_title('"Some object satisfies $P$"\n→ one green dot is enough',
                         fontweight='bold', fontsize=11)
    fig.suptitle('"All" sweeps the domain — "some" searches it', fontweight='bold', fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.9])
    save(fig, '02a-all-some.png')

def s02_negation():
    """Negating quantifiers: not(all) = some(not)."""
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.6))
    for ax in axes:
        ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis('off')
        ax.add_patch(Rectangle((0.7, 0.7), 8.6, 4.6, fc='white', ec='#bbb', lw=1.2))
        ax.add_patch(Rectangle((3.2, 0.7), 6.1, 4.6, fc='#e6f4ea', ec=GREEN, lw=1.6, ls='--'))
        ax.text(3.5, 5.0, r'$P(x)$ region', fontsize=10, color=GREEN)
    ax = axes[0]
    inside = [(4.0, 3.4), (5.0, 2.6), (6.0, 3.6), (7.0, 2.2), (8.0, 3.0), (5.0, 1.6), (7.5, 4.2)]
    for x, y in inside:
        ax.add_patch(Circle((x, y), 0.22, fc=GREEN, ec='white', lw=1))
    ax.add_patch(Circle((1.8, 3.0), 0.24, fc=RED, ec='white', lw=1))
    ax.annotate('counterexample\n(breaks the "all")', (1.8, 3.0), xytext=(2.0, 0.9),
                fontsize=9, color=RED, fontweight='bold')
    ax.set_title(r'$\forall x\,P(x)$ is FALSE' '\n' 'one red dot outside the region',
                 fontweight='bold', fontsize=11)
    ax = axes[1]
    for x, y in inside:
        ax.add_patch(Circle((x, y), 0.22, fc=RED, ec='white', lw=1))
    ax.add_patch(Circle((1.8, 3.0), 0.24, fc=GREEN, ec='white', lw=1))
    ax.annotate('the same dot is the\nwitness for "some not $P$"', (1.8, 3.0), xytext=(2.0, 0.9),
                fontsize=9, color=GREEN, fontweight='bold')
    ax.set_title(r'$\exists x\,\neg P(x)$ is TRUE' '\n' 'the dot outside satisfies ¬P',
                 fontweight='bold', fontsize=11)
    fig.suptitle(r'Negation: $\neg\forall P \equiv \exists \neg P$', fontweight='bold', fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.9])
    save(fig, '02b-negation.png')

def s02_order_swap():
    """for-every-there-exists vs there-exists-for-every."""
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))
    for ax in axes:
        ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis('off')
    ax = axes[0]
    xs = [(2.0, 4.5), (2.0, 3.0), (2.0, 1.5)]
    ys = [(8.0, 4.5), (8.0, 3.0), (8.0, 1.5)]
    for i, (x, y) in enumerate(zip(xs, ys)):
        ax.add_patch(Circle(x, 0.3, fc=BLUE, ec='white', lw=1.2))
        ax.add_patch(Circle(y, 0.3, fc=GREEN, ec='white', lw=1.2))
        ax.annotate('', xy=y, xytext=x,
                    arrowprops=dict(arrowstyle='->', color=RED, lw=1.6,
                                    shrinkA=0.35, shrinkB=0.35))
    ax.text(2.0, 5.4, '$x$ (picks first)', ha='center', fontsize=10, color=BLUE, fontweight='bold')
    ax.text(8.0, 5.4, '$y$ (responds)', ha='center', fontsize=10, color=GREEN, fontweight='bold')
    ax.set_title(r'$\forall x\,\exists y\, L(y,x)$' '\n' 'each $x$ has its own $y$',
                 fontweight='bold', fontsize=12)
    ax = axes[1]
    xs = [(2.0, 4.5), (2.0, 3.0), (2.0, 1.5)]
    ys = [(8.0, 3.0)]
    for i, (x, y) in enumerate(zip(xs, ys)):
        ax.add_patch(Circle(x, 0.3, fc=BLUE, ec='white', lw=1.2))
    ax.add_patch(Circle((8.0, 3.0), 0.3, fc=GREEN, ec='white', lw=1.2))
    for x in xs:
        ax.annotate('', xy=(8.0, 3.0), xytext=x,
                    arrowprops=dict(arrowstyle='->', color=RED, lw=1.6,
                                    shrinkA=0.35, shrinkB=0.38))
    ax.text(2.0, 5.4, '$x$ (all of them)', ha='center', fontsize=10, color=BLUE, fontweight='bold')
    ax.text(8.0, 5.4, 'one $y$', ha='center', fontsize=10, color=GREEN, fontweight='bold')
    ax.set_title(r'$\exists y\,\forall x\, L(y,x)$' '\n' 'one $y$ must serve every $x$',
                 fontweight='bold', fontsize=12)
    fig.suptitle('Order of quantifiers changes the promise', fontweight='bold', fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.9])
    save(fig, '02c-order-swap.png')

# ───────────────────────── Session 03 ─────────────────────────

def s03_templates():
    """The three proof templates as flows."""
    fig, ax = plt.subplots(figsize=(10, 4.8))
    ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis('off')
    ax.set_title('Three proof templates — how to move from assumption to conclusion',
                 fontweight='bold', fontsize=13)
    boxes = [
        (1.0, 4.2, 'DIRECT\nassume $P$\nwalk to $Q$', BLUE, '$P \\to Q$'),
        (4.2, 4.2, 'CONTRAPOSITIVE\nassume $\\neg Q$\nprove $\\neg P$', GREEN, '$\\neg Q \\to \\neg P$'),
        (7.4, 4.2, 'CONTRADICTION\nassume $P \\wedge \\neg Q$\nreach $\\bot$', RED, '$\\to \\bot$'),
    ]
    for x, y, txt, c, _ in boxes:
        ax.add_patch(FancyBboxPatch((x-0.9, y-0.9), 1.8, 1.8, boxstyle='round,pad=0.08',
                                    fc=c, ec='none', alpha=0.15))
        ax.add_patch(FancyBboxPatch((x-0.9, y-0.9), 1.8, 1.8, boxstyle='round,pad=0.08',
                                    fc='none', ec=c, lw=2))
        ax.text(x, y, txt, ha='center', va='center', fontsize=9.5, color='#222', fontweight='bold')
    # decision arrows
    ax.text(1.0, 2.6, 'if the walk is visible', ha='center', fontsize=9, color='#555')
    ax.text(4.2, 2.6, 'if $\\neg Q$ is easier', ha='center', fontsize=9, color='#555')
    ax.text(7.4, 2.6, 'if the claim is sweeping', ha='center', fontsize=9, color='#555')
    for x in (1.0, 4.2, 7.4):
        ax.annotate('', xy=(x, 3.3), xytext=(x, 3.1),
                    arrowprops=dict(arrowstyle='->', color='#555', lw=1.4))
    ax.text(5.0, 1.0, r'All three prove "if $P$ then $Q$" — choose the easiest assumption to work with.',
            ha='center', fontsize=10.5, color='#333')
    fig.tight_layout()
    save(fig, '03a-templates.png')

def s03_contrapositive():
    """Contrapositive vs converse."""
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.6))
    for ax in axes:
        ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis('off')
    ax = axes[0]
    ax.add_patch(FancyBboxPatch((1.0, 3.6), 2.6, 1.4, boxstyle='round,pad=0.05',
                                fc='#e8f0fe', ec=BLUE, lw=2))
    ax.text(2.3, 4.3, 'rain\n$P$', ha='center', va='center', fontsize=11, color=BLUE, fontweight='bold')
    ax.add_patch(FancyBboxPatch((6.4, 3.6), 2.6, 1.4, boxstyle='round,pad=0.05',
                                fc='#e8f0fe', ec=BLUE, lw=2))
    ax.text(7.7, 4.3, 'wet\n$Q$', ha='center', va='center', fontsize=11, color=BLUE, fontweight='bold')
    ax.annotate('', xy=(6.3, 4.3), xytext=(3.7, 4.3),
                arrowprops=dict(arrowstyle='->', color='#333', lw=2))
    ax.text(5.0, 4.9, 'if P then Q', ha='center', fontsize=10)
    # contrapositive
    ax.add_patch(FancyBboxPatch((1.0, 1.1), 2.6, 1.4, boxstyle='round,pad=0.05',
                                fc='#e6f4ea', ec=GREEN, lw=2))
    ax.text(2.3, 1.8, 'not wet\n$\\neg Q$', ha='center', va='center', fontsize=11, color=GREEN, fontweight='bold')
    ax.add_patch(FancyBboxPatch((6.4, 1.1), 2.6, 1.4, boxstyle='round,pad=0.05',
                                fc='#e6f4ea', ec=GREEN, lw=2))
    ax.text(7.7, 1.8, 'not rain\n$\\neg P$', ha='center', va='center', fontsize=11, color=GREEN, fontweight='bold')
    ax.annotate('', xy=(6.3, 1.8), xytext=(3.7, 1.8),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=2))
    ax.text(5.0, 2.4, r'${\neg Q \to \neg P}$  (equivalent ✓)',
            ha='center', fontsize=10, color=GREEN, fontweight='bold')
    ax.set_title('Contrapositive — same promise', fontweight='bold', fontsize=12)
    ax = axes[1]
    ax.add_patch(FancyBboxPatch((1.0, 3.6), 2.6, 1.4, boxstyle='round,pad=0.05',
                                fc='#fce8e6', ec=RED, lw=2))
    ax.text(2.3, 4.3, 'wet\n$Q$', ha='center', va='center', fontsize=11, color=RED, fontweight='bold')
    ax.add_patch(FancyBboxPatch((6.4, 3.6), 2.6, 1.4, boxstyle='round,pad=0.05',
                                fc='#fce8e6', ec=RED, lw=2))
    ax.text(7.7, 4.3, 'rain\n$P$', ha='center', va='center', fontsize=11, color=RED, fontweight='bold')
    ax.annotate('', xy=(6.3, 4.3), xytext=(3.7, 4.3),
                arrowprops=dict(arrowstyle='->', color=RED, lw=2))
    ax.text(5.0, 4.9, r'$Q \to P$  (converse $\times$)', ha='center', fontsize=10, color=RED, fontweight='bold')
    ax.text(5.0, 2.2, 'A sprinkler could wet the ground\nwithout any rain — the converse\nis a different statement.',
            ha='center', fontsize=9.5, color='#555')
    ax.set_title('Converse — NOT equivalent', fontweight='bold', fontsize=12)
    fig.suptitle('Contrapositive vs converse — only one is the same promise',
                 fontweight='bold', fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.9])
    save(fig, '03b-contrapositive.png')

def s03_contradiction():
    """Contradiction flow: assume opposite → chain → contradiction."""
    fig, ax = plt.subplots(figsize=(10, 4.6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis('off')
    steps = [
        (1.1, 3.0, 'assume the\nstatement is FALSE', BLUE),
        (3.7, 3.0, 'follow the\nlogic', '#666'),
        (6.3, 3.0, 'reach an\nimpossibility $\\bot$', RED),
        (8.9, 3.0, 'conclude it\nis TRUE', GREEN),
    ]
    for x, y, txt, c in steps:
        ax.add_patch(FancyBboxPatch((x-0.95, y-0.85), 1.9, 1.7, boxstyle='round,pad=0.06',
                                    fc='white', ec=c, lw=2))
        ax.text(x, y, txt, ha='center', va='center', fontsize=9.5, color='#222', fontweight='bold')
    for (x1, _, _, _), (x2, _, _, _) in zip(steps, steps[1:]):
        ax.annotate('', xy=(x2-1.0, 3.0), xytext=(x1+1.0, 3.0),
                    arrowprops=dict(arrowstyle='->', color='#555', lw=1.8))
    ax.text(5.0, 1.2, 'Example: assume $\\sqrt{2} = a/b$ reduced → $a$ even → $b$ even → "reduced" is broken. $\\bot$',
            ha='center', fontsize=10, color='#333')
    ax.set_title('Proof by contradiction — the negation collapses', fontweight='bold', fontsize=13)
    fig.tight_layout()
    save(fig, '03c-contradiction.png')

# ───────────────────────── Session 04 ─────────────────────────

def s04_domino():
    """Domino chain: base case + chain rule."""
    fig, ax = plt.subplots(figsize=(10, 4.6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis('off')
    n = 8
    xs = np.linspace(1.1, 8.9, n)
    for i, x in enumerate(xs):
        c = RED if i == 0 else (BLUE if i < 4 else '#9aa0a6')
        # tilted domino
        ax.add_patch(Polygon([(x-0.18, 1.0), (x+0.18, 1.0), (x+0.05, 2.2), (x-0.31, 2.2)],
                             fc=c, ec='white', lw=0.6))
    for x in xs[:-1]:
        ax.annotate('', xy=(x+0.62, 1.55), xytext=(x+0.32, 1.55),
                    arrowprops=dict(arrowstyle='->', color='#555', lw=1.5))
    ax.annotate('first domino\n(base case $P(1)$)', (xs[0], 2.5), xytext=(xs[0]-0.4, 3.6),
                fontsize=9.5, color=RED, fontweight='bold')
    ax.annotate('each knocks the next\n(chain rule $P(k)\\to P(k{+}1)$)', (xs[2], 2.6), xytext=(xs[2]+0.2, 4.0),
                fontsize=9.5, color=BLUE, fontweight='bold')
    ax.text(5.0, 0.6, 'two facts → every domino falls → $P(n)$ for ALL $n$',
            ha='center', fontsize=11, color='#333', fontweight='bold')
    ax.set_title('Mathematical induction = the domino chain', fontweight='bold', fontsize=13)
    fig.tight_layout()
    save(fig, '04a-domino.png')

def s04_sum_odds():
    """Sum of odds = squares, gnomons."""
    fig, ax = plt.subplots(figsize=(8, 4.6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis('off')
    # 3x3 grid with L-shaped gnomon colors
    cells = {(0,0): '#f9ab00', (0,1): '#f9ab00', (0,2): '#f9ab00',
             (1,0): '#f9ab00', (2,0): '#f9ab00', (1,1): '#1a73e8',
             (2,1): '#d93025', (1,2): '#188038', (2,2): '#188038'}
    # Draw a 3x3 grid where gnomon colors show 1, +3, +5
    grid = [[None]*3 for _ in range(3)]
    # gnomon k (size k): color index 0,1,2
    gno = {0: '#f9ab00', 1: '#1a73e8', 2: '#d93025'}
    for k in range(3):
        # k-th gnomon occupies row k (cols 0..k) and col k (rows 0..k-1)
        for c in range(k+1):
            grid[k][c] = gno[k]
        for r in range(k):
            grid[r][k] = gno[k]
    for r in range(3):
        for c in range(3):
            ax.add_patch(Rectangle((1.2 + c*1.1, 4.4 - r*1.1), 1.0, 1.0,
                                   fc=grid[r][c], ec='white', lw=1.2))
    ax.text(1.2, 5.6, '1', fontsize=10, ha='left', color='#333')
    ax.text(2.3, 5.6, '+3', fontsize=10, ha='left', color='#333')
    ax.text(3.4, 5.6, '+5', fontsize=10, ha='left', color='#333')
    ax.text(6.0, 3.4, r'$1 + 3 + 5 = 3^2$', fontsize=13, color='#333', fontweight='bold')
    ax.text(6.0, 2.4, r'each gnomon adds $2n{-}1$ cells', fontsize=10.5, color='#555')
    ax.text(6.0, 1.6, r'so $1+3+\cdots+(2n{-}1) = n^2$', fontsize=10.5, color=GREEN, fontweight='bold')
    ax.set_title('Sum of odd numbers = squares (the inductive picture)',
                 fontweight='bold', fontsize=12)
    fig.tight_layout()
    save(fig, '04b-sum-odds.png')

def s04_strong():
    """Strong induction: assume all previous cases."""
    fig, ax = plt.subplots(figsize=(10, 4.6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis('off')
    # stack of previous cases
    for i in range(5):
        x = 1.2 + i*0.55
        ax.add_patch(FancyBboxPatch((x, 2.0 - i*0.12), 0.55, 0.55, boxstyle='round,pad=0.03',
                                    fc='#e6f4ea', ec=GREEN, lw=1.2))
    ax.text(2.0, 3.3, 'assume $P(1), P(2), \\dots, P(k)$', fontsize=11, color=GREEN, fontweight='bold')
    # target
    ax.add_patch(FancyBboxPatch((6.6, 1.9), 1.7, 1.4, boxstyle='round,pad=0.06',
                                fc='#fce8e6', ec=RED, lw=2))
    ax.text(7.45, 2.6, 'prove\n$P(k{+}1)$', ha='center', va='center', fontsize=12, color=RED, fontweight='bold')
    ax.annotate('', xy=(6.5, 2.6), xytext=(3.6, 2.6),
                arrowprops=dict(arrowstyle='->', color='#555', lw=2))
    ax.text(5.05, 3.0, 'use whichever\nprevious cases\nare needed', ha='center', fontsize=9.5, color='#555')
    # example
    ax.text(5.0, 1.0, 'Example: if $k{+}1 = a\\cdot b$ (composite), both $a$ and $b$ are $\\leq k$ —',
            ha='center', fontsize=10, color='#333')
    ax.text(5.0, 0.6, 'so their prime factorizations exist by the hypothesis. (prime factorization theorem)',
            ha='center', fontsize=10, color='#333')
    ax.set_title('Strong induction — the whole stack of previous cases is available',
                 fontweight='bold', fontsize=12)
    fig.tight_layout()
    save(fig, '04c-strong-induction.png')

# ───────────────────────── Session 05 ─────────────────────────

def s05_pairing():
    """Bijection between naturals and evens."""
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))
    # left: apples & oranges
    ax = axes[0]
    ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis('off')
    apos = [(1.8, 4.4), (1.8, 3.0), (1.8, 1.6)]
    opos = [(5.2, 4.4), (5.2, 3.0), (5.2, 1.6)]
    for (x, y) in apos:
        ax.add_patch(Circle((x, y), 0.42, fc=RED, ec='#a52a2a', lw=1.4))
    for (x, y) in opos:
        ax.add_patch(Circle((x, y), 0.42, fc=AMBER, ec='#b06000', lw=1.4))
    for (x1, y1), (x2, y2) in zip(apos, opos):
        ax.annotate('', xy=(x2-0.5, y2), xytext=(x1+0.5, y1),
                    arrowprops=dict(arrowstyle='-', color='#666', lw=1.6))
    ax.text(1.8, 5.2, 'apples', ha='center', fontsize=11, color=RED, fontweight='bold')
    ax.text(5.2, 5.2, 'oranges', ha='center', fontsize=11, color='#b06000', fontweight='bold')
    ax.set_title('Perfect pairing → same size\n(no counting needed)', fontweight='bold', fontsize=11)
    # right: N ↔ evens
    ax = axes[1]
    ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis('off')
    nat = [(1.9, 4.6), (1.9, 3.6), (1.9, 2.6), (1.9, 1.6)]
    evn = [(7.2, 4.6), (7.2, 3.6), (7.2, 2.6), (7.2, 1.6)]
    for (x, y) in nat:
        ax.add_patch(Circle((x, y), 0.35, fc=BLUE, ec='white', lw=1))
    for (x, y) in evn:
        ax.add_patch(Circle((x, y), 0.35, fc=GREEN, ec='white', lw=1))
    for (x1, y1), (x2, y2) in zip(nat, evn):
        ax.annotate('', xy=(x2-0.4, y2), xytext=(x1+0.4, y1),
                    arrowprops=dict(arrowstyle='-', color='#666', lw=1.4))
    for i, (_, y) in enumerate(nat):
        ax.text(1.9, y, str(i+1), ha='center', va='center', fontsize=9, color='white', fontweight='bold')
    for i, (_, y) in enumerate(evn):
        ax.text(7.2, y, str(2*(i+1)), ha='center', va='center', fontsize=9, color='white', fontweight='bold')
    ax.text(1.9, 5.4, r'$\mathbb{N}$', ha='center', fontsize=12, color=BLUE, fontweight='bold')
    ax.text(7.2, 5.4, 'evens', ha='center', fontsize=11, color=GREEN, fontweight='bold')
    ax.text(4.6, 3.0, r'$n \leftrightarrow 2n$', ha='center', fontsize=11, color='#333')
    ax.set_title(r'$\mathbb{N}$ and the evens: same size!' '\n' '(part = whole in infinity)',
                 fontweight='bold', fontsize=11)
    fig.suptitle('Size = pairing, not counting', fontweight='bold', fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.9])
    save(fig, '05a-pairing.png')

def s05_rationals():
    """Diagonal walk through the fraction grid."""
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.set_xlim(0, 7); ax.set_ylim(0, 7); ax.axis('off')
    ax.set_title('Enumerating the positive fractions — the diagonal walk', fontweight='bold', fontsize=13)
    N = 6
    import math as _m
    order = {}
    cnt = 0
    path = []
    for s in range(2, 2*N+1):          # numerator+denominator
        for num in range(1, N+1):
            den = s - num
            if 1 <= den <= N:
                order[(num, den)] = cnt
                path.append((num, den))
                cnt += 1
    # draw grid cells first (no text yet)
    for num in range(1, N+1):
        for den in range(1, N+1):
            reduced = _m.gcd(num, den) == 1
            fc = '#e6f4ea' if reduced else '#f1f3f4'
            ax.add_patch(Rectangle((num-0.5, den-0.5), 1, 1, fc=fc, ec='#ccc', lw=0.6))
    # zig-zag path (under the labels)
    seg = [(num, den) for (num, den) in path if _m.gcd(num, den) == 1]
    xs = [p[0] for p in seg]; ys = [p[1] for p in seg]
    ax.plot(xs, ys, color=RED, lw=1.8, alpha=0.75, zorder=3)
    # fraction labels on top of the path
    for num in range(1, N+1):
        for den in range(1, N+1):
            if _m.gcd(num, den) == 1:
                ax.text(num, den, f'{num}/{den}', ha='center', va='center', fontsize=7.5,
                        color='#333', zorder=4)
            else:
                ax.text(num, den, 'x', ha='center', va='center', fontsize=7, color='#aaa', zorder=4)
    # order numbers as small badges in the top-right corner of each cell
    for (num, den), k in order.items():
        if _m.gcd(num, den) == 1 and k < 12:
            ax.text(num+0.32, den+0.32, str(k+1), ha='center', va='center', fontsize=6.5,
                    color=RED, fontweight='bold', zorder=5)
    ax.text(6.8, 6.6, 'walk diagonals\n(skip reducible)', ha='right', fontsize=9, color=RED)
    ax.text(0.3, 6.6, 'denominator', fontsize=10, color='#333')
    ax.text(6.6, 0.2, 'numerator →', ha='right', fontsize=10, color='#333')
    fig.tight_layout()
    save(fig, '05b-rationals.png')

def s05_diagonal():
    """Cantor diagonal argument on binary strings."""
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))
    ax = axes[0]
    ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis('off')
    ax.set_title('The list (assumed complete)', fontweight='bold', fontsize=11)
    rows = [
        '0 1 0 1 0 0 1',
        '1 0 1 1 0 1 0',
        '1 1 0 1 1 0 1',
        '0 1 1 0 1 1 0',
        '1 0 0 1 0 1 1',
        '0 0 1 1 1 0 1',
    ]
    for i, r in enumerate(rows):
        y = 5.3 - i*0.78
        for j, ch in enumerate(r.replace(' ', '')):
            x = 1.6 + j*0.55
            diag = (i == j)
            ax.add_patch(Rectangle((x, y), 0.45, 0.45, fc=('#fce8e6' if diag else 'white'),
                                   ec='#bbb', lw=0.6))
            ax.text(x+0.225, y+0.225, ch, ha='center', va='center', fontsize=9)
    # left labels
    for i in range(6):
        ax.text(0.8, 5.3 - i*0.78 + 0.225, f'$s_{i+1}$', ha='center', va='center', fontsize=9, color=BLUE)
    ax.text(4.9, 0.6, 'diagonal digits highlighted in red', ha='center', fontsize=9, color=RED)
    ax = axes[1]
    ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis('off')
    ax.set_title('The new number $d$ — differs from every row', fontweight='bold', fontsize=11)
    diag_bits = ['0', '1', '0', '1', '0', '1']
    new_bits = ['1', '0', '1', '0', '1', '0']
    for j, (o, nw) in enumerate(zip(diag_bits, new_bits)):
        x = 1.6 + j*0.55
        ax.add_patch(Rectangle((x, 3.4), 0.45, 0.45, fc='white', ec='#bbb', lw=0.6))
        ax.text(x+0.225, 3.62, o, ha='center', va='center', fontsize=8, color='#aaa')
        ax.add_patch(Rectangle((x, 2.4), 0.45, 0.45, fc='#e6f4ea', ec=GREEN, lw=1.2))
        ax.text(x+0.225, 2.62, nw, ha='center', va='center', fontsize=9, color=GREEN, fontweight='bold')
    ax.annotate('', xy=(1.8, 3.35), xytext=(1.8, 2.9),
                arrowprops=dict(arrowstyle='->', color='#666', lw=1.3))
    ax.text(1.8, 4.4, 'flip each diagonal digit', ha='center', fontsize=9, color='#555')
    ax.text(6.6, 3.0, '$d = 101010\\dots$', fontsize=12, color=GREEN, fontweight='bold')
    ax.text(6.6, 2.2, 'differs from $s_1$ in bit 1,\nfrom $s_2$ in bit 2, …\n→ NOT in the list!',
            fontsize=9.5, color='#333')
    ax.text(5.0, 0.8, 'every list misses some real → $|\\mathbb{R}| > \\aleph_0$',
            ha='center', fontsize=10.5, color=RED, fontweight='bold')
    fig.suptitle("Cantor's diagonal argument", fontweight='bold', fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.9])
    save(fig, '05c-diagonal.png')

def s05_hierarchy():
    """Ladder of infinities."""
    fig, ax = plt.subplots(figsize=(8, 4.8))
    ax.set_xlim(0, 10); ax.set_ylim(0, 6.9); ax.axis('off')
    levels = [
        (1.0, r'$\aleph_0$   (naturals, integers, fractions)'),
        (2.6, r'$2^{\aleph_0}$   (reals, powerset of N)'),
        (4.2, r'$2^{2^{\aleph_0}}$   (all functions)'),
        (5.8, r'$2^{2^{2^{\aleph_0}}}$   ... no largest infinity'),
    ]
    for i, (y, label) in enumerate(levels):
        ax.add_patch(FancyBboxPatch((1.7, y-0.32), 5.9, 0.64, boxstyle='round,pad=0.04',
                                    fc=('#e6f4ea' if i % 2 == 0 else '#e8f0fe'), ec='#999', lw=1.2))
        ax.text(4.65, y, label, ha='center', va='center', fontsize=10, color='#333', fontweight='bold')
    # arrows in the gaps to the RIGHT of the boxes
    for (y1, _), (y2, _) in zip(levels, levels[1:]):
        ax.annotate('', xy=(8.1, y2-0.35), xytext=(8.1, y1+0.35),
                    arrowprops=dict(arrowstyle='->', color=RED, lw=2))
        ax.text(8.25, (y1+y2)/2, 'strictly bigger', fontsize=8.5, color=RED,
                ha='left', va='center')
    ax.text(5.0, 6.6, 'The hierarchy of infinities — powersets climb forever',
            ha='center', fontsize=12, fontweight='bold')
    fig.tight_layout()
    save(fig, '05d-hierarchy.png')

# ───────────────────────── Session 06 ─────────────────────────

def s06_liar():
    """The liar sentence with a self-reference loop."""
    fig, ax = plt.subplots(figsize=(7, 4.6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis('off')
    ax.add_patch(FancyBboxPatch((2.2, 1.8), 5.6, 2.0, boxstyle='round,pad=0.08',
                                fc='#e8f0fe', ec=BLUE, lw=2.5))
    ax.text(5.0, 2.8, '"This sentence\nis FALSE."', ha='center', va='center',
            fontsize=14, color='#0b57d0', fontweight='bold')
    # single self-reference loop arcing over the top of the box
    ax.annotate('', xy=(7.4, 3.1), xytext=(2.6, 3.1),
                arrowprops=dict(arrowstyle='->', color=RED, lw=2.2,
                                connectionstyle='arc3,rad=-0.8'))
    ax.text(5.0, 4.85, 'points at itself', ha='center', fontsize=10, color=RED, fontweight='bold')
    ax.text(5.0, 1.0, 'true ⇒ false ⇒ true ⇒ … — the loop never settles',
            ha='center', fontsize=10.5, color='#333')
    ax.set_title('The liar sentence — self-reference breaks truth', fontweight='bold', fontsize=12)
    fig.tight_layout()
    save(fig, '06a-liar.png')

def s06_godel_number():
    """Encoding a sentence into a Gödel number."""
    fig, ax = plt.subplots(figsize=(12, 4.8))
    ax.set_xlim(0, 12); ax.set_ylim(0, 6); ax.axis('off')
    steps = [
        (1.6, 3.0, '"$x = 0$"', 'sentence', BLUE),
        (4.6, 3.0, '[7, 4, 1]', 'code sequence', '#666'),
        (7.6, 3.0, r'$2^7 \cdot 3^4 \cdot 5^1$', 'prime powers', '#666'),
        (10.6, 3.0, '51840', 'Gödel number', GREEN),
    ]
    for x, y, big, small, c in steps:
        ax.add_patch(FancyBboxPatch((x-1.2, y-0.95), 2.4, 1.9, boxstyle='round,pad=0.06',
                                    fc='white', ec=c, lw=2))
        ax.text(x, y+0.25, big, ha='center', va='center', fontsize=10, color='#222', fontweight='bold')
        ax.text(x, y-0.5, small, ha='center', va='center', fontsize=8.5, color=c)
    for (x1, _, _, _, _), (x2, _, _, _, _) in zip(steps, steps[1:]):
        ax.annotate('', xy=(x2-1.25, 3.0), xytext=(x1+1.25, 3.0),
                    arrowprops=dict(arrowstyle='->', color='#555', lw=1.8))
    ax.text(6.0, 1.0, 'unique prime factorization → decoding is reversible —\nevery sentence gets its own number',
            ha='center', fontsize=10, color='#333')
    ax.set_title('Gödel numbering — a mathematical sentence becomes one natural number',
                 fontweight='bold', fontsize=12)
    fig.tight_layout()
    save(fig, '06b-godel-number.png')

def s06_godel_sentence():
    """G: I am not provable. Two-case conclusion."""
    fig, ax = plt.subplots(figsize=(10, 4.8))
    ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis('off')
    # system box
    ax.add_patch(FancyBboxPatch((1.0, 0.8), 8.0, 4.6, boxstyle='round,pad=0.08',
                                fc='#f1f3f4', ec='#888', lw=1.6))
    ax.text(1.3, 5.2, 'the formal system (arithmetic)', fontsize=9.5, color='#555')
    # G box
    ax.add_patch(FancyBboxPatch((3.4, 1.9), 3.2, 2.2, boxstyle='round,pad=0.08',
                                fc='#fce8e6', ec=RED, lw=2.4))
    ax.text(5.0, 3.0, '$G$: "I am\nnot provable"', ha='center', va='center',
            fontsize=12, color='#d93025', fontweight='bold')
    # single self-reference loop arcing over the top of G
    ax.annotate('', xy=(6.9, 3.4), xytext=(3.1, 3.4),
                arrowprops=dict(arrowstyle='->', color=RED, lw=2.0,
                                connectionstyle='arc3,rad=-0.75'))
    ax.text(5.0, 4.7, r'$G \leftrightarrow \neg\,\mathrm{Provable}(GN(G))$',
            ha='center', fontsize=11, color=RED, fontweight='bold')
    ax.text(5.0, 0.5, 'consistent system ⇒ $G$ unprovable AND $\\neg G$ unprovable ⇒ $G$ is true',
            ha='center', fontsize=10.5, color='#333', fontweight='bold')
    ax.set_title('The Gödel sentence — self-reference made mathematical', fontweight='bold', fontsize=12)
    fig.tight_layout()
    save(fig, '06c-godel-sentence.png')

if __name__ == '__main__':
    s01_connectives(); s01_demorgan(); s01_tautology()
    s02_all_some(); s02_negation(); s02_order_swap()
    s03_templates(); s03_contrapositive(); s03_contradiction()
    s04_domino(); s04_sum_odds(); s04_strong()
    s05_pairing(); s05_rationals(); s05_diagonal(); s05_hierarchy()
    s06_liar(); s06_godel_number(); s06_godel_sentence()
    print('All 19 phase1 graphs written to', BASE)
