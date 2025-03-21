n1 = int(input("Qual o primeiro número?"))
n2 = int(input("Qual o segundo número?"))
n3 = int(input("Qual o terceiro número?"))
n4 = int(input("Qual o quarto número?"))
n5 = int(input("Qual o quinto número?"))
localizadoMenor = ""
localizadoMaior = ""
valores = (n1,n2,n3,n4,n5)
maiorV = max(valores)
menorV = min(valores)
for pos,c in enumerate(valores):
    #print(c)
    if c == menorV:
        localizadoMenor = localizadoMenor + str(pos) + " "
       # print(pos)
    if c == maiorV:
        localizadoMaior = localizadoMaior + str(pos) + " "
       # print(pos)
print(f"O maior valor é {maiorV} e esta localizado em {localizadoMaior} e o menor valor é {menorV} e esta localizado em {localizadoMenor}")
