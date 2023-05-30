#Preço da viagem

distance = float(input('Informe o Km da viagem: '))

if distance <= 200 and distance >= 0:
    preço = distance * 0.50
    print (f'Sua viagem de {distance}Km custará R${preço} reais')
elif distance > 200:
    preço = distance * 0.45
    print (f'Sua viagem de {distance}Km custará R${preço} reais')
else:
    print('Resposta Inválida!')