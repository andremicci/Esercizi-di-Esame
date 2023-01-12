from ROOT import *
from scipy import stats

rnd=TRandom3()
rnd.SetSeed(123456789)

ntot=1000

x0=10
delta=2
sigma=2

h=TH1D("h","h",60,0.,20)
val=[]

for i in range(ntot):

    x_p=rnd.Gaus(x0,sigma)
    x=2*delta*rnd.Rndm()+x_p-delta
    h.Fill(x)
    val.append(x)
    
h.Draw("COLZ")

#test unbinned : kolmogorov test

e=stats.norm(loc=x0,scale=sqrt((delta/sqrt(3.0))**2+sigma**2))
D,p=stats.kstest(val,e.cdf)
print("p-Value=",p)

if p<0.05:
    print("il p-value è minore di 0.05, quindi l'ipotesi nulla (cioè che i dati seguano la pdf)  è rigettata")
else:
    print("Ipotesi nulla accettata")

                 
gApplication.Run(True)
