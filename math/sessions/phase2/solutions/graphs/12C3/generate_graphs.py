#!/usr/bin/env python3
"""12C3 Coordinate Systems and Optimization — visual solution graphs."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
from mpl_toolkits.mplot3d import Axes3D, art3d
from matplotlib.patches import Circle, Polygon, FancyArrowPatch

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUTPUT_DIR, exist_ok=True)
plt.rcParams.update({'figure.dpi': 150, 'savefig.dpi': 150, 'font.size': 11})

def save(fig, name):
    fig.savefig(f'{OUTPUT_DIR}/{name}', bbox_inches='tight', facecolor='white', pad_inches=0.15)
    plt.close(fig)

# ── P1: Hyperbola x^2 - y^2 = 1 in polar ───────────────────────
def p1():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    x = np.linspace(-3, 3, 400)
    yp = np.sqrt(np.maximum(x**2 - 1, 0))

    ax = axes[0]
    ax.plot(x, yp, '-', color='#E74C3C', lw=2.5)
    ax.plot(x, -yp, '-', color='#E74C3C', lw=2.5)
    ax.plot(x, x, '--', color='gray', lw=1, alpha=0.4)
    ax.plot(x, -x, '--', color='gray', lw=1, alpha=0.4)
    ax.set_xlim(-3,3); ax.set_ylim(-3,3)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.15)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.set_title('Cartesian: x^2 - y^2 = 1', fontweight='bold')

    ax = axes[1]
    th = np.linspace(0.01, np.pi-0.01, 500)
    r2 = 1/np.cos(2*th); r2 = np.ma.masked_where(r2 < 0, r2); r = np.sqrt(r2)
    ax.plot(r*np.cos(th), r*np.sin(th), '-', color='#3498DB', lw=2.5)
    ax.plot(-r*np.cos(th), -r*np.sin(th), '-', color='#3498DB', lw=2.5)
    ax.set_xlim(-3,3); ax.set_ylim(-3,3)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.15)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.set_title('Polar: r^2 cos(2theta) = 1', fontweight='bold')

    fig.suptitle('P1: Hyperbola in polar coordinates', fontweight='bold', fontsize=13)
    plt.tight_layout(); save(fig, 'p1-hyperbola.png')

# ── P2: Line-plane intersection ────────────────────────────────
def p2():
    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection='3d')
    xx, yy = np.meshgrid(np.linspace(0,5,10), np.linspace(0,5,10))
    ax.plot_wireframe(xx, yy, (10-3*xx-yy)/2, color='#3498DB', alpha=0.25, rstride=1, cstride=1)
    t = np.linspace(-1, 3, 100)
    ax.plot(2+t, 1-t, t, '-', color='#E74C3C', lw=3)
    ti = 0.75
    ax.scatter([2+ti],[1-ti],[ti], color='#27AE60', s=200, zorder=10)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title('P2: Line-plane intersection at (2.75,0.25,0.75)', fontweight='bold')
    plt.tight_layout(); save(fig, 'p2-line-plane.png')

# ── P3: Point-line distance ────────────────────────────────────
def p3():
    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection='3d')
    t = np.linspace(-1, 4, 100)
    ax.plot(t, t, t, '-', color='#3498DB', lw=3)
    p = np.array([1,2,3])
    ax.scatter(*p, color='#E74C3C', s=150, zorder=10)
    d = np.array([1,1,1])
    proj_t = np.dot(p, d) / np.dot(d, d)
    foot = proj_t * d
    ax.scatter(*foot, color='#27AE60', s=120, zorder=10)
    ax.plot([p[0],foot[0]],[p[1],foot[1]],[p[2],foot[2]], '--', color='#E74C3C', lw=2.5)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title('P3: Distance from (1,2,3) to line = sqrt(2)', fontweight='bold')
    plt.tight_layout(); save(fig, 'p3-point-line.png')

# ── P4: Closest point on sphere ────────────────────────────────
def p4():
    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection='3d')
    u = np.linspace(0, 2*np.pi, 18); v = np.linspace(0, np.pi, 13)
    R = 5
    ax.plot_wireframe(R*np.outer(np.cos(u), np.sin(v)), R*np.outer(np.sin(u), np.sin(v)),
                      R*np.outer(np.ones(np.size(u)), np.cos(v)), color='#3498DB', alpha=0.12, rstride=1, cstride=1)
    ax.scatter([10],[0],[0], color='#E74C3C', s=150, zorder=10)
    ax.scatter([5],[0],[0], color='#27AE60', s=150, zorder=10)
    ax.plot([5,10],[0,0],[0,0], '--', color='#E74C3C', lw=2.5)
    ax.set_xlim(-2,12); ax.set_ylim(-6,6); ax.set_zlim(-6,6)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title('P4: Closest point on sphere to (10,0,0) = (5,0,0)', fontweight='bold')
    plt.tight_layout(); save(fig, 'p4-sphere-closest.png')

# ── P5: Barycentric coordinates ────────────────────────────────
def p5():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    A, B, C = np.array([0,0]), np.array([4,0]), np.array([0,3])
    tri = np.array([A,B,C,A])
    P = 0.5*A + 0.3*B + 0.2*C

    ax = axes[0]
    ax.fill(tri[:,0], tri[:,1], color='#3498DB', alpha=0.08, ec='#2980B9', lw=2)
    # Sub-triangles
    for pts, col in [(np.array([P,B,C,P]), '#E74C3C'),
                     (np.array([A,P,C,A]), '#27AE60'),
                     (np.array([A,B,P,A]), '#F39C12')]:
        ax.fill(pts[:,0], pts[:,1], color=col, alpha=0.15)
    ax.plot(P[0], P[1], 'o', color='#E74C3C', markersize=14, zorder=10)
    ax.set_xlim(-0.5,5); ax.set_ylim(-0.5,4)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.15)
    ax.set_title('Barycentric: P = (1.2, 0.6)', fontweight='bold')

    ax = axes[1]; ax.axis('off')
    ax.text(0.5, 0.5,
            'P = a A + b B + c C  where a+b+c=1\n\n'
            'Given (a,b,c) = (0.5, 0.3, 0.2):\n\n'
            'P = 0.5(0,0) + 0.3(4,0) + 0.2(0,3)\n'
            '  = (0 + 1.2 + 0, 0 + 0 + 0.6)\n'
            '  = (1.2, 0.6)',
            ha='center', va='center', fontsize=12, transform=ax.transAxes,
            bbox=dict(boxstyle='round', facecolor='#D5F5E3', alpha=0.8))
    ax.set_title('Barycentric formula', fontweight='bold')

    fig.suptitle('P5: Barycentric coordinates', fontweight='bold', fontsize=13)
    plt.tight_layout(); save(fig, 'p5-barycentric.png')

# ── P6: Convex hull ────────────────────────────────────────────
def p6():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    pts = np.array([[0,0],[3,0],[3,2],[1,1]])

    ax = axes[0]
    ax.plot(pts[:,0], pts[:,1], 'o', color='#3498DB', markersize=12, zorder=10)
    hull = np.array([pts[0],pts[1],pts[2],pts[3],pts[0]])
    ax.fill(hull[:,0], hull[:,1], color='#27AE60', alpha=0.15, ec='#27AE60', lw=2.5)
    tp = np.array([2, 0.5])
    ax.plot(tp[0], tp[1], 'o', color='#E74C3C', markersize=14, zorder=11)
    ax.set_xlim(-0.5,4); ax.set_ylim(-0.5,3)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.15)
    ax.set_title('Convex hull (4 vertices)', fontweight='bold')

    ax = axes[1]; ax.axis('off')
    ax.text(0.5, 0.5,
            'Hull: (0,0), (3,0), (3,2), (1,1)\n\n'
            'Is (2,0.5) inside?\n'
            '  Edge (0,0)->(3,0): above -> OK\n'
            '  Edge (3,0)->(3,2): left -> OK\n'
            '  Edge (3,2)->(1,1): inside -> OK\n'
            '  Edge (1,1)->(0,0): inside -> OK\n\n'
            'All agree: (2,0.5) is INSIDE',
            ha='center', va='center', fontsize=11, transform=ax.transAxes,
            bbox=dict(boxstyle='round', facecolor='#D5F5E3', alpha=0.8))
    ax.set_title('Inside/outside test', fontweight='bold')

    fig.suptitle('P6: Convex hull', fontweight='bold', fontsize=13)
    plt.tight_layout(); save(fig, 'p6-convex-hull.png')

# ── P7: Skew lines ─────────────────────────────────────────────
def p7():
    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection='3d')
    t = np.linspace(-1, 3, 100)
    ax.plot(1+2*t, t, np.zeros_like(t), '-', color='#3498DB', lw=3)
    s = np.linspace(-1, 3, 100)
    ax.plot(np.zeros_like(s), 1+2*s, 1+s, '-', color='#E74C3C', lw=3)
    # Connect closest points approximately
    ax.plot([1, 0], [0, 1], [0, 1], '--', color='#F39C12', lw=2.5)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title('P7: Skew lines distance = 1/sqrt(21)', fontweight='bold')
    plt.tight_layout(); save(fig, 'p7-skew-lines.png')

# ── P8: Lagrange multipliers ───────────────────────────────────
def p8():
    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection='3d')
    xx, yy = np.meshgrid(np.linspace(-2, 8, 12), np.linspace(-2, 8, 12))
    ax.plot_wireframe(xx, yy, (9-xx-2*yy)/2, color='#3498DB', alpha=0.25, rstride=1, cstride=1)
    ax.scatter([1],[2],[2], color='#E74C3C', s=200, zorder=10)
    ax.scatter([0],[0],[0], color='#333', s=80, zorder=10)
    ax.plot([0,1],[0,2],[0,2], '--', color='#E74C3C', lw=2.5)
    # Tangent sphere
    u = np.linspace(0, 2*np.pi, 12); v = np.linspace(0, np.pi, 10)
    R = 3
    ax.plot_wireframe(1+R*np.outer(np.cos(u), np.sin(v)), 2+R*np.outer(np.sin(u), np.sin(v)),
                      2+R*np.outer(np.ones(np.size(u)), np.cos(v)), color='#27AE60', alpha=0.06, rstride=1, cstride=1)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title('P8: Closest point on plane x+2y+2z=9 = (1,2,2)', fontweight='bold')
    plt.tight_layout(); save(fig, 'p8-lagrange.png')

# ── P9: Polar r=2cos(theta) -> circle ──────────────────────────
def p9():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    ax = axes[0]
    th = np.linspace(-np.pi/2, np.pi/2, 200)
    r = 2*np.cos(th)
    ax.plot(r*np.cos(th), r*np.sin(th), '-', color='#E74C3C', lw=2.5)
    for rad in [0.5, 1, 1.5, 2]:
        ax.add_patch(Circle((0,0), rad, fill=False, color='gray', lw=0.4, alpha=0.3))
    for ang in np.linspace(0, 2*np.pi, 12):
        ax.plot([0, 2.5*np.cos(ang)], [0, 2.5*np.sin(ang)], '-', color='gray', lw=0.2, alpha=0.3)
    ax.set_xlim(-1, 3); ax.set_ylim(-2, 2)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.15)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.set_title('Polar: r = 2 cos(theta)', fontweight='bold')

    ax = axes[1]
    ax.add_patch(Circle((1,0), 1, fill=True, color='#3498DB', alpha=0.2, ec='#2980B9', lw=2.5))
    ax.plot(1, 0, 'o', color='#2980B9', markersize=8, zorder=10)
    ax.set_xlim(-0.5, 3); ax.set_ylim(-2, 2)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.15)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.set_title('Cartesian: (x-1)^2 + y^2 = 1', fontweight='bold')

    fig.suptitle('P9: r=2cos(theta) is a circle', fontweight='bold', fontsize=13)
    plt.tight_layout(); save(fig, 'p9-polar-circle.png')

if __name__ == '__main__':
    for name, fn in [('P1',p1),('P2',p2),('P3',p3),('P4',p4),('P5',p5),
                     ('P6',p6),('P7',p7),('P8',p8),('P9',p9)]:
        fn(); print(f'  12C3 {name} OK')
