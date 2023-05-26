#Programa que calcula quantos litros de tinta são necessarios para pintar uma determianda parede.

height = float(input('Altura da parede(m): '))
width = float(input('Largura da parede(m): '))
area = height * width
litros = float(area / 2)

print (f'A parede tem uma dimensão de {height}x{width}, sua área é de {area}m2')
print (f'Para pintar esta parede sera necessario {litros} litros de tinta')