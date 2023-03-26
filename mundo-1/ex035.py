print('-='*20)
print('ANALISADOR DE TRIÂNGULOS')
print('-='*20)

a = float(input('Segmento 1: '))
b = float(input('Segmento 2: '))
c = float(input('Segmento 3: '))

maior = a
if b > c and b > a:
    maior = b
    if maior ** 2 == a ** 2 + b ** 2 + c ** 2 - maior ** 2:
        print('É possível fomar um triângulo!')
    else:
        print('Não é possível formar um triângulo.')
if c > b and c > a:
    maior = c
    if maior ** 2 == a ** 2 + b ** 2 + c ** 2 - maior ** 2:
        print('É possível fomar um triângulo!')
    else:
        print('Não é possível formar um triângulo.')
if a == b == c:
    print('É possível fomar um triângulo!')
