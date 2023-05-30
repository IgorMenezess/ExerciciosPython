#Verificando primeiras letras de um texto

city = str(input('Em qual cidade você mora? ')).strip()

print(city[:8].upper() == 'ARACAJU')

