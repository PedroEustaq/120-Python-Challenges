def acessarHelp(f):
    print("\033[7;30;46m")
    help(f)
    print("\033[m")
termina = "a"
while termina != "FIM":
    termina = str(input("Função ou Biblioteca >"))
    acessarHelp(termina)