#Criar um vetor A com 8 elementos inteiros. Construir um vetor B do mesmo tipo e tamanho e com os elementos do vetor A multiplicados por 2.
A = []
for i in range(8):
    elemento = int(input(f"Digite o {i+1}º elemento do array A: "))
    A.append(elemento)
B = [elemento * 2 for elemento in A]
print("Vetor A:", A)