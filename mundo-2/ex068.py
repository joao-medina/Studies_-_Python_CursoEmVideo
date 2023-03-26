from random import randint
vitórias = 0

while True:
    imparpar = input("Par ou Ímpar? [P/I] ").lower().strip()[0]
    num = int(input("Escolha um número: "))
    pc = randint(1, 10)
    num = (num + pc) % 2
    if imparpar == "p":
        if num == 0:
            print(f"O computador escolheu {pc}.\n"
                  "Parabéns!! você ganhou.")
        elif num == 1:
            print(f"O computador escolheu {pc}.\n"
                  "PERDEDOR!! HAHAHAHAH")
            break
    elif imparpar == "i":
        if num == 1:
            print(f"O computador escolheu {pc}.\n"
                  "Parabéns!! você ganhou.")

        if num == 0:
            print(f"O computador escolheu {pc}.\n"
                  "PERDEDOR!! HAHAHAHAH")
            break
    else:
        print("Valor não identificado.")
    vitórias += 1

if vitórias > 1:
    print(f"Parabéns! Você teve {vitórias} vitórias consecutivas.")
else:
    if vitórias == 1:
        print("Você conseguiu ganhar apenas umas vez")
    elif vitórias == 0:
        print("Você não ganhou nenhuma vez")