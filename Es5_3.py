import numpy as np
import matplotlib.pyplot as plt

m=1
k=0.25
A=0.1
w=0.25

def a(x,t):
    return -(A/m)*np.sin(w*t)-(k/m)*x



h=0.001
t=0
tmax=100
N=int(tmax/h)

x=np.zeros(N)
v=np.zeros(N)
t=np.arange(0,tmax,h)

#condizioni iniziali:
x[0]=1
v[0]=0

for i in range(N-1):

    x[i+1]=x[i]+h*v[i]+0.5*h**2*a(x[i],t[i])
    v[i+1]=v[i]+0.5*h*(a(x[i+1],t[i+1])+a(x[i],t[i]))



plt.plot(t,x)
plt.show()
