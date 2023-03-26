born = int(input('Em que ano você nasceu? '))

from datetime import date
atual = date.today().year
idade = atual - born

if idade == 18:
    print('Você deve se alistar \033[1mIMEDIATAMENTE\033[m')
elif idade < 18:
    print('Você deve se alistar em {}. Faltam {} anos.'.format(born + 18, born + (18 - atual)))
elif idade > 18:
    print('Você devia ter se alistado em {}. Faz {} anos.'.format(born + 18, atual - (born + 18)))
