peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)

print('\033[1mSeu IMC é de {:.2f}\033[m'.format(imc))

if imc < 18.5:
    print('Você está abaixo do PESO.')
elif 18.5 <= imc < 25:
    print('Você está com o peso IDEAL.')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE.')
else:
    print('Você está com OBESIDADE MÓRBIDA')
