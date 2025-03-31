impar = list()
pares = list()
listaFinal = list()
for c in range(0,7):
    numero = int(input("Digite o número: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impar.append(numero)
pares.sort()
impar.sort()
listaFinal.append(pares[:])
listaFinal.append(impar[:])
print("=-="*30)
print(f"Pares: {listaFinal[0]}, Impares: {listaFinal[1]}")