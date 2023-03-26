from datetime import date
atual = date.today().year

born = int(input('Em que ano você nasceu? '))
idade = atual - born

print('Você tem {} anos, você participará na categoria: '.format(idade))

if idade < 10:
    print('MIRIM')
if 9 < idade < 15:
    print('INFANTIL')
if 14 < idade < 20:
    print('JUNIOR')
if 19 < idade < 26:
    print('SÊNIOR')
if idade > 25:
    print('MASTER')