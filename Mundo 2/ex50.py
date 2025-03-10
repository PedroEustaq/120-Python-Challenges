print("SOMA DE PARES")
soma = 0
for c in range(1,7):
    numero = int(input("Digite o " + str(c) + "º" + " número: "))
    if numero % 2 == 0:
        soma += numero
print("Soma total dos números pares " + str(soma))