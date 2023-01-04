{

  double x1=1;
  double x2=2;
  double ex1,ex2=0.1;

  double diff=x2-x1;
  double ediff=0;

  cout <<" La miglior stima per la differenza è (rho=1):( "<< diff << "+-" << ediff << ")"<< endl;
  
  //In funzione di rho:
  TF1 *f=new TF1("sigma vs. rho","sqrt( 2*pow(0.1,2)*(1-x) )",0,1);
  f->SetTitle("sigma vs. rho");
  f->Draw();

  
}

