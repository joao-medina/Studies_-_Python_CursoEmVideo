print('=' * 30, '\n', '  Progressão Aritimética')
print('=' * 30)

num = int(input('Digite o primeiro número: '))
razão = int(input('Digite a razão: '))

enésimotermo = num + (10) * razão
for c in range (num, enésimotermo, razão):
    print(c, end = ' -> ')
print('Fim')
