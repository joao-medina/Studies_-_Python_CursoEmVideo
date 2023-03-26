print('\033[1;36;40m-='*6, 'JOKENPOO!!!', '=-'*6, '\033[m')
print ( '\033[7;32;40m[ 1 ] PEDRA   \033[m\n'
        '\033[7;34;40m[ 2 ] PAPEL   \033[m\n'
        '\033[7;31;40m[ 3 ] TESOURA \033[m\n'
        '')
opção = int(input('\033[1mEscolha uma opção: \033[m'))

from random import choice
from time import sleep
num = choice([1, 2, 3])

if opção > 3:
        print('\033[1;31mOpção inválida.\033[m')
else:
        print('\033[1;36mJO\033[m')
        sleep(1)
        print('\033[1;36mKEN\033[m')
        sleep(1)
        print('\033[1;36mPOO!!\033[m')
        sleep(1)
        print('\033[1;36;40m-=\033[m' * 12,)

        if opção == 1:
                print('Você escolheu \033[7;32;40mPEDRA!\033[m')
        elif opção == 2:
                print('Você escolheu \033[7;34;40mPAPEL!\033[m')
        elif opção == 3:
                print('Você escolheu \033[7;31;40mTESOURA!\033[m')
        sleep(2)
        if num == 1:
                print('O robô escolheu \033[7;32;40mPEDRA!\033[m')
        elif num == 2:
                print('O robô escolheu \033[7;34;40mPAPEL!\033[m')
        elif num == 3:
                print('O robô escolheu \033[7;31;40mTESOURA!\033[m')

        print('\033[1;36;40m-=\033[m' * 12,)
        print('')

        sleep(1)
        if opção == 1 and num == 3 or opção == 3 and num == 1:
                print('\033[4;36mPEDRA QUEBRA TESOURA!!\033[m')
        elif opção == 2 and num == 1 or opção == 1 and num == 2:
                print('\033[4;36mPAPEL EMBRULHA PEDRA!!\033[m')
        elif opção == 3 and num == 2 or opção == 2 and num == 3:
                print('\033[4;36mTESOURA CORTA PAPEL!!\033[m')

        sleep(1)
        if opção == num:
                print('\033[1;34mVocê EMPATOU com o robô!!\033[m')
        elif opção == 1 and num == 3 or opção == 2 and num == 1 or opção == 3 and num == 2:
                print('\033[1;32mVocê GANHOU do robô!!\033[m')
        else:
                print('\033[1;31mVocê PERDEU pro robô!!\033[m')
