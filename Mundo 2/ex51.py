print("PROGRESSÃO ARITMÉTICA")
primTerm = int(input("Primeiro termo da progressão: "))
razao = int(input("Razão: "))
minimo = 0
for c in range(primTerm, primTerm+100, razao):
    if minimo != 10:
        minimo += 1
        print(c)