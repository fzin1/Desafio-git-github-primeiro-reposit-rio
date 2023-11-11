import copy

def calcular_porcentagem(valor,porcentagem):
    resultado = (valor*porcentagem)/100
    return resultado


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Crie uma cópia profunda dos produtos
novos_produtos = copy.deepcopy(produtos)


tamanho = len(produtos)
i = 0

while i < tamanho:
    # Aumente os preços em 10%
    preco = produtos[i]['preco']
    porcentagem = calcular_porcentagem(preco,10)
    novos_produtos[i]['preco'] += porcentagem
    novos_produtos[i]['preco'] = round(novos_produtos[i]['preco'], 2)
    i += 1

produtos_ordenados_por_nome = sorted(novos_produtos, key=lambda x: x['nome'], reverse=True)
produtos_ordenados_por_preco = sorted(novos_produtos, key=lambda x: float(x['preco']))

print('produtos_ordenados_por_nome')
print(*produtos_ordenados_por_nome, sep= '\n')
print('produtos_ordenados_por_preco')
print(*produtos_ordenados_por_preco, sep= '\n')
