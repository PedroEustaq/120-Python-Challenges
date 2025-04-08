import random
import time
print("ADIVINHE O NÚMERO V2")
print("Vamos jogar um jogo! Pense em um númeoro de 0 a 10")
nAleatorio = random.randint(0,10)
vitoria = 0
while vitoria == 0:
    meuN = int(input("Qual seu chute?"))
    chutes = 0

    print("PROCESSANDO..")
    time.sleep(3)
    if meuN == nAleatorio:
        print("Parabéns,você conseguiu! é uma mestre da computação!")
        print("A propósito o número era {}".format(nAleatorio))
        print("Você chutou " + chutes + " vezes.")
        vitoria = 1
    else:
        print("Você perdeu, afinal, eu sou uma máquina, seu futuro sucessor")
        chutes += 1
