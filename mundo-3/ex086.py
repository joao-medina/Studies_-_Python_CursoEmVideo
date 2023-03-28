matriz = [[],
          [],
          []]
linha = 0
contador = 0

while linha < 3:
    for c in range(0, 3):
        add = int(input("Insira um número: "))
        matriz[linha].append(add)
    linha += 1

for i in range(0, 3):
    for c in range(0,3):
        print(f"[{matriz[i][c]:^5}]", end=" ")
    print()
    
