#Aprovação escolar

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 7:
    print ('o aluno está APROVADO')
elif media < 7 and media >= 5:
    print ('o aluno está RECUPERAÇÃO')
elif media < 5:
    print ('o aluno está REPROVADO')
