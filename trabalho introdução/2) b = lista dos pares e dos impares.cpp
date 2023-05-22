#include <stdio.h>
#include <stdlib.h>

int main() {
    int n1, i, SP, SI;
    
    do {
        printf("Digite um numero ");
        scanf("%d", &n1);
        if(n1<0){
            printf("Obrigado por jogar");
            break;
        }
        SP=0;
        SI=0;
        printf("\nPares: ");
        for(i=0; i<n1;i+=2){
            if(i%2 == 0){
                printf("%d - ", i);
                SP = SP + i;
            }
        }
        printf("\nSoma dos pares: %d\n", SP);
        printf("\nImpares: ");
        for(i=1; i<n1; i++) {
            if(i%2 != 0){
                printf("%d - ", i);
                SI += i;
            }
        }
        printf("\nSoma dos impares: %d\n", SI);
        printf("\n");
        system("pause");
        system("cls");
    } while(n1>=0);
    return 0;
}

