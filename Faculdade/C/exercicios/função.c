#include<stdio.h>
#include<stdlib.h>


void calculo(int n1, int n2){

float s = n1+n2;


printf ("\nSoma: %.0f",s);
printf ("\nMedia: %.1f\n",s/2);


}


int maior(int n1, int n2){

if(n1>=n2){
 return n1;
}else

 return n2;


}


main(){

int a,b;

printf("Numero 1: "); scanf("%d",&a);
printf("Numero 2: "); scanf("%d",&b);

calculo(a,b);

printf("maior numero: %d\n",maior (a,b));
}
