#Usando um set, remova todos os valores repetidos de uma lista de inscrições numa formação e apresente quantos participantes únicos existem.
inscricoes = ["Ana", "Bruno", "Carlos", "Ana", "David", "Bruno"]
participantes_unicos = set(inscricoes)
print(f"Número de participantes únicos: {len(participantes_unicos)}")