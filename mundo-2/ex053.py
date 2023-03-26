frase = input('Escreva uma frase: ').upper()
frasea = frase.replace(' ', '')
frase2 = frase[::-1]
frase2a = frase2.replace(' ', '')


print('{} ao contrário é'.format(frasea), frase2a)
if frasea == frase2a:
    print('Esta frase é um Palíndromo')
