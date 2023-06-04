#Pedra papel tesoura
import random
from time import sleep

game = ['Pedra','Papel','Tesoura']
computador = random.choice(game)

print ("""ESCOLHA SUA OPÇÃO
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA""")

choice = int(input('Sua escolha: '))

print ('JO')
sleep(0.25)
print ('KEN')
sleep(0.25)
print ('PO')
sleep(0.25)

if choice == 1:
    print ('-='*20)
    print (f'Computador escolheu {computador}')
    print ('Jogador escolheu pedra')
    print ('-='*20)
    if computador == "Pedra":
        print ('EMPATE')
    elif computador == "Papel":
        print ('Computador VENCE!')
    elif computador == "Tesoura":
        print ('Você GANHOU!')

elif choice == 2:
    print ('-='*20)
    print (f'Computador escolheu {computador}')
    print ('Jogador escolheu papel')
    print ('-='*20)
    if computador == "Pedra":
        print ('Você GANHOU!')
    elif computador == "Papel":
        print ('EMPATE')
    elif computador == "Tesoura":
        print ('Computador VENCE!')

elif choice == 3:
    print ('-='*20)
    print (f'Computador escolheu {computador}')
    print ('Jogador escolheu tesoura')
    print ('-='*20)
    if computador == "Pedra":
        print ('Computador VENCE!')
    elif computador == "Papel":
        print ('Você GANHOU!')
    elif computador == "Tesoura":
        print ('Você GANHOU!')

else:
    print ('Resposta Invalida')




