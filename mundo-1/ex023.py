num = int(input('Digite um número: '))

a = num % 10
b = num // 10 % 10
c = num // 100 % 10
d = num // 1000

print('Analisando o número', num)

print('Unidade:', a)
print('Dezena:', b)
print('Centena:', c)
print('Milhar:', d)


