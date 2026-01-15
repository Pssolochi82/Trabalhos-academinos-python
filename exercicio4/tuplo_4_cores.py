#Crie um tuplo com 4 cores. Converta-o para uma lista, altere um dos elementos e depois converta de volta para tuplo.
cores = ("vermelho", "verde", "azul", "amarelo")
print("Tuplo original:", cores)
lista_cores = list(cores)
lista_cores[2] = "roxo"
cores = tuple(lista_cores)
print("Tuplo após alteração:", cores)