# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta':'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
    {
        'Pergunta': 'Quanto é 20/2?',
        'Opções': ['16', '7', '10', '18'],
        'Resposta': '10',
    },
]
quantidade_de_perguntas = len(perguntas)

i=0

acertos = 0

while i < quantidade_de_perguntas:
    start = input('Você deseja prosseguir com o jogo?: [s] ou [n]: ')

    if start.lower() == 's':
        pergunta = perguntas[i]['Pergunta']
        opcao = perguntas[i]['Opções']
        resposta_certa = perguntas[i]['Resposta']

        while True:
            print('\n', pergunta, '\n')
            print('Opções: \n')

            for indice, numero in enumerate(opcao):
                print(f"{indice}) {numero}")
            resposta = input('\nEscolha uma opção: ')

            if resposta == resposta_certa:
                print('\nParabéns, você acertou 😎 !\n')
                acertos += 1
                i += 1
                break
            else:
                print('\nResposta errada 😕\n')
                i += 1
                break
                

    elif start.lower() == 'n':
        break
    else:
        print('Resposta inválida')

porcentagem = round((acertos * 100)/quantidade_de_perguntas)
print('\n' f'Você acertou {acertos} de {quantidade_de_perguntas} perguntas''\n')
print(f'Você acertou {porcentagem}% do jogo\n')
