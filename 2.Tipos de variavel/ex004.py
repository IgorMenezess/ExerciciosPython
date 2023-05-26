#Dissecando uma variavel

name = input('Digite algo: ')

print('Tipo primitivo: ', type(name))
print ('Só tem espaços? ', name.isspace())
print ('É um número? ', name.isnumeric())
print ('É alfabetico? ', name.isalpha())
print ('É alfanumerico? ', name.isalnum()())
print ('Está em maiuscula? ', name.isupper())
print ('Está em minuscula? ', name.islower())
print ('Está capitalzada? ', name.istitle())
