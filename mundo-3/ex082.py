lista = []
lista_par = []
lista_impar = []

while True:
    valor = int(input("Digite um número: (0 para encerrar)\n"))
    if valor != 0:
        lista.append(valor)
    else:
        break

for c in lista:
    if c % 2 == 0:
        lista_par.append(c)
    if c % 2 == 1:
        lista_impar.append(c)

print(f"Sua lista: {lista}")
print(f"Sua lista par: {lista_par}")
print(f"Sua lista impar: {lista_impar}")