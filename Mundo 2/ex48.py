print("SOMA IMPARES MULTIPLOS DE TRÊS")

soma = 0
for c in range(1,500):
    if (c % 2 == 1) and (c % 3 == 0):
        print(str(c) + " é impar e multiplo de 3!")
        soma += c

print("A Soma de todos os valores é " + str(soma))