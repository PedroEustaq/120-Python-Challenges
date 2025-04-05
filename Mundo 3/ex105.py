def notas(*notas, sit):
    informac = dict()
    qtn = 0
    maior = 0
    menor = 0
    totalNotas = 0
    for v in notas:
        if qtn == 0:
            menor = v
        elif (v < menor):
            menor = v
        if v > maior:
            maior = v
        totalNotas += v
        qtn += 1
    media = totalNotas / len(notas)
    if sit == True:
        if media >= 7:
            situac = "BOA"
        elif media >= 3:
            situac = "RUIM"
        informac = {"Quantidade De Notas":qtn,"Maior nota":maior,"Menor nota":menor,"Média da Turma":media,"Situação":situac}
    else:
        informac = {"Quantidade De Notas": qtn, "Maior nota": maior, "Menor nota": menor, "Média da Turma": media}
    return informac
print(notas(11,2,8,10,6, sit=True))
