n_termos = int(input("QUANTOS TERMOS VOCÊ QUER MOSTRAR? "))
c = 1 #contador
primeiro = 0
segundo = 1
i = primeiro + segundo #fórmula da sequência de fibonacci

print(0,"→", 1, end =" → ")
while c <= n_termos - 2:
    print(i, end=" → ")
    primeiro = segundo
    segundo = i
    c += 1
    i = primeiro + segundo

print("FIM")
