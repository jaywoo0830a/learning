#!/usr/bin/env python3
"""Generate all 10 inline graphs for 11B-trig-advanced.md"""
import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, FancyBboxPatch
import os

plt.rcParams.update({
    'figure.dpi':200,'font.size':10,'font.family':'sans-serif',
    'axes.titlesize':11,'axes.labelsize':9,'legend.fontsize':8,
    'xtick.labelsize':7.5,'ytick.labelsize':7.5,
    'axes.grid':False,'figure.facecolor':'white','axes.facecolor':'white',
})
OUT=os.path.join(os.path.dirname(__file__),'graphs'); os.makedirs(OUT,exist_ok=True)

def g(ax):
    ax.grid(True,alpha=0.1,lw=0.3)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)

# ── 1: Sum formulas via Euler — rotation on unit circle ──────────
def fig1():
    fig,ax=plt.subplots(figsize=(7,7)); ax.set_aspect('equal')
    ax.set_xlim(-1.5,1.5); ax.set_ylim(-1.4,1.4)
    ax.axhline(0,color='#ccc',lw=0.5); ax.axvline(0,color='#ccc',lw=0.5)
    g(ax); ax.set_xticks([]); ax.set_yticks([])
    t=np.linspace(0,2*np.pi,500); ax.plot(np.cos(t),np.sin(t),'#333',lw=1.8)

    # Two rays: A=45°, B=30° (A+B=75°)
    for ang,c,lbl in [(np.deg2rad(45),'#1a73e8','$A=45°$'),
                       (np.deg2rad(75),'#d93025','$A+B=75°$')]:
        x,y=np.cos(ang),np.sin(ang)
        ax.plot([0,x],[0,y],c,lw=2.5)
        ax.scatter(x,y,color=c,s=60,zorder=6)
        ax.annotate(lbl,(x,y),textcoords="offset points",xytext=(10,10),
                     fontsize=10,color=c,fontweight='bold')

    # Angle arcs
    for rng,c in [(45,'#1a73e8'),(30,'#d93025')]:
        a=Arc((0,0),0.65,0.65,theta1=0 if c=='#1a73e8' else 45,
              theta2=45 if c=='#1a73e8' else 75,color=c,lw=1.5,fill=False)
        ax.add_patch(a)
    ax.text(0.35,0.08,'$A$',color='#1a73e8',fontsize=11)
    ax.text(0.08,0.55,'$A+B$',color='#d93025',fontsize=11)
    ax.set_title('$e^{i(A+B)}=e^{iA}e^{iB}$: Adding Angles = Rotating',fontweight='bold',fontsize=12)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT,'11b1-sum-formula-geometric.png'),bbox_inches='tight')
    plt.close(fig)

# ── 2: Harmonic addition — phasor triangle ───────────────────────
def fig2():
    fig,(ax1,ax2)=plt.subplots(1,2,figsize=(12,5.5)); g(ax1); g(ax2)
    ax1.set_aspect('equal'); ax1.set_xlim(-1,5); ax1.set_ylim(-1,5)
    ax1.plot([0,3],[0,0],'#1a73e8',lw=3,label='$a=3$')
    ax1.plot([3,3],[0,4],'#d93025',lw=3,label='$b=4$')
    ax1.plot([0,3],[4,0],'#333',lw=3,label='$R=5$')
    ax1.text(1.5,-0.5,'$a$',ha='center',color='#1a73e8',fontweight='bold',fontsize=12)
    ax1.text(3.5,2,'$b$',color='#d93025',fontweight='bold',fontsize=12)
    ax1.text(1.2,2.5,'$R$',rotation=-53,color='#333',fontweight='bold',fontsize=12)
    ax1.text(0.5,0.3,'$\\phi$',fontsize=12)
    ax1.set_title('Phasor Triangle',fontweight='bold')
    ax1.legend(fontsize=7,loc='lower right')

    xw=np.linspace(0,2*np.pi,500); phi=np.arctan(4/3)
    ax2.plot(xw,3*np.sin(xw),'#1a73e8',lw=1,alpha=0.4,label='$3\\sin x$')
    ax2.plot(xw,4*np.cos(xw),'#d93025',lw=1,alpha=0.4,label='$4\\cos x$')
    ax2.plot(xw,5*np.sin(xw+phi),'#333',lw=2.5,label='$5\\sin(x+\\phi)$')
    ax2.set_ylim(-6,6); ax2.set_title('Combined Wave',fontweight='bold')
    ax2.legend(fontsize=8)
    xt=[0,np.pi/2,np.pi,3*np.pi/2,2*np.pi]; xl=['0','$\\pi/2$','$\\pi$','$3\\pi/2$','$2\\pi$']
    ax2.set_xticks(xt); ax2.set_xticklabels(xl,fontsize=8); ax2.set_xlabel('$x$')
    fig.suptitle('Harmonic Addition: $3\\sin x+4\\cos x = 5\\sin(x+\\phi)$',fontweight='bold',fontsize=13)
    fig.tight_layout(pad=0.8)
    fig.savefig(os.path.join(OUT,'11b2-harmonic-addition.png'),bbox_inches='tight')
    plt.close(fig)

