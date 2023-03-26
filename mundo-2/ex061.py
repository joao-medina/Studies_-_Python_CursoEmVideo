'''num = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
enésimotermo = num + (10 * razão)

while num <= enésimotermo:
    print(num, end = ' ☛ ')
    num += razão
print('FIM!')'''

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))

termo = primeiro
cont = 1

while cont < 10:
    print('{} ☛ '.format(termo), end='')
    termo += razão
    cont += 1
print(termo)