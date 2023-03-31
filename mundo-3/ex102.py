def fat(fatorial, show = False):
    cont = fatorial - 1
    if show == True:
        print(fatorial, end = " * ")    
    while cont > 0:
        if show == True and cont > 1:
            print(cont, end=" * ")
        if show == True and cont == 1:
            print(cont, end=" = ")
        fatorial *= cont
        cont -= 1
    return fatorial

fatorial = int(input("Número para ver o fatorial: "))
print(fat(fatorial, show=True))
