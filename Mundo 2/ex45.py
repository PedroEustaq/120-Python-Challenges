import random

print("JOKENPÔ")
escolhaJogador = int(input("Escolha sua ação! (1 = Tesoura / 2 = Pedra / 3 = Papel)"))
posibilidades = [1,2,3]
escolhaPC = random.choice(posibilidades)

if escolhaJogador == escolhaPC:
    print("EMPATOU!")
elif (escolhaJogador == 1 and escolhaPC == 2) or (escolhaJogador == 2 and escolhaPC == 3) or (escolhaJogador == 3 and escolhaPC == 1):
    print("O Computador ganhou!")
else:
    print("Você ganhou!")
