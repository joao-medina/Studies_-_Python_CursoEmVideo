from time import sleep
opção = 4

while opção == 4 or opção > 5:
    num1 = int(input('\033[0;32mDigite um número: \033[m'))
    num2 = int(input('\033[0;32mDigite outro número: \033[m'))
    opção = int(input('\033[0;32mO que você gostaria de fazer com esses números?\033[m\n'
                      '\033[1;34;40m[1] SOMAR\033[m\n'
                      '\033[1;31;40m[2] MULTIPLICAR\033[m\n'
                      '\033[1;36;40m[3] MAIOR\033[m\n'
                      '\033[1;33;40m[4] NOVOS NÚMEROS\033[m\n'
                      '\033[1;35;40m[5] ENCERRAR PROGRAMA\033[m\n'))
    if opção > 5:
        print('\033[0;32mComando inválido. Tente novamente \033[m')
if opção == 1:
    print('\033[0;32mA soma entre {} e {} é {}.\033[m'.format(num1, num2,num1 + num2))
if opção == 2:
    print('\033[0;32mA multiplicação entre {} e {} é {}. \033[m'.format(num1, num2, num1 * num2))
if opção == 3:
    if num1 > num2:
        print('\033[0;32mO número {} é maior que {}.\033[m'.format(num1, num2))
    if num1 == num2:
        print('\033[0;32mOs números {} e {} são iguais. \033[m'.format(num1, num2))
    if num2 > num1:
        print('\033[0;32mO número {} é maior que {}.\033[m'.format(num2, num1))
if opção == 5:
    print('\033[0;32mObrigado! Volte sempre.\033[m')
