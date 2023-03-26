maioridade = homens = mulheres_minoridade = 0

while True:
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").lower().strip()[0]
    if idade >= 18:
        maioridade += 1
    elif sexo == "m":
        homens += 1
    elif sexo == "f" and idade < 20:
        mulheres_minoridade += 1
    continuar = input("Deseja continuar? [S/N]: ").lower().strip()[0]
    if continuar == "n":
        break

print(f"Há {maioridade} pessoas de maior.\n"
      f"Há {homens} homens\n"
      f"Há {mulheres_minoridade} mulheres menores de 20 anos")