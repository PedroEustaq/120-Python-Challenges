print("TRIÂNGULOS")
p1 = int(input("Tamanho da Primeira Reta"))
p2 = int(input("Tamanho da Segunda Reta"))
p3 = int(input("Tamanho da Terceira Reta"))
if p1 + p2 > p3:
    if p1 + p3 > p2:
        if p2 + p3 > p1:
            print("Dá sim para formar um triangulo!")
            if p1 == p2 == p3:
                print("É um triângulo equilátero!")
            elif (p1 == p2) or (p1 == p3) or (p2 == p3):
                print("É um triângulo isóceles")
            else:
                print("É um triângulo escaleno")
        else:
            print("Não dá")
    else:
        print("Não tem como!")
else:
    print("Impossivel criar um!")