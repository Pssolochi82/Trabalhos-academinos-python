#Com um dicionário de stock (produto: quantidade), peça input do utilizador, verifique com in se existe e subtraia 1 da quantidade se disponível.
stock = {
    "maçã": 10,
    "banana": 5,
    "laranja": 8
}
produto = input("Digite o nome do produto: ")
if produto in stock:
    if stock[produto] > 0:
        stock[produto] -= 1
        print(f"Quantidade restante de {produto}: {stock[produto]}")
    else:
        print(f"Produto {produto} esgotado.")
else:
    print(f"Produto {produto} não encontrado no stock.")