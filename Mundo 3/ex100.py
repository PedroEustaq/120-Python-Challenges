import random

numeros = list()
def sorteia():
    for n in range(0,5):
        aleato = random.randint(0,10)
        numeros.append(aleato)
    print(f"Os números sorteados foram: {numeros}")

def somaPar():
    ValorPar = 0
    for v in numeros:
        if v % 2 == 0:
            ValorPar += v
    print(f"A Soma de todos os números pares é {ValorPar}")
sorteia()
somaPar()