'''co = float(input('Qual é o comprimento do cateto oposto? (Em metros): '))
ca = float(input('Qual é o comprimento do cateto adjacente? (Em metros): '))
from math import sqrt
hi =sqrt(co**2 + ca**2)
print('Legal! A hipotenusa tem a medida de {:.2f} metros.'.format(hi))'''

co = float(input('Qual é o comprimento do cateto oposto? (Em metros): '))
ca = float(input('Qual é o comprimento do cateto adjacente? (Em metros): '))
from math import hypot
hi = hypot(co, ca)
print('Legal! A hipotenusa tem a medida de {:.2f} metros.'.format(hi))
