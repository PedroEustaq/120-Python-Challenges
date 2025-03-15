import random

minJoga = 0
escolhaPC = 0
perdeu = False
vitorias = 0
while perdeu == False:
    print("VAMOS JOGAR PAR OU ÍMPAR")
    minJoga = int(input(("QUAL SERA SUA ESCOLHA? [ 1 ] PAR [ 2 ] ÍMPAR ")))


    if minJoga == 1:
        while perdeu == False:
            escolhas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            escolhaPC = random.choice(escolhas)

            chuteMeu = int(input("OK AGORA CHUTE UM NÚMERO DE 1 A 10 "))
            numeroTotal = chuteMeu + escolhaPC

            if numeroTotal % 2 == 1:
                print("1...2...3.. deu " + str(numeroTotal) + "!!")
                print("Você perdeu! e você venceu exatamente " + str(vitorias) + " vezes!")
                perdeu = True
                break
            else:
                vitorias += 1
            print("1...2...3.. deu " + str(numeroTotal) +"!!")
    if minJoga == 2:
        while perdeu == False:
            escolhas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            escolhaPC = random.choice(escolhas)

            chuteMeu = int(input("OK AGORA CHUTE UM NÚMERO DE 1 A 10 "))
            numeroTotal = chuteMeu + escolhaPC

            if numeroTotal % 2 == 0:
                print("1...2...3.. deu " + str(numeroTotal) + "!!")
                print("Você perdeu! e você venceu exatamente " + str(vitorias) + " vezes!")
                perdeu = True
                break
            else:
                vitorias += 1
            print("1...2...3.. deu " + str(numeroTotal) +"!!")