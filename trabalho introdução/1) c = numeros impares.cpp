#include <stdio.h>

int main() {
    int n;
    printf("Digite um numero: ");
    scanf("%d", &n);

    printf("Numeros impares menores que %d:\n", n);

    for (int i = 1; i < n; i += 2) {
        printf("%d ", i);
    }

    printf("\n");

    return 0;
}
