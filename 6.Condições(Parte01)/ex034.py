#aumento de salario

salario = float(input('Informe o salário: R$ '))

if salario <= 1250:
    NovoSalario = salario + (salario * 0.15)
    print (f'Voce passara a receber R$ {NovoSalario} reais')
else:
    NovoSalario = salario + (salario * 0.10)
    print (f'Voce passara a receber R$ {NovoSalario} reais')