#!/usr/bin/env python3
"""Generate solution graphs for 11B-solutions.md"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import os

plt.rcParams.update({
    'figure.dpi': 200, 'font.size': 10, 'font.family': 'sans-serif',
    'axes.titlesize': 11, 'axes.labelsize': 9,
    'legend.fontsize': 8, 'xtick.labelsize': 7.5, 'ytick.labelsize': 7.5,
    'axes.grid': False, 'figure.facecolor': 'white', 'axes.facecolor': 'white',
})
OUT = os.path.join(os.path.dirname(__file__), 'graphs')
os.makedirs(OUT, exist_ok=True)

def g(ax):
    ax.grid(True, alpha=0.1, lw=0.3)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)

# ── P3: Harmonic addition — phasor + wave ────────────────────────
def p3():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))
    g(ax1); g(ax2)
    ax1.set_aspect('equal'); ax1.set_xlim(-1, 14); ax1.set_ylim(-1, 7)
    ax1.plot([0,12],[0,0],'#1a73e8',lw=3,label='$a=12$')
    ax1.plot([12,12],[0,5],'#d93025',lw=3,label='$b=5$')
    ax1.plot([0,12],[5,0],'#333',lw=3,label='$R=13$')
    ax1.scatter([12],[5],color='#333',s=50,zorder=5)
    ax1.text(6,-0.6,'$a=12$',ha='center',color='#1a73e8',fontweight='bold',fontsize=11)
    ax1.text(12.6,2.5,'$b=5$',color='#d93025',fontweight='bold',fontsize=11)
    ax1.text(5.5,3.2,'$R=13$',ha='center',rotation=-22.6,color='#333',fontweight='bold',fontsize=11)
    ax1.text(0.8,0.3,'$\\phi$',fontsize=11)
    ax1.set_title('Phasor: $R=\\sqrt{12^2+5^2}=13$',fontweight='bold')
    ax1.legend(fontsize=7.5,loc='lower right')

    xw = np.linspace(0,2*np.pi,600); phi=np.arctan(5/12)
    ax2.plot(xw,12*np.sin(xw),'#1a73e8',lw=1,alpha=0.4,label='$12\\sin x$')
    ax2.plot(xw,5*np.cos(xw),'#d93025',lw=1,alpha=0.4,label='$5\\cos x$')
    ax2.plot(xw,13*np.sin(xw+phi),'#333',lw=2.5,label='$13\\sin(x+\\phi)$')
    ax2.set_ylim(-14,14); ax2.set_title('Combined Wave',fontweight='bold')
    ax2.legend(fontsize=8)
    xt=[0,np.pi/2,np.pi,3*np.pi/2,2*np.pi]; xl=['0','$\\pi/2$','$\\pi$','$3\\pi/2$','$2\\pi$']
    ax2.set_xticks(xt); ax2.set_xticklabels(xl,fontsize=8); ax2.set_xlabel('$x$')

    fig.suptitle('Practice 3: $12\\sin x+5\\cos x = 13\\sin(x+\\phi)$',fontweight='bold',fontsize=12)
    fig.tight_layout(pad=0.8)
    fig.savefig(os.path.join(OUT,'sol11b-p3-harmonic.png'),bbox_inches='tight')
    plt.close(fig)

# ── P4: Quadratic trig solutions on unit circle ──────────────────
def p4():
    fig,ax=plt.subplots(figsize=(7,7))
    ax.set_aspect('equal'); ax.set_xlim(-1.5,1.5); ax.set_ylim(-1.45,1.45)
    ax.axhline(0,color='#ccc',lw=0.5); ax.axvline(0,color='#ccc',lw=0.5)
    g(ax); ax.set_xticks([]); ax.set_yticks([])
    t=np.linspace(0,2*np.pi,500); ax.plot(np.cos(t),np.sin(t),'#333',lw=1.8)

    for ang,lbl,c in [(np.pi/3,'$\\pi/3$','#1a73e8'),(5*np.pi/3,'$5\\pi/3$','#1a73e8')]:
        x,y=np.cos(ang),np.sin(ang)
        ax.plot([0,x],[0,y],c,lw=1.5,alpha=0.5)
        ax.scatter(x,y,color=c,s=70,zorder=6)
        ax.annotate(lbl+'\n$\\cos=\\frac{1}{2}$',(x,y),textcoords="offset points",
                     xytext=(12,12),fontsize=9,color=c,fontweight='bold')
    ax.scatter(1,0,color='#d93025',s=70,zorder=6)
    ax.annotate('$0$\n$\\cos=1$',(1,0),textcoords="offset points",
                 xytext=(12,-18),fontsize=9,color='#d93025',fontweight='bold')
    ax.set_title('Practice 4: $2\\cos^2 x-3\\cos x+1=0$',fontweight='bold',fontsize=11)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT,'sol11b-p4-quadratic.png'),bbox_inches='tight')
    plt.close(fig)

# ── P8: Triangle 7-10-13 ─────────────────────────────────────────
def p8():
    fig,ax=plt.subplots(figsize=(8,7))
    ax.set_aspect('equal'); ax.set_xlim(-2,12); ax.set_ylim(-2,12)
    ax.axis('off')
    A=np.deg2rad(32.20); Bx=13; By=0
    Cx=10*np.cos(A); Cy=10*np.sin(A)
    ax.fill([0,Bx,Cx],[0,By,Cy],facecolor='#e3f2fd',edgecolor='#333',lw=2.5,alpha=0.5)
    for px,py in [(0,0),(Bx,By),(Cx,Cy)]: ax.scatter(px,py,color='#333',s=80,zorder=5)
    ax.text(-0.5,-0.3,'$A$',fontsize=14,fontweight='bold')
    ax.text(Bx+0.3,-0.3,'$C$',fontsize=14,fontweight='bold')
    ax.text(Cx-0.3,Cy+0.4,'$B$',fontsize=14,fontweight='bold')
    ax.text(Bx/2,-0.8,'$c=13$',ha='center',fontsize=12,fontweight='bold',color='#1a73e8')
    ax.text(Cx/2-0.5,Cy/2,'$b=10$',ha='center',fontsize=12,fontweight='bold',color='#d93025')
    ax.text((Bx+Cx)/2+0.5,(By+Cy)/2+0.2,'$a=7$',fontsize=12,fontweight='bold',color='#188038')
    ax.text(1.5,0.4,'$32.2°$',fontsize=9); ax.text(Bx-3.0,0.5,'$98.2°$',fontsize=9)
    ax.text(Cx-0.8,Cy-1.0,'$49.5°$',fontsize=9)
    ax.set_title('Practice 8: Triangle $a=7,b=10,c=13$ — Area $=20\\sqrt{3}$',fontweight='bold',fontsize=12)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT,'sol11b-p8-triangle.png'),bbox_inches='tight')
    plt.close(fig)

# ── A6: cos 20°·cos 40°·cos 80° on unit circle ───────────────────
def a6():
    fig,ax=plt.subplots(figsize=(7.5,7.5))
    ax.set_aspect('equal'); ax.set_xlim(-1.4,1.4); ax.set_ylim(-1.35,1.35)
    ax.axhline(0,color='#ccc',lw=0.5); ax.axvline(0,color='#ccc',lw=0.5)
    g(ax); ax.set_xticks([]); ax.set_yticks([])
    t=np.linspace(0,2*np.pi,500); ax.plot(np.cos(t),np.sin(t),'#333',lw=1.8)
    colors=['#d93025','#1a73e8','#188038']
    for deg,c,lbl in [(20,colors[0],'$20°$'),(40,colors[1],'$40°$'),(80,colors[2],'$80°$')]:
        rad=np.deg2rad(deg); x=np.cos(rad); y=np.sin(rad)
        ax.plot([0,x],[0,y],c,lw=1.5,alpha=0.5)
        ax.plot([x,x],[0,y],c,lw=1.2,ls='--',alpha=0.5)
        ax.scatter(x,0,color=c,s=50,zorder=6)
        ax.annotate(f'{lbl}\n$\\cos={x:.3f}$',(x,0),textcoords="offset points",
                     xytext=(0,-22),ha='center',fontsize=8,color=c,fontweight='bold')
    ax.set_title('A6: $\\cos 20°\\cdot\\cos 40°\\cdot\\cos 80° = \\frac{1}{8}$',fontweight='bold',fontsize=11,pad=12)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT,'sol11b-a6-morrie.png'),bbox_inches='tight')
    plt.close(fig)

# ── A10: Fourier series partial sums ─────────────────────────────
def a10():
    fig,ax=plt.subplots(figsize=(11,5.5)); g(ax)
    xv=np.linspace(-np.pi,np.pi,1000)
    ax.plot(xv,xv,'#333',lw=2.5,label='$f(x)=x$')
    s1=2*np.sin(xv)
    ax.plot(xv,s1,'#d93025',lw=1.8,alpha=0.7,label='1 term: $2\\sin x$')
    s2=2*np.sin(xv)-np.sin(2*xv)
    ax.plot(xv,s2,'#1a73e8',lw=1.8,alpha=0.7,label='2 terms: $2\\sin x-\\sin 2x$')
    s3=2*np.sin(xv)-np.sin(2*xv)+(2/3)*np.sin(3*xv)
    ax.plot(xv,s3,'#188038',lw=1.8,alpha=0.7,label='3 terms: $+\\frac{2}{3}\\sin 3x$')
    ax.axhline(0,color='#ccc',lw=0.5); ax.set_ylim(-4,4)
    ax.set_title('A10: Fourier Series of $f(x)=x$ — Partial Sums',fontweight='bold',fontsize=12)
    ax.legend(fontsize=8.5,loc='upper left'); ax.set_xlabel('$x$')
    xt=[-np.pi,-np.pi/2,0,np.pi/2,np.pi]; xl=['$-\\pi$','$-\\pi/2$','0','$\\pi/2$','$\\pi$']
    ax.set_xticks(xt); ax.set_xticklabels(xl)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT,'sol11b-a10-fourier.png'),bbox_inches='tight')
    plt.close(fig)

# ══════════════════════════════════════════════════════════════════
if __name__=='__main__':
    for f in [p3,p4,p8,a6,a10]:
        print(f'  {f.__name__}...'); f()
    print(f'Done → {OUT}/')
