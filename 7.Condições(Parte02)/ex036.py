#Emprestimo bancario

casa = float(input('Valor da casa: '))
tempo = int(input('Anos de financiamento: '))
salario = float(input('Salario do comprador: '))

prestacao = casa / (tempo * 12)

if prestacao > salario * 0.30:
    print(f'Para pagar uma casa de R${casa} em {tempo} anos a prestação será de R${round(prestacao,2)}\nEmprestimo NEGADO!')
elif prestacao <= salario * 0.30:
    print(f'Para pagar uma casa de R${casa} em {tempo} anos a prestação será de R${round(prestacao,2)}\nEmprestimo APROVADO!')

