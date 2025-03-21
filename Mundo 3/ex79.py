print("Digite parar para parar a execução")
parar = ""
numeros = []
sequencia = 0
while sequencia == 0:
    n = str(input("Cadastre o novo número: "))
    if n == "parar":
        break
    if n in numeros:
        print("Número já cadastrado tente outro")
    else:
        numeros.append(int(n))
        print("Numeros até agora: " + str(numeros))
print("Os números em ordem ficam assim: " + str(sorted(numeros)))