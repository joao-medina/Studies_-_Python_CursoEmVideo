dist = float(input('Digite a distância que vocÊ percorrerá: '))

if dist <= 200:
    print('O valor será {:.2f} reais'.format(dist*0.5))
else:
    print('O valor será {:.2f} reais'.format(dist*0.45))
