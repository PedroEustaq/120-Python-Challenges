querContinuarJogador = "S"
gols = list()
print("FUNÇÕES LEVANTAMENTO DE JOGADOR")
TOT = 0
listaJogadores = list()
while querContinuarJogador == "S":
    nomeJogador = str(input("Nome do jogador: "))
    qtnPart = int(input(f"Quantas partidas {nomeJogador} jogou?"))

    for c in range(0,qtnPart):
        qtnGols = int(input(f"Quantos gols na partida {c}: "))
        TOT += qtnGols
        gols.append(qtnGols)
    querContinuarJogador = str(input("Quer continuar? [S/N]"))
    dicionarioJogador = {"nome":nomeJogador, "gols":gols, "total": TOT}
    listaJogadores.append(dicionarioJogador.copy())
print("=-="*30)
print(dicionarioJogador)
for pos,c in enumerate(listaJogadores):
    print(f"COD: {pos} NOME: {listaJogadores[pos]["nome"]} GOLS: {listaJogadores[pos]["gols"]} TOTAL: {listaJogadores[pos]["total"]}")
mostrarDados = int(input("Mostrar dados de qual jogador? (insira o código): "))
while mostrarDados != 999:
    print(f"- LEVANTAMENTO DO JOGADOR {listaJogadores[mostrarDados]["nome"]}")
    for pos,c in enumerate(listaJogadores[mostrarDados]["gols"]):
        print(f"No Jogo {pos} fez {c} gols.")
    mostrarDados = int(input("Mostrar dados de qual jogador?: "))