print("ANALISADOR DE PRODUTOS DE MERCADO")
listaCompra = []
continuar = "S"
totalGasto = 0
maismil = 0
maisbarato = 0
maisbaratoNome = ""
while continuar == "S":
    nomePro = str(input("Qual o nome do produto? "))
    precoPro = float(input("Qual o preco do produto? "))
    listaCompra += [nomePro,precoPro]
    totalGasto += precoPro
    if precoPro > 1000:
        maismil += 1
    if maisbarato == 0:
        maisbarato = precoPro
        maisbaratoNome = nomePro
    elif precoPro < maisbarato:
        maisbarato < precoPro
        maisbaratoNome = nomePro
    continuar = str(input("Quer continuar? [ S / N ] "))
    print("-"*30)
    print("O valor total da sua compra sera de: " +str(totalGasto) +" reais")
    print("O produto mais barato foi " + maisbaratoNome + " custando apenas " + str(maisbarato) + " reais.")
    print("Temos "+ str(maismil) + " produtos que custam mais de 1000 reais.")
