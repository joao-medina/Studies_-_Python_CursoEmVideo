pessoas = []
pessoa = []

while True:
    continuar = "continuar"
    pessoa.append(input("Nome: "))
    pessoa.append(float(input("Peso: ")))

    pessoas.append(pessoa[:])
    pessoa.clear()

    while continuar != "S" and continuar != "N":    
        continuar = input("Você quer continuar? [S/N] ").upper()
    if continuar == "N":
        break

#maior peso
posicao = 0
maior_peso = pessoas[posicao][1]
while True:
    peso = pessoas[posicao][1]
    if peso > maior_peso:
        maior_peso = peso

    posicao += 1
    if posicao == len(pessoas):
        break

#mais pesados
mais_pesados = []
for c in pessoas:
    if c[1] == maior_peso:
        mais_pesados.append(c[0])

#menor peso
posicao = 0
menor_peso = pessoas[posicao][1]
while True:
    peso = pessoas[posicao][1]
    if peso < menor_peso:
        menor_peso = peso

    posicao += 1
    if posicao == len(pessoas):
        break

#mais leves
mais_leves = []
for l in pessoas:
    if l[1] == menor_peso:
        mais_leves.append(l[0])

print("=-" * 30)   
print(f"Foram cadastradas {len(pessoas)} pessoas.")
print(f"O maior peso foi de {maior_peso}Kg. Peso de {mais_pesados}")
print(f"O menor peso foi de {menor_peso}Kg. Peso de {mais_leves}")