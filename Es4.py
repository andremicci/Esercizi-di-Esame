from   ROOT    import *
from   iminuit import Minuit
import numpy   as     np
from   math    import *

#faccio un fit di ML

def logl(theta):
    f=0.0
    for i in range(len(x)):
        f=f+3*np.log(theta)+x[i]/theta
    return f

hist=TH1D("hist"," ",100,0.,0.)
x=[]

for line in open("Dati_es4.dat"):
    val=float(line)
    hist.Fill(val)
    x.append(val)

m=Minuit(logl,theta=hist.GetMean()/3.0)
m.errordef=0.5
m.print_level=2
m.migrad()
theta=m.values[0]
etheta=m.errors[0]
fun=TF1("fun","[0]*( (pow(x,2)*exp(-x/[1]))/(2*pow([1],3)))",0,30)
fun.FixParameter(0,hist.GetEntries()*hist.GetBinWidth(1))
fun.FixParameter(1,theta)
hist.Draw()
fun.Draw("same")


print("theta= ",round(theta,1))
print("etheta= ",round(etheta,1))



gApplication.Run(True)




        
