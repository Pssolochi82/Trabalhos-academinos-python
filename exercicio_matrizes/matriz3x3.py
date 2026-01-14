#Leia valores do utilizador e preencha uma matriz 3x3. Exiba a matriz no final.
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)
for linha in matriz:
    print(linha)
    