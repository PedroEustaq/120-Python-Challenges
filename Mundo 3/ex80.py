tuplaa = [0,0,0,0,0]
for pos,c in enumerate(tuplaa):
    print(pos)
    n1 = int(input("Digite um valor: "))
    if tuplaa[4] < n1:
        tuplaa[4] = n1

    elif tuplaa[3] < n1:
        tuplaa[3] = n1

    elif tuplaa[2] < n1:
        tuplaa[2] = n1

    elif tuplaa[1] < n1:
        tuplaa[1] = n1

    elif tuplaa[0] < n1:
        tuplaa[0] = n1
print(tuplaa)