from random import randint
computador = randint(0, 5) # faz o computador "pensar"
print('-=-'*20)
print('Vou pensar em um numero ente 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador= int(input('Em que número pensei ?')) # jogador tenta adivinhar
if jogador == computador:
    print('Você venceu!')
else:
    print('Ganhei ! pensei no número {} e não no {}!'.format(computador, jogador))
    