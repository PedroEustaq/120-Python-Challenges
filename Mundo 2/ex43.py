import math
print("IMC")
altura = float(input("Qual sua altura?"))
massa = float(input("Qual seu peso?"))
IMC = round((massa / math.pow(altura, 2)),2 )
print("Seu IMC correspondente é " + str(round(IMC, 2)))
if IMC < 18.5:
    print("Abaixo do peso")
elif IMC < 25:
    print("Peso ideal")
elif IMC < 30:
    print("Sobrepeso")
elif IMC < 40:
    print("Obesidade")
else:
    print("Obesidade mórbida")
