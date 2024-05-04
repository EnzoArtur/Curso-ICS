import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    tentativas = 0

    print('bem-vindo ao jogo de adivinhacao')

    while True:
        palpite = int(input('digite um numero entre 1 e 10: '))
        tentativas += 1

        if palpite == numero_secreto:
            print(f'parabens voce acertou o numero secreto {numero_secreto} em {tentativas} tentativas')
            break
        elif palpite < numero_secreto:
            print('errou, numero secreto maior ,tente novamente.')
        else:
            print('errou, numero secreto e menor, tente novamente.')

jogo_adivinhacao()