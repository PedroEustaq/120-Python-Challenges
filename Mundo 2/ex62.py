print("PROGRESSÃO ARITMÉTICA")
primTerm = int(input("Primeiro termo da progressão: "))
razao = int(input("Razão: "))
minimo = 0
termGeral = primTerm + razao
QueroAte = 1
while minimo != 11:
    print(primTerm + (razao * minimo))
    minimo += 1
while QueroAte != 0:
    QueroAte = int(input("Quer mostrar mais alguns termos?"))
    termosNovos = 0
    while QueroAte != termosNovos:
        print(primTerm + (razao * (minimo + termosNovos)))
        termosNovos += 1
    minimo = minimo + termosNovos

