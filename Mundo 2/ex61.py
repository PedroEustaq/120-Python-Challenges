print("PROGRESSÃO ARITMÉTICA")
primTerm = int(input("Primeiro termo da progressão: "))
razao = int(input("Razão: "))
minimo = 0
termGeral = primTerm + razao
while minimo != 10:
        print(primTerm + (razao * minimo))
        minimo += 1