#!/usr/bin/env python3
"""Generate all graphs for Session 19D — Higher Order & Numerical Methods."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

DPI = 150
OUT_DIR = '19D'

def damping_types():
    """19D-1: Damping types — 3D+2D+1D"""
    fig = plt.figure(figsize=(14, 10))
    
    t = np.linspace(0, 8, 200)
    
    # Parameters for each damping type
    # Underdamped: m=1, c=1, k=5 → λ = -0.5 ± 2.18i
    # Critically damped: m=1, c=2√5≈4.47, k=5 → λ = -2.236 (repeated)
    # Overdamped: m=1, c=6, k=5 → λ = -1, -5
    
    # Solutions
    y_under = np.exp(-0.5*t) * (np.cos(2.179*t) + 0.5/2.179*np.sin(2.179*t))
    y_crit = (1 + 2.236*t) * np.exp(-2.236*t)
    y_over = (5/4)*np.exp(-t) - (1/4)*np.exp(-5*t)
    
    # 3D — state space (y, y', t)
    ax = fig.add_subplot(221, projection='3d')
    ax.plot(t, y_under, np.gradient(y_under, t[1]-t[0]), 'b-', lw=1.5, label='Underdamped')
    ax.plot(t, y_crit, np.gradient(y_crit, t[1]-t[0]), 'g-', lw=1.5, label='Critically')
    ax.plot(t, y_over, np.gradient(y_over, t[1]-t[0]), 'r-', lw=1.5, label='Overdamped')
    ax.set_xlabel('Time t'); ax.set_ylabel('y'); ax.set_zlabel("y'")
    ax.set_title('3D: State Space Trajectories', fontsize=10)
    ax.view_init(25, -60)
    ax.legend(fontsize=7)
    
    # 2D — phase portrait (y, y')
    ax2 = fig.add_subplot(222)
    ax2.plot(y_under, np.gradient(y_under, t[1]-t[0]), 'b-', lw=2, label='Underdamped')
    ax2.plot(y_crit, np.gradient(y_crit, t[1]-t[0]), 'g-', lw=2, label='Critically')
    ax2.plot(y_over, np.gradient(y_over, t[1]-t[0]), 'r-', lw=2, label='Overdamped')
    ax2.scatter(0, 0, color='black', s=50, zorder=5)
    ax2.set_xlabel('y'); ax2.set_ylabel("y'")
    ax2.set_title('2D: Phase Portrait (y, y\')')
    ax2.legend(fontsize=8)
    ax2.grid(True, alpha=0.3)
    ax2.set_aspect('equal')
    ax2.set_xlim(-0.5, 1.2); ax2.set_ylim(-2, 1)
    
    # 1D — time traces
    ax3 = fig.add_subplot(223)
    ax3.plot(t, y_under, 'b-', lw=2, label='Underdamped')
    ax3.plot(t, y_crit, 'g-', lw=2, label='Critically damped')
    ax3.plot(t, y_over, 'r-', lw=2, label='Overdamped')
    ax3.axhline(0, color='gray', lw=0.5)
    ax3.set_xlim(0, 8); ax3.set_ylim(-0.5, 1.2)
    ax3.set_xlabel('Time t'); ax3.set_ylabel('y(t)')
    ax3.set_title('1D: Time Traces')
    ax3.legend(fontsize=8)
    ax3.grid(True, alpha=0.3)
    
    # 1D — exponential envelopes
    ax4 = fig.add_subplot(224)
    ax4.plot(t, y_under, 'b-', lw=1.5, alpha=0.5)
    ax4.plot(t, np.exp(-0.5*t), 'b--', lw=1, label='Envelope ±e^{-0.5t}')
    ax4.plot(t, -np.exp(-0.5*t), 'b--', lw=1)
    ax4.plot(t, y_crit, 'g-', lw=2, label='Critically damped')
    ax4.set_xlim(0, 8); ax4.set_ylim(-0.5, 1.2)
    ax4.set_xlabel('Time t'); ax4.set_ylabel('y(t)')
    ax4.set_title('Underdamped Envelope')
    ax4.legend(fontsize=8)
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'{OUT_DIR}/damping-types.png', dpi=DPI)
    plt.close()
    print('  ✓ damping-types.png')

def euler_method():
    """19D-2: Euler method — 3D+2D+1D for y' = x+y, y(0)=1"""
    fig = plt.figure(figsize=(14, 10))
    
    f = lambda x, y: x + y
    y_exact = lambda x: -x - 1 + 2*np.exp(x)
    
    # Euler approximation
    h = 0.3
    n_steps = int(2.0 / h)
    x_e = np.array([i*h for i in range(n_steps+1)])
    y_e = np.zeros_like(x_e)
    y_e[0] = 1
    for i in range(n_steps):
        y_e[i+1] = y_e[i] + h * f(x_e[i], y_e[i])
    
    x_fine = np.linspace(0, 2, 200)
    y_fine = y_exact(x_fine)
    
    # 3D — staircase
    ax = fig.add_subplot(221, projection='3d')
    Xg, Yg = np.meshgrid(np.linspace(0, 2, 20), np.linspace(0, 6, 20))
    Zg = np.zeros_like(Xg)
    surf = ax.plot_surface(Xg, Yg, Zg, alpha=0.3, color='lightgray')
    
    # Staircase
    for i in range(len(x_e)-1):
        ax.plot([x_e[i], x_e[i]], [y_e[i], y_e[i+1]], [0, 0], 'r-', lw=2)
        ax.plot([x_e[i], x_e[i+1]], [y_e[i+1], y_e[i+1]], [0, 0], 'r-', lw=2)
    
    ax.plot(x_fine, y_fine, np.zeros_like(x_fine), 'b-', lw=2, label='Exact')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('')
    ax.set_title('3D: Euler Staircase', fontsize=10)
    ax.view_init(30, -70)
    ax.legend(fontsize=8)
    
    # 2D — Euler vs exact
    ax2 = fig.add_subplot(222)
    ax2.plot(x_fine, y_fine, 'b-', lw=2, label='Exact y = -x-1+2e^x')
    ax2.plot(x_e, y_e, 'ro-', lw=1.5, markersize=6, label=f'Euler h={h}')
    
    # Show slopes at each step
    for i in range(len(x_e)-1):
        slope = f(x_e[i], y_e[i])
        x_slope = np.array([x_e[i], x_e[i]+0.2])
        y_slope = y_e[i] + slope * (x_slope - x_e[i])
        ax2.plot(x_slope, y_slope, 'g-', lw=1, alpha=0.6)
    
    ax2.set_xlim(0, 2); ax2.set_ylim(0, 7)
    ax2.set_xlabel('x'); ax2.set_ylabel('y')
    ax2.set_title('2D: Euler vs Exact')
    ax2.legend(fontsize=8)
    ax2.grid(True, alpha=0.3)
    
    # 1D — error growth
    ax3 = fig.add_subplot(223)
    y_exact_euler = y_exact(x_e)
    error = np.abs(y_e - y_exact_euler)
    ax3.plot(x_e, error, 'ro-', lw=1.5, markersize=5)
    ax3.set_xlim(0, 2)
    ax3.set_xlabel('x'); ax3.set_ylabel('|Error|')
    ax3.set_title('1D: Absolute Error Growth')
    ax3.grid(True, alpha=0.3)
    
    # 1D — Riemann sum comparison
    ax4 = fig.add_subplot(224)
    # For y' = f(x) case: y' = x, y(0)=1
    f2 = lambda x: x
    y2_exact = lambda x: 1 + x**2/2
    h2 = 0.3
    n2 = int(2.0/h2)
    x2 = np.array([i*h2 for i in range(n2+1)])
    y2_euler = np.zeros_like(x2)
    y2_euler[0] = 1
    for i in range(n2):
        y2_euler[i+1] = y2_euler[i] + h2 * f2(x2[i])
    
    x2_fine = np.linspace(0, 2, 100)
    ax4.plot(x2_fine, y2_exact(x2_fine), 'b-', lw=2, label='Exact y=1+x²/2')
    
    # Draw Riemann rectangles
    for i in range(n2):
        ax4.add_patch(plt.Rectangle((x2[i], y2_exact(x2[i])-f2(x2[i])*h2/2), 
                                     h2, f2(x2[i])*h2, 
                                     alpha=0.3, color='red', lw=0))
    
    ax4.plot(x2, y2_euler, 'ro-', lw=1.5, markersize=5, label='Euler = Left Riemann')
    ax4.set_xlim(0, 2); ax4.set_ylim(1, 3)
    ax4.set_xlabel('x'); ax4.set_ylabel('y')
    ax4.set_title('1D: Euler = Left Riemann Sum (cf. 16A)')
    ax4.legend(fontsize=8)
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'{OUT_DIR}/euler-method.png', dpi=DPI)
    plt.close()
    print('  ✓ euler-method.png')

