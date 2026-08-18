#!/usr/bin/env python3
"""Generate 11C hyperbolic function graphs -- textbook quality with LaTeX."""
import numpy as np, matplotlib, os
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Arc

C={'bg':'#f8f9fa','fg':'#1a1a2e','sin':'#e74c3c','cos':'#2980b9','tan':'#27ae60','csc':'#e67e22','sec':'#9b59b6','cot':'#1abc9c','asymp':'#ccc','hl':'#f1c40f','circ':'#2c3e50'}
D=300;F=16
OUT=os.path.join(os.path.dirname(__file__),'11C')
os.makedirs(OUT,exist_ok=True)
plt.rcParams.update({'font.family':'serif','font.size':F,'axes.facecolor':C['bg'],'figure.facecolor':'white','axes.edgecolor':'#333','axes.grid':True,'grid.color':'#e0e0e0','grid.alpha':0.4,'axes.spines.top':False,'axes.spines.right':False,'text.usetex':True,'pgf.rcfonts':False,'text.latex.preamble':r'\usepackage{noto-serif}'})
bb=dict(boxstyle='round,pad=0.12',facecolor='white',edgecolor='none',alpha=0.85)
def sv(n,fig):
  plt.tight_layout();fig.savefig(os.path.join(OUT,n),dpi=D,bbox_inches='tight')
  fig.savefig(os.path.join(OUT,n.replace('.png','.pdf')),dpi=D,bbox_inches='tight');plt.close(fig)

def c1():
  fig,(a1,a2)=plt.subplots(1,2,figsize=(13,6.5))
  # Left: unit circle
  ax=a1;ax.set_aspect('equal');ax.set_xlim(-1.9,1.9);ax.set_ylim(-1.9,1.9)
  ax.set_title(r'Circle: $x^2+y^2=1$',fontsize=20,fontweight='bold')
  th=0.9
  t=np.linspace(0,2*np.pi,300);ax.plot(np.cos(t),np.sin(t),color=C['circ'],lw=2.5)
  px,py=np.cos(th),np.sin(th)
  ax.fill([0,px,0,0],[0,py,0,0],alpha=0.15,color=C['hl'])
  ax.plot([0,px],[0,py],color=C['sin'],lw=2);ax.plot([px,px],[0,py],'--',color=C['sin'],lw=1.2)
  ax.plot(px,py,'o',color=C['sin'],ms=9,zorder=5)
  ax.annotate(r'$(\cos\theta,\sin\theta)$',(px,py),xytext=(px+0.25,py+0.15),fontsize=17,color=C['sin'],fontweight='bold')
  ax.annotate(r'$\theta$',(0.45,0.13),fontsize=17,color=C['fg'],fontweight='bold')
  ax.plot([-1.9,1.9],[0,0],color='#bbb',lw=1);ax.plot([0,0],[-1.9,1.9],color='#bbb',lw=1)
  ax.text(1.62,0.12,r'$x$',fontsize=15);ax.text(0.12,1.62,r'$y$',fontsize=15)
  ax.annotate(r'$\cos^2\theta+\sin^2\theta=1$',(-1.8,-1.6),fontsize=15,color=C['cos'],fontweight='bold')
  # Right: unit hyperbola
  ax=a2;ax.set_aspect('equal');ax.set_xlim(-1.9,3.2);ax.set_ylim(-1.9,1.9)
  ax.set_title(r'Hyperbola: $x^2-y^2=1$',fontsize=20,fontweight='bold')
  u=np.linspace(-1.8,3.0,400)
  hyp=np.sqrt(np.maximum(u**2-1,0))
  ax.plot(u,hyp,color=C['tan'],lw=2.5);ax.plot(u,-hyp,color=C['tan'],lw=2.5)
  ax.plot([-2.2,3.4],[-2.2,3.4],'--',color=C['asymp'],lw=1.2);ax.plot([-2.2,3.4],[2.2,-3.4],'--',color=C['asymp'],lw=1.2)
  tt=1.1;hx,hy=np.cosh(tt),np.sinh(tt)
  xs=np.linspace(0,hx,50)
  ax.fill_between(xs,np.sqrt(np.maximum(xs**2-1,0)),-np.sqrt(np.maximum(xs**2-1,0)),alpha=0.15,color=C['hl'])
  ax.plot([0,hx],[0,hy],color=C['sin'],lw=2)
  ax.plot(hx,hy,'o',color=C['sin'],ms=9,zorder=5)
  ax.annotate(r'$(\cosh t,\sinh t)$',(hx,hy),xytext=(hx+0.15,hy+0.18),fontsize=17,color=C['sin'],fontweight='bold')
  ax.annotate(r'$t$',(0.42,0.16),fontsize=17,color=C['fg'],fontweight='bold')
  ax.plot([-1.9,3.2],[0,0],color='#bbb',lw=1);ax.plot([0,0],[-1.9,1.9],color='#bbb',lw=1)
  ax.text(3.0,0.12,r'$x$',fontsize=15);ax.text(0.12,1.7,r'$y$',fontsize=15)
  ax.text(1.05,1.55,r'asymptotes $y=\pm x$',fontsize=13,color='#888')
  ax.annotate(r'$\cosh^2 t-\sinh^2 t=1$',(-1.8,-1.6),fontsize=15,color=C['tan'],fontweight='bold')
  fig.suptitle(r'Circle vs Hyperbola: The Same Parametrization Idea',fontsize=22,fontweight='bold',y=1.0)
  sv('11c1-hyperbola-analogy.png',fig)