# ── 3: Sum-to-product — beat patterns ────────────────────────────
def fig3():
    fig,(ax1,ax2)=plt.subplots(2,1,figsize=(10,7)); g(ax1); g(ax2)
    x=np.linspace(0,4*np.pi,1500)
    # Beat: sin 10x + sin 9x
    ax1.plot(x,np.sin(10*x)+np.sin(9*x),'#1a73e8',lw=1.5)
    env=2*np.cos(x/2)
    ax1.plot(x,env,'#d93025',lw=2,ls='--',label='envelope $2\\cos(x/2)$')
    ax1.plot(x,-env,'#d93025',lw=2,ls='--')
    ax1.set_ylim(-2.5,2.5); ax1.set_title('Beat Pattern: $\\sin 10x+\\sin 9x$',fontweight='bold')
    ax1.legend(fontsize=9)
    # Product → sum
    y_p=np.sin(7*x)*np.cos(2*x)
    y_s1=np.sin(9*x); y_s2=np.sin(5*x)
    ax2.plot(x,y_p,'#333',lw=2,label='$\\sin 7x\\cos 2x$')
    ax2.plot(x,0.5*y_s1,'#1a73e8',lw=1,alpha=0.5,ls='--',label='$\\frac{1}{2}\\sin 9x$')
    ax2.plot(x,0.5*y_s2,'#d93025',lw=1,alpha=0.5,ls='--',label='$\\frac{1}{2}\\sin 5x$')
    ax2.set_ylim(-1.2,1.2); ax2.set_title('Product→Sum: $\\sin 7x\\cos 2x = \\frac{1}{2}[\\sin 9x+\\sin 5x]$',fontweight='bold')
    ax2.legend(fontsize=8)
    ax2.set_xlabel('$x$')
    fig.tight_layout(pad=0.8)
    fig.savefig(os.path.join(OUT,'11b3-sum-product-waves.png'),bbox_inches='tight')
    plt.close(fig)

# ── 4: Trig equations — solutions repeat every period ────────────
def fig4():
    fig,ax=plt.subplots(figsize=(10,5)); g(ax)
    x=np.linspace(0,4*np.pi,1200); ax.plot(x,np.sin(x),'#333',lw=2)
    ax.axhline(0.5,color='#d93025',lw=1.5,ls='--',label='$y=\\frac{1}{2}$')
    # Mark solutions
    for n in range(0,3):
        s1=np.pi/6+2*n*np.pi; s2=5*np.pi/6+2*n*np.pi
        for s in [s1,s2]:
            if s<=4*np.pi:
                ax.scatter(s,0.5,color='#d93025',s=60,zorder=5)
    ax.set_ylim(-1.3,1.3)
    ax.set_title('$\\sin x = \\frac{1}{2}$ — Two Solutions Per $2\\pi$ Period',fontweight='bold',fontsize=12)
    ax.legend(fontsize=10,loc='upper right'); ax.set_xlabel('$x$')
    xt=[0,np.pi,2*np.pi,3*np.pi,4*np.pi]; xl=['0','$\\pi$','$2\\pi$','$3\\pi$','$4\\pi$']
    ax.set_xticks(xt); ax.set_xticklabels(xl,fontsize=9)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT,'11b4-trig-equation-solutions.png'),bbox_inches='tight')
    plt.close(fig)

