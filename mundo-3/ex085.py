#Primeiro modo:
'''
lista = []

for c in range(1, 8):
    lista.append(int(input(f"Digite o {c}° valor: ")))

lista.sort()

print("=-" * 25)

print("Os valore pares digitados foram: ", end= "") 
for p in lista:
    if p % 2 == 0:
        print(p, end=" ")

print("\nOs valores ímpares digitados foram: ", end= "")
for i in lista:
    if i % 2 == 1:
        print(i, end=" ")'''

#Segundo modo:

par = []
impar = []
lista =[par, impar]

for c in range(0, 7):
    add = int(input("Digite um valor: "))
    if add % 2 == 0:
        par.append(add)
    if add % 2 == 1:
        impar.append(add)

print(f"Os valores pares digitados foram {lista[0]}")
print(f"Os valores impares digitados foram {lista[1]}")
