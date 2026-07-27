
#!/usr/bin/env python3
import numpy as np, matplotlib, os
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
C={'bg':'#f8f9fa','fg':'#1a1a2e','sin':'#e74c3c','cos':'#2980b9','tan':'#27ae60','csc':'#e67e22','sec':'#9b59b6','cot':'#1abc9c','asymp':'#ccc','hl':'#f1c40f','circ':'#2c3e50'}
D=300;F=16
A=os.path.join(os.path.dirname(__file__),'11A')
B=os.path.join(os.path.dirname(__file__),'11B')
os.makedirs(A,exist_ok=True);os.makedirs(B,exist_ok=True)
plt.rcParams.update({'font.family':'serif','font.size':F,'axes.facecolor':C['bg'],'figure.facecolor':'white','axes.edgecolor':'#333','axes.grid':True,'grid.color':'#e0e0e0','grid.alpha':0.4,'axes.spines.top':False,'axes.spines.right':False,'text.usetex':True,'pgf.rcfonts':False})
bb=dict(boxstyle='round,pad=0.12',facecolor='white',edgecolor='none',alpha=0.85)
def sv(n,fig,folder=A):
  plt.tight_layout();fig.savefig(os.path.join(folder,n),dpi=D,bbox_inches='tight');fig.savefig(os.path.join(folder,n.replace('.png','.pdf')),dpi=D,bbox_inches='tight');plt.close(fig)
def ar(ax,cx,cy,r,a1,a2,**kw):
  t=np.linspace(np.radians(a1),np.radians(a2),50);ax.plot(cx+r*np.cos(t),cy+r*np.sin(t),**kw)

def a1():
  fig,ax=plt.subplots(figsize=(6,6));ax.set_aspect('equal');ax.set_xlim(-1.8,1.8);ax.set_ylim(-1.8,1.8)
  ax.set_title(r"1 Radian",fontsize=22,fontweight='bold');r=1.2;th=1.0
  ax.add_patch(plt.Circle((0,0),r,fill=False,color=C['circ'],lw=2))
  ax.plot([0,r],[0,0],color=C['fg'],lw=2);ax.plot([0,r*np.cos(th)],[0,r*np.sin(th)],color=C['fg'],lw=2)
  a=np.linspace(0,th,100);ax.plot(r*np.cos(a),r*np.sin(a),color=C['sin'],lw=3)
  ar(ax,0,0,0.35,0,np.degrees(th),color=C['hl'],lw=2)
  ax.annotate(r'1 rad',(0.2,0.1),fontsize=16,color=C['hl'],fontweight='bold',bbox=bb)
  ax.annotate(r'$r$',(r/2,-0.15),fontsize=18,ha='center')
  ax.annotate(r'$r$',(r/2*np.cos(th/2),r/2*np.sin(th/2)+0.1),fontsize=18,ha='center',color=C['sin'],bbox=bb)
  ax.axhline(0,color='#999',lw=0.5);ax.axvline(0,color='#999',lw=0.5);sv('11a1-radian-definition.png',fig)

def a2():
  fig,ax=plt.subplots(figsize=(7,7));ax.set_aspect('equal');ax.set_xlim(-1.5,1.5);ax.set_ylim(-1.5,1.5)
  ax.set_title(r'Degrees $\leftrightarrow$ Radians',fontsize=22,fontweight='bold');ax.axis('off');r=1.2
  ax.add_patch(plt.Circle((0,0),r,fill=False,color=C['circ'],lw=2))
  deg=[0,30,45,60,90,120,135,150,180,210,225,240,270,300,315,330]
  ld=[r'$0^\circ$',r'$30^\circ$',r'$45^\circ$',r'$60^\circ$',r'$90^\circ$',r'$120^\circ$',r'$135^\circ$',r'$150^\circ$',r'$180^\circ$',r'$210^\circ$',r'$225^\circ$',r'$240^\circ$',r'$270^\circ$',r'$300^\circ$',r'$315^\circ$',r'$330^\circ$']
  lr=[r'$0$',r'$\frac{\pi}{6}$',r'$\frac{\pi}{4}$',r'$\frac{\pi}{3}$',r'$\frac{\pi}{2}$',r'$\frac{2\pi}{3}$',r'$\frac{3\pi}{4}$',r'$\frac{5\pi}{6}$',r'$\pi$',r'$\frac{7\pi}{6}$',r'$\frac{5\pi}{4}$',r'$\frac{4\pi}{3}$',r'$\frac{3\pi}{2}$',r'$\frac{5\pi}{3}$',r'$\frac{7\pi}{4}$',r'$\frac{11\pi}{6}$']
  for d,dl,rl in zip(deg,ld,lr):
    th=np.radians(d);ax.plot([0,r*np.cos(th)],[0,r*np.sin(th)],color='#ddd',lw=0.8);ax.plot(1.05*np.cos(th),1.05*np.sin(th),'o',color=C['fg'],ms=4)
    ax.annotate(dl,((r+0.4)*np.cos(th),(r+0.4)*np.sin(th)),fontsize=11,ha='center',va='center',color='#e74c3c',fontweight='bold')
    ax.annotate(rl,((r-0.4)*np.cos(th),(r-0.4)*np.sin(th)),fontsize=11,ha='center',va='center',color='#2980b9',fontweight='bold')
  ml=[Line2D([0],[0],color='#e74c3c',lw=2),Line2D([0],[0],color='#2980b9',lw=2)]
  ax.legend(handles=ml,labels=['Degrees','Radians'],fontsize=12,loc='upper right')
  sv('11a2-degree-radian-circle.png',fig)

print("Functions defined, now running main...")
# Just define, don't run yet
