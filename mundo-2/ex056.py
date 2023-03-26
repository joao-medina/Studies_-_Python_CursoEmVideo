listanome = []
listaidade = []
listasexo = []
menorde20 = []
totaldehomens = []
somaidade = 0

for c in range(1, 5):
    print('\033[1;35;40m=' * 10, '{}° PESSOA'.format(c), '=' * 10, '\033[m')
    nome = input('Qual é o nome da {}° pessoa? '.format(c))
    listanome += [nome]

    idade = int(input('Quantos anos ela tem? '))
    somaidade += idade

    sexo = input('Qual o sexo desta pessoa? [M\F] ').lower()
    listasexo += [sexo]
    if sexo == 'm':
        totaldehomens += [sexo]
        listaidade += [idade]
    if sexo == 'f':
        if idade < 20:
            menorde20 += [idade]


print('\n\n\033[1;30;45mA média da idade das pessoas é {:.2f} anos.'.format(somaidade / 4))

tothom = len(totaldehomens)
if tothom == 0:
    print('Não há homens.')
else:
    print('O homem mais velho tem {} anos.'.format(max(listaidade)))

totmul = len(menorde20)
if totmul == 1:
    print('Há apenas uma mulher menor de 20 anos.'.format(len(menorde20)))
elif totmul == 0:
    print('Não há mulheres menores de 20 anos.')
else:
    print('Há {} mulheres menores de 20 anos\033[m'.format(totmul))
