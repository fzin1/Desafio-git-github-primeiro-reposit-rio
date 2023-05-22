#include <stdio.h>

int squart(int A,int B,int C){
	if(A>B)
		if(B>C)
			printf("%d < %d < %d", C, B, A);
			else
			if(A>C)
				printf("%d < %d < %d", B, C, A);
				else
					printf("%d < %d < %d", B, A, C);
		else
			if(B>C)
				if(A>C)
					printf("%d < %d < %d", C, A, B);
				else
					printf("%d < %d < %d", A, C, B);
					
					else
					printf("%d < %d < %d", A, B, C);		
}
int main(){
	int n1, n2, n3, res;
	
	printf("Digite o primeiro numero: ");
	scanf("%d", &n1);
	printf("Digite o segundo numero: ");
	scanf("%d", &n2);
	printf("Digiite o terceiro numero: ");
	scanf("%d", &n3);
	res = squart(n1, n2, n3);
	
	return 0;
}
