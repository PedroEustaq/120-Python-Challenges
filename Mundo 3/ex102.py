print("FUNÇÃO FATORIAL")
def fatorial(numero,show=True):
    '''
    -> Faz uma contagem e mostra na tela
    :param numero: o numero que deseja fatoral
    :param show: devemos mostrar o processo fatorial?
    :return: Sem retorno
    '''

    c = numero
    fat = 1
    c -= 1
    fat *= numero
    if show == True:
        print(f"{numero} ", end="")
        for v in range(1,numero):
            fat *= c
            print(f"X {c} ", end='')
            c -= 1
    print(f"\n O Fatorial é: {fat}")
fatorial(10,False)