casa = float(input('Qual o valor da casa? '))
sal = float(input('Quanto é o seu salário? '))
ano = int(input('Quantos anos você pretende pagar?'))

prestação = casa / (ano * 12)

print('\033[4mPara pagar uma casa de R${:.2f} em {} anos. '.format(casa, ano), end='')
print('A prestação será de R${:.2f}\033[m'.format(prestação))

if prestação > (3 / 10) * sal:
    print('\033[1;31;40mPedido negado.\033[m')
else:
    print('\033[1;32;40mParabéns! pedido aprovado.\033[m')
