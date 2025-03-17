import random

r1 = random.randint(0, 10)
r2 = random.randint(0, 10)
r3 = random.randint(0, 10)
r4 = random.randint(0, 10)
tuplaGerada = (r1,r2,r3,r4)
maior = 0
menor = 0

for c in range(0,4):
        if tuplaGerada[c] > maior:
            maior = tuplaGerada[c]
        if menor == 0:
            menor = tuplaGerada[c]

        elif tuplaGerada[c] < menor:

            menor = tuplaGerada[c]

print("Tupla gerada: " + str(tuplaGerada))
print("Maior número: " + str(maior))
print("Menor número: " + str(menor))
