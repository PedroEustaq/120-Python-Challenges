n = "oi"
lista = []
cincoEsta = ""
qtn = 0
print("O VALOR 5, ESTÁ PRESENTE?")
while n != "parar":
    n = str(input("Digite um valor: "))
    lista.append(int(n))
    qtn += 1
    if 5 in lista:
        cincoEsta = " \n O valor 5 esta presente na lista! "
    else:
        cincoEsta = " \n O valor 5 não esta presente na lista. "
    print(str(sorted(lista, reverse=True)) + cincoEsta + f"Foram digitados {qtn} valores")
