#include <iostream>
#include "TRandom3.h"
#include "TApplication.h"
#include "TMath.h"
#include "TGraph.h"
#include "TH1D.h"
#include <cmath>
#include "TF1.h"
/*
(Esame 21/01/19) L’area del cerchio (sfera 2D) vale πr 2 , il volume della sfera 3D vale 4/3πr 3 . Non è difficile
immaginare che la sfera 4D abbia volume αr 4 . Determinare α con il metodo Monte Carlo. Verificare che il valore
n/2
tenda a Γ π n +1 r n (n dimesioni della sfera) all’aumentare di N (numero di estrazioni). La funzione Γ (Gamma) è
( 2 )
disponibile in ROOT (TMath).*/


using namespace std;


double VOLn(double r,double n){

  return ((pow(TMath::Pi(),n*0.5)*pow(r,n)))/(TMath::Gamma(n*0.5+1));}

int main(){

  auto app=new TApplication("app",0,NULL);

  TRandom3 rnd;
  rnd.SetSeed(123456);

  
		      
  /*

  int N=1000; //iterazioni
  int n_max=4; //dimensione sfera
  double r=1;
  vector<double> X(n_max);
  vector<double> Volumi(n_max);
  int n_acc=0;
  
  int n=1;
  /*
  while(n<n_max){

    n_acc=0;
  
        for(int i=0;i<N;i++){
    
	  double R2_tmp=0;
  
	  for(int i=0;i<n;i++){
	    
	    X[i]=2*r*rnd.Rndm()-r;
	    R2_tmp=R2_tmp+X[i]*X[i];}
  
	  if(R2_tmp<r*r){
	    n_acc++;
	  }
    
	}
  
     double Vol_tot=pow(2*r,n);
     double p=n_acc/N;
     double Vol=Vol_tot*p;
     if(n==4){
       
       double  alpha=Vol/pow(r,4);
       double Vol4=VOLn(r,4);
       cout << "alpha= "<< alpha << endl;
       cout << "Vol4= " << Vol4 << endl;
     }

     Volumi[n]=Vol;
     n++;
  
  }
 */
  
  double N=100000;
  double n=4;
  double r=1;
  double n_acc=0;

  int i=1;
  int npoint=0;

  cout << VOLn(r,n) << endl;

  auto  gr=new TGraph();
  
  double Vol_tot=pow(2*r,4);
    
  
  while(i<N){

    double x1=2*r*rnd.Rndm()-r;
    double x2=2*r*rnd.Rndm()-r;
    double x3=2*r*rnd.Rndm()-r;
    double x4=2*r*rnd.Rndm()-r;

    double R2=x1*x1+x2*x2+x3*x3+x4*x4;
     if(R2<r*r){
      n_acc++;
     }
   
    if(!(i%100)){
      
    double p=n_acc/i;
    double Vol=Vol_tot*p;
    double alpha=Vol/pow(r,4);
   
    gr->SetPoint(npoint,i,alpha);
    npoint++;
    }
    i++;
    
  }

  gr->SetMarkerStyle(7);

  auto f=new TF1("lin","[0]");
  f->SetParameter(0,VOLn(r,n)/pow(r,n));
  cout << VOLn(r,n)/pow(r,n) << endl;
  gr->Draw("AP");
  f->Draw("same");
  
  
 app->Run(true);
  return 0;
  
}
