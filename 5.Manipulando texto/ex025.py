#Verificando sobrenome

name = str(input('Digite seu nome completo: ')).strip()

print (f'Seu nome tem Menezes? {"menezes" in name.lower()}')