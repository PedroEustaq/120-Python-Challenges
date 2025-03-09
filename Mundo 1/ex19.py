import  random
print("ALUNO ALEATÓRIO")
n1 = input("Qual o nome do primeiro?")
n2 = input("Qual o nome do Segundo")
n3 = input("Qual o nome do Terceiro")
n4 = input("Qual o nome do Quarto")
lista = [n1,n2,n3,n4]
S = random.choice(lista)
print("o aluno escolhido sera o {}".format(S))
