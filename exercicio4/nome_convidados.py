#Peça ao utilizador um nome e verifique, com o operador in, se esse nome está numa lista predefinida de convidados.
convidados = ["Ana", "Carlos", "Beatriz", "Daniel", "Eva"]
nome = input("Digite um nome: ")
if nome in convidados:
    print(f"O nome {nome} está na lista de convidados.")
else:
    print(f"O nome {nome} não está na lista de convidados.")