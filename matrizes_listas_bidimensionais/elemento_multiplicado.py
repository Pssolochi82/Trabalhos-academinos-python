#Criar um vetor A com 10 elementos inteiros. Construir um vetor B do mesmo tipo e tamanho, sendo que cada elemento do vetor B deverá ser o respetivo elemento de A multiplicado pela sua posição.
A = []
for i in range(10):
    elemento = int(input(f"Digite o {i+1}º elemento do array A: "))
    A.append(elemento)
B = [A[i] * i for i in range(10)]
print("Vetor A:", A)
print("Vetor B (elementos de A multiplicados pela posição):", B)
