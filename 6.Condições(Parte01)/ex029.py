#Radar

speed = int(input('Qual a sua velocidade? '))
MaxSpeed = 80

if speed <= MaxSpeed and speed > 0:
    print ('Tenha uma boa viagem!')
elif speed > MaxSpeed:
    multa = (speed - MaxSpeed) * 7
    print (f'Você está MULTADO!, o limite de {MaxSpeed}Km/h foi ultrapassado.\nSua multa sera de R${multa} reais.')
else:
    print('Resposta invalida!')