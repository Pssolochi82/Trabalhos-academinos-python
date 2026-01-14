#Escreva um programa que leia 10 números inteiros do utilizador e os armazene num array. Em seguida, verifique se um número específico fornecido pelo utilizador está presente no array. Se estiver, imprima "O número está presente no array". Se não estiver, imprima "O número não está presente no array".
numeros = []
for i in range(10):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num) 
numero_procurado = int(input("Digite um número para verificar se está no array: "))
if numero_procurado in numeros:
    print("O número está presente no array.")
else:
    print("O número não está presente no array.")
    