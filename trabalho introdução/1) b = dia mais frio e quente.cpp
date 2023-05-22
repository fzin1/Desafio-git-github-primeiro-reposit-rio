#include <stdio.h>

int main() {
    int temperaturas[7];
    int i, diaMaisFrio, diaMaisQuente;

    for (i = 0; i < 7; i++) {
        printf("Digite a temperatura do dia %d: ", i+1);
        scanf("%d", &temperaturas[i]);
    }

    diaMaisFrio = 0;
    diaMaisQuente = 0;

    for (i = 1; i < 7; i++) {
        if (temperaturas[i] < temperaturas[diaMaisFrio]) {
            diaMaisFrio = i;
        }
        if (temperaturas[i] > temperaturas[diaMaisQuente]) {
            diaMaisQuente = i;
        }
    }


    printf("O dia mais frio da semana foi o dia %d, com temperatura de %d graus.\n", diaMaisFrio+1, temperaturas[diaMaisFrio]);
    
    printf("O dia mais quente da semana foi o dia %d, com temperatura de %d graus.\n", diaMaisQuente+1, temperaturas[diaMaisQuente]);

    return 0;
}
