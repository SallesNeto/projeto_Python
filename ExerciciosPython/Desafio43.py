peso = float(input('Qual o seu peso kg ?'))
altura = float(input('Qual sua altura ?'))
imc = peso / (altura ** 2)
print('O Imc dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('IMC Abaixo do peso normal!')
elif imc <= 25:
    print('Parabéns, você está na faixa de Peso Normal!')
elif imc <= 30:
    print('Você está com Sobrepeso!')
elif imc <= 40:
    print('Você está com Obesidade!')
else:
    print('Você está com Obesidade Mórbida! ') 
    
