import math
num = float(input('Digite um numero:'))
inteiro= math.trunc(num)
print ('O numeoro: {}, tem a parte inteira {}'.format(num,math.trunc(inteiro)))

from math import trunc
num = float(input('Digite um numero:'))
inteiro = trunc(num)
print('O numero: {}, tem a parte inteira {}'.format(num,trunc(inteiro)))
