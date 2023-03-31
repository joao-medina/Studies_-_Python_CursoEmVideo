from random import randint

def aleatorio(tamanho):
    lista = []
    for c in range(0, tamanho):
        num = randint(1, 9)
        lista.append(num)
    return lista

def somapar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    return soma


tamanho = int(input("Defina o tamanho da lista: "))
lista = aleatorio(tamanho)
print(lista)
print (f"A soma de todos os números pares desta lista é {somapar(lista)}")