def lotka_volterra():
    """19D-3: Lotka-Volterra phase plane"""
    fig = plt.figure(figsize=(14, 5))
    
    a, b, c, d = 0.4, 0.02, 0.3, 0.01
    
    def lv_system(t, z):
        x, y = z
        dx = a*x - b*x*y
        dy = -c*y + d*x*y
        return [dx, dy]
    
    from scipy.integrate import solve_ivp
    
    # 2D — phase plane
    ax = fig.add_subplot(121)
    for x0, y0, color in [(30, 5, 'blue'), (20, 15, 'green'), (40, 20, 'red'), (10, 10, 'purple')]:
        sol = solve_ivp(lv_system, [0, 50], [x0, y0], method='RK45', max_step=0.1)
        ax.plot(sol.y[0], sol.y[1], color=color, lw=1.5, label=f'({x0},{y0})')
        ax.scatter([x0], [y0], color=color, s=30, zorder=5)
    
    # Equilibrium
    ax.scatter([c/d], [a/b], color='black', s=100, marker='*', zorder=5, label='Equilibrium')
    ax.set_xlabel('Prey x'); ax.set_ylabel('Predator y')
    ax.set_title('2D: Lotka-Volterra Phase Plane')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)
    
    # 1D — time traces
    ax2 = fig.add_subplot(122)
    sol = solve_ivp(lv_system, [0, 50], [30, 5], method='RK45', max_step=0.1, dense_output=True)
    t = sol.t
    x, y = sol.y
    ax2.plot(t, x, 'b-', lw=2, label='Prey')
    ax2.plot(t, y, 'r-', lw=2, label='Predator')
    ax2.set_xlabel('Time t'); ax2.set_ylabel('Population')
    ax2.set_title('1D: Time Traces')
    ax2.legend(fontsize=8)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'{OUT_DIR}/lotka-volterra.png', dpi=DPI)
    plt.close()
    print('  ✓ lotka-volterra.png')

if __name__ == '__main__':
    damping_types()
    euler_method()
    lotka_volterra()
