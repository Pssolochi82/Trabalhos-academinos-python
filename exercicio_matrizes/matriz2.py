#Crie duas matrizes 2x2 preenchidas pelo utilizador e calcule a matriz resultante da sua multiplicação.
def multiplicar_matrizes(matriz1, matriz2):
    resultado = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    return resultado
def main():
    matriz1 = []
    matriz2 = []
    print("Digite os elementos da primeira matriz 2x2:")
    for i in range(2):
        linha = []
        for j in range(2):
            elemento = int(input(f"Elemento [{i+1},{j+1}]: "))
            linha.append(elemento)
        matriz1.append(linha)
    print("Digite os elementos da segunda matriz 2x2:")
    for i in range(2):
        linha = []
        for j in range(2):
            elemento = int(input(f"Elemento [{i+1},{j+1}]: "))
            linha.append(elemento)
        matriz2.append(linha)
    resultado = multiplicar_matrizes(matriz1, matriz2)
    print("Matriz resultante da multiplicação:")
    for linha in resultado:
        print(linha)
if __name__ == "__main__":
    main()
    


