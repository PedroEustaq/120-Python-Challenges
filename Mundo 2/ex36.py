print("PRESTAÇÃO DE CASA")
valorDaCasa= int(input("Qual o valor da casa?"))
salarioComprador = int(input("Qual o seu salário?"))
quantosAnosVaiPagar = int(input("Em anos você gostaria de pagar a casa?"))

emMeses = quantosAnosVaiPagar * 12

prestaCaoMensal = valorDaCasa / emMeses

if prestaCaoMensal < ((salarioComprador / 100) * 30):
    print("Prestação de R$" + str(valorDaCasa) + " aprovada! Valor atual " + str(round(prestaCaoMensal, 2)))
else:
    print("Prestação de R$" + str(valorDaCasa) + " recusada! \n Não podemos exceder seu salário em 30%")
