ano = int(input('Digite um ano para saber se ele é bissexto: (0 para o ano atual)'))

if ano % 4 == 0:
    if ano % 100 == 0:
       if ano % 400 == 0:
           print('O ano é bissexto.')
       else:
           print('O ano não é um ano bissexto.')
    else:
        print('O ano é bissexto.')
else:
    print('A ano não é um ano bissexto.')