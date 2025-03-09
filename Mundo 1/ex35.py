print("MONTAR UM TRIÂNGULO")
p1 = int(input("Tamanho da Primeira Reta"))
p2 = int(input("Tamanho da Segunda Reta"))
p3 = int(input("Tamanho da Terceira Reta"))
if p1 + p2 > p3:
    if p1 + p3 > p2:
        if p2 + p3 > p1:
            print("Dá sim para formar um triangulo!")
        else:
            print("Não dá")
    else:
        print("Não tem como!")
else:
    print("Impossivel criar um!")