def c2():
  fig,axes=plt.subplots(2,1,figsize=(10,9))
  x=np.linspace(-3,3,600)
  ax=axes[0]
  ax.plot(x,np.cosh(x),color=C['cos'],lw=2.5,label=r'$\cosh x$')
  ax.plot(x,np.sinh(x),color=C['sin'],lw=2.5,label=r'$\sinh x$')
  ax.plot(x,np.tanh(x),color=C['tan'],lw=2.5,label=r'$\tanh x$')
  ax.axhline(1,color=C['asymp'],ls='--',lw=1);ax.axhline(-1,color=C['asymp'],ls='--',lw=1)
  ax.set_ylim(-3.5,3.5);ax.set_ylabel(r'$y$',fontsize=16);ax.legend(fontsize=15,loc='upper left')
  ax.set_title(r'$\cosh$, $\sinh$, $\tanh$',fontsize=19,fontweight='bold')
  ax=axes[1]
  eps=0.12
  xp=x[np.abs(x)>eps]
  ax.plot(xp,1/np.cosh(xp),color=C['sec'],lw=2.5,label=r'$\mathrm{sech}\,x$')
  ax.plot(xp,1/np.sinh(xp),color=C['csc'],lw=2.5,label=r'$\mathrm{csch}\,x$')
  ax.plot(xp,1/np.tanh(xp),color=C['cot'],lw=2.5,label=r'$\coth x$')
  ax.axvline(0,color=C['asymp'],ls='--',lw=1)
  ax.axhline(1,color=C['asymp'],ls='--',lw=1);ax.axhline(-1,color=C['asymp'],ls='--',lw=1)
  ax.set_ylim(-5,5);ax.set_ylabel(r'$y$',fontsize=16);ax.set_xlabel(r'$x$',fontsize=16)
  ax.legend(fontsize=15,loc='upper left')
  ax.set_title(r'$\mathrm{sech}$, $\mathrm{csch}$, $\coth$',fontsize=19,fontweight='bold')
  fig.suptitle(r'Hyperbolic Functions',fontsize=22,fontweight='bold',y=1.0)
  sv('11c2-hyperbolic-graphs.png',fig)

