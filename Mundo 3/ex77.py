palavras = ('COMER', 'BEBER', 'CORRER', 'ANDAR', 'PULAR', 'DORMIR', 'FALAR', 'OUVIR', 'ESCREVER', 'LER', 'ESTUDAR')


aeiou = ("A","E","I","O","U")
for c in range(0,len(palavras)):
    temos = ""
    if aeiou[0] in palavras[c]:
        temos += "A "
    if aeiou[1] in palavras[c]:
        temos += "E "
    if aeiou[2] in palavras[c]:
        temos += "I "
    if aeiou[3] in palavras[c]:
        temos += "O "
    if aeiou[4] in palavras[c]:
        temos += "U "
    print(f"para a palavra {palavras[c]} temos como vogais: {temos}")