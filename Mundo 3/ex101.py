print("FUNÇÃO VOTO")
from datetime import datetime
def voto(ano):
    idade = datetime.now().year - ano
    if idade < 16:
        print("NEGADO")
    elif idade < 18:
        print("OPCIONAL")
    elif idade < 59:
        print("OBRIGATÓRIO")
    else:
        print("OPCIONAL")
voto(2007)