quantosNum = int(input("Quantos números na sequencia fibonacci voce deseja?"))

primeiro = 0
segundo = 1
contagem = 3
print("\n 0 1")
while contagem <= quantosNum:
    final = segundo + primeiro
    print(final)
    primeiro = segundo
    segundo = final
    contagem += 1
