print("ANALISADOR DE UNIDADES")
numAleato = int(input("Digite um numero"))
u = numAleato // 1 % 10
d = numAleato // 10 % 10
c = numAleato // 100 % 10
m = numAleato // 1000 % 10

print("Unidades: " + str(u))
print("Dezenas: " + str(d))
print("Centenas: " + str(c))
print("Unidades de Milhar: " + str(m))