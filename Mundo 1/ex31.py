print("CORRIDA TÁXI")
km = int(input("Quantos Km?"))
if km <200:
    custo = km * 0.50
    print("O custo total sera de {}".format(custo))
else:
    custo= km * 0.45
    print("O custo total sera de {}".format(custo))