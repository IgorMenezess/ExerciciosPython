#Grupo de pessoas

Nome_Mulher_Mais_Velha1 = []
Nome_Mulher_Mais_Velha2 = []
Nome_Mulher_Mais_Velha3 = []
Nome_Mulher_Mais_Velha4 = []

print ('PRIMEIRA PESSOA')
for a in range(1):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M)(F): '))
print ('-='*20)

print ('SEGUNDA PESSOA')
for b in range(1):
    nome2 = str(input('Nome: '))
    idade2 = int(input('Idade: '))
    sexo2 = str(input('Sexo (M)(F): '))
print ('-='*20)

print ('TERCEIRA PESSOA')
for c in range(1):
    nome3 = str(input('Nome: '))
    idade3 = int(input('Idade: '))
    sexo3 = str(input('Sexo (M)(F): '))
print ('-='*20)

print ('QUARTA PESSOA')
for d in range(1):
    nome4 = str(input('Nome: '))
    idade4 = int(input('Idade: '))
    sexo4 = str(input('Sexo (M)(F): '))
print ('-='*20)

#Média das idades

media = (idade + idade2 + idade3 + idade4) / 4
print (f'A média de idade é {media}')

#Nome do homem MAIS velho

if sexo == "M" and idade > (idade2, idade3, idade4):
    print (f'Homem mais velho: {nome}')

elif sexo2 == "M" and idade2 > (idade, idade3, idade4):
    print (f'Homem mais velho: {nome2}')

elif sexo3 == "M" and idade3 > (idade, idade2, idade4):
    print (f'Homem mais velho: {nome3}')

elif sexo4 == "M" and idade4 > (idade, idade2, idade3):
    print (f'Homem mais velho: {nome4}')

else:
    print ('Resposta inválida!')

#Mulheres com MENOS de 20 anos

if sexo == "F" and idade < 20:
    Nome_Mulher_Mais_Velha1.append(nome)

elif sexo2 == "F" and idade < 20:
    Nome_Mulher_Mais_Velha2.append(nome2)

elif sexo3 == "F" and idade < 20:
    Nome_Mulher_Mais_Velha3.append(nome3)

elif sexo4 == "F" and idade < 20:
    Nome_Mulher_Mais_Velha4.append(nome4)
else:
    print('Resposta invalida!')

print (f"""Mulheres com menos de 20 anos: {print(Nome_Mulher_Mais_Velha1)}
{print(Nome_Mulher_Mais_Velha2)}
{print(Nome_Mulher_Mais_Velha3)}
{print(Nome_Mulher_Mais_Velha4)}""")