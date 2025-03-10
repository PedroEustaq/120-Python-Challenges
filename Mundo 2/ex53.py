print("FRASE PÁLINDROMA")
frase = str(input("Escreva sua frase: "))
array = list(frase)
if array[::-1] == array:
    print("É uma frase palíndroma!")
else:
    print("Não é uma frase palíndroma")
print(array[::-1])
print(array)