num = (int(input("Digite um valor: ")),
       int(input("Digite outro valor: ")),
       int(input("Digite mais um valor: ")),
       int(input("Digite o último valor: ")))
par = []
cont = 0

print(f"Os números escolhidos foram: {num}")
print(f"O número 9 apareceu {num.count(9)} vezes.")
for c in num:
    if c == 3:
        cont += 1

if cont > 0:
    print(f"O número 3 apareceu primeiro na posição {num.index(3) + 1}.")
else:
    print("O número 3 não aparece nenhuma vez")

print("Os valores pares digitados foram: ")
for n in num:
    if c % 2 == 0:
        print(n, end=" ")