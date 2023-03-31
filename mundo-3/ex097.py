def titulo(txt):
    linha = len(txt) * 3
    print("=" * linha)
    print(" " * (len(txt)-1), f"{txt}".upper(), " "*len(txt))
    print("=" * linha)

texto = titulo(input("Insira um texto para virar um título: "))

print(texto)

