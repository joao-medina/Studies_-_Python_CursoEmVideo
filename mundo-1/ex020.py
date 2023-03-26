from random import shuffle

a = str(input('Nome 1: '))
b = str(input('Nome 2: '))
c = str(input('Nome 3: '))
d = str(input('Nome 4: '))

lista = [a, b, c, d]
shuffle(lista)

print('A ordem será: ')
print(lista)

