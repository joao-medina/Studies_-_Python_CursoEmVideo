lista = []

for c in range(0, 5):
    valor = int(input("Insira um valor: "))

    if c == 0 or valor > lista[-1]:
        lista.append(valor)

    else:
        posicao = 0
        while posicao <= len(lista):
            if valor <= lista[posicao]:
                lista.insert(posicao, valor)
                break
        posicao += 1

print("-=" * 20)
print(f"Os valores digitados em ordem foram: {lista}")