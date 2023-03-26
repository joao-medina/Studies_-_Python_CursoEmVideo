sal = float(input('Digite o valor do seu salário: '))

if sal > 1250.00:
    print('Seu novo salário é R${:.2f}'.format(sal + 0.1 * sal))
else:
    print('Seu novo salário é R${:.2f}'.format(sal + 0.15 * sal))
