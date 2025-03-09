nome = str(input("Qual seu nome?"))
if nome == "Pedro":
    print("Seu nome é lindo!")
elif nome == "Gustavo" or  nome == "Maria" or nome == "Paulo":
    print("Seu nome é bem popular no Brasil!")
elif nome in 'Ana Jéssica Clara Raquel':
    print("Belo nome feminino!")
else:
    print("Huum.. seu nome é bem normal.")
print("Tenha um bom dia, " + nome + "!")