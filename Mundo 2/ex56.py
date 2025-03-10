print("INFORMAÇÔES CADASTRADAS")
mediaIdade = 0
maiorIdade = 0
nomeMaiorIdade = ""
mulheresMenorQue = 0
for c in range(0,4):
    print("====")
    nome = str(input("Qual seu nome?"))
    idade = int(input("Qual sua idade?"))
    sexo = int(input("Qual seu sexo? (Masculino : 1 / Feminino : 2)"))
    mediaIdade += idade
    if (idade > maiorIdade) and (sexo == 1):
        maiorIdade = idade
        nomeMaiorIdade = nome
    if (sexo == 2) and (idade < 20):
        mulheresMenorQue += 1
mediaIdade = mediaIdade / 4
print("====")
print("A Média da idade do grupo é " + str(mediaIdade) + " anos")
print("O Homem com maior idade é " + nomeMaiorIdade)
print("A Quantidade de mulheres com menos de 20 anos é " + str(mulheresMenorQue))
