import math
co=float(input('comprimento do cateto oposto:'))
ad=float(input('Comprimento do cateto adjacente:'))
hp = math.hypot(co,ad)
print('A hipotenusa vai medir{:.2f}'.format(hp))

from math import hypot
co =float(input('comprimento do cateto oposto:'))
ad =float(input('comprimento do cateto adjacente:'))
hp = hypot(co,ad)
print('A hipotenusa vai medir {:.2f}'.format(hp))
