import matplotlib.pyplot as plt
import numpy as np
import sys
'''
6. (Esame 04/02/19) Si risolva il problema di una corda vibrante di lunghezza L = 20 m che all’istante t = 0 ha la
forma y = sin[π(x/L)π]. Gli estremi restano vincolati a y = 0 durante il moto. La velocità di propagazione è
v = 1 m/s. Si disegni l’andamento del punto centrale (y per x = L/2) in funzione del tempo.
'''
L=20 #m
N=601
t=0
tmax=5
x=np.linspace(0,L,N)
y=np.sin(3*np.pi*(x/L))
y[0]=0
y[N-1]=0



v=1
dx=x[1]-x[0]
dt=0.001
v_simulation=dx/dt
print(v_simulation)

x_med_index=np.argmin(np.abs(x - L/2))
t_plot=[0]
x_med=[y[x_med_index]]

plt.ion()
fig=plt.figure()
ax0=fig.add_subplot(111)
bb,=ax0.plot(x,y)


if v>v_simulation:
    print("Stabilita non garantita")
    sys.exit()
    
y_old=np.copy(y)
y_new=np.zeros(N)

y_new[1:N-2]=y[1:N-2]+(v/v_simulation)**2*(y[2:N-1]+y[0:N-3]-2*y[1:N-2])

i=0
while t<tmax:
    
    y_new[1:N-2]=2*y[1:N-2]-y_old[1:N-2]+(v/v_simulation)**2*(y[2:N-1]+y[0:N-3]-2*y[1:N-2])
    y_old=np.copy(y)
    
    y=np.copy(y_new)
    i+=1
    if(not i%60):
        plt.ylim(-2,2)
        plt.xlim(0,L)
        bb.set_xdata(x)
        bb.set_ydata(y_new)
        
        fig.canvas.flush_events()
        plt.pause(0.1)

    x_med.append(y[x_med_index])
    t_plot.append(t)
          
    t=t+dt

fig2=plt.figure()
plt.plot(t_plot,x_med)
plt.show(block=True)

