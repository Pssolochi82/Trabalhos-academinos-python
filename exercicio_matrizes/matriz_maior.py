#Leia uma matriz 3x3 e determine o maior elemento presente nela.
def encontrar_maior_elemento(matriz):
    maior = matriz[0][0]
    for linha in matriz:
        for elemento in linha:
            if elemento > maior:
                maior = elemento
    return maior
def main():
    matriz = []
    print("Digite os elementos da matriz 3x3:")
    for i in range(3):
        linha = []
        for j in range(3):
            elemento = int(input(f"Elemento [{i+1},{j+1}]: "))
            linha.append(elemento)
        matriz.append(linha)
    maior_elemento = encontrar_maior_elemento(matriz)
    print(f"O maior elemento da matriz é: {maior_elemento}")
if __name__ == "__main__":
    main()