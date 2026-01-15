#Crie um dicionário em que as chaves são nomes de alunos e os valores são tuplos com (nota1, nota2). Calcule a média de cada aluno.
alunos = {"Ana": (8.5, 9.0), "Bruno": (7.0, 8.5), "Carlos": (9.5, 10.0)}
for nome, (nota1, nota2) in alunos.items():
    media = (nota1 + nota2) / 2
    print(f"A média de {nome} é {media}")