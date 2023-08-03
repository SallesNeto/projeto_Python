num = int(input('Digite um numero inteiro:'))

print('''Escolha uma das bases para conversão:
[1] converter para BINARIO
[2]converter para OCTAL
[3] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido em Binario é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido em Octal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{}convertido em Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Não escolheu uma opção valida, tente novamente')
    