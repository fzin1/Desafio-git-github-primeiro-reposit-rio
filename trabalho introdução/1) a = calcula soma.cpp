#include <stdio.h>

int calcular_soma(int n) {
    int soma = 0;
    for (int i = 1; i <= n; i++) {
        soma += i;
    }
    return soma;
}

int main() {
    int n;
    printf("Digite o valor de n: ");
    scanf("%d", &n);

    int soma = calcular_soma(n);
    printf("A soma dos %d primeiros numeros naturais e %d\n", n, soma);

    return 0;
}
