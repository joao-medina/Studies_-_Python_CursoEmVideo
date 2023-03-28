from time import sleep
import random
jogo = list()
jogos = list()

print("-" * 30)
print(" " * 10, "MEGA SENA")
print("-" * 30, "\n")

n_jogos = int(input("Quantos jogos você quer que eu sorteie?: "))

for j in range(0, n_jogos):
    jogo.clear()
    for c in range(0, 6):
        numero_aleatorio = random.randrange(61)
        jogo.append(numero_aleatorio)
    jogos.append(jogo[:])

for p, e in enumerate(jogos):
    sleep(0.5)
    print(f"Jogo {p + 1}", e)

print(" ")
print("-" * 30)
print(" " * 9, "BOA SORTE!")
print("-" * 30)

