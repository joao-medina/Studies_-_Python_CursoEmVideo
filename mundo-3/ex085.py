lista = []

for c in range(1, 8):
    lista.append(int(input(f"Digite o {c}° valor: ")))

lista.sort()

print("=-" * 25)

print("Os valore pares digitados foram: ", end= "") 
for p in lista:
    if p % 2 == 0:
        print(p, end=" ")

print("\nOs valores ímpares digitados foram: ", end= "")
for i in lista:
    if i % 2 == 1:
        print(i, end=" ")
