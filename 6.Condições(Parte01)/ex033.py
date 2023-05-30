#maior e menor

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))

lista = [num1,num2,num3]

lista.sort()
print (f'O menor número é {lista[0]}')

lista.reverse()
print (f'O maior número é {lista[0]}')
