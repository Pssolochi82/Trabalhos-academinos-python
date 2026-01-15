#Crie dois sets: um com vogais e outro com consoantes de uma frase introduzida pelo utilizador; mostre a diferença simétrica entre eles.
frase = input("Digite uma frase: ")
vogais = {"a", "e", "i", "o", "u"}
consoantes = set()
for letra in frase.lower():
    if letra.isalpha() and letra not in vogais:
        consoantes.add(letra)
print("Vogais:", vogais)
print("Consoantes:", consoantes)
diferenca_simetrica = vogais.symmetric_difference(consoantes)
print("Diferença simétrica entre vogais e consoantes:", diferenca_simetrica)