print("TABUADA DO USUÁRIO")
inicial = int(input("Qual o numero inicial da tabuada?"))
ate = int(input("E vai até quanto?"))

for c in range(inicial,ate+1):
    resultado = c * inicial
    print(str(inicial) + "X" + str(c) + "=" + str(resultado))
