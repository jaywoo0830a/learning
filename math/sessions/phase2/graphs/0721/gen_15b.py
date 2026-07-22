#!/usr/bin/env python3
"""Generate graphs for Session 15B: Optimization and Related Rates."""
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np, os

OUT = os.path.dirname(os.path.abspath(__file__)) + "/15B"
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({'figure.dpi': 150, 'font.size': 10, 'axes.titlesize': 12, 'axes.labelsize': 10})

def save(name):
    plt.tight_layout(pad=1.5); plt.savefig(f"{OUT}/{name}", bbox_inches='tight', facecolor='white', edgecolor='none'); plt.close()
    print(f"  ✓ {name}")

def fig_box_optimization():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    x = np.linspace(0, 6, 200)
    V = lambda x: x*(12-2*x)**2
    axes[0].plot(x, V(x), 'b-', lw=2.5)
    axes[0].plot(2, V(2), 'ro', markersize=12, zorder=5)
    axes[0].annotate('Max: $x=2$, $V=128$', (2,V(2)), textcoords="offset points", xytext=(10,-20), fontsize=11, color='red', fontweight='bold')
    axes[0].set_title('$V(x)=x(12-2x)^2$ — Volume function', fontweight='bold')
    axes[0].set_xlabel('$x$ (cut size)'); axes[0].set_ylabel('$V(x)$')
    axes[0].set_xlim(0,6); axes[0].grid(True,alpha=0.3)
    # Right: derivative
    Vp = lambda x: 4*(6-x)*(6-3*x)
    axes[1].plot(x, Vp(x), 'r-', lw=2.5, label="$V'(x)$")
    axes[1].axhline(0,color='gray',lw=1)
    axes[1].fill_between(x, 0, Vp(x), where=(Vp(x)>0), alpha=0.15, color='green', label='$V\'>0$')
    axes[1].fill_between(x, 0, Vp(x), where=(Vp(x)<0), alpha=0.15, color='red', label='$V\'<0$')
    axes[1].plot(2,0,'ro',markersize=10,zorder=5)
    axes[1].set_title("$V'(x)$ — sign change + → − confirms max", fontweight='bold')
    axes[1].set_xlabel('$x$'); axes[1].set_ylim(-100,150); axes[1].grid(True,alpha=0.3); axes[1].legend(fontsize=8)
    fig.suptitle('Box Volume Optimization', fontsize=14, fontweight='bold')
    save('15b-box-optimization.png')

def fig_distance_minimization():
    fig, ax = plt.subplots(figsize=(9, 7))
    x = np.linspace(0, 4, 200)
    ax.plot(x, np.sqrt(x), 'b-', lw=2.5, label='$y=\\sqrt{x}$')
    ax.plot(2,0,'ro',markersize=10,zorder=5,label='$(2,0)$')
    ax.plot(1.5,np.sqrt(1.5),'go',markersize=12,zorder=5)
    ax.plot([2,1.5],[0,np.sqrt(1.5)],'r--',lw=2)
    ax.annotate('Closest point\n$(1.5,\\sqrt{1.5})$', (1.5,np.sqrt(1.5)), textcoords="offset points", xytext=(10,-20), fontsize=11, color='green', fontweight='bold')
    ax.set_title('Minimize Distance from $(2,0)$ to $y=\\sqrt{x}$\n$D(x)=\\sqrt{(x-2)^2+(\\sqrt{x})^2}$', fontweight='bold')
    ax.set_xlim(0,4); ax.set_ylim(-0.5,2.5); ax.grid(True,alpha=0.3); ax.legend(fontsize=9); ax.set_aspect('equal')
    save('15b-distance-minimization.png')

