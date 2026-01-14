#Leia uma matriz 3x3 e calcule a soma dos elementos da diagonal principal e da diagonal secundária.

matriz = [[0 for _ in range(3)] for _ in range(3)]


print("Introduza os valores da matriz 3x3:")
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Elemento [{i}][{j}]: "))


print("\nMatriz introduzida:")
for linha in matriz:
    print(linha)


soma_principal = 0
soma_secundaria = 0

for i in range(3):
    soma_principal += matriz[i][i]
    soma_secundaria += matriz[i][2 - i]

print("\nSoma da diagonal principal:", soma_principal)
print("Soma da diagonal secundária:", soma_secundaria)
