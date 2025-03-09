import math
import random
import time
print("ADIVINHE O NÚMERO")
print("Vamos jogar um jogo! Pense em um númeoro de 0 a 5")
nAleatorio = random.randint(0,5)
meuN = int(input("Qual seu chute?"))
print("PROCESSANDO..")
time.sleep(3)
if meuN == nAleatorio:
    print("Parabéns,você conseguiu! é uma mestre da computação!")
else:
    print("Você perdeu, afinal, eu sou uma máquina, seu futuro sucessor")
print("A propósito o número era {}".format(nAleatorio))