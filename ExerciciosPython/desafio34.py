sal = float(input('Qual o salario do funcionário? R$'))
if sal >= 1250.00:
    aumento = (sal * 10 / 100) + sal
else:
      aumento = (sal * 15 / 100) + sal
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sal, aumento))

