
while True:
    try:
        numstr_1 = input('Escolha o primeiro número: ')
        numstr_2 = input('Escolha o segundo número: ')
        operador = input('Escolha o operador: ')
        num_1 = int(numstr_1)
        num_2 = int(numstr_2)

        while operador not in {"*", "/", "-", "+"}:
            operador = input('Escolha um operador correto: ')

        if operador == "+":
            print(f'O resultado é: {num_1 + num_2}')
        elif operador == "-":
            print(f'O resultado é: {num_1 - num_2}')
        elif operador == "/":
            if num_2 == 0:
                print("Erro: Divisão por zero.")
            else:
                print(f'O resultado é: {num_1 / num_2}')
        elif operador == "*":
            print(f'O resultado é: {num_1 * num_2}')

        sair = input("Deseja sair? (s/n): ")
        if sair.lower() == 's':
            break

    except ValueError:
        print("Coloque um número válido.")
