sexo = input('Qual é o seu sexo? [F/M] ').upper().strip()

if sexo == 'M' or sexo == 'F':
    print('Legal!')
else:
    while sexo != 'F' or sexo != 'M':
        sexo = input('Comando inválido, tente novamente: ').upper()
        if sexo == 'M' or sexo == 'F':
            print('Legal!')