def fig_ladder_rates():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    # Left: ladder geometry
    ax = axes[0]
    theta = np.linspace(0, np.pi/2, 100)
    ax.plot(5*np.cos(theta), 5*np.sin(theta), 'b-', lw=2.5)
    ax.plot([0,3],[0,4],'k-',lw=3)
    ax.plot(3,0,'ro',markersize=8); ax.plot(0,4,'ro',markersize=8)
    ax.annotate('$x=3$', (3,0), textcoords="offset points", xytext=(5,-15)); ax.annotate('$y=4$', (0,4), textcoords="offset points", xytext=(-20,5))
    ax.arrow(3,0,0.5,0,head_width=0.2,head_length=0.2,fc='red',ec='red',lw=2)
    ax.arrow(0,4,0,-0.3,head_width=0.2,head_length=0.2,fc='green',ec='green',lw=2)
    ax.text(2,0.5,'$dx/dt=1$',color='red',fontweight='bold')
    ax.text(-1.2,2.5,'$dy/dt=-3/4$',color='green',fontweight='bold')
    ax.set_title('Ladder: $x^2+y^2=25$\n$2x\\frac{dx}{dt}+2y\\frac{dy}{dt}=0$', fontweight='bold')
    ax.set_xlim(-0.5,5.5); ax.set_ylim(-0.5,5.5); ax.grid(True,alpha=0.3); ax.set_aspect('equal')
    # Right: dy/dt as function of x
    ax = axes[1]
    x = np.linspace(0, 5, 100)
    y = np.sqrt(25-x*x)
    dydt = -x/y * 1
    ax.plot(x, dydt, 'r-', lw=2.5)
    ax.plot(3, -0.75, 'bo', markersize=10, zorder=5)
    ax.annotate('$x=3$: $dy/dt=-0.75$', (3,-0.75), textcoords="offset points", xytext=(10,-20), fontsize=10, color='blue', fontweight='bold')
    ax.axhline(0,color='gray',lw=0.5); ax.axvline(0,color='gray',lw=0.5)
    ax.set_title('$dy/dt$ as function of $x$\nTop accelerates as bottom slides out', fontweight='bold')
    ax.set_xlabel('$x$ (bottom distance)'); ax.set_ylabel('$dy/dt$')
    ax.set_xlim(0,5); ax.grid(True,alpha=0.3)
    fig.suptitle('Related Rates — The Ladder Problem', fontsize=14, fontweight='bold')
    save('15b-ladder-rates.png')

def fig_conical_tank():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    # Left: tank cross-section
    ax = axes[0]
    # Draw cone
    R, H = 2, 5
    ax.plot([-R,R],[0,0],'k-',lw=1); ax.plot([0,0],[0,H],'gray',linestyle='--',lw=0.5)
    ax.plot([0,-R],[H,0],'k-',lw=2); ax.plot([0,R],[H,0],'k-',lw=2)
    # Water level
    h = 1
    r = R*h/H
    ax.plot([-r,r],[h,h],'b-',lw=3)
    ax.fill([-r,-R/R*5, R/R*5, r], [h, 0, 0, h], alpha=0.15, color='blue')
    ax.annotate(f'$h={h}$m', (r+0.1, h), fontsize=10, color='blue', fontweight='bold')
    ax.annotate(f'$r={r}$m', (r+0.1, h/2), fontsize=10, color='blue')
    ax.annotate('$R=2$m', (R+0.1, 0.3), fontsize=9)
    ax.annotate('$H=5$m', (0.1, H), fontsize=9)
    ax.text(-1.5, 2.5, 'Similar triangles:\n$\\frac{r}{h} = \\frac{R}{H} = \\frac{2}{5}$', fontsize=9,
            bbox=dict(boxstyle='round',facecolor='wheat',alpha=0.7))
    ax.set_title('Conical Tank Cross-Section\n$V = \\frac{1}{3}\\pi r^2 h$', fontweight='bold')
    ax.set_xlim(-3,3); ax.set_ylim(-0.5,6); ax.set_aspect('equal'); ax.axis('off')
    # Right: dh/dt vs h
    ax = axes[1]
    h_vals = np.linspace(0.1, 5, 100)
    dhdt = 3 / (0.16*np.pi * h_vals**2)
    ax.plot(h_vals, dhdt, 'b-', lw=2.5)
    ax.plot(1, 3/(0.16*np.pi), 'ro', markersize=10, zorder=5)
    ax.annotate('$h=1$: $dh/dt \\approx 5.97$', (1, 3/(0.16*np.pi)), textcoords="offset points", xytext=(10,10), fontsize=10, color='red', fontweight='bold')
    ax.set_title('$\\frac{dh}{dt} = \\frac{3}{0.16\\pi h^2}$\nRise rate slows as tank fills', fontweight='bold')
    ax.set_xlabel('$h$ (water depth)'); ax.set_ylabel('$dh/dt$ (m/min)')
    ax.set_xlim(0,5.5); ax.grid(True,alpha=0.3)
    fig.suptitle('Related Rates — Conical Tank', fontsize=14, fontweight='bold')
    save('15b-conical-tank.png')

