#IMC

altura = float(input('Sua altura(m): '))
peso = float(input('Seu peso(kg): '))
imc = peso / (altura**2)

if imc < 18.5:
    print (f'IMC: {round(imc,2)}')
    print ('Status: ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print (f'IMC: {round(imc,2)}')
    print ('Status: PESO IDEAL')
elif imc >= 25 and imc < 30:
    print (f'IMC: {round(imc,2)}')
    print ('Status: SOBREPESO')
elif imc >= 30 and imc <= 40:
    print (f'IMC: {round(imc,2)}')
    print ('Status: OBESIDADE')
elif imc > 40:
    print (f'IMC: {round(imc,2)}')
    print ('Status: OBESIDADE MORBIDA')
else:
    print ('Resposta Invalida')
