print("MAIOR E MENOR NÚMERO")
p1 = int(input("Primeiro valor"))
p2 = int(input("Segundo Valor"))
p3 = int(input("Terceiro Valor"))
maior = 0
menor = 9 * 9999
if p1 > maior:
    maior = p1
if p2 > maior:
    maior = p2
if p3 > maior:
    maior = p3
if p1 < menor:
    menor = p1
if p2 < menor:
    menor = p2
if p3 < menor:
    menor = p3
print("O Maior numero é {} e o menor é {}".format(maior,menor))