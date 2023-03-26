nome = str(input('Digite seu nome: ')).lstrip()

print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

lista = (nome.split())

print('Seu segundo nome é {} e ele tem {} letras.'.format(lista[1], len(lista[1])))
