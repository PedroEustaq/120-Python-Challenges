n = 0
s = 0
qtn = 0
while n != 999:
    n = int(input("Digite um número"))
    if n == 999:
        break
    s += n
    qtn += 1
print("A Soma dos números é " + str(s))
print("A Quantidade de números digitados foram "+ str(qtn) + " números")