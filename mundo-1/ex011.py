h = float(input('Insira a altura da sua parede: '))
l = float(input('Insira, também, a largura: '))
print('Sua parede tem uma área de {:.2f} m², Será necessário no mínimo {:.0f} l de tinta para pinta-la.'.format(h*l, ((h*l)//2+1)))
