aluno = dict()
aluno["nome"] = input("Nome: ")
aluno["media"] = float(input(f"Média de {aluno['nome']}: "))

if aluno["media"] >= 6:
    aluno["situacao"] = "Aprovado"
else:
    aluno["situacao"] = "Reprovado"

print("=" * 30)
print(f" - Nome é igual a {aluno['nome']}")
print(f" - Média é igual a {aluno['media']}")
print(f" - Situação é igual a {aluno['situacao']}")