matriz = [[],
          [],
          []]
linha = 0
contador = 0

while linha < 3:

    for c in range(1, 4):
        add = int(input("Insira um número: "))
        matriz[linha].append(add)

    linha += 1

while contador < 3:
    for c, e in enumerate(matriz[contador]):
        if c == 2:
            print(e)
        if c != 2:
            print(e, end=" ")

    contador += 1
 
