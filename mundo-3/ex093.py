gol = list()
jogador = dict()

nome = input("Nome do jogador: ")
partidas = int(input(f"Quantas partidas {nome} jogou? "))

for c in range(1, partidas + 1):
    gol.append(int(input(f"Quantos gols fez na {c}° partida: ")))

total = sum(gol)

jogador = {"nome":nome, "gols":gol, "total":total}

print("-=" * 30)
print(jogador)
print("-=" * 30)

print(f"O campo nome tem o valor {jogador['nome']}")
print(f"O campo gols tem o valor {jogador['gols']}")
print(f"O campo total tem o valor {jogador['total']}")
print("-=" * 30)

print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")

for c in range(1, partidas + 1):
    gol_partida = gol[c-1]
    print(f"     =>Na partida {c}, fez {gol_partida} gols.")