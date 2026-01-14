#Calcule e exiba a soma dos elementos de uma linha específica de uma matriz 4x4.
matriz = []
soma = 0
for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)
linha_especifica = int(input("Digite o número da linha (0-3) que deseja somar: "))
for j in range(4):
    soma += matriz[linha_especifica][j]
for linha in matriz:
    print(linha)
print(f"A soma dos elementos da linha {linha_especifica} é: {soma}")
