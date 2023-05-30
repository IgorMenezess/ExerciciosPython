#Ocorrencia, primeira e ultima letra

name = str(input('Digite uma frase: ')).strip()
name = name.upper()

print(f'Quantidade de letras A: {name.count("A")}')
print(f'O primeiro A aparece na posição {name.find("A")+1}')
print(f'O ultimo A aparece na posição {name.rfind("A")+1}')

