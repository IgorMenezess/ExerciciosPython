#Soma dos pares
cont = 0
soma = 0

for i in range(1, 7):
    num = int(input(f'Digite o {i}° valor: '))
    if num % 2 == 0:
        cont += 1
        soma += num
print (f'A soma dos {cont} valores pares é igual a {soma}')