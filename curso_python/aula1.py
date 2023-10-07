# comentarios

print(12,34,56,78, sep='-', end=' :)\n')
print(20,21,22,23, sep='-', end=' :)\n')
print('oi', sep='-', end=' :)\n')

# sep = separador
# end = como vai terminar o seu print (\n é o padrao)

#string
print('Fabricio Ramos')

#caracter de escape
print('Fabricio \"Ramos') # a \ é um caracter de escape, ele ignora a ação do proximo caracter e printa ele normalmente

#string em python é str

# 1**2 = 1 ao quadrado

#string = f'teste {teste:.2f} teste' # fstring oq ta entre chaves vira variavel
#:.2f = quantas casas decimais

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)


input()
#input = coletar dados do usuario


# if / elif      / else
# se / se não se / se não
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')

    print(12341234)
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair.')

print('FORA DOS BLOCOS')

