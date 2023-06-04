#Pagamento

produto = float(input('Digite o valor do produto: '))
print ("""FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro
[ 2 ] À vista cartão
[ 3 ] 2X Cartão
[ 4 ] 3x ou mais Cartão""")
pagamento = int(input('Forma de pagamento: '))

if pagamento == 1:
    desconto = produto - (produto * 0.10)
    print (f'O valor final do produto será de R${desconto}')

elif pagamento == 2:
    desconto = produto - (produto * 0.5)
    print (f'O valor final do produto será de R${desconto}')

elif pagamento == 3:
    print (f'O valor final do produto será de R${produto}')

elif pagamento == 4:
    juros = produto + (produto * 0.20)
    print (f'O valor final do produto será de R${juros}')

else:
    print ('Resposta Invalida')
