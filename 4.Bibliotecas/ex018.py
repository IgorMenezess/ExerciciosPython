#Seno, cosseno e tangente
from math import sin, cos, tan

angle = float(input('Insira o valor do ângulo: '))
seno = round(sin(angle), 2)
cos = round(cos(angle), 2)
tg = round(tan(angle), 2)

print (f'Angulo: {angle}')
print (f'Seno: {seno}')
print (f'Cosseno: {cos}')
print (f'Tangente: {tg}')
