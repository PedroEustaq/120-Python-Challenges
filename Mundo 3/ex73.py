print("INFORMAÇÕES DE TIMES")
times = (
    "América-MG",
    "Athletico Paranaense",
    "Atlético Goianiense",
    "Atlético-MG",
    "Avaí",
    "Bahia",
    "Botafogo",
    "Ceará",
    "Corinthians",
    "Coritiba",
    "Cuiabá",
    "Flamengo",
    "Fluminense",
    "Fortaleza",
    "Goiás",
    "Chapecoense",
    "Grêmio",
    "Internacional",
    "Palmeiras",
    "Santos",
    "São Paulo"
)
print("Os Primeiros 5 times do campeonoato são " + str(times[:5]))
print("Os Últimos 4 colocados do campeonoato são " + str(times[-4:]))
print("Em ordem alfabética os times ficam assim: " + str(sorted(times)))
print("O time chapecoense está na posição: " + str(times.index("Chapecoense") + 1))