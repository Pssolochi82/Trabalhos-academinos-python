#Usando um dicionário que guarda o stock de uma loja, verifique com in se um produto pedido pelo cliente existe antes de tentar aceder ao seu valor.
stock = {"camiseta": 0, "calça": 5, "sapato": 8}
produto = input("Digite o nome do produto: ")
if produto in stock:
    print(f"O produto '{produto}' está disponível. Quantidade em stock: {stock[produto]}.")
else:
    print(f"O produto '{produto}' não está disponível.")