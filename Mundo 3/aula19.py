#pessoas = {'nome': "gustavo", 'sexo': "M","idade": 22}
#print(f"O {pessoas["nome"]} tem {pessoas["idade"]}")
#print(pessoas.items())
#del pessoas["sexo"]
#pessoas["nome"] = "Leandro"
#pessoas["peso"] = 99.5
#for k,v in pessoas.items():
#    print(k,v)
#estado1 = {"uf":"Rio de Janeiro","sigla":"RJ"}
#estado2 = {"uf":"São Paulo","sigla":"SP"}
#brasil = []
#brasil.append(estado1)
#brasil.append(estado2)
#print(brasil[0]["uf"])
#print(estado2)
estado = dict()
brasil = list()
for c  in range(0,3):
    estado["uf"] = str(input("Unidade Federativa: "))
    estado["sigla"] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())
print(brasil)