print ('-=-'*20)
print('Analisadro de Triângulos')
print ('-=-'*20)
v1 = float(input('Primeiro segmento:'))
v2 = float(input('Segundo segmento:'))
v3 = float(input('terceiro segmento:'))
if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
    print('Os segmentos acima PODEM FORMAR triângulo !')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
    