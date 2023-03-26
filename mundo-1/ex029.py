velo = int(input('Digite quanto estava a sua velocidade(Km/h): '))

if velo <= 80:
    print('Boa viagem!')
else:
    print('Devagar aí, campeão. Você foi multado em {} reais'.format((velo-80)*7))
