#Triangulo V2.0

reta1 = float(input('Medida da primeira reta: '))
reta2 = float(input('Medida da segunda reta: '))
reta3 = float(input('Medida da terceira reta: '))


if reta1 > (reta2 % reta3) and reta1 < (reta2 + reta3):
    print('As retas inseridas podem formar um triangulo')
    if reta1 == reta2 and reta1 == reta3:
        print ('Tipo: EQUILATERO!')
    elif reta1 != reta2 and reta1 != reta3:
        print ('Tipo: ESCALENO!')
    else:
        print ('Tipo: ISOCELES!')
else:
    print ('As retas não podem formar um triangulo!')