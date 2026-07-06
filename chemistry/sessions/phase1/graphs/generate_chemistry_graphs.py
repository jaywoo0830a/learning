"""
Chemistry visualization graphs for Phase 1 sessions 01-07.
01: Subatomic particle counting diagram
02: g↔mol conversion flowchart
03: Balancing equation visual
04: Mole ratio bridge
05: 3-step stoichiometry
06: Limiting reactant comparison
07: Empirical formula + combustion analysis flowchart
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle, Arc
from matplotlib import rcParams

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True

OUT = '/home/rlawjddn/learning/chemistry/sessions/phase1/graphs/'
import os
os.makedirs(OUT, exist_ok=True)


def draw_box(ax, x, y, w, h, text, color='lightblue', fontsize=11, bold=False):
    """Draw a rounded box with text."""
    ax.add_patch(FancyBboxPatch((x-w/2, y-h/2), w, h, boxstyle='round,pad=0.15',
                                 facecolor=color, edgecolor='black', alpha=0.85, linewidth=1.2))
    weight = 'bold' if bold else 'normal'
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize, fontweight=weight)


def draw_arrow(ax, x1, y1, x2, y2, color='black'):
    """Draw an arrow from (x1,y1) to (x2,y2)."""
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
               arrowprops=dict(arrowstyle='->', color=color, lw=1.8))


# ================================================================
# 01: Subatomic Particle Counting
# ================================================================
fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 14); ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.3, 'Counting Subatomic Particles from Nuclear Notation', fontsize=16, ha='center', fontweight='bold')

# Notation display
ax.text(7, 8.2, r'$\mathbf{^{A}_{Z}X^{charge}}$', fontsize=22, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

# Three paths
# Protons
draw_box(ax, 2.5, 6.5, 3.5, 1.0, 'Protons = Z\n(top integer)', 'lightgreen', 12, True)
draw_arrow(ax, 6, 7.8, 3.5, 7.0)

# Neutrons
draw_box(ax, 7, 6.5, 4.5, 1.0, 'Neutrons = A − Z\n(top-left − top)', 'lightcoral', 12, True)
draw_arrow(ax, 6.5, 7.5, 7, 7.0)

# Electrons
draw_box(ax, 11.5, 6.5, 3.8, 1.0, 'Electrons = Z − charge\n(charge: + → subtract, − → add)', 'lightblue', 11, True)
draw_arrow(ax, 7.8, 7.5, 11, 7.0)

# Example
ax.text(7, 4.5, r'Example: $^{56}_{26}\mathrm{Fe}^{3+}$', fontsize=14, ha='center', fontweight='bold')
ax.text(7, 3.8, 'Protons = 26    |    Neutrons = 56−26 = 30    |    Electrons = 26−3 = 23',
        fontsize=12, ha='center',
        bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.6))
ax.text(7, 2.8, 'Never use the decimal below (e.g., 55.85 for Fe). Always use integers.',
        fontsize=10, ha='center', style='italic', color='gray')

plt.tight_layout()
plt.savefig(OUT + '01-subatomic-particles.png', dpi=180, bbox_inches='tight')
plt.close()
print("01 done")


# ================================================================
# 02: g↔mol Conversion Flowchart
# ================================================================
fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 14); ax.set_ylim(0, 10)
ax.axis('off')

ax.text(7, 9.3, 'Converting Between Grams and Moles', fontsize=16, ha='center', fontweight='bold')

# Left: g→mol
draw_box(ax, 3, 7.5, 3.0, 1.2, 'GRAMS (g)\n(from balance)', 'lightcoral', 12, True)
draw_arrow(ax, 3, 6.8, 3, 6.0)
draw_box(ax, 3, 5.3, 3.5, 1.0, '÷ molar mass\n(g/mol)', 'lightyellow', 11, True)
draw_arrow(ax, 3, 4.7, 3, 3.9)
draw_box(ax, 3, 3.2, 3.0, 1.2, 'MOLES (mol)\n(for reactions)', 'lightgreen', 12, True)

# Right: mol→g
draw_box(ax, 11, 7.5, 3.0, 1.2, 'MOLES (mol)\n(from equation)', 'lightgreen', 12, True)
draw_arrow(ax, 11, 6.8, 11, 6.0)
draw_box(ax, 11, 5.3, 3.5, 1.0, '× molar mass\n(g/mol)', 'lightyellow', 11, True)
draw_arrow(ax, 11, 4.7, 11, 3.9)
draw_box(ax, 11, 3.2, 3.0, 1.2, 'GRAMS (g)\n(to weigh out)', 'lightcoral', 12, True)

# Middle: Molar Mass box
draw_box(ax, 7, 5.8, 4.0, 1.5, 'MOLAR MASS\nSum of atomic masses\nfrom periodic table', 'lightblue', 11, True)
ax.plot([4.5, 5.2], [5.5, 5.8], 'gray', linewidth=1, alpha=0.5)
ax.plot([9.5, 9.0], [5.5, 5.8], 'gray', linewidth=1, alpha=0.5)

# Formula
ax.text(7, 1.5, r'$n = \frac{m}{M}$ (g → mol)          $m = n \times M$ (mol → g)', fontsize=13, ha='center',
        bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.7))

plt.tight_layout()
plt.savefig(OUT + '02-grams-moles.png', dpi=180, bbox_inches='tight')
plt.close()
print("02 done")


# ================================================================
# 03: Balancing Equations Visual
# ================================================================
fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 14); ax.set_ylim(0, 10)
ax.axis('off')

ax.text(7, 9.3, 'Balancing Chemical Equations — Method', fontsize=16, ha='center', fontweight='bold')

# Steps
steps = [
    (2.5, 7.5, '1. Pick most complex\nmolecule → coeff = 1', 'lightblue'),
    (7, 7.5, '2. Balance metals →\nnonmetals → H → O', 'lightgreen'),
    (11.5, 7.5, '3. If O₂ fraction,\nmultiply ALL by 2', 'lightcoral'),
]
for x, y, text, color in steps:
    draw_box(ax, x, y, 3.5, 1.4, text, color, 11, True)

# Arrows between steps
draw_arrow(ax, 4.25, 7.5, 5.25, 7.5)
draw_arrow(ax, 8.75, 7.5, 9.75, 7.5)

# Example
ax.text(7, 5.5, 'Example: C₂H₆ + O₂ → CO₂ + H₂O', fontsize=13, ha='center', fontweight='bold')

example_steps = [
    'C₂H₆ coeff=1 → C: need 2CO₂, H: need 3H₂O',
    'O: right=7 → O₂=3.5 (fraction!)',
    '×2: 2C₂H₆ + 7O₂ → 4CO₂ + 6H₂O  ✓',
]
for i, s in enumerate(example_steps):
    ax.text(7, 4.8 - i*0.6, s, fontsize=10, ha='center', style='italic')

# Warning
ax.text(7, 2.5, '⚠  Never change subscripts (H₂O → H₂O₂ is WRONG). Only change the big numbers in front.',
        fontsize=11, ha='center', color='darkred', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='mistyrose', alpha=0.6))

plt.tight_layout()
plt.savefig(OUT + '03-balancing-equations.png', dpi=180, bbox_inches='tight')
plt.close()
print("03 done")


# ================================================================
# 04: Mole Ratio Bridge
# ================================================================
fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 14); ax.set_ylim(0, 10)
ax.axis('off')

ax.text(7, 9.3, 'Mole Ratios from Balanced Coefficients', fontsize=16, ha='center', fontweight='bold')

# Equation display
ax.text(7, 8.2, r'$\mathbf{N_2 + 3H_2 \rightarrow 2NH_3}$', fontsize=16, ha='center')
ax.text(7, 7.6, 'Coefficients:  1   :   3   :   2', fontsize=12, ha='center', color='gray')

# Bridge diagram
draw_box(ax, 2.5, 6.0, 3.0, 1.0, 'Known\nsubstance\n(mol)', 'lightgreen', 11, True)
draw_box(ax, 7, 6.0, 2.5, 1.0, '×  coefficient you WANT\n÷  coefficient you KNOW', 'lightyellow', 10, True)
draw_box(ax, 11.5, 6.0, 3.0, 1.0, 'Unknown\nsubstance\n(mol)', 'lightcoral', 11, True)
draw_arrow(ax, 4.0, 6.0, 5.75, 6.0)
draw_arrow(ax, 8.25, 6.0, 10.0, 6.0)

# Examples
examples = [
    ('5.0 mol N₂ → NH₃', '5.0 × 2/1 = 10.0 mol NH₃'),
    ('9.0 mol H₂ → NH₃', '9.0 × 2/3 = 6.0 mol NH₃'),
    ('8.0 mol Fe → Fe₂O₃ (4Fe+3O₂→2Fe₂O₃)', '8.0 × 2/4 = 4.0 mol Fe₂O₃'),
]
ax.text(7, 4.2, 'Examples:', fontsize=12, ha='center', fontweight='bold')
for i, (question, answer) in enumerate(examples):
    ax.text(7, 3.6 - i*0.6, f'{question}  →  {answer}', fontsize=10, ha='center')

# Warning
ax.text(7, 1.5, '⚠  Numerator = what you WANT. Denominator = what you KNOW. Never flip.', fontsize=11, ha='center',
        color='darkred', bbox=dict(boxstyle='round', facecolor='mistyrose', alpha=0.6))

plt.tight_layout()
plt.savefig(OUT + '04-mole-ratios.png', dpi=180, bbox_inches='tight')
plt.close()
print("04 done")


# ================================================================
# 05: 3-Step Stoichiometry Flowchart
# ================================================================
fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 14); ax.set_ylim(0, 10)
ax.axis('off')

ax.text(7, 9.3, 'g → mol → mol → g : The Three-Step Stoichiometry Pipeline', fontsize=14, ha='center', fontweight='bold')

# Pipeline boxes
boxes_05 = [
    (2.2, 'g (known)', 'lightcoral'),
    (5.3, 'mol (known)', 'lightyellow'),
    (8.7, 'mol (target)', 'lightyellow'),
    (12, 'g (target)', 'lightgreen'),
]
step_labels_05 = ['Divide by\nmolar mass', 'Multiply by\ncoeff ratio', 'Multiply by\nmolar mass', 'WEIGH IT']

for i, (x_pos, label, color) in enumerate(boxes_05):
    draw_box(ax, x_pos, 7.0, 2.4, 1.2, label, color, 11, True)

for i in range(3):
    draw_arrow(ax, boxes_05[i][0]+1.2, 7.0, boxes_05[i+1][0]-1.2, 7.0)

for i, (x_pos, _, _) in enumerate(boxes_05):
    ax.text(x_pos, 5.5, step_labels_05[i], fontsize=9, ha='center', style='italic', color='gray')

# Example
ax.text(7, 3.8, 'Example: N₂ + 3H₂ → 2NH₃.  28.0 g N₂ → ? g NH₃  (N=14.0, H=1.0)',
        fontsize=11, ha='center', fontweight='bold')
steps_05 = [
    '① N₂ mol = 28.0 ÷ 28.0 = 1.00 mol',
    '② NH₃ mol = 1.00 × 2/1 = 2.00 mol',
    '③ NH₃ g = 2.00 × 17.0 = 34.0 g',
]
for i, s in enumerate(steps_05):
    ax.text(7, 3.1 - i*0.55, s, fontsize=10, ha='center')

plt.tight_layout()
plt.savefig(OUT + '05-grams-to-grams.png', dpi=180, bbox_inches='tight')
plt.close()
print("05 done")


# ================================================================
# 06: Limiting Reactant Comparison
# ================================================================
fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# Left: Limiting reactant method
ax = axes[0]
ax.set_xlim(0, 10); ax.set_ylim(0, 10)
ax.axis('off')
ax.text(5, 9.5, 'Finding the Limiting Reactant', fontsize=14, ha='center', fontweight='bold')

steps_06 = [
    (5, 8.2, '1. Convert each reactant: g → mol', 'lightblue'),
    (5, 7.0, '2. Divide each mol by its coefficient', 'lightyellow'),
    (5, 5.8, '3. Smaller quotient = RUNS OUT FIRST', 'lightcoral'),
    (5, 4.6, '4. Use that one to calculate product', 'lightgreen'),
]
for x, y, text, color in steps_06:
    draw_box(ax, x, y, 6, 0.7, text, color, 11, True)

ax.text(5, 3.2, 'Example: 2Al + 3Cl₂ → 2AlCl₃', fontsize=11, ha='center', fontweight='bold')
ax.text(5, 2.5, 'Al: 2.00÷2=1.00    Cl₂: 1.50÷3=0.500  →  Cl₂ LIMITS', fontsize=10, ha='center')

# Right: Percent yield
ax = axes[1]
ax.set_xlim(0, 10); ax.set_ylim(0, 10)
ax.axis('off')
ax.text(5, 9.5, 'Percent Yield', fontsize=14, ha='center', fontweight='bold')

draw_box(ax, 5, 8.0, 5, 0.8, 'Theoretical Yield (g) — from calculation', 'lightyellow', 11, True)
draw_box(ax, 5, 6.5, 5, 0.8, 'Actual Yield (g) — from lab measurement', 'lightblue', 11, True)
draw_box(ax, 5, 5.0, 5, 0.8, r'% Yield = (Actual ÷ Theoretical) × 100', 'lightgreen', 12, True)

ax.text(5, 3.5, 'Example: Theoretical = 78.0 g', fontsize=11, ha='center')
ax.text(5, 2.9, 'Actual = 62.4 g  →  (62.4÷78.0)×100 = 80.0%', fontsize=11, ha='center', fontweight='bold')

ax.text(5, 1.8, 'Reasons <100%: incomplete reaction, side products,\nproduct lost during transfer, measurement errors.',
        fontsize=9, ha='center', style='italic', color='gray')

fig.suptitle('Graph 06: Limiting Reactant & Percent Yield', fontsize=15, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig(OUT + '06-limiting-reactant.png', dpi=180, bbox_inches='tight')
plt.close()
print("06 done")


# ================================================================
# 07: Empirical Formula + Combustion Analysis
# ================================================================
fig, axes = plt.subplots(1, 2, figsize=(16, 7.5))

# Left: Empirical formula method
ax = axes[0]
ax.set_xlim(0, 10); ax.set_ylim(0, 10)
ax.axis('off')
ax.text(5, 9.5, 'Empirical Formula — 3 Steps', fontsize=13, ha='center', fontweight='bold')

steps_07a = [
    (5, 8.3, '1. Each element: g ÷ atomic mass → mol', 'lightblue'),
    (5, 7.2, '2. Divide all mol by the SMALLEST mol', 'lightyellow'),
    (5, 6.1, '3. Multiply by 2,3,... until all integers', 'lightgreen'),
]
for x, y, text, color in steps_07a:
    draw_box(ax, x, y, 6.5, 0.65, text, color, 11, True)

ax.text(5, 4.8, 'Example: C 40.0%, H 6.7%, O 53.3%', fontsize=10, ha='center', fontweight='bold')
ax.text(5, 4.2, 'C: 40÷12=3.33  H: 6.7÷1=6.7  O: 53.3÷16=3.33', fontsize=10, ha='center')
ax.text(5, 3.7, '÷3.33: C=1, H=2, O=1  →  CH₂O', fontsize=10, ha='center', fontweight='bold')

ax.text(5, 2.8, 'Molecular Formula:', fontsize=11, ha='center', fontweight='bold')
ax.text(5, 2.2, 'n = Molar mass ÷ Empirical mass', fontsize=10, ha='center')

# Right: Combustion analysis
ax = axes[1]
ax.set_xlim(0, 10); ax.set_ylim(0, 10)
ax.axis('off')
ax.text(5, 9.5, 'Combustion Analysis', fontsize=13, ha='center', fontweight='bold')

draw_box(ax, 2.5, 8.0, 3.5, 1.0, 'Burn sample\nCₓHᵧO₂', 'lightcoral', 11, True)
draw_arrow(ax, 4.25, 8.0, 6.0, 8.0)
draw_box(ax, 7.5, 8.5, 3.0, 0.9, 'CO₂ captured\n→ C mass', 'lightblue', 10, True)
draw_box(ax, 7.5, 7.2, 3.0, 0.9, 'H₂O captured\n→ H mass', 'lightblue', 10, True)

draw_box(ax, 5, 5.7, 5, 0.9, 'O mass = sample mass − C mass − H mass', 'lightyellow', 11, True)
draw_box(ax, 5, 4.5, 5, 0.8, 'Then: g→mol → ÷smallest → empirical formula', 'lightgreen', 11, True)

ax.text(5, 3.2, 'Key: 1 CO₂ molecule → 1 C atom', fontsize=10, ha='center')
ax.text(5, 2.6, '1 H₂O molecule → 2 H atoms', fontsize=10, ha='center', fontweight='bold', color='darkred')

fig.suptitle('Graph 07: Empirical Formula & Combustion Analysis', fontsize=14, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig(OUT + '07-empirical-formula.png', dpi=180, bbox_inches='tight')
plt.close()
print("07 done")

print("\n=== ALL 7 CHEMISTRY GRAPHS DONE ===")
