#include<stdio.h>
#include<stdlib.h>
#include<locale.h>

int main(){

	setlocale(LC_ALL, "portuguese");

	int opcao;
	float n1,n2,resultado;

	printf("----- MENU -----\n");
	printf("|1 - Soma       |\n");
	printf("|2 - subtrair   |\n");
	printf("|3 - multiplicar|\n");
	printf("|4 - dividir    |\n\n");
	do{
	printf("Selecione uma opcao (1-4): ");

	scanf("%d",&opcao);

	switch(opcao){

	    case 1:


	    	printf("Digite o primeiro numero: ");
			scanf("%f",&n1);
			printf("Digite o segundo numero: ");
			scanf("%f",&n2);
			resultado = n1+n2;
			printf("O resultado foi: %.1f",resultado);
			break;

		case 2:

		printf("Digite o primeiro numero: ");
			scanf("%f",&n1);
			printf("Digite o segundo numero: ");
			scanf("%f",&n2);
			resultado = n1-n2;
			printf("O resultado foi: %.1f",resultado);
			break;

		case 3:

		printf("Digite o primeiro numero: ");
			scanf("%f",&n1);
			printf("Digite o segundo numero: ");
			scanf("%f",&n2);
			resultado = n1*n2;
			printf("O resultado foi: %.1f",resultado);
			break;

		case 4:

		printf("Digite o primeiro numero: ");
			scanf("%f",&n1);
			printf("Digite o segundo numero: ");
			scanf("%f",&n2);
			resultado = n1/n2;
			printf("O resultado foi: %.1f",resultado);
			break;

		default:
			printf("\nOpção inválida. Tente novamente.\n\n");

	 }

	} while (opcao > 4);

}
