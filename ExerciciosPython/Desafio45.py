from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('jogador Ganhou!')
    elif jogador == 2:
        print('Computador Ganhou !')
    else:
       print('JOGADA INVALIDA')
elif computador == 1:# computador jogou PAPEL
    if jogador == 0:
        print('computador Venceu !')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador Venceu!')
    else:
        print('JOGADA INVALIDA')
elif computador == 2:# computador jogou TESOURA
    if jogador == 0:
        print('Jogador Venceu!')
    elif jogador == 1:
        print('Computador Venceu !')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')


