from datetime import date
ano = int(input('Qua ano quer analisar? Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano {} é \033[1;34;40mBISSEXTO\033[m'.format(ano))
else:
    print('O ano {} \033[4;36;40mnão é BISSEXTO\033[m'.format(ano))
    