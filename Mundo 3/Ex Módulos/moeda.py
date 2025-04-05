import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
valor = 1234.56

def aumentar(p,a):
    n = p + a
    return n

def diminuir(p,a):
    n = p - a
    return n
def dobro(p):
    p *= 2
    return p
def metade(p):
    n = p / 2
    return n

def moeda(p):
    n = locale.currency(p, grouping=True)
    return n

def resumo(p):
    print("---"*30)
    print("  RESUMO DO VALOR   ")
    print("---"*30)
    print(f"Preço analisado: {moeda(p)}")
    print(f"Dobro do preço: {moeda(dobro(p))}")
    print(f"Metade do preço: {moeda(metade(p))}")
    print(f"R$80 a mais do preço: {moeda(aumentar(p,80))}")
    print(f"R$35 a menos do preço: {moeda(diminuir(p,35))}")