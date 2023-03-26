primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))

termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print('{} ☛ '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSE')
    mais = int(input('Quantos termos você quer mais? '))
print('{} Termos mostrados'.format(cont - 1))