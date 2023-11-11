
# def teste(x,y):
#     if x == 10: 
#         teste = x+y
#         print(teste)
#     elif x==20: 
#         teste = x-y
#         print(teste)
        
# teste(20,10)

def num_multiplicados(*args):
    multiplicados = 1
    for numeros in args:
       multiplicados *= numeros
    return multiplicados

def par_ou_impar(numero):
    resultado = 'Par' if numero % 2 == 0 else 'impar'
    return resultado
    
multiplicacao = num_multiplicados(3    )
par_impar = par_ou_impar(multiplicacao)
print(f'{multiplicacao} é {par_impar}')

