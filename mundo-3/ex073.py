brasileirão = ("Atlético Mineiro", "Palmeiras", "Flamengo", "Fortaleza", "Bragantino", "Corinthians", "Internacionaç", "Fluminense", "Athletico-PR", "Atléico Goianiense", "Cuibá", "Ceará", "São Paulo", "América-MG", "Juventude", "Santos", "Bahia", "Grêmio", "Sport Recife", "Chapecoense")

print("1 - Mostrar os 5 primeiros colocados.\n"
      "2 - Mostrar os 4 últimos colocados.\n"
      "3 - Lista com os times em ordem alfabéticaz.\n"
      "4 - Em qual posição está o time da Chapecoense.")
opção = int(input("Escolha uma opção: "))

if opção == 1:
    print("Os cinco primeiros colocados são: ")
    for c in range(0,5):
        print(brasileirão[c])

if opção == 2:
    print("Os últimos colocados da tabela são:")
    for c in range(16,20):
        print(brasileirão[c])

if opção == 3:
    ord = sorted(brasileirão)
    for c in ord:
        print(c)

if opção == 4:
    print(f"{brasileirão[19]} está na 20 posição")