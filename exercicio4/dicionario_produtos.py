#A partir de um dicionário de preços de produtos, peça ao utilizador o nome de um produto e mostre o preço correspondente.
precos = {"arroz": 10.5, "feijão": 8.0, "carne": 25.0, "vegetais": 12.0}
nome_produto = input("Digite o nome do produto: ")
if nome_produto in precos:
    print(f"O preço do produto {nome_produto} é {precos[nome_produto]}")
else:
    print("Produto não encontrado.")