#analisando triangulo (v1.0)

seg1 = float(input('Valor do primeiro segmento: '))
seg2 = float(input('Valor do segundo segmento: '))
seg3 = float(input('Valor do terceiro segmento: '))

if seg1 > (seg2 % seg3):
    print ('Os segmentos PODEM formar um triangulo!')
else:
    print ('Os segmentos NÃO PODEM formar um triangulo!')