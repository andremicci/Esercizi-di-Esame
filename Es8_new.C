


void Es8_new(){


  ifstream file("Dati_es8.dat");
  TH1D *h=new TH1D("h","h",80,-1,1);
  double x;
  
  while(file >> x){
    h->Fill(x);
    
  }

  
  h->Draw();
  double mat[3][3];
  
  TTree *tree=new TTree();
  tree->ReadFile("Dati_es8.dat","x/D");
  
  TF1 *f1=new TF1("f1","[0]*(3/(6+2*[2]))*(1+[1]*x+[2]*pow(x,2))",-1,1);
  f1->FixParameter(0,1);
  
  //TF1 *f1=new TF1("f1","[0]*(1+[1]*x+[2]*pow(x,2))",-1,1);
  //f1->FixParameter(3,1);
  
  tree->UnbinnedFit("f1","x");
  gMinuit->mnemat(&mat[0][0],3);

  double alpha=f1->GetParameter(1);
  double e_alpha=f1->GetParError(1);
  double beta=f1->GetParameter(2);
  double e_beta=f1->GetParError(2);

  double k=f1->GetParameter(0);
  f1->FixParameter(0,h->GetEntries()*h->GetBinWidth(2));
  f1->Draw("same");
		
  
  
  cout <<"alpha= "<< alpha << " +- " << e_alpha << endl;
  cout <<"beta= "<< beta << " +- " << e_beta << endl;
  cout <<"COV[alpha,beta]=  "<<  mat[1][2] << endl;
   
  
  double rho=mat[1][2]/(e_alpha*e_beta);
  cout <<"coefficiente di correlazione: " <<  rho << endl;
  double gamma=3*alpha-2*beta;
  double e_gamma=sqrt( abs(3*pow(e_alpha,2) + pow(2*e_beta,2) -2*rho*6*e_beta*e_alpha ));

  cout << "La miglior stima per gamma è: " << gamma << "+- "<< e_gamma<< endl;

 
  

 
  
}
