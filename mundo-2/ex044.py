print('\033[1;35;40m='*7, 'Loja GUANABARA', '=======\033[m')

preço = float(input('Qual foi o valor da compra? '))

print('[ 1 ] À vista \033[1;34mdinheiro/cheque\033[m.\n'
      '[ 2 ] À vista no \033[1;34mcartão\033[m.\n'
      '[ 3 ] Em até \033[1;34m2x no cartão\033[m.\n'
      '[ 4 ] Em \033[1;34m3x ou mais no cartão\033[m')
opção = int(input('Escolha uma opção: '))

if opção == 1:
    print('\033[1mO valor a ser pago é de {:.2f} reais'.format((9 / 10) * preço))
elif opção == 2:
    print('\033[1mO valor a ser pago é de {:.2f} reais'.format((19 / 20) * preço))
elif opção == 3:
    print('\033[1mSerão 2 parcelas de {:.2f} reais.'.format(preço / 2))
elif opção == 4:
    parcelas = int(input('Quantas parcelas você gostaria? '))
    print('\033[1mSerão {} parcelas de {:.2f} reais'.format(parcelas, ((12 / 10) * preço) / parcelas))
else:
    print('\033[1mOpção inválida.')
