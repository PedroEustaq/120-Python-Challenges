def contador(i,f,p):
    if p == 0:
        p = 1
    if p < 0:
        p = p * -1
    if i > f:
        p -= p*2
    for v in range(i,f,p):
        print(v)
contador(1,10,1)
contador(10,1,2)
contador(int(input("Inicio: ")),int(input("Final: ")),int(input("Passo:")) )