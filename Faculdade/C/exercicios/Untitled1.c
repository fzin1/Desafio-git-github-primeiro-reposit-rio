#include<stdio.h>

int main(){

int numero, cont, produto = 1;

for(cont = 1; cont <= 10; cont++){

scanf("%d", &numero);

produto *= numero;

}

printf("%d", produto);

return 0;
}
