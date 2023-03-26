número = int(input('Digite um número inteiro: '))

print('''Escolha uma base para conversão:
\033[1;33m[ 1 ]\033[m converter para \033[1;33mBINÁRIO\033[m
\033[1;34m[ 2 ]\033[m converter para \033[1;34mOCTAL\033[m
\033[1;36m[ 3 ]\033[m converter para \033[1;36mHEXADECIMAL\033[m ''')

num = int(input(' '))

if num == 1:
    print('{} convertido para \033[1;33mBINÁRIO\033[m é igual a {}'.format(número, bin(número)[2:]))
if num == 2:
    print('{} convertido para \033[1;34mOCTAL\033[m é igual a {}'.format(número, oct(número)[2:]))
if num == 3:
    print('{} convertido para \033[1;36mHEXADECIMAL\033[m é igual a {}'.format(número, hex(número)[2:]))
else:
    print('Esta opção não existe.')