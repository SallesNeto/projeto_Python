distância = float(input('Qual a distância da sua viagem ?'))
print('Você esta prestes a começar uma viagem de {:.1f}KM'.format(distância))
if distância <= 200:
    preço = distância * 0.50

else:
    preço = distância * 0.45
    print('O preço da sua passagem R$ {:.2f}'.format(preço))
    