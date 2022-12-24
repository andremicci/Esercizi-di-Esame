/*4. (Esame 21/01/19) Sono state effettuate n misure x 1 , ..., x n di una grandezza X distribuita secondo (file DatiGamma.dat)
la distribuzione:
f (x, θ) =
x 2 exp(−x/θ)
2θ 3
• Si determini la miglior stima del parametro theta e il suo errore.
• Si sovrapponga la distribuzione (con il parametro determinato al punto precedente) ai dati.
*/


using namespace std;


namespace data{
  vector<double> x;
}


void logl(int &npar, double *gin, double &f, double *par, int iflag){
  
  f = 0.0;
  for(int i=0;i<data::x.size();i++){
    f+=3*log(par[0])+data::x[i]/par[0];
  }
}

 void Es4(){

    auto app=new TApplication("app",0,NULL);

    auto h=new TH1D("h","h",100,0.,0.);

    ifstream file("Dati_es4.dat");
    double val;
    
    
    while(file >> val){
      h->Fill(val);
      data:: x.push_back(val);
      
    }

    h->Draw();
    
    
    TMinuit minuit(1);
    minuit.SetFCN(logl);
    minuit.SetErrorDef(0.5);
    minuit.DefineParameter(0,"theta",(1.0/3.0)*h->GetMean(),0.01,0.,0.);

    minuit.Command("MIGRAD");
    double theta,etheta;
    minuit.GetParameter(0,theta,etheta);
    
    cout << "La miglior stima per il parametro theta è:" << endl;
    cout << "theta= " << theta << endl;
    cout << "etheta= "  << etheta << endl;

    TF1 f("f","[1]*((x*x*exp(-x/[0]))/(2*pow([0],3)))",0,25);
    f.FixParameter(0,theta);
    f.FixParameter(1,h->GetEntries()*h->GetBinWidth(1));
    f.Draw("same");
    

    app->Run(true);
 }
