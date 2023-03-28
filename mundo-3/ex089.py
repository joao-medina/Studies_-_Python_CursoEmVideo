numero_alunos = int(input("Quantos alunos você deseja inserir? "))
boletim = []
nota = []

for c in range(0, numero_alunos):
    nome = input("Nome: ")
    nota.append(float(input("Nota: ")))
    nota.append(float(input("Nota: ")))
    media = sum(nota) / 2

    aluno = [nome, nota[:], media]
    boletim.append(aluno[:])
    nota.clear()
    aluno.clear()

print("=" * 21)
print(" "* 2,"Boletim Escolar")
print("=" * 21)
print("  No. Nome     Média")
print("-"* 21)

for posicao, valor in enumerate(boletim):
    print("{:^6} {:^6} {:^6}".format(posicao + 1, valor[0], valor[2]))


while True:
    continuar = int(input("Qual aluno você deseja ver a nota? (0) para encerrar.\n"))
    if continuar > 0 and continuar <= len(boletim):
        print(f"{boletim[continuar - 1][0]} tirou {boletim[continuar - 1][1]}")
    elif continuar == 0:
        break
    else: 
        print("Aluno inválido")

print("Programa finalizado.")
