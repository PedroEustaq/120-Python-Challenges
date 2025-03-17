n1 = int(input("Qual o primeiro valor? "))
n2 = int(input("Qual o segundo valor? "))
n3 = int(input("Qual o terceiro valor? "))
n4 = int(input("Qual o quarto valor? "))

tupla = (n1,n2,n3,n4)

nove = tupla.count(9)
if 3 in tupla:
    valortres = tupla.index(3)
else:
    print("Não há nenhum valor 3")
p1 = ""
p2 = ""
p3 = ""
p4 = ""

if (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0) and (n4 % 2 == 0):
    for c in tupla:
        if n1 % 2 == 0:
            p1 = n1
        if n2 % 2 == 0:
            p2 = n2
        if n3 % 2 == 0:
            p3 = n3
        if n4 % 2 == 0:
            p4 = n4
    print("Os números pares são: " + p1, p2, p3, p4)
else:
    print("Não possui números pares")
print("O número nove aparece: " + str(nove) + " vezes")
