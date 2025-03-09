from datetime import  datetime
print("ALISTAMENTO MILITAR")
anoNasci = int(input("Em que ano você nasceu?"))
anoAtual = datetime.now().year
restante = 18 - (anoAtual - anoNasci)
restTemp = (anoAtual - anoNasci) - 18
if (anoAtual - anoNasci) < 18:
    print("Daqui a  " + str(restante) +" anos")
    print("Você ainda vai se alistar ao serviço militar")
elif (anoAtual - anoNasci) > 18:
    print("Já passou " + str(restTemp) +" anos des de seu alistamento")
    print("Você não precisa se alistar ao serviço militar")
else:
    print("Você precisa se alistar ao serviço militar")