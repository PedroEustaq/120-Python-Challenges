print("FATORIAL DE UM NÚMERO")
num = int(input("Qual o número a ser fatorado?"))

fatorial = num
for num in range(1,num):
    fatorial = fatorial * num
print("Fatorial: " + str(fatorial))
