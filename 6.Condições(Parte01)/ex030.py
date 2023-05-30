#par ou impar

num = int(input('Informe um número inteiro qualquer: '))
par = num % 2

if par == 0:
    print(f'O número {num} é par.')
else:
    print('O número é ímpar.')
