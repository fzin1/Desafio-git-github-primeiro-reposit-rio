#include <stdio.h>

void squart(int num) {
    if (num == 0) { 
        printf("obrigado por jogar");
        return;
    }
    int bits[32]; 
    int i = 0;
    while (num > 0) {
        bits[i] = num % 2; 
        num /= 2; 
        i++;
    }
    for (int j = i - 1; j >= 0; j--) {
        printf("%d", bits[j]); 
    }
}

int main() {
    int num;
    do {
        printf("Digite um numero: ");
        scanf("%d", &num);
        if (num != 0) {
            printf("\n%d em binario e: ", num);
            squart(num);
            printf("\n");
            printf("\n");
        }
    } while (num != 0);
    return 0;
}

