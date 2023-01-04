
from ROOT import *
import numpy as np
import math as m
import matplotlib.pyplot as plt
import  scipy.stats as stats




rnd=TRandom3()
rnd.SetSeed(192239)
h=TH1D("h","h",150,0.0,60)


mu=30
x1=np.array([])

ntot=50000
for i in range(ntot):

    N=0
    S=0
    while True:
        
        dt=-np.log(1-rnd.Rndm())
        S=S+dt
        
        N=N+1
        if S>mu:
            break

    
    h.Fill(N-1)
    x1=np.append(x1,N-1)
    


h.Draw()

D,pvalue=stats.ks_1samp(x1,stats.poisson.pmf,(30,))
print(pvalue)



'''
h2=TH1D("h2","h2",100,0,60)

f=TF1("f","TMath::Poisson(x,30)",0,60)
x2=np.array([])

for i in range(1,h.GetNbinsX()):
    xmin=h.GetBinLowEdge(i)
    xmax=h.GetBinLowEdge(i)+h.GetBinWidth(i)
    nu=f.Integral(xmin,xmax,100)
    h2.SetBinContent(i,h.GetEntries()*nu)
    x2=np.append(x2,nu*h.GetEntries())

h2.SetLineColor(kRed)
h2.Draw("SAME")

#non posso fare il test del chi2 perche ci sono bin con meno di 5 valori.
#kolmogorov non riesco a farlo
#Likelihood (perchè dovrei?:Non voglio mica testare che il parametro sia quello)


#p=h.Chi2Test(h2)
#print(p)
D,p=stats.ks_2samp(x1,x2)
print(p)




'''
'''
f=TF1("f","[1]*TMath::Poisson(x,[0])",0,60)
f.FixParameter(1,h.GetEntries())
f.SetParameter(0,30)
h.Fit("f")
print(f.GetProb())

'''

gApplication.Run(True)
