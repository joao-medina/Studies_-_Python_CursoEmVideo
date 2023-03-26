total_gasto = mil_ou_mais = mais_barato = cont = 0

while True:
    nome = input("Nome do produto: ")
    preço = float(input("Preço do produto: "))
    total_gasto += preço
    cont += 1

    if cont == 1:
        mais_barato = preço
        produto_mais_barato = nome

    if preço >= 1000:
        mil_ou_mais += 1

    if preço < mais_barato:
        mais_barato = preço
        produto_mais_barato = nome

    continuar = input("Você quer continuar? [S/N]: ").lower().strip()[0]
    if continuar == "n":
        break

print(f"O total gastos na compra foi de R${total_gasto:.2f}\n"
      f"{mil_ou_mais} produtos custam mil ou mais.\n"
      f"O produto mais barato foi {produto_mais_barato} que custa R${mais_barato:.2f}")
