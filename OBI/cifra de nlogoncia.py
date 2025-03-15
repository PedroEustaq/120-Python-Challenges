palavra = str(input("Qual a palavra que deseja cifrar meu rei?"))
cont = 1
largura = len(palavra)
alfabeto = "abcdefghijklmnopqrstuv"
for cont in range(largura):
    print(palavra[cont])
    if palavra[cont] == ("a" or "e" or "i" or "u" or "o"):
        print(palavra.find(palavra[cont]))
    else:
        print(palavra.find(palavra[cont]))

