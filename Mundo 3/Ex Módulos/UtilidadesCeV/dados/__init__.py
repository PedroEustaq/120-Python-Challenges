def leiaDinheiro(f):
    num = str(input(f))
    if num.isdigit():
        return int(num)
    else:
        print("Não é um número!")
    while num.isdigit() == False:
        num = str(input("Digite o preço: "))
        if num.isdigit():
            return int(num)