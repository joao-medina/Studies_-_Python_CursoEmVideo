palavras = "Aprender", "Programar", "Linguagem", "Python"

for c in palavras:
    print(f"Na palavra {c} temos:", end=" ")
    for letra in c:
        if letra.lower() in "a e i o u":
            print(letra, end=" ")
    print(" \n")