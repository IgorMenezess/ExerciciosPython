#Programa que calcula valor total a pagar em carro, $60 por dia e $0.15 por km. 

days = int(input('Dias rodados: '))
distance = float(input('Km rodados: '))

value = (days * 60) + (distance * 0.15)

print (f'O valor a pagar é ${value} reais.')