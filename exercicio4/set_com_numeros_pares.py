#Crie um set com números pares de 0 a 20 e outro com números ímpares de 1 a 19. Mostre a união dos dois sets.
pares = {i for i in range(0, 21, 2)}
impares = {i for i in range(1, 20, 2)}
uniao = pares | impares
print("União dos sets de números pares e ímpares:", uniao)

