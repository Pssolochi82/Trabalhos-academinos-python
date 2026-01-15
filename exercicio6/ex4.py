#Defina um dicionário com notas de alunos (nome: tuplo de 3 notas);use in para verificar se um aluno existe e calcule a média das suas notas.
alunos = {
    "Ana": (15, 16, 17),
    "Carlos": (14, 13, 12),
    "Maria": (18, 19, 20)
}
nome_aluno = "Ana"
if nome_aluno in alunos:
    notas = alunos[nome_aluno]
    media = sum(notas) / len(notas)
    print(f"A média das notas de {nome_aluno} é: {media}")
else:
    print(f"O aluno {nome_aluno} não existe.")