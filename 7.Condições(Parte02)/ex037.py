#Bi, Octal ou hexa

num = int(input('Digite um número inteiro: '))
print ('Escolha uma base de conversão\n[ 1 ] BINÁRIO\n[ 2 ] OCTAL\n[ 3 ] HEXADECIMAL')
base = int(input('Sua opção: '))

if base == 1:
    print (f'{num} em binário fica {bin(num)}')
elif base == 2:
    print (f'{num} em ocatal fica {oct(num)}')
elif base == 3:
    print (f'{num} em hexadecimal fica {hex(num)}')
else:
    print('Resposta Inválida')


