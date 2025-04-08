n = 0
print("CRIADOR DE TABUADAS")
calcN = 0
while calcN >= 0:
    calcN = int(input("De qual número você gostaria de ver a tabuada?"))
    if calcN < 0:
        break
    for c in range(1,11):
        resul = calcN * c
        print(str(calcN) + " X " + str(c) + " = " + str(resul))
print("TABUADA ENCERRADA!")
