#Leia uma matriz 2x3 e exiba a sua matriz transposta.
matriz = []
for i in range(2):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)
transposta = []
for j in range(3):
    linha_transposta = []
    for i in range(2):
        linha_transposta.append
        (matriz[i][j])
    transposta.append(linha_transposta)
for linha in matriz:
    print(linha)
print("Matriz Transposta:") 