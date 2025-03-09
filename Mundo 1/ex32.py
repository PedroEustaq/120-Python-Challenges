print("ANO BISSEXTO")
ano = int(input("Verificar se um ano é bissexto! Qual o ano?"))
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("Opa, é um ano bissexto!!")
        else:
            print("não é um ano bissexto..")
    else:
        print("não é um ano bissexto")
else:
    print("não é um ano bissexto..")