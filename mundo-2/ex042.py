l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 == l3:
        print('Triângulo EQUILÁTERO')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Triângulo ISÓSCELES')
    elif l1 != l2 != l3 != l1:
        print('Triângulo ESCALENO')
else:
    print('Com os segmentos acima não é possível formar um triângulo')
