#Classificação
import datetime

nascimento = int(input('Seu ano de nascimento: '))
classe = datetime.date.today().year - nascimento

if classe <= 9:
    print (f'Idade do atleta: {classe}')
    print ('Classificação: MIRIN')
elif classe > 9 and classe <= 14:
    print (f'Idade do atleta: {classe}')
    print ('Classificação: INFANTIL')
elif classe > 14 and classe <= 19:
    print (f'Idade do atleta: {classe}')
    print ('Classificação: JUNIOR')
elif classe > 19 and classe <= 25:
    print (f'Idade do atleta: {classe}')
    print ('Classificação: SENIOR')
elif classe > 25:
    print (f'Idade do atleta: {classe}')
    print ('Classificação: MASTER')
else:
    print ('Resposta Invalida.')