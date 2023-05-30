#Jogo da adivinhação

import random
from time import sleep

print('------Jogo de adivinha------')
SystemNum = random.randint(0,5)
UserNum = int(input('Chute um valor de 0 a 5: '))
print ('VERIFICANDO...')
sleep(1)

if SystemNum == UserNum:
    print ('Você acertou!')
else:
    print ('Você errou!')
