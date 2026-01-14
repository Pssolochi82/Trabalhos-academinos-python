#Criar dois vetores A e B cada um com 10 elementos inteiros. Construir um vetor C, onde cada elemento de C é a soma dos respetivos elementos de A e B.
A = []
B = []
for i in range(10):
    elemento_a = int(input(f"Digite o {i+1}º elemento do array A: "))
    A.append(elemento_a)
for i in range(10):
    elemento_b = int(input(f"Digite o {i+1}º elemento do array B: "))
    B.append(elemento_b)
C = [A[i] + B[i] for i in range(10)]
print("Vetor A:", A)
print("Vetor B:", B)
print("Vetor C (soma de A e B):", C)
