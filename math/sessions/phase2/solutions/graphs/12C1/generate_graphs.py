#!/usr/bin/env python3
"""12C1 Geometric Transformations — visual solution graphs."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
from mpl_toolkits.mplot3d import Axes3D

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUTPUT_DIR, exist_ok=True)
plt.rcParams.update({'figure.dpi': 150, 'savefig.dpi': 150, 'font.size': 11})

def save(fig, name):
    fig.savefig(f'{OUTPUT_DIR}/{name}', bbox_inches='tight', facecolor='white', pad_inches=0.15)
    plt.close(fig)

# ── P1: Scale then rotate 45° ──────────────────────────────────
def p1():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    sq = np.array([[0,0],[1,0],[1,1],[0,1],[0,0]])
    S = np.array([[2,0],[0,3]])
    c = np.cos(np.pi/4); s = np.sin(np.pi/4)
    M = np.array([[c,-s],[s,c]]) @ S
    tsq = np.array([M @ v for v in sq])

    for ax in axes:
        ax.fill(sq[:,0], sq[:,1], color='gray', alpha=0.15, ec='gray', lw=1)
        ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
        ax.set_aspect('equal'); ax.grid(True, alpha=0.15)

    ax = axes[0]
    sc = np.array([S @ v for v in sq])
    ax.fill(sc[:,0], sc[:,1], color='#3498DB', alpha=0.3, ec='#2980B9', lw=2)
    ax.arrow(0,0,2,0, head_width=0.15, head_length=0.15, fc='#E74C3C', ec='#E74C3C', lw=2.5)
    ax.arrow(0,0,0,3, head_width=0.15, head_length=0.15, fc='#27AE60', ec='#27AE60', lw=2.5)
    ax.set_xlim(-1,5); ax.set_ylim(-1,5)
    ax.set_title('Scale x2 y3', fontweight='bold')

    ax = axes[1]
    ax.fill(tsq[:,0], tsq[:,1], color='#E74C3C', alpha=0.3, ec='#C0392B', lw=2)
    ax.arrow(0,0, M[0,0], M[1,0], head_width=0.15, head_length=0.15, fc='#C0392B', ec='#C0392B', lw=2.5)
    ax.arrow(0,0, M[0,1], M[1,1], head_width=0.15, head_length=0.15, fc='#8E44AD', ec='#8E44AD', lw=2.5)
    ax.set_xlim(-3,5); ax.set_ylim(-2,5)
    ax.set_title('Then rotate 45 deg CCW', fontweight='bold')

    fig.suptitle('P1: Scale then Rotate', fontweight='bold', fontsize=13)
    plt.tight_layout(); save(fig, 'p1-scale-rotate.png')

# ── P2: Rotation 90 deg about (1,2) ────────────────────────────
def p2():
    fig, ax = plt.subplots(figsize=(7, 7))
    c = np.array([1,2])
    pts = np.array([[1,2],[2,2],[1,3],[0,2],[2,3],[0,3],[2,1],[0,1]])
    def rot(p): return np.array([-p[1]+3, p[0]+1])

    th = np.linspace(0, np.pi/2, 100)
    for p in pts:
        if not np.all(p == c):
            r = np.linalg.norm(p-c); a0 = np.arctan2(p[1]-c[1], p[0]-c[0])
            ax.plot(c[0]+r*np.cos(a0+th), c[1]+r*np.sin(a0+th), '-', color='gray', lw=0.5, alpha=0.3)

    ax.plot(c[0], c[1], 'o', color='#27AE60', markersize=16, zorder=10)
    ax.plot(pts[:,0], pts[:,1], 'o', color='#3498DB', markersize=8, zorder=5)
    rp = np.array([rot(p) for p in pts])
    ax.plot(rp[:,0], rp[:,1], 'o', color='#E74C3C', markersize=8, zorder=5)

    ax.set_xlim(-1,5); ax.set_ylim(-1,5)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.15)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.set_title('P2: 90 deg rotation about (1,2)', fontweight='bold')
    plt.tight_layout(); save(fig, 'p2-rotation-about.png')

# ── P3: Eigenvectors of [[4,1],[2,3]] ──────────────────────────
def p3():
    fig, ax = plt.subplots(figsize=(7, 7))
    A = np.array([[4,1],[2,3]])

    th = np.linspace(0, 2*np.pi, 200)
    c = np.array([np.cos(th), np.sin(th)])
    e = A @ c
    ax.plot(c[0], c[1], '--', color='gray', lw=1, alpha=0.4)
    ax.plot(e[0], e[1], '-', color='#3498DB', lw=2)

    # eigenvectors
    for val, vec, col in [(2, np.array([1,-2]), '#E74C3C'), (5, np.array([1,1]), '#27AE60')]:
        v = vec / np.linalg.norm(vec) * 3
        av = A @ v
        ax.arrow(0,0,v[0],v[1], head_width=0.15, head_length=0.15, fc=col, ec=col, lw=2.5)
        ax.arrow(0,0,av[0],av[1], head_width=0.15, head_length=0.15, fc=col, ec=col, lw=1.5, ls=':')

    ax.set_xlim(-4,4); ax.set_ylim(-4,4)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.15)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.set_title('P3: Eigenvectors (l=2 along [1,-2], l=5 along [1,1])', fontweight='bold')
    plt.tight_layout(); save(fig, 'p3-eigenvectors.png')

# ── P4: Rotation eigenvectors (no real ones) ───────────────────
def p4():
    fig, ax = plt.subplots(figsize=(7, 7))
    th = np.linspace(0, 2*np.pi, 100)
    ax.plot(np.cos(th), np.sin(th), '--', color='gray', lw=1, alpha=0.4)

    angs = np.linspace(0, np.pi*15/16, 8)
    for a, col in zip(angs, plt.cm.rainbow(np.linspace(0,1,len(angs)))):
        v = np.array([np.cos(a), np.sin(a)])
        rv = np.array([-np.sin(a), np.cos(a)])
        ax.arrow(0,0,v[0],v[1], head_width=0.06, head_length=0.06, fc=col, ec=col, lw=2, alpha=0.7)
        ax.arrow(0,0,rv[0],rv[1], head_width=0.06, head_length=0.06, fc=col, ec=col, lw=2, alpha=0.4, ls=':')

    ax.set_xlim(-1.5,1.5); ax.set_ylim(-1.5,1.5)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.15)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.set_title('P4: Pure rotation - no vector keeps direction', fontweight='bold')
    plt.tight_layout(); save(fig, 'p4-rotation-eigen.png')

# ── P5: SVD sigma1=5 sigma2=2 ──────────────────────────────────
def p5():
    fig, ax = plt.subplots(figsize=(7, 7))
    th = np.linspace(0, 2*np.pi, 200)
    c = np.array([np.cos(th), np.sin(th)])
    e = np.array([5*np.cos(th), 2*np.sin(th)])
    ax.plot(c[0], c[1], '--', color='gray', lw=1, alpha=0.4)
    ax.plot(e[0], e[1], '-', color='#E74C3C', lw=2.5)
    ax.arrow(0,0,5,0, head_width=0.2, head_length=0.2, fc='#3498DB', ec='#3498DB', lw=2.5)
    ax.arrow(0,0,0,2, head_width=0.2, head_length=0.2, fc='#27AE60', ec='#27AE60', lw=2.5)
    ax.set_xlim(-6,6); ax.set_ylim(-4,4)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.15)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.set_title('P5: SVD - unit circle -> ellipse (s1=5, s2=2, |det|=10)', fontweight='bold')
    plt.tight_layout(); save(fig, 'p5-svd.png')

# ── P6: Reflect across y=2x then translate ─────────────────────
def p6():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    x = np.linspace(-2, 5, 100)
    F = np.array([[-3/5, 4/5],[4/5, 3/5]])
    T = np.array([3, -1])

    ax = axes[0]
    ax.plot(x, 2*x, '-', color='#27AE60', lw=2.5)
    p = np.array([1,1])
    pr = F @ p
    ax.arrow(0,0,p[0],p[1], head_width=0.1, head_length=0.1, fc='#3498DB', ec='#3498DB', lw=2.5)
    ax.arrow(0,0,pr[0],pr[1], head_width=0.1, head_length=0.1, fc='#E74C3C', ec='#E74C3C', lw=2.5)
    # projection
    u = np.array([1,2])/np.sqrt(5)
    proj = np.dot(p, u) * u
    ax.plot([p[0],proj[0]],[p[1],proj[1]], ':', color='gray', lw=1.5)
    ax.plot([proj[0],pr[0]],[proj[1],pr[1]], ':', color='gray', lw=1.5)
    ax.set_xlim(-2,5); ax.set_ylim(-2,5)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.15)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.set_title('Reflect across y=2x', fontweight='bold')

    ax = axes[1]
    pf = pr + T
    ax.plot(x, 2*x, '-', color='#27AE60', lw=1.5, alpha=0.4)
    ax.plot(p[0], p[1], 'o', color='#3498DB', markersize=12, zorder=5)
    ax.plot(pf[0], pf[1], 'o', color='#E74C3C', markersize=12, zorder=5)
    ax.annotate('', xy=pf, xytext=pr, arrowprops=dict(arrowstyle='->', color='#F39C12', lw=2.5))
    ax.set_xlim(-2,6); ax.set_ylim(-2,5)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.15)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.set_title('Then translate by (3,-1)', fontweight='bold')

    fig.suptitle('P6: Reflection + Translation', fontweight='bold', fontsize=13)
    plt.tight_layout(); save(fig, 'p6-reflection.png')

# ── P7: 3D rotations ───────────────────────────────────────────
def p7():
    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection='3d')
    p = np.array([1,2,3])
    Rz = np.array([[0,-1,0],[1,0,0],[0,0,1]])
    Rx = np.array([[1,0,0],[0,0,-1],[0,1,0]])
    p1 = Rz @ p; p2 = Rx @ p1
    for pt, col, lbl in [(p,'#3498DB','(1,2,3)'),(p1,'#F39C12','after Rz'),(p2,'#E74C3C','final')]:
        ax.scatter(*pt, color=col, s=150, zorder=10)
    ax.plot([p[0],p1[0]],[p[1],p1[1]],[p[2],p1[2]], ':', color='#F39C12', lw=2)
    ax.plot([p1[0],p2[0]],[p1[1],p2[1]],[p1[2],p2[2]], ':', color='#E74C3C', lw=2)
    ax.quiver(0,0,0,4,0,0, color='red', alpha=0.3, arrow_length_ratio=0.05)
    ax.quiver(0,0,0,0,4,0, color='green', alpha=0.3, arrow_length_ratio=0.05)
    ax.quiver(0,0,0,0,0,4, color='blue', alpha=0.3, arrow_length_ratio=0.05)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title('P7: Rz(90) then Rx(90) on (1,2,3)', fontweight='bold')
    plt.tight_layout(); save(fig, 'p7-3d-rotation.png')

# ── P8: Reflection across 3x+4y=10 ─────────────────────────────
def p8():
    fig, ax = plt.subplots(figsize=(7.5, 7))
    x = np.linspace(-2, 6, 100)
    ax.plot(x, (10-3*x)/4, '-', color='#27AE60', lw=2.5)
    F = np.array([[7/25,-24/25],[-24/25,-7/25]])
    p = np.array([2,1]); pr = F @ p
    ax.plot(p[0],p[1],'o', color='#3498DB', markersize=14, zorder=10)
    ax.plot(pr[0],pr[1],'o', color='#E74C3C', markersize=14, zorder=10)
    ax.plot([p[0],pr[0]],[p[1],pr[1]], '--', color='#8E44AD', lw=2)
    n = np.array([3,4])/5
    foot = p + ((10-3*p[0]-4*p[1])/5) * n
    ax.plot(foot[0],foot[1],'o', color='#F39C12', markersize=8, zorder=10)
    ax.plot([p[0],foot[0]],[p[1],foot[1]], ':', color='gray', lw=1.5)
    ax.plot([foot[0],pr[0]],[foot[1],pr[1]], ':', color='gray', lw=1.5)
    ax.set_xlim(-3,6); ax.set_ylim(-4,5)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.15)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.set_title('P8: Reflect (2,1) across line 3x+4y=10', fontweight='bold')
    plt.tight_layout(); save(fig, 'p8-reflection-line.png')

# ── P9: Ellipse SVD ────────────────────────────────────────────
def p9():
    fig, ax = plt.subplots(figsize=(7, 7))
    th = np.linspace(0, 2*np.pi, 200)
    c = np.array([np.cos(th), np.sin(th)])
    e = np.array([5*np.cos(th), 3*np.sin(th)])
    ax.plot(c[0], c[1], '--', color='gray', lw=1.5, alpha=0.4)
    ax.plot(e[0], e[1], '-', color='#E74C3C', lw=2.5)
    ax.arrow(0,0,5,0, head_width=0.2, head_length=0.2, fc='#3498DB', ec='#3498DB', lw=2.5)
    ax.arrow(0,0,0,3, head_width=0.2, head_length=0.2, fc='#27AE60', ec='#27AE60', lw=2.5)
    ax.set_xlim(-6,6); ax.set_ylim(-4,4)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.15)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.set_title('P9: Ellipse x^2/25 + y^2/9 = 1 (SVD: s1=5,s2=3,|det|=15)', fontweight='bold')
    plt.tight_layout(); save(fig, 'p9-ellipse-svd.png')

if __name__ == '__main__':
    for name, fn in [('P1',p1),('P2',p2),('P3',p3),('P4',p4),('P5',p5),
                     ('P6',p6),('P7',p7),('P8',p8),('P9',p9)]:
        fn(); print(f'  12C1 {name} OK')
