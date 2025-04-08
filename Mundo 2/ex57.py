print("M OU F?")
fimResposa = 0

while fimResposa == 0:
    sexoP = str(input("Qual seu sexo? [ M/F ]"))
    if sexoP == "M":
        print("Você é masculino")
        fimResposa = 1
    if sexoP == "S":
        fimResposa = 1
        print("Você é feminina")