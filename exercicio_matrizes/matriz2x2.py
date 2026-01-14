#Escreva um programa que leia uma matriz 2x2 e calcule a soma de todos os seus elementos.
matriz = []
soma = 0
for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
        soma += valor
    matriz.append(linha)
for linha in matriz:
    print(linha)
print(f"A soma de todos os elementos da matriz é: {soma}")
