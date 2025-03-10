print("NÚMERO PRIMO")
numero = int(input("Qual o seu número: "))




if (numero == 2) or (numero == 3):
    print("É Primo!")
elif (numero % 2 == 0) or (numero % 3 == 0) or (numero <= 1):
    print("Não é primo!")
else:
    print("É Primo!")