#Progressão aritmetica

FirstNum = int(input('Primeiro valor: '))
Jump = int(input('Razão: '))

for i in range(FirstNum, 10*Jump, Jump):
    print (i)
print ('Fim')