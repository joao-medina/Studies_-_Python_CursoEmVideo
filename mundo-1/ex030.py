nummer = int(input('Digite um número para descobrir se ele é ímpar ou par: '))
nummer2 = nummer % 2

if nummer2 == 0:
    print('Par')
else:
    print('Ímpar')