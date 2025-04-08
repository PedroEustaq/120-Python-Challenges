print("FUNÇÃO GOLS DE UM JOGADOR")
def ficha(nome="SemNome" , gols=0):
    print(f"O jogador {nome} fez {gols}")
nomeJoga = str(input("Nome do jogador"))
golsJoga = str(input("Gols feitos:"))
if golsJoga.isnumeric():
    golsJoga = int(golsJoga)
else:
    golsJoga = 0
if nomeJoga.strip() == "":
    ficha(gols=golsJoga)
else:
    ficha(nomeJoga,golsJoga)

