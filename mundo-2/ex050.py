soma = 0

for num in range(1, 7):
    nume = (int(input('Digite o {}° número: '.format(num))))
    if nume % 2 == 0:
        soma += nume
print('A soma entre os números pares é', soma)


