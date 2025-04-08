querContinua = "S"
pessoas = list()
totPessoas = 0
print("CALCULAR MÉDIA DE IDADE ENTRE N PESSOAS")
totalIdade = 0
todasMulheres = list()
while querContinua.upper() == "S":
    nome = str(input("Nome: "))
    sexo = str(input("Sexo [M/F]: "))
    idade = int(input("Idade: "))
    dicionaPessoa = {"nome":nome,"sexo":sexo,"idade":idade}
    pessoas.append(dicionaPessoa)
    totPessoas += 1
    totalIdade += idade
    if sexo.upper() == "F":
        todasMulheres.append(nome)
    querContinua = str(input("Quer continuar? [S / N]: "))
media = totalIdade / len(pessoas)
maiorQMedia = list()
for pos,c in enumerate(pessoas):
    if pessoas[pos]["idade"] > media:
        maiorQMedia.append(pessoas[pos]["nome"])
print(f"A média de idade é: {media}")
print(f"Resultados maiores que a média: {maiorQMedia}")
