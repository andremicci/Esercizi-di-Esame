import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from ROOT import *
from IPython.display import display, clear_output
import time

#Soluzione dell'equazione dell'oscillatore armonico forzato
def a(x,t):
    return (A*np.sin(w*t)-k*x)/m

def Verlet_solve():
    global x
    global v
    x_n=x
    x=x+h*v+(0.5*h**2)*a(x,t)
    v=v+h*0.5*(a(x,t+h)+a(x_n,t))
    return x
    

A=0.1 #N
m=1 #kg
w=0.25 #rad/s
k=0.25 #N/m

h=0.001
Tmax=100

x_plot=[]
v_plot=[]
t_plot=[]

x_plot.append(1)
t_plot.append(0)
x=1
v=0
t=0

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.xlabel('t')
plt.ylabel('x')

i=0
while t<Tmax:

    x_t=Verlet_solve()

    t_plot.append(t)
    x_plot.append(x_t)
    
    if not i%500:
        ax.set_xlim(0, Tmax)
        ax.set_ylim(-2,2)
        ax.plot(t, x_t, 'b.', linewidth=20, markersize=5)
        plt.pause(0.001)
    t=t+h
    i+=1
    
f2=plt.figure()
ax2=f2.add_subplot(1,1,1)
plt.xlabel('t')
plt.ylabel('x')
ax2.plot(t_plot,x_plot)
plt.show()

