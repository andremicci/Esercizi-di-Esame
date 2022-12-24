


void Es8(){


  ifstream file("Dati_es8.dat");
  TH1D *h=new TH1D("h","h",80,-1.1,1.1);

  
  double x;
  
  while(file >> x){
    h->Fill(x);
    
  }

  
  h->Draw();
  double mat[3][3];
  cout << endl;
  cout << endl;
  cout << "Fit likelihood binned" << endl;
  
  TF1 *f=new TF1("f","(3/(6+2*[2]))*(1+[1]*x+[2]*pow(x,2))*[0]",-1.1,1.1);
  f->FixParameter(0,h->GetEntries()*h->GetBinWidth(1));
  
  //f->SetParameter(2,);
  h->Fit("f","0 MULTI");

  f->Draw("same");
  
  gMinuit->mnemat(&mat[0][0],3);
  
  double alpha=f->GetParameter(1);
  double e_alpha=f->GetParError(1);
  double beta=f->GetParameter(2);
  double e_beta=f->GetParError(2);
  
  
  cout <<"alpha= "<< alpha << " +- " << e_alpha << endl;
  
  cout <<"beta= "<< beta << " +- " << e_beta << endl;
  cout <<"COV[alpha,beta]=  "<<  mat[1][2] << endl;

  double rho=mat[1][2]/(e_alpha*e_beta);
  cout <<"coefficiente di correlazione: " <<  rho << endl;
  double gamma=3*alpha-2*beta;
  double e_gamma=sqrt( abs(3*pow(e_alpha,2) - 2*pow(e_beta,2) -2*rho*6*e_beta*e_alpha ));

  cout << "La miglior stima per gamma è: " << gamma << "+- "<< e_gamma<< endl;

  cout << "------------______---------__________-------__________------_________------__________------_________-----________------______------______"<< endl;
  cout << " Unbinned likelihood fit con TTree" << endl;

      
  TTree *tree=new TTree();
  tree->ReadFile("Dati_es8.dat","x/D");
  
  f->FixParameter(0,1);
  f->SetParameter(2,-2);
  //tree->UnbinnedFit("f","x");
  f->FixParameter(0,h->GetEntries()*h->GetBinWidth(1));
 

 
  
}
