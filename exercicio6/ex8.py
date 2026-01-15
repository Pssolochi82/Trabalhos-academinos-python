#Gere um set de números primos até 20; crie outro set de múltiplos de 3 até 20 e mostre a união e interseção.
primos = {2, 3, 5, 7, 11, 13, 17, 19}
multiplos_de_3 = {3, 6, 9, 12, 15, 18}
print("União:", primos.union(multiplos_de_3))
print("Interseção:", primos.intersection(multiplos_de_3))