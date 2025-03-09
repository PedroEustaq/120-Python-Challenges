print("AUMENTAR SALÁRIO")
sal = int(input("Qual o seu salario?"))
if sal >=1250:
    aum = (sal / 100) * 10 + sal
    print("Seu novo salário é {}".format(aum))
else:
    aum = (sal /100) * 15 + sal
    print("Seu novo salario é {}".format(aum))