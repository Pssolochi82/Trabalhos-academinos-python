#Criar um vetor A com 15 elementos inteiros. Construir um vetor B do mesmo tipo e tamanho, sendo que cada elemento do vetor B deverá ser a raiz quadrada do respetivo elemento de A.
import math
A = []
for i in range(15):
    elemento = int(input(f"Digite o {i+1}º elemento do array A: "))
    A.append(elemento)
B = [math.sqrt(elemento) for elemento in A]
print("Vetor A:", A)
print("Vetor B (raízes quadradas de A):", B)