# ── 5: Weierstrass substitution ──────────────────────────────────
def fig5():
    fig,ax=plt.subplots(figsize=(7.5,7.5)); ax.set_aspect('equal')
    ax.set_xlim(-1.6,1.8); ax.set_ylim(-1.4,2.2)
    ax.axhline(0,color='#ccc',lw=0.5); ax.axvline(0,color='#ccc',lw=0.5)
    g(ax); ax.set_xticks([]); ax.set_yticks([])
    t=np.linspace(0,2*np.pi,500); ax.plot(np.cos(t),np.sin(t),'#333',lw=1.8)
    ax.scatter(-1,0,color='#333',s=60,zorder=5); ax.text(-1.15,-0.18,'$(-1,0)$',fontsize=9)

    ang=np.deg2rad(50); x,y=np.cos(ang),np.sin(ang)
    ax.scatter(x,y,color='#1a73e8',s=60,zorder=6)
    ax.annotate('$(\\cos x,\\sin x)$',(x,y),textcoords="offset points",
                 xytext=(8,8),fontsize=9,color='#1a73e8',fontweight='bold')

    # Line from (-1,0) through point to y-axis
    t_val=np.tan(ang/2)
    ax.plot([-1,x],[0,y],'#d93025',lw=2,alpha=0.7)
    ax.plot([-1,0],[0,t_val],'#d93025',lw=2,alpha=0.7)
    ax.scatter(0,t_val,color='#d93025',s=60,zorder=6)
    ax.annotate(f'$(0,t)$\n$t=\\tan(x/2)$',(0,t_val),textcoords="offset points",
                 xytext=(12,8),fontsize=10,color='#d93025',fontweight='bold')
    ax.set_title('Weierstrass: $t=\\tan(x/2)$ — Stereographic Projection',fontweight='bold',fontsize=12)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT,'11b5-weierstrass-substitution.png'),bbox_inches='tight')
    plt.close(fig)

# ── 6: Trig inequalities on unit circle ──────────────────────────
def fig6():
    fig,(ax1,ax2,ax3)=plt.subplots(1,3,figsize=(14,5))
    for ax in (ax1,ax2,ax3): ax.set_aspect('equal'); g(ax)
    for ax,ang1,ang2,title,clr in [
        (ax1,np.pi/6,5*np.pi/6,'$\\sin x > 1/2$','#d93025'),
        (ax2,3*np.pi/4,5*np.pi/4,'$\\cos x \\leq -\\sqrt{2}/2$','#1a73e8'),
        (ax3,np.pi/4,np.pi/2,'$\\tan x > 1$','#e37400')]:
        ax.set_xlim(-1.5,1.5); ax.set_ylim(-1.4,1.4)
        ax.axhline(0,color='#ccc',lw=0.5); ax.axvline(0,color='#ccc',lw=0.5)
        ax.set_xticks([]); ax.set_yticks([])
        t=np.linspace(0,2*np.pi,500); ax.plot(np.cos(t),np.sin(t),'#333',lw=1.5)
        at=np.linspace(ang1,ang2,200)
        ax.fill_between(np.cos(at),np.sin(at),1.3,alpha=0.12,color=clr)
        ax.plot(np.cos(at),np.sin(at),clr,lw=3)
        for a in [ang1,ang2]:
            ax.scatter(np.cos(a),np.sin(a),color=clr,s=50,zorder=6)
        ax.set_title(title,fontweight='bold',fontsize=11)
        if ax==ax1: ax.axhline(0.5,color=clr,lw=1,ls='--',alpha=0.5)
        if ax==ax2: ax.axvline(-np.sqrt(2)/2,color=clr,lw=1,ls='--',alpha=0.5)
    fig.suptitle('Trigonometric Inequalities — Unit Circle Method',fontweight='bold',fontsize=13)
    fig.tight_layout(pad=0.8)
    fig.savefig(os.path.join(OUT,'11b6-trig-inequalities.png'),bbox_inches='tight')
    plt.close(fig)

# ── 7: Euler's formula — complex plane ───────────────────────────
def fig7():
    fig,ax=plt.subplots(figsize=(7,7)); ax.set_aspect('equal')
    ax.set_xlim(-1.5,1.5); ax.set_ylim(-1.4,1.4)
    ax.axhline(0,color='#ccc',lw=0.5); ax.axvline(0,color='#ccc',lw=0.5)
    g(ax); ax.set_xticks([]); ax.set_yticks([])
    t=np.linspace(0,2*np.pi,500); ax.plot(np.cos(t),np.sin(t),'#333',lw=1.8)

    ang=np.deg2rad(60); x,y=np.cos(ang),np.sin(ang)
    ax.plot([0,x],[0,y],'#d93025',lw=2.5)
    ax.scatter(x,y,color='#d93025',s=70,zorder=6)
    ax.annotate('$e^{i\\theta}=\\cos\\theta+i\\sin\\theta$\n$=(0.5, 0.866)$',
                (x,y),textcoords="offset points",xytext=(12,12),
                fontsize=10,color='#d93025',fontweight='bold')
    ax.text(1.05,-0.08,'Re',fontsize=11,color='#555')
    ax.text(0.02,1.08,'Im',fontsize=11,color='#555')
    a=Arc((0,0),0.55,0.55,theta1=0,theta2=60,color='#d93025',lw=1.5,fill=False)
    ax.add_patch(a); ax.text(0.25,0.12,'$\\theta$',color='#d93025',fontsize=12)
    ax.set_title("Euler's Formula: $e^{i\\theta}=\\cos\\theta+i\\sin\\theta$",fontweight='bold',fontsize=13)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT,'11b7-euler-formula-complex.png'),bbox_inches='tight')
    plt.close(fig)

