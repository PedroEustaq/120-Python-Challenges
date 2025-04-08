print("EXPRESSÃO MATEMÁTICA")
expressao = str(input("Digite a expressão matemática: "))
outroParente = expressao.count(")")
if expressao.count("(") == outroParente:
    print("Expressao válida!")
else:
    print("Expressao inválida...")
print(expressao)
print(expressao.count("("))
