#Conversor de medidas

medida = float(input('Medida em metros: '))

#formulas
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

#Visualização do usuario
print (f'A medida de {medida} metros, equivale a:')
print (f'{km} km')
print (f'{hm} hm')
print (f'{dam} dam')
print (f'{dm} dm')
print (f'{cm} cm')
print (f'{mm} mm')


