from datetime import datetime

nome = str(input("Nome: "))
Nascimento = int(input("Ano de Nascimento: "))
anoA = datetime.now().year
idade = anoA - Nascimento
ctps = int(input("Carteira de Trabalho (0 não tem): "))
if ctps == 0:
    print("=-="*30)
    pessoa = {"nome":nome, "idade":idade, "ctps":ctps}
    for k,v in pessoa.items():
        print(f"{k} tem o valor {v}")
anoContratacao = int(input("Ano de contratação: "))
sala = int(input("Salario: "))
aposenta = anoContratacao + 35 - Nascimento
pessoa = {"nome":nome, "idade":idade, "ctps":ctps,"contratação":anoContratacao,"salário":sala,"aposentadoria":aposenta}
print("=-=" * 30)
for k,v in pessoa.items():
    print(f"{k} tem o valor {v}")