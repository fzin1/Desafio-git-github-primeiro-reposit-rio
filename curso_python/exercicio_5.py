palavra = 'safado'
palavra_secreta = '*' * len(palavra)
tentativa = 0

print(f'Palavra secreta: {palavra_secreta}')

while '*' in palavra_secreta:
    letra_digitada = input('Digite apenas uma letra: ')

    while len(letra_digitada) != 1:
        letra_digitada = input('Digite apenas uma letra: ')

    if letra_digitada in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra_digitada:
                palavra_secreta = palavra_secreta[:i] + letra_digitada + palavra_secreta[i+1:]

        print(f'Palavra secreta: {palavra_secreta}')
    else:
        print(f'A letra {letra_digitada} não está na palavra.')

    tentativa += 1

print(f'Parabéns! Você adivinhou a palavra em {tentativa} tentativas. A palavra é: {palavra}')
