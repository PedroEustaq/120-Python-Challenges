print("ANO DE NASCIMENTO MAIOR IDADE")

maior = 0
menor = 0
for c in range(0,7):
    idade = int(input("Qual sua idade?"))
    if idade > 21:
        maior += 1
    else:
        menor += 1
print("De 7 pessoas "+ str(maior) + " são de maior idade, e " + str(menor) + " são de menor idade.")
