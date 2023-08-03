from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento:'))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE !')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} ano(s) para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
else:
    saldo = idade - 18
    print('Você ja deveria ter se alistado há {} ano(s)'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano)) 
    
