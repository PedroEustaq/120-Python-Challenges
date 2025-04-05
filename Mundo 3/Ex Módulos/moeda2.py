import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
valor = 1234.56

def aumentar(p,a,f):
    n = p + a
    if f == True:
        n = locale.currency(n, grouping=True)
    return n

def diminuir(p,a,f):
    n = p - a
    if f == True:
        n = locale.currency(n, grouping=True)
    return n
def dobro(p,f):
    p *= 2
    if f == True:
        p = locale.currency(p, grouping=True)
    return p
def metade(p,f):
    n = p / 2
    if f == True:
        n = locale.currency(n, grouping=True)
    return n

