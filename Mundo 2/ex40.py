print("ALUNO APROVADO OU REPROVADO?")
nota1 = float(input("Primeira nota do aluno:"))
nota2 = float(input("Segunda nota do aluno:"))
media = (nota1 + nota2) / 2
if media < 5:
    print("Reprovado")
elif media < 6.9:
    print("Recuperação")
else:
    print("Aprovado")