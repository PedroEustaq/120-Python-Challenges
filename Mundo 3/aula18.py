#teste = list()

#teste.append("Gustavo")
#teste.append(40)
#galera = list()
#galera.append(teste[:])
#teste[0] = "Maria"
#teste[1] = 32

#print(teste)
#print(galera)

#galera = [["joao",19],["ana", 33],["joaguin", 13],["maria", 33]]
#print(galera[2][1])
#for p in galera:
#    print(f"{p[0]} tem {p[1]} anos de idade")

galera = list()
dado = list()
for c in range(0,5):
    dado.append(str(input("Nome:")))
    dado.append(int(input("Idade:")))
    galera.append(dado[:])
    dado.clear()
print(galera)