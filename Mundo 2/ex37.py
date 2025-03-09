print("FORMATADOR DE BASES")
numeroInt = int(input("Escreva o número:"))
escolha = int(input("Escolha uma opção: \n 1 - Binário \n 2 - Octal \n 3 - hexadecimal \n"))
if escolha == 1:
    print(bin(numeroInt)[2:])
if escolha == 2:
    print(oct(numeroInt)[2:])
if escolha == 3:
    print(hex(numeroInt)[2:].upper())