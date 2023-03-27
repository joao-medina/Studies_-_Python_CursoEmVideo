lista = []

while True:
    lista.append(int(input("Digite um valor: ")))
    continuar = input("Você quer continuar? [S/N] ").upper()
    if continuar == "S":
        continue
    elif continuar == "N":
        break

lista.sort(reverse = True)
num_elementos = len(lista)

print(f"Você digitou {num_elementos} elementos.")
print(f"Os valores em ordem decrescente são {lista}")
if 5 in lista:
    print("O valor 5 faz parte da lista.")
else:
    print("O valor 5 não faz parte da lista.")

    


