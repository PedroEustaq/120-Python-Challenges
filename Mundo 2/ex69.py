continuar = "S"
qtnDezoi = 0
qtnHome = 0
sexo = "A"
mulheresVint = 0
while continuar == "S":
    print("CADASTRAR PESSOAS")
    idade = int(input("IDADE: "))
    while sexo not in ["M","F"]:
        sexo = str(input("SEXO [ M / F ]: "))
    if idade > 18:
        qtnDezoi += 1
    if sexo == "M":
        qtnHome += 1
    if (idade < 20) and (sexo == "F"):
        mulheresVint += 1
    sexo = "A"
    continuar = "A"
    while continuar not in ["S","N"]:
        continuar = str(input("QUER CONTINUAR? [ S / N ] ?"))
        if continuar == "N":
            continuar = "N"
print("PESSOAS COM MAIS DE 18 ANOS: " + str(qtnDezoi))
print("HOMENS CADASTRADOS: " + str(qtnHome))
print("MULHERES COM MENOS DE 20 ANOS: " + str(mulheresVint))