def fig_trig_optimization():
    fig, ax = plt.subplots(figsize=(9, 7))
    theta = np.linspace(0.01, np.pi/2-0.01, 200)
    # Rain gutter area: A(theta) = 300*sin(theta) + 100*cos(theta)*sin(theta)
    # Simplified: 30cm sheet, bent at 10cm each side
    A = lambda t: 10*np.sin(t)*(10+10*np.cos(t))
    ax.plot(theta, A(theta), 'b-', lw=2.5)
    opt_t = np.pi/3
    ax.plot(opt_t, A(opt_t), 'ro', markersize=12, zorder=5)
    ax.annotate(f'Optimum: $\\theta = {60}^\\circ$\nMax area = {A(opt_t):.1f} cm²', 
               (opt_t, A(opt_t)), textcoords="offset points", xytext=(10,-30), fontsize=11, color='red', fontweight='bold')
    ax.set_title('Trigonometric Optimization\nRain Gutter Cross-Sectional Area', fontweight='bold')
    ax.set_xlabel('$\\theta$ (radians)'); ax.set_ylabel('Area (cm²)')
    ax.set_xlim(0, np.pi/2); ax.grid(True,alpha=0.3)
    # Add degree labels
    ax.set_xticks([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
    ax.set_xticklabels(['$0$', '$30°$', '$45°$', '$60°$', '$90°$'])
    save('15b-trig-optimization.png')

def fig_related_rates_overview():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    # 1) Ladder
    ax = axes[0]
    theta = np.linspace(0, np.pi/2, 100)
    ax.plot(10*np.cos(theta), 10*np.sin(theta), 'gray', lw=1)
    ax.plot([0,6],[0,8],'b-',lw=2.5)
    ax.plot(6,0,'ro',markersize=6); ax.plot(0,8,'ro',markersize=6)
    ax.arrow(6,0,0.5,0,head_width=0.2,head_length=0.2,fc='red',ec='red')
    ax.arrow(0,8,0,-0.3,head_width=0.2,head_length=0.2,fc='green',ec='green')
    ax.set_title('Pythagorean\n$x^2+y^2=L^2$', fontweight='bold'); ax.set_aspect('equal')
    ax.set_xlim(-0.5,10.5); ax.set_ylim(-0.5,10.5); ax.grid(True,alpha=0.3)
    # 2) Tank
    ax = axes[1]
    R,H = 2,5
    ax.plot([0,-R],[H,0],'k-',lw=2); ax.plot([0,R],[H,0],'k-',lw=2)
    ax.plot([-1,1],[2.5,2.5],'b-',lw=3)
    ax.fill([-1,-R,R,1],[2.5,0,0,2.5],alpha=0.1,color='blue')
    ax.text(-1,1.5,'Similar triangles',fontsize=8,rotation=90)
    ax.set_title('Similar Triangles\n$\\frac{r}{h}=\\frac{R}{H}$', fontweight='bold')
    ax.set_xlim(-3,3); ax.set_ylim(-0.5,6); ax.axis('off')
    # 3) Spotlight
    ax = axes[2]
    ax.plot([0,0],[-1,1],'k-',lw=2,label='wall')
    ax.plot([0,2],[0,0],'gray',linestyle='--',lw=0.5)
    ax.plot([0,2],[0,2],'b-',lw=2.5,label='$x = 100\\tan\\theta$')
    ax.plot(2,2,'ro',markersize=8)
    ax.annotate('$\\theta=45°$', (1.5,1), fontsize=9)
    ax.set_title('Trigonometric\n$x = d\\tan\\theta$', fontweight='bold')
    ax.set_xlim(-0.5,3); ax.set_ylim(-0.5,3); ax.grid(True,alpha=0.3); ax.legend(fontsize=8)
    fig.suptitle('Related Rates — Three Classic Patterns', fontsize=14, fontweight='bold')
    save('15b-related-rates-overview.png')

if __name__ == "__main__":
    print("Generating 15B graphs...")
    fig_box_optimization(); fig_distance_minimization(); fig_ladder_rates()
    fig_conical_tank(); fig_trig_optimization(); fig_related_rates_overview()
    print("Done! ✓")
