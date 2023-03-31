def maior(* num):
    maior = 0
    for c in num:
        if c > maior:
            maior = c
    return maior    




maiornum = maior(1, 3, 4, 2, 8, 4)

print(maiornum)

