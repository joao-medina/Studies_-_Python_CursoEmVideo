from time import sleep

'''fat = int(input('Qual número você gostaria de saber o fatorial? '))
fat1 = fat

for c in range(fat - 1, 0, -1):
    fat *= c
print('\033[1;30;46m{}! = {}\033[m'.format(fat1, fat))'''
#Com "for"

fat = int(input('Qual número você gostaria de saber o fatorial? '))
fat1 = fat

while fat > 1:
    print('{} x'.format(fat), end=' ')
    sleep(0.25)
    fat -= 1
    fat1 *= fat
print('1 = {}'.format(fat1))
#com "while"
