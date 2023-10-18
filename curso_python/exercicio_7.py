'''
Faça uma lista de compras com lista
o usuario deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
não permita que o programa quebre com
erros de indices inexistentes da lista.

'''


lista = []

while True:
    opcao = input("Selecione uma opção \n [i]nserir [a]pagar [l]istar: ")
    
    if opcao == 'i':
        adicionar = input("Qual item deseja adicionar a sua lista?: ")
        lista.append(adicionar)
    
    elif opcao == 'l':
        for numero, valor in enumerate(lista):
            print(numero, valor)

    elif opcao == 'a':
        deletar = int(input("selecione o indice que deseja deletar: "))
        if 0 <= deletar < len(lista):
            del lista[deletar]
            print("Valor apagado com sucesso!")        
