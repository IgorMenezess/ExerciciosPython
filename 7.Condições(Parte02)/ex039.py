#Alistamento militar
import datetime

nascimento = int(input('Digite seu ano de nascimento: '))
idade = datetime.date.today().year - nascimento
militar = 18

if idade < militar:
    print('Você ainda vai se alistar')
elif idade == militar:
    print ('Está na hora exata de voce se alistar')
elif idade > militar:
    ultrapassou = idade - militar
    print (f'O seu tempo de se alistar já passou em {ultrapassou} anos')





