
#include <stdio.h>

int main() {
    int i, n1, j;
    printf("Digite um número ");
    scanf("%d", &n1);
    for(i=n1; i>=1; i--){
        for(j = 1; j<=i; j++) {
            printf("%d ", j);
        }
        printf("\n");
        
    }

    return 0;
}
