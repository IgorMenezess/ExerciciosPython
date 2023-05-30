#primeiro e ultimo nome

name = str(input('Digite seu nome completo: ')).strip()
name = name.split()

print(f'Seu primeiro nome é {name[0]}')
print(f'Seu ultimo nome é {name[len(name)-1]}')