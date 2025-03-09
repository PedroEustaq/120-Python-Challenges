vel = int(input("Qual a velocidade do Carro?"))
if vel >= 80:
    preco = vel - 80
    precoF = 7 * preco
    print("O preço final sera de {}".format(precoF))
else:
    print("Nada será cobrado")
