a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite outro número: '))

menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c

maior = a
if b > c and b > a:
    maior = b
if c > b and c > a:
    maior = c

print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))
