from datetime import  datetime
print("CATEGORIA DE NATAÇÃO")
anoNasc = int(input("Qual seu ano de nascimento"))
anoAtual = datetime.now().year
idade = anoAtual - anoNasc

if idade <= 9:
    print("Sua categoria na natação é Mirim")
elif idade <= 14:
    print("Sua categoria na natação é Infantil")
elif idade <= 19:
    print("Sua categoria na natação é Junior")
elif idade == 20:
    print("Sua categoria na natação é Senior")
else:
    print("Sua categoria na natação é MASTER")