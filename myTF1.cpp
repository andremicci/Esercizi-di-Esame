
#include <iostream>
#include "TF1.h"
#include <cmath>
#include "TMath.h"
using namespace std;

class myTF1: public TF1{

public:
  using TF1 :: TF1;
  double zeros(double);
};

double myTF1 :: zeros(double xstart){


  double xnew=0;
  double x_zero;
  double x=xstart;
  double xn=x;

  while(abs(xn-xnew)>1e-06){

    double diff=Derivative(x);
    xnew=x-Eval(x)/diff;
    xn=x;
    x=xnew;
   }
  x_zero=xnew;
  
  return x_zero;

}

int main(){


  myTF1 f("f", "1-pow(x,3)",0,10);
  double x0= f.zeros(10);
  cout << x0 << endl;


  
  
  myTF1 f1("f", "log(2+pow(x,2))-2");
  double x1= f1.zeros(5);
  cout << x1 << endl;

}
  
