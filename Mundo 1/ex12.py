print("DESCONTO EM PRODUTO 5%")
preco = int(input("Qual o preço do produto"))
desc = preco / 100 * 5
final = preco - desc
print("Seu desconto sera de {} reais".format(final))