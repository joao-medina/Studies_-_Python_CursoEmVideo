num = int(input('Digite um número: '))

tot = 0
for c in range(1, num + 1):
    if num % c == 0:
       print('\033[32m', end = ' ')
       tot += 1
    else:
        print('\033[31m', end = ' ')
    print('{}'.format(c), end = ' ')

print('')
print('\033[mO número {} foi dividido {} vezes'.format(num, tot))

if tot == 2:
    print('É primo.')
else:
    print('Não é primo.')