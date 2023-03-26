import math

ang = float(input('Digite o ângulo que você deseja: '))

s = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print('O seno é {:.2f}'.format(s))
print('O cosseno é {:.2f}'.format(cos))
print('A tangente é {:.2f}'.format(tang))
