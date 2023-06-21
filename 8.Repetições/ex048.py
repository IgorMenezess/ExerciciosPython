#soma de impares e multiplos de 3

num = 0
quant = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        quant += 1
        num += i

print (f'A soma dos {quant} valores deu {num}')   