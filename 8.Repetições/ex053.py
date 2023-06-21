#Palindromo

frase = str(input('Digite uma frase: ')).strip()
frase = frase.split()
frase2 = "".join(frase)
reverso = frase2[::-1]

print (f'A frase {frase2.upper()} ao contrario é {reverso.upper()}')

if frase2.upper() == reverso.upper():
    print ('A frase é um POLINDROMO')
else: 
    print ('A frase não é um POLINDROMO')