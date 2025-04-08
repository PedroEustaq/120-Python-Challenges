quercontinuar = "S"
print("CADASTRO E NOTAS DE ALUNOS")
tuplaAlunos = list()
novoAluno = list()
mostrarNota = 0
while quercontinuar.upper() == "S":
    nomeAluno = str(input("Nome: "))
    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    novoAluno.append(nomeAluno)
    novoAluno.append(nota1)
    novoAluno.append(nota2)
    tuplaAlunos.append(novoAluno[:])
    novoAluno.clear()
    quercontinuar = str(input("Quer continuar? [S / N]"))
print("-=-"*30)
print("No.  NOME   MÉDIA")
print("---"*30)

for pos,a in enumerate(tuplaAlunos):
    media = (a[1] + a[2]) / 2
    print(f"{pos}....{a[0]}.....{media}")
print("---"*30)
while mostrarNota != 999:
    mostrarNota = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if mostrarNota == 999:
        break
    print(f"Notas de {tuplaAlunos[mostrarNota][0]} são {tuplaAlunos[mostrarNota][1]} e {tuplaAlunos[mostrarNota][2]}")
