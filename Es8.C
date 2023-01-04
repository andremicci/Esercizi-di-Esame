


void Es8(){


  ifstream file("Dati_es8.dat");
  TH1D *h=new TH1D("h","h",80,-1.1,1.1);

  
  double x;
  
  while(file >> x){
    h->Fill(x);
    
  }

  
  h->Draw();
  double mat[3][3];
  
  TTree *tree=new TTree();
  tree->ReadFile("Dati_es8.dat","x/D");
  
  TF1 *f1=new TF1("f1","(3/(6+2*[1]))*(1+[0]*x+[1]*pow(x,2))",-1.1,1.1);
  tree->UnbinnedFit("f1","x","x>-1");

 
 
  gMinuit->mnemat(&mat[0][0],2);

  double alpha=f1->GetParameter(0);
  double e_alpha=f1->GetParError(0);
  double beta=f1->GetParameter(1);
  double e_beta=f1->GetParError(1);

  TF1 *f2=new TF1("f2","[0]*(3/(6+2*[2]))*(1+[1]*x+[2]*pow(x,2))",-1.1,1.1);
  f2->FixParameter(0,h->GetEntries()*h->GetBinWidth(1));
  f2->FixParameter(1,alpha);
  f2->FixParameter(2,beta);
  f2->Draw();
  
 
  
  cout <<"alpha= "<< alpha << " +- " << e_alpha << endl;
  cout <<"beta= "<< beta << " +- " << e_beta << endl;
  cout <<"COV[alpha,beta]=  "<<  mat[0][1] << endl;
 
  

 
  
}
