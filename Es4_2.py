from ROOT import *


file=open("Dati_es4.dat","r")
hist=TH1D("hist","",100,0,25)

for line in file:

    val=float(line)
    hist.Fill(val)


fun=TF1("fun","[0]*( (pow(x,2)*exp(-x/[1]))/(2*pow([1],3)))",0,30)
fun.FixParameter(0,1)
fun.SetParameter(1,hist.GetMean()/3.0)
hist.Fit("fun","MULTI 0")

theta=fun.GetParameter(1)
etheta=fun.GetParError(1)
fun.FixParameter(0,hist.GetEntries()*hist.GetBinWidth(1))
fun.FixParameter(1,theta)
hist.Draw()
fun.Draw("same")
print("theta=",theta,"+-",etheta)
gApplication.Run(True)
