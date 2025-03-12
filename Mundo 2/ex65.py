querContinua = "S"
totalNum = 0
quantNum = 0
maiorNum = 0
menorNum = 0
while querContinua == "S":
    novoNum = int(input("Adicionar novo número"))
    if (maiorNum == 0) and (menorNum == 0):
        maiorNum = novoNum
        menorNum = novoNum
    if novoNum > maiorNum:
        maiorNum = novoNum
    if novoNum < menorNum:
        menorNum = menorNum
    quantNum += 1
    totalNum = totalNum + novoNum
    mediaNums = totalNum / quantNum
    querContinua = str(input("Quer continuar?"))
print("Valor total dos números: " + str(totalNum))
print("Quantia total de números: " + str(quantNum))
print("Média de números: " + str(mediaNums))
