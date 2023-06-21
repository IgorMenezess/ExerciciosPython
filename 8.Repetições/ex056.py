# Grupo de pessoas

Nome_Mulher_Menos_Vinte = []

print('PRIMEIRA PESSOA')
for a in range(1):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M)(F): '))
print('-='*20)

print('SEGUNDA PESSOA')
for b in range(1):
    nome2 = str(input('Nome: '))
    idade2 = int(input('Idade: '))
    sexo2 = str(input('Sexo (M)(F): '))
print('-='*20)

print('TERCEIRA PESSOA')
for c in range(1):
    nome3 = str(input('Nome: '))
    idade3 = int(input('Idade: '))
    sexo3 = str(input('Sexo (M)(F): '))
print('-='*20)

print('QUARTA PESSOA')
for d in range(1):
    nome4 = str(input('Nome: '))
    idade4 = int(input('Idade: '))
    sexo4 = str(input('Sexo (M)(F): '))
print('-='*20)

# Média das idades

media = (idade + idade2 + idade3 + idade4) / 4
print(f'A média de idade é {media}')

# Nome do homem MAIS velho

homem_mais_velho = ''
idade_homem_mais_velho = 0

if sexo == "M" and idade > idade_homem_mais_velho:
    homem_mais_velho = nome
    idade_homem_mais_velho = idade

if sexo2 == "M" and idade2 > idade_homem_mais_velho:
    homem_mais_velho = nome2
    idade_homem_mais_velho = idade2

if sexo3 == "M" and idade3 > idade_homem_mais_velho:
    homem_mais_velho = nome3
    idade_homem_mais_velho = idade3

if sexo4 == "M" and idade4 > idade_homem_mais_velho:
    homem_mais_velho = nome4
    idade_homem_mais_velho = idade4

if homem_mais_velho:
    print(f'Homem mais velho: {homem_mais_velho}')
else:
    print('Não há homens no grupo.')

# Mulheres com MENOS de 20 anos

if sexo == "F" and idade < 20:
    Nome_Mulher_Menos_Vinte.append(nome)

if sexo2 == "F" and idade2 < 20:
    Nome_Mulher_Menos_Vinte.append(nome2)

if sexo3 == "F" and idade3 < 20:
    Nome_Mulher_Menos_Vinte.append(nome3)

if sexo4 == "F" and idade4 < 20:
    Nome_Mulher_Menos_Vinte.append(nome4)

if len(Nome_Mulher_Menos_Vinte) > 0:
    print(f"Mulheres com menos de 20 anos: {(Nome_Mulher_Menos_Vinte)}")
else:
    print('Não há mulheres com menos de 20 anos.')