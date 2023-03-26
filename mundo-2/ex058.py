from random import randint

adv = int(input('O Robô pensou em um número de 1 a 10, tente adivinhar: '))

robo = randint(1, 10)
tentativas = 1

while adv != robo:
    if adv < robo:
        print('\033[1;36;40mUm pouco mais!\033[m')
    if adv > robo:
        print('\033[1;36;40mUm pouco menos!\033[m')
    adv = int(input('\033[1;31;40mERROU!\033[m Tente novamente: '))
    tentativas += 1
if tentativas == 1:
    print('\033[1;32;40mBOA! Você conseguiu acertar em apenas {} tentativa. \033[m'.format(tentativas))
else:
    print('\033[1;32;40mBOA! Você conseguiu acertar em {} tentativas. \033[m'.format(tentativas))