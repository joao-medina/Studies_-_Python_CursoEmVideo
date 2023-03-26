import random

a = str(input('Nome 1: '))
b = str(input('Nome 2: '))
c = str(input('Nome 3: '))
d = str(input('Nome 4: '))

lista = [a, b, c, d]
sort = random.choice(lista)

print('O nome sorteado foi {}.'.format(sort))