"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
espaco = ' ' in nome
contagem = len(nome) - espaco
invertido = nome[::-1]
letra1 = nome[0]
letrau = nome[-1]
nada = "Desculpe, você deixou campos vazios."

if nome and idade :
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {invertido}')
    print(f'Seu nome tem espaços? {espaco}')
    print(f'Seu nome tem {contagem} letras')
    print(f'A primeira letra do seu nome é: {letra1}')
    print(f'A ultima letra do seu nome é: {letrau}')
else:
    print(nada)