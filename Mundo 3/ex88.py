import random
print("SORTEADOR DE JOGOS DA MEGA SENA")
quantosJogos = int(input("Quantos jogos você quer que eu sorteie?"))
presentes = list()
jogos = list()
novalist = list()
for c in range(0,quantosJogos):
    for n in range(1,7):
        num =  random.randint(1, 60)
        while num in novalist:
            num = random.randint(1, 60)
            #print("ja esta na lista")
        novalist.append(num)
    presentes.append(novalist[:])
    novalist.clear()
    print(f"O {c}º sorteio contém: {presentes[c]}")