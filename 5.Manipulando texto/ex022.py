#Manipulando nome completo

name = str(input('Digite seu nome completo: '))

UpperName = name.upper()
LowerName = name.lower()
NameCount = name.replace(' ', '')
FirstName =  len(name.split()[0])

print (f'Upper: {UpperName}')
print (f'Lower: {LowerName}')
print (f'Caracters: {len(NameCount)}')
print (f'First Name: {FirstName}')

