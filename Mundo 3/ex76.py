print("MERCADO TUPLA'S")
tuplaPreco = ("Banana",2,"Morango",5,"Bolinho",10,"Pão",3,"Chocottone",14)
print("-"*25)
for c in range(0, len(tuplaPreco), 2):
    print(f'{tuplaPreco[c]:<20}{tuplaPreco[c + 1]}')