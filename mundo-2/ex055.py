maior = 0
menor = 0

for p in range(1, 4):
    peso = float(input('Peso da {}° pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso é', maior)
print('O menor peso é', menor)


'''lst = []  #lista vazia
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    lst += [peso]   #adc os valores de peso na lista

print('\nO Maior peso foi {:.2f}Kg'.format(max(lst)))  #maximo valor da lista
print('O Menor peso foi {:.2f}Kg'.format(min(lst)))  #minimo valor da lista
'''