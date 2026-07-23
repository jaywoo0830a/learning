#!/usr/bin/env python3
"""Generate individual graphs for Session 25B."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

DPI = 150
OUT_DIR = '25B'

def spherical_3d():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    R = 2; u = np.linspace(0, 2*np.pi, 20); v = np.linspace(0, np.pi, 20)
    U, V = np.meshgrid(u, v)
    ax.plot_wireframe(R*np.cos(U)*np.sin(V), R*np.sin(U)*np.sin(V), R*np.cos(V),
                      color='gray', alpha=0.2, linewidth=0.5)
    phi0, th0 = np.pi/3, np.pi/4
    x0 = R*np.sin(phi0)*np.cos(th0); y0 = R*np.sin(phi0)*np.sin(th0); z0 = R*np.cos(phi0)
    ax.scatter([x0], [y0], [z0], color='red', s=80, zorder=10)
    ax.plot([0, x0], [0, y0], [0, z0], 'r-', lw=2, label=r'$\rho$')
    r_xy = R*np.sin(phi0)
    th_arc = np.linspace(0, th0, 30)
    ax.plot(r_xy*np.cos(th_arc), r_xy*np.sin(th_arc), np.full_like(th_arc, z0), 'g-', lw=1.5, label=r'$\theta$')
    ph_arc = np.linspace(0, phi0, 30)
    ax.plot(R*np.sin(ph_arc)*np.cos(th0), R*np.sin(ph_arc)*np.sin(th0), R*np.cos(ph_arc),
            'b-', lw=1.5, label=r'$\phi$')
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12); ax.set_zlabel('z', fontsize=12)
    ax.set_title(r'Spherical Coordinates $(\rho,\phi,\theta)$', fontsize=12)
    ax.view_init(25, -60); ax.legend(fontsize=10)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/spherical-3d.png', dpi=DPI); plt.close()
    print('  ✓ spherical-3d.png')

def spherical_jacobian_rho():
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111)
    rho = np.linspace(0, 3, 100)
    ax.plot(rho, rho**2, 'b-', lw=2.5, label=r'$\rho^2$ factor')
    ax.set_xlabel(r'$\rho$', fontsize=12); ax.set_ylabel(r'$\rho^2$', fontsize=12)
    ax.set_title(r'Spherical Jacobian Factor $\rho^2$ — Radial Stretch', fontsize=12)
    ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/spherical-jacobian-rho.png', dpi=DPI); plt.close()
    print('  ✓ spherical-jacobian-rho.png')

def spherical_jacobian_phi():
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111)
    ph = np.linspace(0.01, np.pi-0.01, 100)
    ax.plot(ph, np.sin(ph), 'r-', lw=2.5, label=r'$\sin\phi$')
    ax.set_xlabel(r'$\phi$', fontsize=12); ax.set_ylabel(r'$\sin\phi$', fontsize=12)
    ax.set_title(r'Spherical Jacobian Factor $\sin\phi$ — Polar Stretch', fontsize=12)
    ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/spherical-jacobian-phi.png', dpi=DPI); plt.close()
    print('  ✓ spherical-jacobian-phi.png')

def jacobian_3d():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    u = np.linspace(0, 2, 10); v = np.linspace(0, 2, 10)
    U, V = np.meshgrid(u, v)
    Xt, Yt = U+V, U-V
    for i in range(len(u)):
        ax.plot(U[i,:], V[i,:], np.zeros_like(U[i,:])-0.1, 'b-', lw=0.5, alpha=0.5)
        ax.plot(Xt[i,:], Yt[i,:], np.zeros_like(Xt[i,:])+1, 'r-', lw=0.5, alpha=0.5)
    for j in range(len(v)):
        ax.plot(U[:,j], V[:,j], np.zeros_like(U[:,j])-0.1, 'b-', lw=0.5, alpha=0.5)
        ax.plot(Xt[:,j], Yt[:,j], np.zeros_like(Xt[:,j])+1, 'r-', lw=0.5, alpha=0.5)
    sq_u = [0,2,2,0,0]; sq_v = [0,0,2,2,0]
    ax.plot(sq_u, sq_v, [0,0,0,0,0], 'b-', lw=2, label='(u,v) square')
    ax.plot([0,2,4,2,0], [0,-2,0,2,0], [1,1,1,1,1], 'r-', lw=2, label='(x,y) image')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('')
    ax.set_title(r'3D: Jacobian Maps Square to Parallelogram', fontsize=12)
    ax.view_init(25, -60); ax.legend(fontsize=10)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/jacobian-3d.png', dpi=DPI); plt.close()
    print('  ✓ jacobian-3d.png')

def jacobian_2d():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    sq = np.array([[0,0],[1,0],[1,1],[0,1],[0,0]])
    ax.fill(sq[:,0], sq[:,1], alpha=0.3, color='blue', label='Unit square in (u,v)')
    ax.plot(sq[:,0], sq[:,1], 'b-', lw=2)
    J = np.array([[1,1],[1,-1]])
    trans = sq @ J.T
    ax.fill(trans[:,0], trans[:,1], alpha=0.3, color='red', label='Image in (x,y)')
    ax.plot(trans[:,0], trans[:,1], 'r-', lw=2)
    ax.quiver(0, 0, 1, 1, color='green', scale=5, width=0.05, label=r'$J_{*1}$')
    ax.quiver(0, 0, 1, -1, color='orange', scale=5, width=0.05, label=r'$J_{*2}$')
    ax.set_xlim(-1, 2); ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12)
    ax.set_title(r'$|\det J| = 2$ = Area Scaling Factor', fontsize=12)
    ax.set_aspect('equal'); ax.legend(fontsize=9); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/jacobian-2d.png', dpi=DPI); plt.close()
    print('  ✓ jacobian-2d.png')

def jacobian_1d():
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111)
    r = np.linspace(0, 3, 100)
    ax.plot(r, r, 'b-', lw=2, label='Polar: det J = r')
    ax.plot(r, r**2, 'g-', lw=2, label=r'Spherical: det J $\propto \rho^2$')
    ax.plot(r, np.full_like(r, -2), 'r--', lw=2, label='Linear: det J = -2 (constant)')
    ax.axhline(0, color='gray', lw=0.5)
    ax.set_xlabel('Position', fontsize=12); ax.set_ylabel('det(J)', fontsize=12)
    ax.set_title(r'$\det J$ — Varies (Nonlinear) vs Constant (Linear Transform)', fontsize=12)
    ax.legend(fontsize=9); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/jacobian-1d.png', dpi=DPI); plt.close()
    print('  ✓ jacobian-1d.png')

if __name__ == '__main__':
    spherical_3d(); spherical_jacobian_rho(); spherical_jacobian_phi()
    jacobian_3d(); jacobian_2d(); jacobian_1d()
