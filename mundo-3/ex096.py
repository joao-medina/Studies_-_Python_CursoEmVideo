def area(largura, comprimento):
    a = largura * comprimento
    return a

largura = float(input("Qual a largura do terreno? "))
comprimento = float(input("Qual o comprimento do terreno"))

area = area(largura, comprimento)
print(f"A área do terreno é {area}m")