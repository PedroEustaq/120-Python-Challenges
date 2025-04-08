print("NOTAS ALUNO COM DICIONÁRIOS")
nome = str(input("Nome: "))
media = float(input("Média: "))
aluno = dict()

if media >= 6:
    aluno["situacao"] = "Aprovado"
elif media >= 3:
    aluno["situacao"] = "Recuperação"
else:
    aluno["situacao"] = "Reprovado"
aluno["nome"] = nome
aluno["media"] = media
for k,v in aluno.items():
    print(f"O {k} é {v}")
