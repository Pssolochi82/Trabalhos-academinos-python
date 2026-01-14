#Construa uma matriz 3 por 3 e realize as seguintes operações:
#a. Leia valores para a matriz
#b. Devolva a media de todos os valores lidos.
#c. Devolva quantos número positivo, negativos e nulos.
#d. Devolva quantos pares e impares.
#e. E por fim multiplique cada um dos elementos lidos por 10 e a seguir imprima.
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)
soma = 0
total_elementos = 0
positivos = 0
negativos = 0
nulos = 0
pares = 0
impares = 0
for i in range(3):
    for j in range(3):
        valor = matriz[i][j]
        soma += valor
        total_elementos += 1
        if valor > 0:
            positivos += 1
        elif valor < 0:
            negativos += 1
        else:
            nulos += 1
        if valor % 2 == 0:
            pares += 1
        else:
            impares += 1
media = soma / total_elementos
print(f"Média dos valores lidos: {media}")
print(f"Números positivos: {positivos}, negativos: {negativos}, nulos: {nulos}")
print(f"Números pares: {pares}, ímpares: {impares}")    
print("Matriz com elementos multiplicados por 10:")
for i in range(3):
    for j in range(3):
        matriz[i][j] *= 10
        print(matriz[i][j], end=' ')
    print()
