
using namespace std;
#include <iostream>
#include <cmath>

double f(double x){
  return 1/x;
}
void Es17(){

  
  double x=1;
  double e=0.01;
    
  double fplus=0;
  double fmin=0;
  
 
  
  while(fabs(fplus-fmin) <0.01){

    fplus=fabs(f(x+e)-f(x));
    fmin=fabs(f(x-e)-f(x));
    e+=0.0001;
    

  }

  cout << "Il valore di epsilon per cui non vale più l'approssimazione lineare è: " << e << endl;


  double sigma=2*e;
  TRandom3 rnd;
  TH1D *h=new TH1D("h","h",100,0,2);
  int ntot=1000000;
  for(int i=0;i<ntot;i++){

    double val= rnd.Gaus(x,sigma);
    if (val !=0){
	h->Fill(f(val));}
    
   }

  h->Draw();
  double err=h->GetRMS();
  cout << "f(x)=( "<< x << "+-" << err << ")" << endl;

}
