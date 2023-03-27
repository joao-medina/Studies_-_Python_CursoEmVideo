lista = []
posicoes_maior = []
posicoes_menor = []

for c in range(1, 6):
    lista.append(input("Escolha um valor: "))
print("\n", "=--="*10, "\n")

lista_comparativa = lista[:] #copia da lista

#maior valor:
lista_comparativa.sort(reverse=True)
maior_valor = lista_comparativa[0]
for posicao, valor in enumerate(lista):
    if valor == maior_valor:
        posicoes_maior.append(posicao)
print(f"O maior valor foi {maior_valor} nas posições {posicoes_maior}")

#menor valor:
lista_comparativa.sort(reverse=False)
menor_valor = lista_comparativa[0]
for posicao, valor in enumerate(lista):
    if valor == menor_valor:
        posicoes_menor.append(posicao)
print(f"O menor valor foi {menor_valor} nas posições {posicoes_menor}")    
