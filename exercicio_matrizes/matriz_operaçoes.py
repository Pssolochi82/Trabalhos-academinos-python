#Construa uma matriz 3 por 3 e realize as seguintes operações:
#a. Leia valores para a matriz
#b. Devolva a media de todos os valores lidos.
#c. Devolva quantos número positivo, negativos e nulos.
#d. Devolva quantos pares e ímpares.
#e. E por fim multiplique cada um dos elementos lidos por 10 e a seguir imprima.

def ler_matriz():
    matriz = []
    print("Digite os elementos da matriz 3x3:")
    for i in range(3):
        linha = []
        for j in range(3):
            elemento = int(input(f"Elemento [{i+1},{j+1}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz
def calcular_media(matriz):
    total = sum(sum(linha) for linha in matriz)
    return total / 9
def contar_positivos_negativos_nulos(matriz):
    positivos = negativos = nulos = 0
    for linha in matriz:
        for elemento in linha:
            if elemento > 0:
                positivos += 1
            elif elemento < 0:
                negativos += 1
            else:
                nulos += 1
    return positivos, negativos, nulos
def contar_pares_impares(matriz):
    pares = impares = 0
    for linha in matriz:
        for elemento in linha:
            if elemento % 2 == 0:
                pares += 1
            else:
                impares += 1
    return pares, impares
def multiplicar_por_dez(matriz):
    for i in range(3):
        for j in range(3):
            matriz[i][j] *= 10
def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)
def main():
    matriz = ler_matriz()
    media = calcular_media(matriz)
    positivos, negativos, nulos = contar_positivos_negativos_nulos(matriz)
    pares, impares = contar_pares_impares(matriz)
    print(f"Média dos valores: {media}")
    print(f"Números positivos: {positivos}, negativos: {negativos}, nulos: {nulos}")
    print(f"Números pares: {pares}, ímpares: {impares}")
    multiplicar_por_dez(matriz)
    print("Matriz após multiplicar por 10:")
    imprimir_matriz(matriz)
if __name__ == "__main__":
    main()