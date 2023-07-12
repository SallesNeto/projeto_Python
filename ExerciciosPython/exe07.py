from math import hypot
co = float(input('Comprimento do cateto oposto :'))
ca = float(input('comprinto do cateto adjacente: '))
hi = hypot(co, ca)
print('a hipotenusa: {:.2f}'.format(hi))
