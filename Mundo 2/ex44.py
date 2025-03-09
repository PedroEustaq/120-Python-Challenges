print("VALOR DE PRODUTO E CONDIÇÃO DE PAGAMENTO150")
precodoProdu = float(input("Qual o preco do produto?"))
meiodePagamento = str(input("Qual sera o meio de pagamento? (Dinheiro / Cartão) "))

if meiodePagamento.upper() == "DINHEIRO":
    precodoProdu = precodoProdu * 0.9
    print("O preco com desconto de 10% ficará em " + str(precodoProdu) + " reais")
elif meiodePagamento.upper() == "CARTÃO":
    aVista = int(input("Em Quantas vezes no cartão?"))
    if aVista == 1:
        precodoProdu = precodoProdu * 0.95
        print("O preco com descodo de 5% ficará em " + str(precodoProdu))
    elif aVista == 2:
        print("O preco do produto sera de" + str(precodoProdu))
    else:
        precodoProdu = precodoProdu * 1.20
        print("Vamos adicionar 20% de juros no preco do produto, resultando em " + str(precodoProdu))
