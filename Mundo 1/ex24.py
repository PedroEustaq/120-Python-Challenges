print("SUA CIDADE COMEÇA COM SANTO?")
nomeInput = str(input("Qual sua cidade?")).strip()
print(nomeInput[:5].upper() == "SANTO")