def c3():
  fig,ax=plt.subplots(figsize=(10,6))
  x=np.linspace(-3,3,600)
  ax.plot(x,np.exp(x),color=C['fg'],lw=2.5,label=r'$e^x$')
  ax.plot(x,np.cosh(x),color=C['cos'],lw=2.5,ls='--',label=r'$\cosh x=\frac{e^x+e^{-x}}{2}$')
  ax.plot(x,np.sinh(x),color=C['sin'],lw=2.5,ls='-.',label=r'$\sinh x=\frac{e^x-e^{-x}}{2}$')
  ax.plot(x,-np.exp(-x),color='#999',lw=1.2,ls=':',label=r'$-e^{-x}$')
  ax.set_ylim(-3.5,8);ax.set_xlabel(r'$x$',fontsize=16);ax.set_ylabel(r'$y$',fontsize=16)
  ax.legend(fontsize=15,loc='upper left')
  ax.set_title(r'$e^x=\cosh x+\sinh x$: Even + Odd Decomposition',fontsize=20,fontweight='bold')
  ax.annotate(r'$\cosh$ is the even part: $\frac{e^x+e^{-x}}{2}$',(1.4,np.cosh(1.4)),xytext=(0.5,6.6),fontsize=13,color=C['cos'],arrowprops=dict(arrowstyle='->',color=C['cos']))
  ax.annotate(r'$\sinh$ is the odd part: $\frac{e^x-e^{-x}}{2}$',(1.4,np.sinh(1.4)),xytext=(0.3,2.9),fontsize=13,color=C['sin'],arrowprops=dict(arrowstyle='->',color=C['sin']))
  sv('11c3-even-odd-decomposition.png',fig)

def c4():
  fig,ax=plt.subplots(figsize=(10,6))
  a=3;x=np.linspace(-6,6,600)
  ax.plot(x,a*np.cosh(x/a),color=C['cos'],lw=3,label=r'$y=3\cosh(x/3)$')
  ax.plot(x,3+x**2/6,color=C['tan'],lw=2,ls='--',label=r'parabola $3+x^2/6$ (near bottom)')
  ax.plot(0,3,'o',color=C['sin'],ms=8,zorder=5)
  ax.annotate(r'lowest point $(0,3)$',(0,3),xytext=(0.7,3.7),fontsize=14,color=C['sin'],fontweight='bold')
  ax.set_ylim(0,10);ax.set_xlabel(r'$x$',fontsize=16);ax.set_ylabel(r'$y$',fontsize=16)
  ax.legend(fontsize=15,loc='upper left')
  ax.set_title(r'Catenary: A Hanging Cable',fontsize=20,fontweight='bold')
  ax.annotate(r'$\cosh x\approx 1+\frac{x^2}{2}$ near $0$',(-5.8,9.3),fontsize=14,color=C['tan'])
  sv('11c4-catenary.png',fig)

def c5():
  fig,axes=plt.subplots(1,3,figsize=(15,5))
  x1=np.linspace(-3,3,400);x2=np.linspace(1,3.6,300);x3=np.linspace(-0.95,0.95,400)
  ax=axes[0];ax.plot(x1,np.arcsinh(x1),color=C['sin'],lw=2.5)
  ax.set_title(r'$\mathrm{arsinh}\,x$',fontsize=19,fontweight='bold');ax.set_xlabel(r'$x$',fontsize=15);ax.set_ylabel(r'$y$',fontsize=15)
  ax.text(-2.9,-2.3,r'domain: all real $x$',fontsize=13)
  ax=axes[1];ax.plot(x2,np.arccosh(x2),color=C['cos'],lw=2.5);ax.plot(x2,-np.arccosh(x2),color=C['cos'],lw=2.5,ls='--')
  ax.axvline(1,color=C['asymp'],ls='--',lw=1)
  ax.set_title(r'$\mathrm{arcosh}\,x$',fontsize=19,fontweight='bold');ax.set_xlabel(r'$x$',fontsize=15)
  ax.text(1.15,-1.4,r'domain $x\ge 1$',fontsize=13);ax.text(1.15,1.4,r'two branches',fontsize=13,color='#888')
  ax=axes[2];ax.plot(x3,np.arctanh(x3),color=C['tan'],lw=2.5)
  ax.axvline(1,color=C['asymp'],ls='--',lw=1);ax.axvline(-1,color=C['asymp'],ls='--',lw=1)
  ax.set_ylim(-3.5,3.5)
  ax.set_title(r'$\mathrm{artanh}\,x$',fontsize=19,fontweight='bold');ax.set_xlabel(r'$x$',fontsize=15)
  ax.text(-0.93,2.9,r'domain $|x|<1$',fontsize=13)
  fig.suptitle(r'Inverse Hyperbolic Functions',fontsize=22,fontweight='bold',y=1.0)
  sv('11c5-inverse-hyperbolic.png',fig)

if __name__=='__main__':
  print("Generating 11C...")
  [print(f"  OK {f.__name__}") or f() for f in [c1,c2,c3,c4,c5]]
  print("All done!")
