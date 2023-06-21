#Maior e menor peso
lista = []

for i in range(1,6):
    peso = float(input(f'Pessoa da {i}° pessoa: '))
    lista.append(peso)
    

lista.sort()
menor = lista[0]
maior = lista[-1]

print (f'O menor peso foi {menor} Kg')
print (f'O maior peso foi {maior} Kg')