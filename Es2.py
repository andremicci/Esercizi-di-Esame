
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
plt.ion()

L=0.5
e0=8.65e-12
N=101

x=np.linspace(-L,L,N)
dx=x[1]-x[0]

y=np.copy(x)
X,Y=np.meshgrid(x,y)

V=np.zeros((N,N))
r=np.copy(V)


charge=np.zeros((N,N))
d=15
charge[int(N/2)-d,int(N/2)-d]=1e-06
charge[int(N/2)+d,int(N/2)+d]=+1e-06
charge[int(N/2)-d,int(N/2)+d]=-1e-06
charge[int(N/2)+d,int(N/2)-d]=-1e-06
nrep=200

fig=plt.figure()
fig.tight_layout()
ax = fig.add_subplot(111, projection="3d")

w=1.8

for iter in range(nrep):

    for i in range(1,N-1):
        for j in range(1,N-1):
            r[i,j]=0.25*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])+0.25*(1/e0)*charge[i,j]-V[i,j]
            V[i,j]=V[i,j]+w*r[i,j]

    
    #ax.plot_surface(X,Y,V,cmap='cool')
    #plt.pause(1e-06)
    #ax.clear()
    print(iter)


print("Rilassamento completato")
ax.plot_surface(X,Y,V,cmap='cool')
plt.show()

fig2=plt.figure()
ax2=fig2.add_subplot(1,1,1)

Ex,Ey=np.gradient(-V)
ax2.streamplot(X,Y,Ey,Ex)

fig3,ax3=plt.subplots()
ax3.plot(x,Ex[0])




plt.show(block=True)
    

    



    
    

    


    

