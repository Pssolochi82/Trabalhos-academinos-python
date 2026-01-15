#Escreva um programa que leia uma frase do utilizador e use in para verificar se a palavra 'python' aparece na frase, independentemente de maiúsculas/minúsculas.
frase = input("Digite uma frase: ")
if 'python' in frase.lower():
    print("A palavra 'python' está presente na frase.")
else:
    print("A palavra 'python' não está presente na frase.")
    