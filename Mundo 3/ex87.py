print("ANALISADOR DE MATRIZES 3x3")
matriz = [ [[0],[1],[2]], [[0],[1],[2]], [[0],[1],[2]] ]
matrizR = list()
somaPares = 0
posInicial = 0
somaTerceiraCol = 0
maiorValorSegundaLin = 0
montarLinha = list()
for l in range(0,3):
        #print(matriz[l])
        #print(matriz)
    for c in range(0,3):
            #print(matriz[l][c])
        valor = int(input(f"Digite um valor para a posição {l}, {c}: "))
        if valor % 2 == 0:
            somaPares = somaPares + valor
        if c == 2:
            somaTerceiraCol = somaTerceiraCol + valor
        if l == 1:
            if valor > maiorValorSegundaLin:
                maiorValorSegundaLin = valor
        montarLinha.append(valor)
    matrizR.append(montarLinha[:])
    montarLinha.clear()
print("-=-"*30)
print("A Matriz sera assim: ")
print(f"{matrizR[0]}")
print(f"{matrizR[1]}")
print(f"{matrizR[2]}")
print(f"A Soma dos valores pares é {somaPares}")
print(f"A Soma dos valores da terceira coluna é {somaTerceiraCol}")
print(f"O Maior valor da segunda linha é {maiorValorSegundaLin}")