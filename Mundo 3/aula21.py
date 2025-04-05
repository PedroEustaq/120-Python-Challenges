

#def contador(i,f,p):
#    '''
#    -> Faz uma contagem e mostra na tela
#    :param i: inicio da contagem
#    :param f: fim da contagem
#    :param p: passo da contagem
#    :return: Sem retorno
#    '''
#    c = i
#    while c <= f:
#        print(f"{c}", end=" ")
#        c += p
#    print('FIM!')
#contador(2,10,2)
#help(contador)

#def somar(a=0,b=0,c=0):
#    '''
#    -> Faz uma contagem e mostra na tela
#    :param a: valor 1
#    :param b: valor 2
#    :param c: valor 3
#    :return: Sem retorno
#    '''
#    s = a + b + c
#    print(f'A Soma vale {s}')
#somar(2,10,2)
#help(somar)

#def teste():
#    x = 8
#    print(f"Na função teste, n vale {n}")
#    print(f"Na função teste, x vale {x}")
#n = 2
#print(f"No programa principal n vale {n}")
#print(f"No programa principal, x vale {x}")
#teste()

#def teste(b):
#    a = 8
#    b += 4
#    c = 2
#    print(f"A dentro vale {a}")
#    print(f"B dentro vale {b}")
#    print(f"C dentro vale {c}")
#a = 5
#print(f"A fora vale {a}")
#teste(a)

def somar(a=0,b=0,c=0):
    s = a + b + c
    return s
somar(2,10,2)
print(f"{somar(2,3)}")