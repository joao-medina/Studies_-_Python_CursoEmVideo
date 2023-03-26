while True:
    valor = int(input("Digite o valor que você deseja: "))
    cinquenta = vinte = dez = um = 0

    cinquenta = valor / 50
    resto = valor % 50

    vinte = resto / 20
    resto %= 20

    dez = resto / 10
    resto %= 10

    um = resto / 1
    resto %= 1

    if resto == 0:
        break

print("Você recebe da máquina:\n"
      f"{int(cinquenta)} --- R$50,00\n"
      f"{int(vinte)} --- R$20,00\n"
      f"{int(dez)} --- R$10,00\n"
      f"{int(um)} --- R$1,00)")
