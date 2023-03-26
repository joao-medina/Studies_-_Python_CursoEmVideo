lista = ("Lápis", 2.50,
         "Caneta", 3,
         "Tesoura", 4.75,
         "Cola", 9.75,
         "Estojo", 22.50)

for c in range(0, len(lista), 2):
    print(f"{lista[c]:.<30}"
          f"R${lista[c-1]:.2f}")



