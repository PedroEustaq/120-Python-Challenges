print("MOSTRAR NÚMEROS INFINITAMENTE A MENOS QUE 999")
digite = int(input("Digite um número"))
soma = digite
while digite != 999:
    soma = digite + soma
    print(digite)
    digite = int(input("Digite um número"))
print(soma)

