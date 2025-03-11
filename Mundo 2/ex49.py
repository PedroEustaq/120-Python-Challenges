print("TABUADA DO USUÁRIO")
inicial = int(input("Qual o numero inicial da tabuada?"))
inicio = 1
for c in range(1,11):
    resultado = c * inicial
    print(str(inicial) + "X" + str(c) + "=" + str(resultado))
    inicio += 1