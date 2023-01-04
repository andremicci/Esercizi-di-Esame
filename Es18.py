import numpy as np
from ROOT import *

rnd=TRandom3()
rnd.SetSeed(1234)
ntot=100000
h=TH1D("h","h",100,-0.1,1.1)

f=open("dat18.dat","w")

for i in range(ntot):

    eta=rnd.Rndm()
    x=np.cbrt(eta)
    h.Fill(x)
    f.write(repr(x)+"\n")

h.Draw()
f.close()

tree=TTree()
tree.ReadFile("dat18.dat","x/D")

f=TF1("f","[0]*pow(x,[0]-1)*[1]",0,1)
f.SetParameter(0,3)
f.FixParameter(1,1)
tree.UnbinnedFit("f","x")

f.FixParameter(1,h.GetEntries()*h.GetBinWidth(1))
f.Draw("same")
gApplication.Run(True)

    
