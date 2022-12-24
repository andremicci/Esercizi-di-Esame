/*#include <iostream>
#include "TGraph.h"
#include "TH1D.h"
#include "TF1.h"
#include "TApplication.h"
#include "TMinuit.h"
#include <fstream>
#include <vector>
using namespace std;*/
{

namespace data{
  vector<double> x;
}


void logl(int &npar, double *gin, double &f, double *par, int iflag){
  
  f = 0.0;
  for(int i=0;i<data::x.size();i++){
    f+=3*log(par[0])+data::x[i]/par[0];
  }
}


//int main(){

    auto app=new TApplication("app",0,NULL);

    auto h=new TH1D("h","h",100,0.,0.);

    ifstream file("Dati_es4.dat");
    double val;
    //vector<double> x;
    
    while(file >> val){
      h->Fill(val);
      data:: x.push_back(val);
      
    }

    h->Draw();
    
    
    TMinuit minuit(1);
    minuit.SetFCN(logl);
    minuit.SetErrorDef(0.5);
    minuit.DefineParameter(0,"theta",(1.0/3.0)*h->GetMean(),(1.0/3.0)*h->GetRMS(),0.,0.);

    minuit.Command("MIGRAD");
    double theta,etheta;
    minuit.GetParameter(0,theta,etheta);
    cout << "theta= " << theta << endl;
    cout << "etheta= "  << etheta << endl;
    

    app->Run(true);
    // return 0;
//}
}
