print("PRIMEIRO E ÚLTIMO NOME")
nome = str(input("Qual o seu nome?")).strip()
nomL = nome.split(" ")
print("Primeiro nome {}, ultimo nome {}".format(nomL[0],nomL[len(nomL)-1]))