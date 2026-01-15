#Crie um dicionário de inventário (produto -> quantidade). Atualize as quantidades após uma venda.
inventario = {"camiseta": 10, "calça": 5, "sapato": 8}
print("Inventário inicial:", inventario)
# Simular uma venda de 2 camisetas
if "camiseta" in inventario:
    inventario["camiseta"] -= 2
print("Inventário após venda:", inventario)