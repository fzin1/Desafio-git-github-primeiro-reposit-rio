#include <stdio.h>
#include <string.h>

int main() {
    char nome[50];
    int num=0, i, nome_tamanho;

    printf("Digite um nome: ");
    scanf("%s", nome);
    nome_tamanho = strlen(nome);
    for (i = 0; i < nome_tamanho; i++) {
        if (nome[i] == 'A' || nome[i] == 'a') {
            num++;
        }
    }

	if(num==1){
	
    printf("\nA letra 'a' se repete no seu nome %d vez ", num);
}else{

	printf("\nA letra 'a' se repete no seu nome %d vezes ", num);
}

    return 0;
}
