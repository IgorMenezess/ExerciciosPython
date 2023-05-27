# Hipotenusa
from math import hypot

value1 = float(input('Insira o valor do cateto oposto: '))
value2 = float(input('Insira o valor do cateto adjacente: '))
hyp = hypot(value1, value2)

print (f'O valor da hipotesusa é: ', round(hyp, 2))