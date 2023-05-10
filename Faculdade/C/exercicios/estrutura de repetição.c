#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(){

char nome[20], nomemaior[20];
float av1,av2,media,mediamaior;

int cont;
mediamaior = 0;
media = (av1+av2)/2;

for (cont=0;cont < 4;cont++){

printf("Aluno %d\n",cont);

printf("Digite o seu nome: ");
scanf("%s",&nome[0]);

printf("Digite a nota da av1: ");
scanf("%f",&av1);

printf("Digite a nota da av2: ");
scanf("%f",&av2);



printf("\nAluno: %s\n", nome);
printf("Media Final: %.2f\n\n", media);


if(media > mediamaior){
    mediamaior = media;
    strcpy(nomemaior,nome);
}

}
printf("%s\n",nomemaior);
printf("%.2f",mediamaior);

}

