#!/usr/bin/env python3
"""12C2 Parametric Curves and Surfaces — visual solution graphs."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
from mpl_toolkits.mplot3d import Axes3D, art3d
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUTPUT_DIR, exist_ok=True)
plt.rcParams.update({'figure.dpi': 150, 'savefig.dpi': 150, 'font.size': 11})

def save(fig, name):
    fig.savefig(f'{OUTPUT_DIR}/{name}', bbox_inches='tight', facecolor='white', pad_inches=0.15)
    plt.close(fig)

# ── P1: Line segment in 3D ─────────────────────────────────────
def p1():
    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection='3d')
    t = np.linspace(0, 1, 100)
    ax.plot(3+4*t, -1+3*t, 4+6*t, color='#E74C3C', lw=3)
    ax.scatter([3],[ -1],[4], color='#3498DB', s=150, zorder=10)
    ax.scatter([7],[2],[10], color='#27AE60', s=150, zorder=10)
    ax.quiver(3,-1,4,4,3,6, color='#8E44AD', lw=2, alpha=0.4, arrow_length_ratio=0.08)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title('P1: 3D line segment', fontweight='bold')
    plt.tight_layout(); save(fig, 'p1-line-3d.png')

# ── P2: Ellipse ────────────────────────────────────────────────
def p2():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    t = np.linspace(0, 2*np.pi, 200)
    x, y = 5*np.cos(t), 3*np.sin(t)

    ax = axes[0]
    ax.plot(x, y, '-', color='#E74C3C', lw=2.5)
    for tm in np.linspace(0, 2*np.pi, 12):
        ax.plot([0,5*np.cos(tm)],[0,3*np.sin(tm)], ':', color='gray', lw=0.6, alpha=0.3)
    ax.arrow(0,0,5,0, head_width=0.15, head_length=0.15, fc='#2980B9', ec='#2980B9', lw=2)
    ax.arrow(0,0,0,3, head_width=0.15, head_length=0.15, fc='#27AE60', ec='#27AE60', lw=2)
    ax.set_xlim(-6,6); ax.set_ylim(-4,4)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.15)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.set_title('Ellipse: semi-axes a=5, b=3', fontweight='bold')

    ax = axes[1]; ax.axis('off')
    ax.text(0.5, 0.5,
            'Parametric:\n  r(t) = (5 cos t, 3 sin t)\n\n'
            'Verify: x^2/25 + y^2/9\n'
            '  = cos^2 t + sin^2 t = 1',
            ha='center', va='center', fontsize=13, transform=ax.transAxes,
            bbox=dict(boxstyle='round', facecolor='#D5F5E3', alpha=0.8))
    ax.set_title('Verification', fontweight='bold')

    fig.suptitle('P2: Ellipse Parametrization', fontweight='bold', fontsize=13)
    plt.tight_layout(); save(fig, 'p2-ellipse.png')

# ── P3: Helix ──────────────────────────────────────────────────
def p3():
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    t = np.linspace(0, 4*np.pi, 500)
    ax.plot(2*np.cos(t), 2*np.sin(t), 3*t, color='#3498DB', lw=2)
    ax.plot(2*np.cos(t), 2*np.sin(t), np.zeros_like(t), '--', color='gray', lw=1, alpha=0.4)
    ax.scatter([2],[0],[0], color='#E74C3C', s=80, zorder=10)
    ax.scatter([2],[0],[12*np.pi], color='#E74C3C', s=80, zorder=10)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title('P3: Helix (speed=sqrt(13), L=4pi sqrt(13))', fontweight='bold')
    plt.tight_layout(); save(fig, 'p3-helix.png')

# ── P4: Bezier curve ───────────────────────────────────────────
def p4():
    fig, ax = plt.subplots(figsize=(8, 7))
    P = np.array([[0,0],[1,3],[4,3],[5,0]])
    t = np.linspace(0, 1, 200)
    b = np.array([(1-t)**3, 3*(1-t)**2*t, 3*(1-t)*t**2, t**3]).T @ P
    ax.plot(b[:,0], b[:,1], '-', color='#E74C3C', lw=3, zorder=5)
    ax.plot(P[:,0], P[:,1], 'o--', color='#3498DB', lw=2, markersize=12, markerfacecolor='white', markeredgewidth=2, zorder=10)
    # t=0.5 point
    t05 = 0.5
    b05 = np.array([(1-t05)**3, 3*(1-t05)**2*t05, 3*(1-t05)*t05**2, t05**3]) @ P
    ax.plot(b05[0], b05[1], 'o', color='#F39C12', markersize=16, zorder=15)
    ax.set_xlim(-0.5,6); ax.set_ylim(-1,4)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.15)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.set_title('P4: Cubic Bezier (t=0.5 at (2.5,2.25))', fontweight='bold')
    plt.tight_layout(); save(fig, 'p4-bezier.png')

# ── P5: Sphere normal ──────────────────────────────────────────
def p5():
    fig = plt.figure(figsize=(9, 8))
    ax = fig.add_subplot(111, projection='3d')
    u = np.linspace(0, 2*np.pi, 18); v = np.linspace(0, np.pi, 13)
    R = 1
    ax.plot_wireframe(R*np.outer(np.cos(u), np.sin(v)), R*np.outer(np.sin(u), np.sin(v)),
                      R*np.outer(np.ones(np.size(u)), np.cos(v)), color='gray', alpha=0.15, rstride=1, cstride=1)
    th, ph = np.pi/4, np.pi/3
    px = R*np.sin(ph)*np.cos(th); py = R*np.sin(ph)*np.sin(th); pz = R*np.cos(ph)
    ax.scatter([px],[py],[pz], color='#E74C3C', s=150, zorder=10)
    sc = 0.5
    rt = np.array([-np.sin(ph)*np.sin(th), np.sin(ph)*np.cos(th), 0])
    rp = np.array([np.cos(ph)*np.cos(th), np.cos(ph)*np.sin(th), -np.sin(ph)])
    ax.quiver(px,py,pz, rt[0]*sc, rt[1]*sc, rt[2]*sc, color='#3498DB', lw=2.5, arrow_length_ratio=0.2)
    ax.quiver(px,py,pz, rp[0]*sc, rp[1]*sc, rp[2]*sc, color='#27AE60', lw=2.5, arrow_length_ratio=0.2)
    ax.quiver(px,py,pz, px*sc, py*sc, pz*sc, color='#E74C3C', lw=3, arrow_length_ratio=0.2)
    ax.set_xlim(-1.2,1.2); ax.set_ylim(-1.2,1.2); ax.set_zlim(-1.2,1.2)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title('P5: Surface normal on sphere', fontweight='bold')
    plt.tight_layout(); save(fig, 'p5-sphere-normal.png')

# ── P6: Conical spiral ─────────────────────────────────────────
def p6():
    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection='3d')
    t = np.linspace(0, 4*np.pi, 500)
    ax.plot(t*np.cos(t), t*np.sin(t), t, color='#E74C3C', lw=2)
    th = np.linspace(0, 2*np.pi, 24)
    T, TH = np.meshgrid(np.linspace(0, 4*np.pi, 12), th)
    ax.plot_wireframe(T*np.cos(TH), T*np.sin(TH), T, color='gray', alpha=0.06, rstride=1, cstride=2)
    ax.plot(t*np.cos(t), t*np.sin(t), np.zeros_like(t), '--', color='#3498DB', lw=1.5, alpha=0.5)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title('P6: Conical spiral', fontweight='bold')
    plt.tight_layout(); save(fig, 'p6-conical-spiral.png')

# ── P7: Cycloid ────────────────────────────────────────────────
def p7():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    t = np.linspace(0, 2*np.pi, 300)
    x = t - np.sin(t); y = 1 - np.cos(t)

    ax = axes[0]
    ax.plot(x, y, '-', color='#3498DB', lw=2.5)
    for tv, col in [(0,'#E74C3C'), (np.pi/2,'#27AE60'), (np.pi,'#F39C12')]:
        circle = plt.Circle((tv, 1), 1, fill=False, color=col, lw=1.5, alpha=0.5)
        ax.add_patch(circle)
        px, py = tv-np.sin(tv), 1-np.cos(tv)
        ax.plot(px, py, 'o', color=col, markersize=10, zorder=10)
        ax.plot([tv, px], [1, py], ':', color=col, lw=1.5)
    ax.set_xlim(-0.5, 2*np.pi+0.5); ax.set_ylim(-0.5, 2.5)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.15)
    ax.set_title('Cycloid: rolling wheel', fontweight='bold')

    ax = axes[1]
    ts = np.linspace(0, 2*np.pi, 200)
    sp = 2*np.abs(np.sin(ts/2))
    ax.plot(ts, sp, '-', color='#E74C3C', lw=2.5)
    ax.fill_between(ts, 0, sp, alpha=0.1, color='#E74C3C')
    ax.set_xlabel('t'); ax.set_ylabel('speed')
    ax.set_title('Speed = 2|sin(t/2)|', fontweight='bold')
    ax.grid(True, alpha=0.15)

    fig.suptitle('P7: Cycloid speed', fontweight='bold', fontsize=13)
    plt.tight_layout(); save(fig, 'p7-cycloid.png')

# ── P8: Sphere surface area ────────────────────────────────────
def p8():
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(121, projection='3d')
    u = np.linspace(0, 2*np.pi, 16); v = np.linspace(0, np.pi, 12)
    R = 1
    ax.plot_wireframe(R*np.outer(np.cos(u), np.sin(v)), R*np.outer(np.sin(u), np.sin(v)),
                      R*np.outer(np.ones(np.size(u)), np.cos(v)), color='gray', alpha=0.12, rstride=1, cstride=1)
    # Highlight area element
    ti, pi = np.pi/2, np.pi/3
    dt, dp = 0.5, 0.4
    verts = R*np.array([[np.cos(ti)*np.sin(pi), np.sin(ti)*np.sin(pi), np.cos(pi)],
                        [np.cos(ti+dt)*np.sin(pi), np.sin(ti+dt)*np.sin(pi), np.cos(pi)],
                        [np.cos(ti+dt)*np.sin(pi+dp), np.sin(ti+dt)*np.sin(pi+dp), np.cos(pi+dp)],
                        [np.cos(ti)*np.sin(pi+dp), np.sin(ti)*np.sin(pi+dp), np.cos(pi+dp)]])
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
    ax.add_collection3d(Poly3DCollection([verts], alpha=0.5, color='#E74C3C'))
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title('Sphere area element dS', fontweight='bold')

    ax2 = fig.add_subplot(122); ax2.axis('off')
    ax2.text(0.5, 0.5,
             'Surface area:\n\n  S = int |r_u x r_v| du dv\n'
             '  = int_0^{2pi} int_0^{pi} R^2 sin(phi) dphi dtheta\n'
             '  = 2pi R^2 [ -cos(phi) ]_0^{pi}\n'
             '  = 4pi R^2\n\nFamiliar formula!',
             ha='center', va='center', fontsize=12, transform=ax2.transAxes,
             bbox=dict(boxstyle='round', facecolor='#D5F5E3', alpha=0.8))
    ax2.set_title('Integration', fontweight='bold')

    fig.suptitle('P8: Sphere surface area = 4pi R^2', fontweight='bold', fontsize=13)
    plt.tight_layout(); save(fig, 'p8-sphere-area.png')

# ── P9: Bezier matrix ──────────────────────────────────────────
def p9():
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.axis('off')
    info = (
        'Cubic Bezier: r(t) = (1-t)^3 P0 + 3(1-t)^2 t P1 + 3(1-t) t^2 P2 + t^3 P3\n\n'
        'In matrix form:\n'
        'r(t) = [t^3  t^2  t  1] * M * [P0  P1  P2  P3]^T\n\n'
        'where M = [[-1, 3, -3, 1],\n'
        '           [ 3, -6, 3, 0],\n'
        '           [-3, 3, 0, 0],\n'
        '           [ 1, 0, 0, 0]]\n\n'
        'Expand each Bernstein polynomial:\n'
        '(1-t)^3 = -t^3 + 3t^2 - 3t + 1\n'
        '3(1-t)^2 t = 3t^3 - 6t^2 + 3t\n'
        '3(1-t) t^2 = -3t^3 + 3t^2\n'
        't^3 = t^3\n\n'
        'Coefficients form exactly the matrix M.'
    )
    ax.text(0.5, 0.5, info, ha='center', va='center', fontsize=11, transform=ax.transAxes,
            bbox=dict(boxstyle='round', facecolor='#D5F5E3', alpha=0.8, ec='#27AE60'))
    ax.set_title('P9: Bezier curve as matrix', fontweight='bold', fontsize=13)
    plt.tight_layout(); save(fig, 'p9-bezier-matrix.png')

if __name__ == '__main__':
    for name, fn in [('P1',p1),('P2',p2),('P3',p3),('P4',p4),('P5',p5),
                     ('P6',p6),('P7',p7),('P8',p8),('P9',p9)]:
        fn(); print(f'  12C2 {name} OK')
