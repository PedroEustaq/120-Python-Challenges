sOUn = "s"
print("SEPARAR POR PESO LEVE/PESADO")
galera = list()
novaPessoa = list()
maisPesada = list()
maisLeve = list()
qtnCada = 0
while sOUn.upper() == "S":
    nome = str(input("Nome: "))
    peso = int(input("Peso: "))
    sOUn = str(input("Quer Continuar? [S/N] "))
    if peso >= 100:
        maisPesada.append(nome)
    elif peso <= 70:
        maisLeve.append(nome)
    novaPessoa.append(nome)
    novaPessoa.append(peso)
    galera.append(novaPessoa[:])
    qtnCada += 1
    novaPessoa.clear()
print("=-="*30)
print(f"Foram cadastradas {qtnCada} pessoas.")
print(f"As pessoas mais pesadas são: {maisPesada} e as pessoas mais leves são {maisLeve}")
