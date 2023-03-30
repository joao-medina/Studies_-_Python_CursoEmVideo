from datetime import date

atual = date.today().year

usuario = dict()
usuario["nome"] = input("Nome: ")
datanasc = int(input("Ano em que nasceu: "))
usuario["idade"] = atual - datanasc

cart = int(input("Carteira de trabalho: (0) não tem "))
if cart != 0:
    usuario["carteira-trabalho"] = cart
    usuario["contratacao"] = int(input("Ano de contratação: "))
    usuario["salario"] = int(input("Salário: "))
    usuario["idade-aposentadoria"] = (usuario["contratacao"] - datanasc) + 35

print("=" * 45)
print(f"Nome        -  {usuario['nome']}")
print(f"Idade       -  {usuario['idade']}")
if cart != 0:
    print(f"ctps        -  {usuario['carteira-trabalho']}")
    print(f"Contratação -  {usuario['contratacao']}")
    print(f"Salário     -  {usuario['salario']}")
    print("=" * 45)
    print(f"Você irá se aposentar em {usuario['contratacao'] + 35} com {usuario['idade-aposentadoria']} anos.")
print("=" * 45)