# ── 8: Chebyshev polynomials T₁–T₅ ───────────────────────────────
def fig8():
    fig,ax=plt.subplots(figsize=(10,6)); g(ax)
    x=np.linspace(-1,1,500)
    T=[lambda x,n=n:np.cos(n*np.arccos(x)) for n in range(1,6)]
    colors=['#d93025','#1a73e8','#188038','#e37400','#9334e6']
    for n,(Tn,c) in enumerate(zip(T,colors),1):
        ax.plot(x,Tn(x),c,lw=2,label=f'$T_{n}(x)$')
    ax.set_ylim(-1.2,1.2); ax.axhline(0,color='#ccc',lw=0.5)
    ax.set_title('Chebyshev Polynomials $T_1$–$T_5$ on $[-1,1]$',fontweight='bold',fontsize=13)
    ax.legend(fontsize=9,ncol=5,loc='upper center',bbox_to_anchor=(0.5,1.08))
    ax.set_xlabel('$x$')
    fig.tight_layout()
    fig.savefig(os.path.join(OUT,'11b8-chebyshev-polynomials.png'),bbox_inches='tight')
    plt.close(fig)

# ── 9: Cubic solved via trigonometry ─────────────────────────────
def fig9():
    fig,ax=plt.subplots(figsize=(9,5.5)); g(ax)
    xv=np.linspace(-2.5,2.5,600)
    ax.plot(xv,xv**3-3*xv-1,'#333',lw=2.5)
    ax.axhline(0,color='#d93025',lw=1.2,ls='--')
    roots=[2*np.cos(np.pi/9),2*np.cos(7*np.pi/9),2*np.cos(13*np.pi/9)]
    for r in roots:
        ax.scatter(r,0,color='#d93025',s=80,zorder=5)
        ax.annotate(f'{r:.3f}',(r,0),textcoords="offset points",
                     xytext=(0,-18),ha='center',fontsize=9,color='#d93025',fontweight='bold')
    ax.set_ylim(-4,4)
    ax.set_title('$x^3-3x-1=0$ — Three Real Roots via $x=2\\cos\\theta$',fontweight='bold',fontsize=12)
    ax.set_xlabel('$x$'); ax.set_ylabel('$f(x)$')
    fig.tight_layout()
    fig.savefig(os.path.join(OUT,'11b9-cubic-trigonometric.png'),bbox_inches='tight')
    plt.close(fig)

# ── 10: Fourier series — square wave approximation ───────────────
def fig10():
    fig,axes=plt.subplots(2,2,figsize=(11,8))
    x=np.linspace(-np.pi,np.pi,800)
    sw=np.where(x>0,1.0,-1.0)
    for ax,(nterms,title) in zip(axes.flat,[(1,'1 term'),(3,'3 terms'),(5,'5 terms'),(10,'10 terms')]):
        g(ax)
        y=np.zeros_like(x)
        for k in range(1,2*nterms,2):
            y+=(4/(k*np.pi))*np.sin(k*x)
        ax.plot(x,sw,'#999',lw=1.5,alpha=0.6,label='Square wave')
        ax.plot(x,y,'#d93025',lw=2.2,label=f'{nterms} term(s)')
        ax.set_ylim(-1.5,1.5); ax.set_title(title,fontweight='bold',fontsize=11)
        ax.legend(fontsize=7.5)
        ax.set_xticks([-np.pi,0,np.pi]); ax.set_xticklabels(['$-\\pi$','0','$\\pi$'],fontsize=8)
    fig.suptitle('Fourier Series: Square Wave $\\frac{4}{\\pi}(\\sin x+\\frac{\\sin3x}{3}+\\frac{\\sin5x}{5}+\\cdots)$',
                 fontweight='bold',fontsize=13)
    fig.tight_layout(pad=0.8)
    fig.savefig(os.path.join(OUT,'11b10-fourier-series.png'),bbox_inches='tight')
    plt.close(fig)

# ══════════════════════════════════════════════════════════════════
if __name__=='__main__':
    funcs=[fig1,fig2,fig3,fig4,fig5,fig6,fig7,fig8,fig9,fig10]
    for i,f in enumerate(funcs,1):
        print(f'[{i:2d}/10] {f.__name__}...'); f()
    print(f'Done → {OUT}/')
