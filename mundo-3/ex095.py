lista = list()
jogador = dict()
gol_partida = list()

continuar = "S"

while continuar == "S":
    nome = input("Nome do jogador: ")
    n_partidas = int(input(f"Quantas partidas {nome} jogou? "))
    for c in range(0, n_partidas):
        gol_partida.append(int(input(f"Quantos gols na partida {c + 1}? ")))

    jogador = {"nome":nome, "partidas":gol_partida[:]}
    lista.append((jogador).copy())
    gol_partida.clear()

    while True:
        continuar = input("Você quer continuar? [S/N] ").upper()
        if continuar == "S" or continuar == "N":
            break
        else:
            print("COMANDO INVÁLIDO!")

print("=" * 40)
print("{:^4} {:^10} {:^10}".format("cod", "nome", "gols"))
print("-" * 40)

cod = 1
for p in range(0, len(lista)):
    nomejog = lista[p]['nome']
    gols = lista[p]['partidas']
    soma = sum(gols)
    print("{:^4} {:^10} {:^10} {}".format(cod, nomejog, soma, gols))
    cod += 1

print("-" * 40)

while True:
    escolha = int(input("Qual jogador você gostaria de ver? [0] para encerrar "))
    while escolha > len(lista):
        escolha = int(input("Insira um código de jogador válido: "))
    if escolha == 0:
        break

    print(f" -- Levantamento do jogador: {lista[escolha - 1]['nome']}")
    lista_analisada = (lista[escolha - 1]['partidas'][:])
    for posicao, a in enumerate(lista_analisada):
        print(f"No jogo {posicao + 1} fez {a} gols. ")

    lista_analisada.clear()
    print("-" * 40)

print("<<ENCERRADO>>")
