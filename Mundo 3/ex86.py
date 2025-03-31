
matriz = [ [[0],[1],[2]], [[0],[1],[2]], [[0],[1],[2]] ]
matrizR = list()
tru = True
posInicial = 0
montarLinha = list()
for l in range(0,3):
        #print(matriz[l])
        #print(matriz)
    for c in range(0,3):
            #print(matriz[l][c])
        valor = int(input(f"Digite um valor para a posição {l}, {c}: "))
        montarLinha.append(valor)
    matrizR.append(montarLinha[:])
    montarLinha.clear()
print("-=-"*30)
print("A Matriz sera assim: ")
print(f"{matrizR[0]}")
print(f"{matrizR[1]}")
print(f"{matrizR[2]}")