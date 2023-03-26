nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

média = (nota1 + nota2) / 2
print('A sua média é \033[4;30;47m{}\033[m'.format(média))

if média < 5:
    print('\033[1;30;41mREPROVADO\033[m')
elif média >= 7:
    print('\033[1;30;42mAPROVADO\033[m')
else:
    print('\033[1;30;43mRECUPERAÇÃO\033[m')