
def nova_capacidade(capacidade_atual, aumento_percentual):
    porcentagem = (capacidade_atual * aumento_percentual)/100
    resultado = porcentagem + capacidade_atual
    print(int(resultado))


capacidade_atual, aumento_percentual = map(int, input().split())

nova_capacidade(capacidade_atual, aumento_percentual)


#TODO: Imprima a nova capacidade

