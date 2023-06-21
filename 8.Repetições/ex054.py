#Maioridade
import datetime
data = datetime.date.today().year

cont = 0
cont2 = 0

for i in range(1, 8):
    ano =int(input(f'Ano de Nascimento da {i}° pessoa: '))
    i += 1
    if (data - ano) < 18:
        cont += 1
    elif (data - ano) >= 18:
        cont2 += 1

print (f'{cont} pessoas são MENOR de idade')
print (f'{cont2} pessoas são MAIOR de idade')
