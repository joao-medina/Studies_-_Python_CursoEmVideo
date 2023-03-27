expressao = input("Digite uma expressão matemática: ")
parenteses_abrindo = []
parentes_fechando = []

for c in expressao:
    if c == "(":
        parenteses_abrindo.append(c)
    if c == ")":
        parentes_fechando.append(c)

if len(parenteses_abrindo) == len(parentes_fechando):
    print("Expressão válida! :D")
else:
    print("Expressão inválida >:c")
