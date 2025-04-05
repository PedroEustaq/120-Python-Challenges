def leiaInt(frase):
    valor = ""
    while not valor.isdigit():
        valor = str(input(frase))
    if valor.isdigit():
        print(valor)
leiaInt("Digite um número")
