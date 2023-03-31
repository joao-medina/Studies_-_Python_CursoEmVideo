from datetime import date

def validacao(ano):
    idade = date.today().year - ano
    if idade >= 18 and idade <= 65:
        obg = "VOTO OBRIGATÓRIO"
    elif idade < 16:
        obg = "NÃO PODE VOTAR"
    else:
        obg = "VOTO OPCIONAL"
    print(obg)

ano_nasc = int(input("Em que ano você nasceu? "))
print("Status de votação: ")
print(validacao(ano_nasc))

