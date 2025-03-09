print("ALUGUEL DE CARRO")
dias = int(input("Quantos dias usou o carro?"))
km = float(input("Quantos Km rodou com o carro?"))
diasF = dias * 60
kmf = km * 0.15
f = diasF + kmf
print("O total a pagar será de {}".format(f))