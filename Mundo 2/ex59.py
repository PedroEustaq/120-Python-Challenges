print("MENU DE SOMA, MULTIPLICAR...")
sairPrograma = 0
print("Digite dois números")
num1 = int(input("Valor número 1: "))
num2 = int(input("Valor número 2: "))
while sairPrograma == 0:
    print(" [1] SOMAR \n [2] MULTIPLICAR \n [3] MAIOR \n [4] NOVOS NÚMEROS \n [5] SAIR DO PROGRAMA")
    escolha = int(input(""))
    if escolha == 1:
        soma = num1 + num2
        print(soma)
    if escolha == 2:
        mult = num1 * num2
        print(mult)
    if escolha == 3:
        if num1 > num2:
            print(num1)
        else:
            print(num2)
    if escolha == 4:
        num1 = int(input("Valor número 1: "))
        num2 = int(input("Valor número 2: "))
    if escolha == 5:
        sairPrograma = 1
print("ENCERRANDO O PROGRAMA...")