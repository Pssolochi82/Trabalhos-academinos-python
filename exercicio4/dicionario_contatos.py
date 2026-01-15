#Crie um dicionário com três contactos (nome -> telefone). Adicione um novo contacto e remova outro.
contatos = {"Ana": "123456789", "Bruno": "987654321", "Carlos": "456789123"}
contatos["Diana"] = "321654987"
del contatos["Ana"]
print("Dicionário após adicionar Diana e remover Ana:", contatos)