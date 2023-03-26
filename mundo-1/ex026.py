frase = (str(input('Digite uma frase: ')).lower()).strip()

print('A letra A aparece {} vezes'.format(frase.count('a')))
print('A primeira letra A aparece na posição', frase.find('a')+1)
print('A última letra A aparece na posição', frase.rfind('a')+1)
