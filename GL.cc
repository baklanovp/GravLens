#include <stdio.h>
#include <math.h>
#define NUMNUM 3000


double mvec(double x, double y){       //modul of vector
    return (double) sqrt(x*x+y*y);
}

double theta(double m, double p){        //function of deflection angle
    return m/p;
}

double rn(){
  return  (double)(rand())/RAND_MAX;
}

// double mdist(double mrand, double power, double min_mass, double max_mass){
//   return  (pow(mrand*(pow(max_mass,(1+power))-(min_mass,(1+power)))+pow(min_mass,(1+power))),(1/(1+power)));
// }

int main()
{


  double gamma=0.1;
  double kappac=0.0;

  double pix=10;
  double xx0=-pix;
  double yy0=-pix;
  double xxe=pix;
  double yye=pix;

  double vecx, vecy, vx, vy;
  int obj, lens = 0;


  double dx, dy;
  dx=(xxe-xx0)/NUMNUM;
  dy=(yye-yy0)/NUMNUM;

  double objectx;
  double objecty;

  int Nlens=1;
  double lensposx[]={0.92, -0.92};
  double lensposy[]={0.0001, 0.0001};
  double m[]={0.2, 2};

//   int Nlens=1000;
//   double lensposx[Nlens];
//   double lensposy[Nlens];
//   double m[Nlens];
//   double power=-1.3;
//   double min_mass=0.01;
//   double max_mass=2;
//   double mm;
//   printf("Generation lenses...\n");
//   FILE *fpos = fopen ("lenspos","w");
//   if (fpos!=NULL)
//   {
//   for(int lens=0; lens<=Nlens; lens++){
//       lensposx[lens]=rn()*2*pix-pix;
//       lensposy[lens]=rn()*2*pix-pix;
//       mm=rn()*1;
//       // m[lens]=mdist(mm, power, min_mass, max_mass);//((mm*(max_mass**(1+power)-min_mass**(1+power))+min_mass**(1+power))**(1/(1+power)));
//       m[lens]=pow(mm*(pow(max_mass, 1+power)-pow(min_mass, 1+power))+pow(min_mass, 1+power),(1/(1+power)));
//       fprintf(fpos,"%10.8f    %10.8f    %10.8f\n",lensposx[lens], lensposy[lens], m[lens]);
//   }
// }
// fclose (fpos);


  double th, modvec;
  printf("Generation map amplification...\n");

  double vsumx=0.0;
  double vsumy=0.0;

  int cc = 1;

FILE *fp = fopen ("INPUT","w");
if (fp!=NULL)
{


  for(int i=0; i<NUMNUM; i++){
    for(int j=0; j<NUMNUM; j++){
      objecty=j*dy+yy0;
      objectx=i*dx+xx0;

      for(int lens=0; lens<=Nlens; lens++){
            modvec=mvec((lensposx[lens]-objectx),(lensposy[lens]-objecty));
            th=theta(m[lens], modvec);
            vecx=(lensposx[lens]-objectx)/modvec*th;
            vecy=(lensposy[lens]-objecty)/modvec*th;

            vsumx=vsumx+vecx;
            vsumy=vsumy+vecy;

          }
          vx=vsumx+objectx-kappac*objectx+gamma*objectx;
          vy=vsumy+objecty-kappac*objectx-gamma*objecty;

          fprintf(fp,"%10.8f    %10.8f \n",vx, vy);
          vsumx=0.0;
          vsumy=0.0;
        }
    }

  fclose (fp);
};
printf("Done!\n");
}
