#Criar um array A com 5 elementos inteiro. Construir um vetor B do mesmo tipo e tamanho e com os “mesmo” elementos do vetor A.
A = []
for i in range(5):
    elemento = int(input(f"Digite o {i+1}º elemento do array A: "))
    A.append(elemento)
B = A.copy()
print("Array A:", A)
print("Array B (cópia de A):", B)
