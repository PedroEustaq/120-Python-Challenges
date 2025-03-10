print("MAIOR PESO E MENOR PESO")

maior = 0
menor = 0
for c in range(0,5):
    pesoAtual = int(input("Qual seu peso?"))
    if pesoAtual > maior:
        maior = pesoAtual
    elif menor == 0:
        menor = pesoAtual
    elif pesoAtual < menor:
        menor = pesoAtual
print("O maior peso é " + str(maior) + " e o menor peso é " + str(menor))