velocidade = float(input('Qual é a velocidade atual do carro?'))
if velocidade > 80:
    print('Multado! Você excedeu o limite permitido de que é de 80Km/h')
    multa= (velocidade - 80) * 7
    print('Sua multa sera de R$ {:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
