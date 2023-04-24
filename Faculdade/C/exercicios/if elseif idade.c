#include<stdio.h>
#include<stdlib.h>

int main(){

int idade;

printf("Qual a sua idade?: ");
scanf("%d",&idade);
if (idade<0 || idade > 130)
    printf("voce nao existe");

else if (idade<18)
    printf("Voce e jovem");


else if(idade<=60)
    printf("Voce e adulto");


else
    printf("Voce e idoso");

}





