soma = 0
cont = 0
for vezestrês in range(0, 501, 3):
    if vezestrês % 2 == 1:
        cont += 1
        soma += vezestrês
print('A soma de todos os valores é', soma)
print('Contem', cont, 'números.')
