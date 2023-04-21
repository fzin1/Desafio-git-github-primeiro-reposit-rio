#include<stdlib.h>
#include<stdio.h>
#include<locale.h>

int main(){
	
	setlocale(LC_ALL, "portuguese");

  int produto, qtd_produto,qtd_total_produto;
  float valor_produto=0, valor_total;
  

printf("Digite o número do produto: "); scanf("%d",&produto);
 if (produto < 0){
 	printf("Opção inválida, tente novamente");

 }
 
 else{
 
while (produto != 0) {


	printf("Digite o valor do produto: "); 
	scanf("%f",&valor_produto);
if (valor_produto < 0) {
		printf("Digite um valor acima de 0\n");
		continue;
	}
else{
	
	qtd_produto += 1;
	valor_total = valor_produto + valor_total;
	
	printf("Digite o número do novo produto: "); 
	scanf("%d",&produto);
}
}
}

printf("O valor total da compra foi: %.2f\n",valor_total);
printf("A quantidade de produtos comprados foi: %d",qtd_produto);
}











 	
	
	



	
	
	

	
	
	
