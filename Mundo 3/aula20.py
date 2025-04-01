#def lin():
#    print("=-="*30)

#lin()
#print("CURSO EM VÍDEO")
#lin()
#print("APRENDA PYTHON")
#lin()

#def titulo(msg):
#    print("=-="*20)
#    print(msg)
#    print("=-="*20)
#titulo("ERRO")
#titulo("Pedro Eustáquio")
#def soma(a,b):
#    c = a + b
#    print(f"A soma de {a} e {b} é igual a {c}")
#soma(2,3)
#def contador(*num):
#    print(num)
#    for v in num:
#        print(v)
#    print("FIM!")

#contador(2,3,9)
#contador(0,8)
#contador(4,4,3,2,4)
valores = [2,5,3,4,8,1,9]
def dobra(list):
    for pos,v in enumerate(list):
        list[pos] *= 2
        print(list[pos])


dobra(valores)
print(valores)
