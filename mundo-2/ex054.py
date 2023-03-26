from datetime import date

maior = 0
menor = 0
for c in range(1, 5):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    if date.today().year - ano >= 18:
        maior += 1
    if date.today().year - ano < 18:
        menor += 1

print('\n\033[1;32;40mAo todo há {} pessoas maiores de idade\033[m'.format(maior))
print('\033[1;32;40mE também há {} pessoas menores de idade\033[m'.format(menor))
