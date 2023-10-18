"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
'''

num = input("Digite um número inteiro: ")
try:

    num_int = int(num)
    impar = (num_int % 2) == 1
    par = (num_int % 2) == 0
    if par:
        print("Você digitou um número inteiro par")
    else: 
        print("Você digitou um número inteiro impar")
except:
    print("não é um numero inteiro")
'''

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
'''

hora_atual = input("Digite a hora: ")
try:
    hora_int = int(hora_atual)

    if hora_int >= 0 and hora_int <= 11:
        print("Bom dia")
    elif hora_int >= 12 and hora_int <= 17:
        print("Boa tarde")
    elif hora_int >= 18 and hora_int <= 23:
        print("Boa noite")
    else:
        print("Não é uma hora válida")
except:
    print("Por favor digite apenas numeros inteiros")

'''

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

'''

nome = input("Digite o seu nome: ")

letras = len(nome)

if letras > 0 and letras <= 4:
    print("Seu nome é curto")
elif letras >= 5 and letras <= 6:
    print("Seu nome é normal")
elif letras > 6:
    print("Seu nome é muito grande")
else:
    print("Impossivel seu nome ter essa quantidade")
    
'''