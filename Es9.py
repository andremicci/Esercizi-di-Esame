import numpy as np
import matplotlib.pyplot as plt



G=1


x=float(input("Inserire x0 "))
vy=float(input("Inserire vy "))
M=float(input("Inserire M "))


v=np.array([0,vy])
r=np.array([x,0])
vnew=np.array([0,0])
rnew=np.array([0,0])
dt=0.001
tmax=200

x_plot=[r[0]]
y_plot=[r[1]]
n=1

def acc(r):
    return -M*G*r/(np.linalg.norm(r)**3)
    
    
for i in np.arange(0,tmax,dt):

    rnew=r+v*dt
    vnew=v+acc(rnew)*dt

    r=np.copy(rnew)
    v=np.copy(vnew)

    n+=1
    if n%500==0:
        x_plot.append(rnew[0])
        y_plot.append(rnew[1])
size=10

plt.plot(x_plot,y_plot)
plt.show()
    

    
