
# Digito_1 CPF

CPF = ['893.555.580-07']
cpf_int = []
numeros_9 = [10,9,8,7,6,5,4,3,2]

j = 0
cpf_soma = 0

for i in CPF[0]:
    if i.isdigit():
        cpf_int.append(int(i))
cpf_int = cpf_int[:9]

while j < 9:
    item_multiplicado = cpf_int[j] * numeros_9[j]
    cpf_soma += item_multiplicado 
    resto = (cpf_soma * 10) % 11
    j+=1

resultado = resto if resto < 9 else 0

# ---------------------------------------------------------------------
# Digito_2

cpf_int_2 = cpf_int + [resultado]
numeros_10 = numeros_9.copy()
numeros_10.insert(0,11)
cpf_soma_2 = 0
j_2 = 0
    
while j_2 < 10:
    item_multiplicado_2 = cpf_int_2[j_2] * numeros_10[j_2]
    cpf_soma_2 += item_multiplicado_2 
    resto_2 = (cpf_soma_2 * 10) % 11
    j_2+=1

resultado_2 = resto_2 if resto_2 < 9 else 0

print(resultado)
print(resultado_2)




