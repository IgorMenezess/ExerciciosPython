#Programa que calcula o desconto de um determiando produto

value = float(input('Valor do produto: '))
discount = int(input('Desconto do produto: '))

FinalValue = value * (discount/100)

print (f'O valor a pagar é ${FinalValue} reais')    