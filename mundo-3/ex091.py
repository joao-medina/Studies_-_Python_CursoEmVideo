from random import randint
from operator import itemgetter
from time import sleep

ranking = list()
jogo = {"jogador-1": randint(1,6),
        "jogador-2": randint(1,6),
        "jogador-3": randint(1,6),
        "jogador-4": randint(1,6)}

print("=" * 35)
print(" "* 9, "Jogo de Dados")
print("=" * 35)
print()

for k, v in jogo.items():
    print(f"{k}: {v}\n")
    sleep(0.5)
print("=" * 35, "\n")

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for c, d in enumerate(ranking):
    print(f"{c + 1}° lugar: {d[0]} com {d[1]} pontos")
    print()
    sleep(0.5)

