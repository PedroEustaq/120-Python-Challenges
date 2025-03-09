import math
print("TRIÂNGULO RETÂNGULO")
cOposto = float(input("Cateto Oposto vale quanto?"))
cAdjace = float(input("Adjacente vale quanto?"))
hip = math.hypot(cOposto,cAdjace)

print("o tamanho é de {:.2f}".format(hip))