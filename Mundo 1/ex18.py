import math
print("SENO COSSENO E TANGENTE")
ang = float(input("Qual o valor do angulo?"))
seno = math.sin(math.radians(ang))
print("o angulo {} tem o seno de {}".format(ang,seno))
cos = math.cos(math.radians(ang))
print("o angulo de {} tem o cosseno de {}".format(ang,cos))
tange = math.tan(math.radians(ang))
print("o angulo de {} tem a tangente de {}".format(ang,tange))