nome = 'Luiz Otávio'
tamanho = len(nome)
contador = 0 

while contador < tamanho:
    novo_nome = f'*{nome[contador]}'
    contador += 1
    print(novo_nome, end='')
    