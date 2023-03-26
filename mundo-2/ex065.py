cont = soma = maior = menor = 0
continuar = "s"

while continuar == "s":
    num = int(input("Digite um número: "))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    continuar = input("Desejas continuar? [S/N] ").lower().strip()[0]

print("Você digitou {} números e a média foi {:.2f}\n"
      "O maior valor foi {} e o menor foi {}".format(cont, soma / cont, maior, menor))
