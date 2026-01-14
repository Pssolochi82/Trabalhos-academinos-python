#Construa um programa que:
#a. Crie e armazene num vetor os 50 números (aleatoriamente ou por introdução)
#b. calcule a soma dos 50 números
#c. Apresente no ecrã todos os números pares
#d. Indique qual o menor número lido
#e. Pesquisar um número no vetor (caso o número não seja encontrado deve ser apresentada uma mensagem de erro: "numero não encontrado".)

import random
vetor = []
for i in range(50):
    numero = random.randint(1, 100)  # Números aleatórios entre 1 e 100
    vetor.append(numero)
soma = sum(vetor)
print("Vetor:", vetor)
print("Soma dos 50 números:", soma)
print("Números pares no vetor:")
for numero in vetor:
    if numero % 2 == 0:
        print(numero, end=' ')
menor_numero = min(vetor)
print("\nMenor número lido:", menor_numero)
numero_pesquisado = int(input("\nDigite um número para pesquisar no vetor: "))
if numero_pesquisado in vetor:
    print(f"Número {numero_pesquisado} encontrado no vetor.")
else:
    print("Número não encontrado.")
