#Crie um set com nomes de alunos e verifique se um determinado nome está no set usando o operador in.
nomes_alunos = {"Ana", "Bruno", "Carlos", "Diana", "Eduardo"}
nome_verificar = "Carlos"
if nome_verificar in nomes_alunos:
    print(f"O nome {nome_verificar} está no set.")
else:
    print(f"O nome {nome_verificar} não está no set.")