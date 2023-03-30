def titulo(txt):
    print("="*40)
    print("{:^40}".format(txt).upper())
    print("="*40)

texto = titulo(input("Insira um texto para virar um título: "))

print(texto)

