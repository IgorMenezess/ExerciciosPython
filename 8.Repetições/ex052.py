#Numero primo

num = int(input('Digite um valor: '))
cont = 0

for i in range(1, num+1):
    div = num % i
    print (i, end=' ')
    if div == 0:
        cont += 1

print (f'O numero {num} foi dividido {cont} vezes.')
if cont > 2:
    print (f'Portanto {num} não é PRIMO')
else: 
    print (f'Portanto {num} é PRIMO')



