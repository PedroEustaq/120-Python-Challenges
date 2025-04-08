nomeJogador = str(input("Nome do jogador: "))
print("ANALISANDO UM JOGADOR")
qtnPart = int(input(f"Quantas partidas {nomeJogador} jogou?"))
gols = list()
TOT = 0
for c in range(0,qtnPart):
    qtnGols = int(input(f"Quantos gols na partida {c}: "))
    TOT += qtnGols
    gols.append(qtnGols)

dicionarioJogador = {"nome":nomeJogador, "gols":gols, "total": TOT}
print("=-="*30)
for k,v in dicionarioJogador.items():
    print(f" o campo {k} tem o valor {v}")
print("=-="*30)
for pos,c in enumerate(gols):
    print(f"Na partida {pos}, fez {c} gols.")
