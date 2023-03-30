user = dict()
lista = list()
idades = list()
mulheres = list()
acimamedia = list()

while True:
    nome = input("Nome: ")
    sexo = input("Sexo: [M/F] ").upper()
    while True:
        if sexo == "F":
            mulheres.append(nome)
        if sexo == "M" or sexo == "F":
            break
        else:
            sexo = input("ERRO! Responda apenas M ou F: ").upper()

    idade = int(input("Idade: "))

    continuar = input("Continuar? [S/N] ").upper()
    while True:
        if continuar == "S" or continuar == "N":
            break
        else:
            continuar = input("ERRO! Responda apenas S ou N: ").upper()

    user = {"nome":nome, "sexo":sexo, "idade":idade, }
    lista.append(user.copy())

    if continuar == "N":
        break

#calcular média de idade
for c in lista:
    idades.append(c['idade'])
media = sum(idades) / len(idades)

#calcular quais estão acima da média:
for c in lista:
    if c['idade'] > media:
        acimamedia.append(c)


print("=" * 50)
print(f"A) Ao todo temos {len(lista)} pessoas cadastradas.")
print(f"B) A média de idade é de {media} anos")
print("C)", end=" ")
if len(mulheres) == 0:
    print("Nenhuma mulher foi cadastrada.")
if len(mulheres) == 1:
    print(f"A única mulher cadastrada foi {mulheres[0]}")
else:
    print(f"As mulheres cadastradas foram", end=" ")
    for v, m in enumerate(mulheres):
        if v + 1 == len(mulheres):
            print(f"e {m}.")
        else:
            if v + 2 == len(mulheres):
                print(f"{m}", end =" ") 
            else:    
                print(f"{m},", end =" ")

print("Lista de quem está acima da média: ")
for h in acimamedia:
    print(f"     - Nome = {h['nome']}; sexo = {h['sexo']}; idade = {h['idade']}")      

print()
print("<< ENCERRADO >>")