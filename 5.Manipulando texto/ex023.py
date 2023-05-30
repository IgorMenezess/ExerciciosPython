# Qubrando um número

num = int(input('Digite um numero: '))
uni = num // 1 % 10
dez = num // 10 % 10
cent = num // 100 % 10
mile = num // 1000 % 10

print (f'Unidade: {uni}\nDezena: {dez}\nCentena: {cent}\nMilhar: {mile}')