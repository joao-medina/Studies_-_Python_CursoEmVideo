lista = []
continuar = "S"

while True:
    valor = int(input("Digite um valor: "))
    if valor in lista:
        print("Valor duplicado! Não vou adicionar...")
    else:
        lista.append(valor)
        print("Valor adicionado com sucesso...")

    continuar = (input("Você quer continuar? [S/N]")).upper()
    if continuar == "S":
        continue
    elif continuar == "N":
        break

lista.sort()
print("-=" * 15, "\n", f"Você digitou os valores: {lista}")