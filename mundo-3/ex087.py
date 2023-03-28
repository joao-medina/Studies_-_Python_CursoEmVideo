matriz = [[],
          [],
          []]
linha = 0
par = []
soma_par = 0
soma_coluna = 0
maior_linha = 0
contador = 0

while linha < 3:

    for c in range(1, 4):
        add = int(input("Insira um número: "))
        matriz[linha].append(add)
        if add % 2 == 0:
            par.append(add)

    if linha == 1:
        maior_linha = matriz[linha]

    soma_coluna += add
    linha += 1

for p in par:
    soma_par += p


print("=x" * 15)

while contador < 3:
    for l, v in enumerate(matriz[contador]):
            if l == 2:
                 print(v)
            if l != 2:
                 print(v, end="  ")
    contador += 1

print("=x" * 15)

maior_linha.sort(reverse = True)
print(f"A soma de todos os números pares digitados é {soma_par}.")
print(f"A soma dos valores da terceira coluna é {soma_coluna}.")
print(f"O maior valor da segunda linha é {maior_linha[0]}.")
 