import random

tente = int(input('Tente adivinhar o número (entre 1 e 5) que o robô pensou: '))

number = [1, 2, 3, 4, 5]
nselect = random.choice(number)

if tente == nselect:
    print('PARABÉNS! Você acertou!')
else:
    print('Número errado, eu pensei no {}.'.format(nselect))
