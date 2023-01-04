import numpy as np
import matplotlib.pyplot as plt
import time
import matplotlib.animation as animation



def solution(x,t):
    sigma=np.sqrt(2*k*t)
    x0=L/2
    if t==0 :
        return T0
    else:
        
        return (1/np.sqrt(2*np.pi*sigma))*np.exp(- (x-x0)**2/(2*sigma*2))


k=2
L=10
N=100
x=np.linspace(0,L,N)
T=np.zeros(N)
T0=100
T[50]=T0

dx=x[1]-x[0]
dt=0.0001
eta=(2*k*dt)/(dx**2)
n=0
tmax=10



fig=plt.figure()
ax=plt.subplot()
line,=ax.plot(x,T)
line2,=ax.plot(x,solution(x,1e-07))


     

nframes=int(tmax/dt)
frames=np.zeros((nframes,N))
frames[0]=T

for t in np.arange(0,tmax,dt):
    
    T_new=np.zeros(N)
    T_new[0]=T[0]+eta*(T[1]-2*T[0])
    T_new[N-1]=T[N-1]+eta*(T[N-2]-2*T[N-1])

    T_new[1:N-1]=T[1:N-1]+eta*(T[2:N]+T[0:N-2]-2*T[1:N-1])
   
    T=np.copy(T_new)
    
    frames[n]=T_new

    n+=1
    

def animate(i):
    
    plt.ylim(0,T0/3)
    plt.xlim(0,L)
    
    line.set_xdata(x)
    line.set_ydata(frames[50*i])
    
    line2.set_xdata(x)
    line2.set_ydata(solution(x,50*i*dt))

    
    ax.relim()
    ax.autoscale_view()
    return line2,line


ani = animation.FuncAnimation(fig, animate, frames=range(100), blit=True)
plt.show()



 
'''
    if n%50==0:
        plt.ylim(0,T0/3)
        plt.xlim(0,L)
        line.set_xdata(x)
        line.set_ydata(T_new)
        ax.relim()  # Ricalcola i limiti dell'asse in base ai nuovi dati
        ax.autoscale_view()  # Ridisegna il grafico con i nuovi limiti dell'asse
          # Aggiorna il grafico
        #ax.plot(x,solution(x,t)
        fig.canvas.flush_events()
        time.sleep(0.001)
'''
   
