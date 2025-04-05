import moeda2

p = float(input('Digite o preço: R$'))
print(f"A metade de {p} é  {moeda2.metade(p,True)}")
print(f"O dobro de {p} é  {moeda2.dobro(p,False)}")
print(f"Aumentando em 10, {p} vira  {moeda2.aumentar(p,10,False)}")
print(f"Diminuindo 10 de {p} é  {moeda2.diminuir(p,10,True)}")