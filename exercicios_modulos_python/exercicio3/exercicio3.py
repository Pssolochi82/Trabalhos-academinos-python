import random

numero = random.randint(1, 100)

cores = ["vermelho", "verde", "azul", "amarelo"]
cor_escolhida = random.choice(cores)

numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)

print("Número aleatório:", numero)
print("Cor aleatória:", cor_escolhida)
print("Lista embaralhada:", numeros)
