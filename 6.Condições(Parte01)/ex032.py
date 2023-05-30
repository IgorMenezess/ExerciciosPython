#Ano Bissexto

import datetime

year = int(input('Qual ano você quer analisar? Digite 0 para analisar o ano atual: '))


if year == 0:
    MachineYear = datetime.date.today().year
    if MachineYear % 4 == 0 and MachineYear % 100 != 0 or MachineYear % 400 == 0:
        print (f'O ano {MachineYear} é BISSEXTO!')
    else:
        print (f'O ano {MachineYear} NÃO é BISSEXTO!')
elif year != 0 and year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print (f'O ano {year} é BISSEXTO')
else:
    print (f'O ano {year} NÃO é BISSEXTO')

