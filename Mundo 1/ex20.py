from random import shuffle
print("EMBARALHAR ORDEM")
n1 = input("Qual o nome do Primeiro?")
n2 = input("Qual o nome do Segundo")
n3 = input("Qual o nome do Terceiro")
n4 = input("Qual o nome do Quarto")
lista = [n1,n2,n3,n4]
shuffle(lista)
print("A ordem de apresentação começará com " + str(lista))