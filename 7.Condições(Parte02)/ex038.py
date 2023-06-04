#comparando numeros

num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))

if num1 == num2:
    print (f'{num1} e {num2} são IGUAIS!')
elif num1 > num2:
    print (f'{num1} é maior que {num2}')
elif num1 < num2:
    print (f'{num2} é maior que {num1}')
else:
    print ('Resposta invalida.')