n = "oi"
lista = []
impar = []
par = []
while n != "parar":
    n = str(input("Digite um valor: "))
    if n == "parar":
        break
    lista.append(int(n))
    if (int(n) % 2 == 0):
        par.append(int(n))
    else:
        impar.append(int(n))
    print("Lista padrão: " +str(lista))
    print("Lista impar: "+ str(impar))
    print("Lista par: " + str(par))