import random

print("ROLANDO UM DADO")
dadosJogadores = {"Jogador1":random.randint(1,6),"Jogador2":random.randint(1,6),"Jogador3":random.randint(1,6),"Jogador4":random.randint(1,6)}
dadosOrdenados = dict(sorted(dadosJogadores.items(), key=lambda item: item[1], reverse=True))
for k,v in dadosJogadores.items():
    print(f"O {k} tirou {v}")
contagem = 1
print("-=-"*30)
print("COLOCAÇÃO FINAL:")
for k,v in dadosOrdenados.items():
    print(f"{contagem}º {k} tirou {v}")
    contagem += 1