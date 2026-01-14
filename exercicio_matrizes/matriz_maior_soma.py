#Leia uma matriz 3x3 e determine qual linha ou coluna tem a maior soma.
def soma_linha(matriz, linha):
    return sum(matriz[linha])
def soma_coluna(matriz, coluna):
    return sum(matriz[i][coluna] for i in range(3))
def main():
    matriz = []
    print("Digite os elementos da matriz 3x3:")
    for i in range(3):
        linha = []
        for j in range(3):
            elemento = int(input(f"Elemento [{i+1},{j+1}]: "))
            linha.append(elemento)
        matriz.append(linha)
    maior_soma = float('-inf')
    tipo = ''
    indice = -1
    for i in range(3):
        soma_l = soma_linha(matriz, i)
        if soma_l > maior_soma:
            maior_soma = soma_l
            tipo = 'linha'
            indice = i
    for j in range(3):
        soma_c = soma_coluna(matriz, j)
        if soma_c > maior_soma:
            maior_soma = soma_c
            tipo = 'coluna'
            indice = j
    print(f"A {tipo} {indice + 1} tem a maior soma: {maior_soma}")
if __name__ == "__main__":
    main()
