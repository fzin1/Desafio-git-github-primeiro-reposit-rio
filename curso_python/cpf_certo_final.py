import random

#criando cpfs
for _ in range(1): #gerar varios cpfs
    
    nove_digitos = '' #diz que vai entrar uma str 

    for i in range(9): #loop para randomizar numeros de 0-9 com limite de 9 caracteres
        nove_digitos += str(random.randint(0,9))

    # Digito_1 CPF

    # cpf = '746.824.890-70'.replace('.','').replace('-','')

    contador_10 = 10
    mult_soma = 0

    for digito_9 in nove_digitos: 
        mult_soma += int(digito_9) * contador_10
        contador_10 -= 1

    resto = (mult_soma * 10) % 11

    digito_1 = resto if resto < 9 else 0

    # ---------------------------------------------------------------------
    # Digito_2

    dez_digitos = nove_digitos + str(digito_1)
    contador_11 = 11
    mult_soma_2 = 0

    for digitos_10 in dez_digitos:
        mult_soma_2 += int(digitos_10) * contador_11
        contador_11 -= 1

    resto_2 = (mult_soma_2 * 10) % 11

    digito_2 = resto_2 if resto_2 < 9 else 0

    # ---------------------------------------------------------------------
    # novo cpf

    novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'

    print(novo_cpf)



