print("FUNÇÃO ESCREVA")
def escreva(t):
    largura = len(t) + 2
    print("-"*largura)
    print(" "+ t)
    print("-" * largura)
escreva(str(input("Texto: ")))