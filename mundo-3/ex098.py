from time import sleep

def contador(inicio, fim, intervalo):
    if intervalo < 0:
        intervalo *= -1
    if intervalo == 0:
        intervalo = 1
    if fim > inicio and inicio > 0:
        for c in range(inicio, fim + 1, intervalo):
            print(c)
            sleep(0.3)
    if inicio > fim:
        for c in range(inicio, fim -1, -intervalo):
            print(c)
            sleep(0.3)
    if inicio < 0 and fim < 0:
        for c in range(inicio, fim + 1, intervalo):
            print(c)
            sleep(0.3)
    if inicio < 0 and fim > 0:
        for c in range(inicio, fim + 1, intervalo):
            print(c)
            sleep(0.3)
    print("FIM!")


while True:
    inicio = int(input("Inicio: "))
    fim = int(input("Fim: "))
    intervalo = int(input("Intervalo: "))

    print(contador(inicio, fim, intervalo))