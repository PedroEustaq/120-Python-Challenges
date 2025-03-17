valorSerSacado = int(input("Qual o valor a ser sacado?"))

Celula1 = valorSerSacado / 50
valorSerSacado = valorSerSacado % 50

Celula2 = valorSerSacado / 20
valorSerSacado = valorSerSacado % 20

Celula3 = valorSerSacado / 10
valorSerSacado = valorSerSacado % 10

Celula4 = valorSerSacado / 1
valorSerSacado = valorSerSacado % 1

print(" Notas de R$ 50 Reais: "+ str(int(Celula1))+ "\n Notas de R$ 20 Reais: "+ str(int(Celula2))+ "\nNotas de R$ 10 Reais: " + str(int(Celula3))+ " \n Notas de 1 Real: " + str(int(Celula4)))